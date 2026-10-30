"""Paper-trading bot: deterministic arbitrage between Polymarket and Kalshi, with fictional money.

Loop (until MAX_RUNTIME_MIN):
  * every DISCOVER_MIN: find games (football, NBA, NFL, NHL) listed on both venues that start within WINDOW_H hours;
  * every POLL_SEC, for each game between KO - WINDOW_H and KO - 1 min (pre-game only): read Polymarket order books
    and Kalshi top of book, solve the arbitrage LP over the game's final-score states, net of each market's taker fee;
  * a gap above THRESH must still be there at the next check (one polling interval of reaction time); the bot then
    "buys" at that moment's best prices, never more than the displayed size (minus what it already took), at least the
    venue's minimum order size, at most CAP_PER_TRADE, and only with the cash it has on each venue;
  * positions settle from the venues' official resolutions; cash returns to each venue.
No order is ever sent: this is a simulation on live public data.
Outputs (results/): trades.jsonl, trades.csv, opportunities.csv, polls/<date>.csv, state.json, summary.md
"""
import os, sys, json, csv, math, time, gzip, subprocess, threading, traceback, datetime as dt
from concurrent.futures import ThreadPoolExecutor
import numpy as np
from .common import get, GAMMA, KS, now, iso, parse, pm_books, ks_quote, solve, KS_FEE, odds_key_check
from . import markets_us, markets_fb, books as bk
from .grid_us import USGrid, unique_rows

ROOT = os.path.join(os.path.dirname(__file__), "..")
RES = os.environ.get("BOT_RESULTS_DIR") or os.path.join(ROOT, "results")
RAW = os.environ.get("BOT_RAW_DIR")                      # raw top-of-book snapshots (kept out of the public repo)
E = lambda k, d: type(d)(os.environ.get(k, d))
POLL_SEC, WINDOW_H, DISCOVER_MIN = E("POLL_SEC", 30), E("WINDOW_H", 3.0), E("DISCOVER_MIN", 10)
MAX_RUNTIME_MIN, COMMIT_MIN = E("MAX_RUNTIME_MIN", 340), E("COMMIT_MIN", 20)
THRESH, MIN_PROFIT, CAP_PER_TRADE = E("THRESH", 0.002), E("MIN_PROFIT", 0.02), E("CAP_PER_TRADE", 250.0)
START_CASH = {"PM": E("CASH_PM", 1000.0), "KS": E("CASH_KS", 1000.0)}
RAW_EVERY = E("RAW_EVERY", 10)          # raw snapshot every 10th check of a game (~5 min) + every check with t* > -0.5%
CAP_BOOK_LEG = E("CAP_BOOK_LEG", 250.0)  # assumed bookmaker stake limit per leg (measurement only, no paper fills)
SETTLE_AFTER_H = {"nba": 3.0, "nhl": 3.0, "nfl": 4.0, "football": 2.5}
US = ("nba", "nfl", "nhl")
GRIDS = {}
LOCK = threading.Lock()                  # games are checked in parallel threads: file appends must not interleave
STATUS = {"checks": 0, "errors": 0, "raw_snapshots": 0, "results_pushes": 0, "raw_pushes": 0, "book_calls": 0, "book_games": 0}
ODDS_KEYS = {i: os.environ.get(f"ODDS_API_KEY_{i}", "").strip() for i in range(1, 6)}  # GitHub secrets; never logged


def log(*a): print(iso(now()), *a, flush=True)


# ---------------------------------------------------------------- persistence
def load_state():
    p = os.path.join(RES, "state.json")
    if os.path.exists(p): return json.load(open(p))
    return {"cash": dict(START_CASH), "start_cash": dict(START_CASH), "open": [], "consumed": {}, "started": iso(now()),
            "n_trades": 0, "n_settled": 0, "realized_pnl": 0.0, "runs": 0}


def save_state(st):
    os.makedirs(RES, exist_ok=True)
    json.dump(st, open(os.path.join(RES, "state.json"), "w"), indent=1)


def append_csv(path, row):
    with LOCK:
        new = not os.path.exists(path)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(row)); new and w.writeheader(); w.writerow(row)


def raw_write(game, pm, ks):
    """Raw top-of-book snapshot, only into the private data repository (never into this public one)."""
    if not RAW: return
    with LOCK:
        d = os.path.join(RAW, now().strftime("%Y-%m-%d")); os.makedirs(d, exist_ok=True)
        with gzip.open(os.path.join(d, now().strftime("%H") + ".jsonl.gz"), "at") as f:
            f.write(json.dumps({"t": iso(now()), "game": game["id"], "pm": pm, "ks": ks}) + "\n")
        STATUS["raw_snapshots"] += 1


def git(repo, *args):
    """Run git silently: the Actions logs of a public repository are public, so no git output is ever printed."""
    try: return subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True, timeout=300).returncode
    except Exception: return -1


def git_commit(msg):
    if os.environ.get("BOT_COMMIT") != "1": return
    for name, repo, paths in (("results", ROOT, ["results"]), ("raw", os.environ.get("BOT_RAW_REPO"), ["."])):
        if not repo or not os.path.isdir(os.path.join(repo, ".git")): continue
        if git(repo, "add", *paths) != 0: log(f"{name}: git add failed"); STATUS["errors"] += 1; continue
        if git(repo, "diff", "--cached", "--quiet") == 0: continue
        if git(repo, "commit", "-q", "-m", msg) != 0: log(f"{name}: commit failed"); STATUS["errors"] += 1; continue
        for i in range(4):
            git(repo, "pull", "-q", "--rebase", "-X", "theirs")
            if git(repo, "push", "-q") == 0: STATUS[f"{name}_pushes"] += 1; break
            time.sleep(2 ** (i + 1))
        else:
            log(f"{name}: push failed"); STATUS["errors"] += 1


def code_id(ref):
    """Identity of the bot code and workflow at a git ref (tree hashes)."""
    out = []
    for path in ("bot", ".github", "requirements.txt"):
        r = subprocess.run(["git", "-C", ROOT, "rev-parse", f"{ref}:{path}"], capture_output=True, text=True)
        out.append(r.stdout.strip())
    return tuple(out)


def code_updated(start):
    """True when new bot code has been pushed: this run then ends so that the next run (queued by the push) uses it."""
    if os.environ.get("BOT_COMMIT") != "1" or not all(start): return False
    if git(ROOT, "fetch", "-q", "origin", "main") != 0: return False
    new = code_id("origin/main")
    return all(new) and new != start


# ---------------------------------------------------------------- games
class Game:
    def __init__(self, meta):
        self.m = meta; self.pm, self.pm_t, self.pend, self._sig, self._pay, self.n = [], 0.0, None, None, None, 0
        self.book = None                                  # bookmaker snapshot waiting to be combined with PM/KS prices

    @property
    def ko(self): return parse(self.m["kickoff"])

    def refresh_pm(self):
        mod = markets_fb if self.m["sport"] == "football" else markets_us
        try: self.pm = sorted(mod.pm_contracts(self.m), key=lambda c: c["id"]); self.pm_t = time.time()
        except Exception as e: log("pm contracts error", self.m["id"], e)

    def payoffs(self, contracts):
        """State x contract payoff matrix (YES payoff per share)."""
        if self.m["sport"] == "football": return np.column_stack([c["payoff"] for c in contracts])
        sig = tuple((c["kind"], c.get("side"), c.get("line"), c.get("lo"), c.get("hi"), c.get("counts_so")) for c in contracts)
        if sig != self._sig:
            g = GRIDS.get(self.m["sport"]) or GRIDS.setdefault(self.m["sport"], USGrid(self.m["sport"]))
            C = np.empty((g.H.size, len(contracts)), np.uint8)                  # codes 0 / 1 / 2 = pays 0 / 0.5 / 1
            for j, c in enumerate(contracts): C[:, j] = np.rint(g.payoff(c) * 2)
            self._pay, self._sig = unique_rows(C, codes=True) / 2.0, sig
        return self._pay


def discover(games):
    for lg in (*US, *markets_fb.LEAGUES):
        mod = markets_us if lg in US else markets_fb
        try: found = mod.discover(lg, WINDOW_H + 0.5)
        except Exception as e: log("discover error", lg, e); continue
        for m in found:
            if m["id"] not in games: games[m["id"]] = Game(m); log("new game", m["id"], m["title"], m["kickoff"])
            else: games[m["id"]].m["kickoff"] = m["kickoff"]
    for k in [k for k, g in games.items() if now() > g.ko + dt.timedelta(minutes=10)]: games.pop(k)


# ---------------------------------------------------------------- one check of one game
def snapshot(game):
    """Fetch prices: Kalshi markets (one request per series event) and Polymarket books (batched)."""
    if time.time() - game.pm_t > 600 or not game.pm: game.refresh_pm()
    mod = markets_fb if game.m["sport"] == "football" else markets_us
    try: ks = sorted(mod.ks_contracts(game.m), key=lambda c: c["id"])     # stable order keeps the payoff cache valid
    except Exception as e: log("ks error", game.m["id"], e); ks = []
    books = pm_books([c["token"] for c in game.pm]) if game.pm else {}
    return ks, books


def tickets(game, ks, books, consumed):
    """Buyable positions: (contract index, side, all-in cost per share, price, size available, fee rate, venue, id)."""
    contracts, T = [], []
    for c in game.pm:                                   # every listed contract enters the payoff table (stable cache)
        j = len(contracts); contracts.append(c)
        b = books.get(c["token"])
        if not b: continue
        ask, asz, bid, bsz = b
        for side, px, sz in (("YES", ask, asz), ("NO", None if bid is None else 1 - bid, bsz)):
            if px is None or not 0.005 < px < 0.995: continue
            sz -= consumed.get(f"PM|{c['id']}|{side}|{px:.4f}", {}).get("n", 0.0)
            if sz > 0: T.append((j, side, px + c["fee"] * px * (1 - px), px, sz, c["fee"], "PM", c["id"], c.get("min_size", 5)))
    for c in ks:
        ya, ys, na, ns = ks_quote(c["market"]); j = len(contracts); contracts.append(c)
        for side, px, sz in (("YES", ya, ys), ("NO", na, ns)):
            if px is None or not 0.005 < px < 0.995: continue
            sz -= consumed.get(f"KS|{c['id']}|{side}|{px:.4f}", {}).get("n", 0.0)
            if sz >= 1: T.append((j, side, px + KS_FEE * px * (1 - px), px, sz, KS_FEE, "KS", c["id"], 1))
    return contracts, T


def check(game, st):
    ks, books = snapshot(game)
    contracts, T = tickets(game, ks, books, st["consumed"])
    game.n += 1
    with LOCK: STATUS["checks"] += 1
    t_star, x, W = np.nan, None, None
    if len(T) >= 2:
        P = game.payoffs(contracts)                               # states x contracts
        W = np.column_stack([P[:, j] if s == "YES" else 1.0 - P[:, j] for j, s, *_ in T])   # payoff per share of each ticket
        cost = np.array([t[2] for t in T])
        t_star, x = solve(W / cost)
    if game.n % RAW_EVERY == 1 or (np.isfinite(t_star) and t_star > -0.005):
        raw_write(game.m, {c["token"]: books.get(c["token"]) for c in game.pm}, {c["id"]: ks_quote(c["market"]) for c in ks})
    if W is None: return None
    if game.book is not None:
        try: books_check(game, contracts, T, P, t_star)
        except Exception: log("books error", game.m["id"], traceback.format_exc(limit=2)); STATUS["errors"] += 1
    row = {"time": iso(now()), "game": game.m["id"], "title": game.m["title"], "min_to_ko": round((game.ko - now()).total_seconds() / 60, 1),
           "n_pm": len(game.pm), "n_ks": len(ks), "n_states": P.shape[0], "n_tickets": len(T),
           "t_star": round(t_star, 6) if np.isfinite(t_star) else ""}
    append_csv(os.path.join(RES, "polls", now().strftime("%Y-%m-%d") + ".csv"), row)
    return t_star, x, T, W, contracts


# ---------------------------------------------------------------- bookmakers (measurement only)
def fetch_books(games, keys, st):
    """One The Odds API call per sport when one of its games is 8-30 minutes from kick-off (each kick-off time once)."""
    if not keys.keys: return
    slots = st.setdefault("book_slots", {})
    due = {}
    for g in games.values():
        mins = (g.ko - now()).total_seconds() / 60
        slot = f"{g.m['league']}|{g.m['kickoff'][:16]}"
        if bk.SNAP_MIN <= mins <= bk.SNAP_MAX and slot not in slots and g.m["league"] in bk.SPORTS:
            due.setdefault(g.m["league"], []).append((slot, g))
    for lg, items in due.items():
        markets, regions = bk.params(lg)
        data, msg = keys.call(bk.SPORTS[lg], markets, regions, bk.cost(lg))
        log(f"odds {lg}: {msg}")                                  # msg never contains a key
        for slot, g in items: slots[slot] = iso(now())
        if data is None: continue
        STATUS["book_calls"] += 1
        with LOCK: bk.raw_write(RAW, bk.SPORTS[lg], data)
        for slot, g in items:
            ev, side = bk.match_event(g.m, data, markets_fb.sim)
            if ev: g.book = (ev, side)
            else: log("odds: game not found at the bookmakers", g.m["id"])
    old = (now() - dt.timedelta(days=2)).strftime("%Y-%m-%d")
    st["book_slots"] = {k: v for k, v in slots.items() if v >= old}


def books_check(game, contracts, T, P, t_pmks):
    """Combine the bookmaker snapshot with this minute's Polymarket/Kalshi prices (one LP), log the result."""
    ev, side = game.book; game.book = None
    lines = bk.best_lines(ev, side)
    if game.m["sport"] == "football":
        bl = [(L, v) for L in lines if (v := bk.payoff_football(L)) is not None]
        if not bl: return
        Pc, B = P, np.column_stack([v for _, v in bl])
    else:
        g = GRIDS.get(game.m["sport"]) or GRIDS.setdefault(game.m["sport"], USGrid(game.m["sport"]))
        bl = [(L, v) for L in lines if (v := bk.payoff_us(L, g)) is not None]
        if not bl: return
        nc = len(contracts); C = np.empty((g.H.size, nc + len(bl)), np.uint8)
        for j, c in enumerate(contracts): C[:, j] = np.rint(g.payoff(c) * 2)
        for k, (L, v) in enumerate(bl): C[:, nc + k] = np.where(v == 0, 0, np.where(v == 1.0, 1, 2))
        U = unique_rows(C, codes=True)
        Pc = U[:, :nc] / 2.0
        B = np.column_stack([np.where(U[:, nc + k] == 0, 0.0, np.where(U[:, nc + k] == 1, 1.0, L["eff"])) for k, (L, _) in enumerate(bl)])
    Wt = np.column_stack([Pc[:, j] if s == "YES" else 1.0 - Pc[:, j] for j, s, *_ in T])
    cost = np.array([t[2] for t in T] + [1.0] * B.shape[1])
    t_all, x = solve(np.column_stack([Wt, B]) / cost)
    with LOCK: STATUS["book_games"] += 1
    legs, caps = [], []
    if x is not None and np.isfinite(t_all) and t_all > THRESH:
        for i in np.where(x > 1e-6)[0]:
            if i < len(T):
                j, s, allin, px, sz, fee, venue, cid, mn = T[i]
                legs.append(f"{venue} {s} {px:.3f} x{x[i]:.3f} {contracts[j]['label']}"); caps.append(sz * allin / x[i])
            else:
                L = bl[i - len(T)][0]
                legs.append(f"{L['book']} {L['market']} {L['outcome']} {'' if L['point'] is None else L['point']} @{L['odds']} x{x[i]:.3f}")
                caps.append(CAP_BOOK_LEG / x[i])
    cap = min(caps) if caps else 0.0
    append_csv(os.path.join(RES, "opportunities_books.csv"), {
        "time": iso(now()), "game": game.m["id"], "title": game.m["title"], "league": game.m["league"],
        "min_to_ko": round((game.ko - now()).total_seconds() / 60, 1), "book_lines": B.shape[1],
        "t_pm_ks": round(t_pmks, 6) if np.isfinite(t_pmks) else "", "t_with_books": round(t_all, 6) if np.isfinite(t_all) else "",
        "capacity_usd": round(cap, 2) if legs else "", "paper_profit_usd": round(t_all * cap, 2) if legs else "", "legs": " | ".join(legs)})


# ---------------------------------------------------------------- paper execution
def ks_fee(n, p): return math.ceil(KS_FEE * n * p * (1 - p) * 100 - 1e-9) / 100


def execute(game, st, t_star, x, T, W, contracts):
    used = [i for i in range(len(T)) if x[i] > 1e-6]
    cap = min(T[i][4] * T[i][2] / x[i] for i in used)                     # displayed size
    cash = min((st["cash"][v] / s) for v in ("PM", "KS") if (s := sum(x[i] for i in used if T[i][6] == v)) > 1e-9)
    need = max(T[i][8] * T[i][2] / x[i] for i in used)                    # minimum order sizes
    S = min(CAP_PER_TRADE, cap, cash)
    if S < need:                                                          # minimum sizes may exceed the cap per trade
        if need <= min(cap, cash): S = need
        else: return ("no_cash" if need <= cap else "below_min_size"), None
    legs, payout, total = [], np.zeros(W.shape[0]), 0.0
    for i in used:
        j, side, allin, px, sz, fee, venue, cid, mn = T[i]
        n = math.floor(S * x[i] / allin * 100) / 100 if venue == "PM" else math.floor(S * x[i] / allin)
        if n < mn: return "below_min_size", None
        f = round(fee * n * px * (1 - px), 5) if venue == "PM" else ks_fee(n, px)
        c = n * px + f; total += c; payout += n * W[:, i]
        legs.append({"venue": venue, "id": cid, "label": contracts[j]["label"], "side": side, "price": px, "shares": n,
                     "fee": round(f, 5), "cost": round(c, 4)})
    guaranteed = float(payout.min())
    if guaranteed - total < MIN_PROFIT: return "rounding", None
    for L in legs:
        st["cash"][L["venue"]] -= L["cost"]
        k = f"{L['venue']}|{L['id']}|{L['side']}|{L['price']:.4f}"
        st["consumed"][k] = {"n": st["consumed"].get(k, {}).get("n", 0.0) + L["shares"], "t": iso(now())}
    st["n_trades"] += 1
    tr = {"trade_id": st["n_trades"], "time": iso(now()), "game": game.m["id"], "title": game.m["title"], "league": game.m["league"],
          "kickoff": game.m["kickoff"], "min_to_ko": round((game.ko - now()).total_seconds() / 60, 1), "t_lp": round(t_star, 6),
          "cost": round(total, 4), "guaranteed_payout": round(guaranteed, 4), "guaranteed_profit": round(guaranteed - total, 4),
          "legs": legs, "status": "open"}
    st["open"].append(tr)
    with open(os.path.join(RES, "trades.jsonl"), "a") as f: f.write(json.dumps(tr) + "\n")
    log(f"TRADE #{tr['trade_id']} {game.m['title']} cost ${total:.2f} guaranteed +${guaranteed - total:.2f} ({100 * t_star:.2f}%)")
    return "executed", tr


def handle(game, st, res):
    if res is None: return
    t_star, x, T, W, contracts = res
    if not (np.isfinite(t_star) and t_star > THRESH):
        if game.pend: opp(game, game.pend["t"], "vanished", T, x)
        game.pend = None; return
    if game.pend is None or time.time() - game.pend["ts"] > 3 * POLL_SEC:
        game.pend = {"ts": time.time(), "t": t_star}; opp(game, t_star, "seen", T, x); return
    action, tr = execute(game, st, t_star, x, T, W, contracts)
    opp(game, t_star, action, T, x); game.pend = None


def opp(game, t_star, action, T, x):
    used = [i for i in range(len(T)) if x is not None and x[i] > 1e-6]
    cap = min((T[i][4] * T[i][2] / x[i] for i in used), default=0.0)
    append_csv(os.path.join(RES, "opportunities.csv"), {
        "time": iso(now()), "game": game.m["id"], "title": game.m["title"], "league": game.m["league"],
        "min_to_ko": round((game.ko - now()).total_seconds() / 60, 1), "t_lp": round(t_star, 6), "capacity_usd": round(cap, 2),
        "action": action, "legs": " | ".join(f"{T[i][6]} {T[i][1]} {T[i][3]:.3f} x{x[i]:.3f} {T[i][7]}" for i in used)})


# ---------------------------------------------------------------- settlement
def resolution(leg):
    """YES payout per share once resolved, else None."""
    try:
        if leg["venue"] == "KS":
            m = get(f"{KS}/markets/{leg['id']}").get("market", {})
            if m.get("status") not in ("settled", "finalized", "determined"): return None
            v = m.get("settlement_value_dollars")                    # payout per YES contract (0.5 for a 50/50 tie)
            if v not in (None, ""): return float(v)
            return {"yes": 1.0, "no": 0.0}.get(m.get("result"))
        ms = get(f"{GAMMA}/markets", {"condition_ids": leg["id"], "closed": "true"})
        if not ms: return None
        op = ms[0].get("outcomePrices"); op = json.loads(op) if isinstance(op, str) else op
        p = float(op[0])
        return p if p in (0.0, 0.5, 1.0) else None
    except Exception:
        return None


def settle(st):
    keep = []
    for tr in st["open"]:
        sport = "football" if tr["league"] not in US else tr["league"]
        if now() < parse(tr["kickoff"]) + dt.timedelta(hours=SETTLE_AFTER_H[sport]): keep.append(tr); continue
        pays = [resolution(L) for L in tr["legs"]]
        if any(p is None for p in pays): keep.append(tr); continue
        total = 0.0
        for L, p in zip(tr["legs"], pays):
            v = L["shares"] * (p if L["side"] == "YES" else 1 - p); total += v; st["cash"][L["venue"]] += v
        tr.update(status="settled", settled=iso(now()), payout=round(total, 4), pnl=round(total - tr["cost"], 4),
                  check="ok" if total >= tr["guaranteed_payout"] - 1e-6 else "BELOW_GUARANTEE")
        st["n_settled"] += 1; st["realized_pnl"] += total - tr["cost"]
        with open(os.path.join(RES, "trades.jsonl"), "a") as f: f.write(json.dumps(tr) + "\n")
        log(f"SETTLED #{tr['trade_id']} {tr['title']} payout ${total:.2f} pnl ${total - tr['cost']:+.2f} ({tr['check']})")
    st["open"] = keep


# ---------------------------------------------------------------- reporting
def report(st):
    trades = {}
    p = os.path.join(RES, "trades.jsonl")
    if os.path.exists(p):
        for line in open(p): t = json.loads(line); trades[t["trade_id"]] = t
    rows = [{k: v for k, v in t.items() if k != "legs"} | {"n_legs": len(t["legs"])} for t in trades.values()]
    if rows:
        cols = list(dict.fromkeys(k for r in rows for k in r))
        with open(os.path.join(RES, "trades.csv"), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    opps = list(csv.DictReader(open(os.path.join(RES, "opportunities.csv")))) if os.path.exists(os.path.join(RES, "opportunities.csv")) else []
    acts = {}
    for o in opps: acts[o["action"]] = acts.get(o["action"], 0) + 1
    locked = sum(t["cost"] for t in st["open"])
    equity = sum(st["cash"].values()) + locked
    start = sum(st["start_cash"].values())
    days = max(1e-9, (now() - parse(st["started"])).total_seconds() / 86400)
    lines = [f"# Paper-trading bot: status at {iso(now())}", "",
             f"Started {st['started']} with ${start:,.0f} (fictional; Polymarket ${st['start_cash']['PM']:,.0f}, Kalshi ${st['start_cash']['KS']:,.0f}).", "",
             "| | |", "|---|---|",
             f"| Trades executed | {st['n_trades']} |", f"| Trades settled | {st['n_settled']} |",
             f"| Realised profit | ${st['realized_pnl']:,.2f} |",
             f"| Open positions (cost) | ${locked:,.2f} |",
             f"| Cash: Polymarket / Kalshi | ${st['cash']['PM']:,.2f} / ${st['cash']['KS']:,.2f} |",
             f"| Equity (cash + open at cost) | ${equity:,.2f} |",
             f"| Return so far (realised / start) | {100 * st['realized_pnl'] / start:.3f}% over {days:.1f} days |", "",
             "Gaps above the threshold seen by the bot: " + (", ".join(f"{k} {v}" for k, v in sorted(acts.items())) or "none yet") + ".", "",
             "`seen` = first sighting; `executed` = still there at the next check and filled; `vanished` = gone at the next check;",
             "`below_min_size` / `rounding` / `no_cash` = too small to fill, or no cash left on a venue.", ""]
    ob = os.path.join(RES, "opportunities_books.csv")
    if os.path.exists(ob):
        bo = list(csv.DictReader(open(ob)))
        pos = [r for r in bo if r["legs"]]
        best = max((float(r["t_with_books"]) for r in pos), default=None)
        lines += ["## Bookmakers (measurement only, no paper fills)", "",
                  f"Snapshots combined with Polymarket/Kalshi prices: {len(bo)} games. Gaps above {100 * THRESH:.1f}% including "
                  f"bookmaker odds: {len(pos)}" + (f" (best {100 * best:+.2f}%, paper profit at ${CAP_BOOK_LEG:.0f} per bookmaker leg: "
                  f"${sum(float(r['paper_profit_usd'] or 0) for r in pos):,.2f})." if pos else "."), ""]
    if rows:
        lines += ["## Last trades", "", "| # | time (UTC) | game | min to KO | gap | cost | guaranteed profit | status | P&L |", "|---|---|---|---|---|---|---|---|---|"]
        for t in sorted(trades.values(), key=lambda t: -t["trade_id"])[:25]:
            pnl = "" if t.get("pnl") is None else f"${t['pnl']:+.2f}"
            lines.append(f"| {t['trade_id']} | {t['time'][5:16]} | {t['title']} | {t['min_to_ko']} | {100 * t['t_lp']:.2f}% | ${t['cost']:.2f} | "
                         f"${t['guaranteed_profit']:.2f} | {t['status']} | {pnl} |")
    open(os.path.join(RES, "summary.md"), "w").write("\n".join(lines) + "\n")


def write_status(st, games, start_code, t_start):
    """Public health file (no secrets): lets the run be checked without access to the Actions logs."""
    json.dump({"run": st["runs"], "run_started": iso(dt.datetime.fromtimestamp(t_start, dt.timezone.utc)),
               "last_update": iso(now()), "code_version": (start_code[0] or "")[:12],
               "private_raw_storage": bool(RAW), "odds_api_keys": STATUS.get("odds_keys", {}),
               "odds_credits_remaining": {f"ODDS_API_KEY_{i}": r for i, r in sorted(st.get("odds", {}).get("remaining", {}).items())},
               "odds_credits_spent_today": st.get("odds", {}).get("spent", {}).get(now().strftime("%Y-%m-%d"), 0),
               "games_tracked": len(games),
               "games_in_window": sum(1 for g in games.values() if g.ko - dt.timedelta(hours=WINDOW_H) <= now() < g.ko),
               **{k: v for k, v in STATUS.items() if k != "odds_keys"}}, open(os.path.join(RES, "status.json"), "w"), indent=1)


# ---------------------------------------------------------------- main
def main():
    st = load_state(); st["runs"] += 1; t_start = time.time()
    games, last_disc, last_commit, last_settle, last_code = {}, 0.0, 0.0, 0.0, time.time()
    start_code = code_id("HEAD")
    STATUS["odds_keys"] = {f"ODDS_API_KEY_{i}": (odds_key_check(k) if k else "not set") for i, k in ODDS_KEYS.items()}
    keys = bk.Keys(st)
    for i, r in STATUS["odds_keys"].items():                 # start from the true remaining credits of each key
        if isinstance(r, dict) and r.get("valid"): keys.st["remaining"][i.rsplit("_", 1)[1]] = r["remaining"]
    log(f"run {st['runs']} | window {WINDOW_H} h | poll {POLL_SEC} s | threshold {100 * THRESH:.2f}% | cap ${CAP_PER_TRADE:.0f}"
        f" | private raw storage: {'yes' if RAW else 'no'}")
    pool = ThreadPoolExecutor(int(os.environ.get("WORKERS", 8)))
    while time.time() - t_start < MAX_RUNTIME_MIN * 60:
        t0 = time.time(); active = []
        try:
            if t0 - last_disc > DISCOVER_MIN * 60: discover(games); last_disc = t0
            fetch_books(games, keys, st)
            active = [g for g in games.values() if g.ko - dt.timedelta(hours=WINDOW_H) <= now() < g.ko - dt.timedelta(minutes=1)]
            for g, res in zip(active, pool.map(lambda g: check(g, st), active)):
                try: handle(g, st, res)
                except Exception: log("handle error", g.m["id"], traceback.format_exc(limit=2)); STATUS["errors"] += 1
            if t0 - last_settle > 600:
                settle(st); last_settle = t0
                old = now() - dt.timedelta(hours=12)                      # liquidity "taken" by the bot expires
                st["consumed"] = {k: v for k, v in st["consumed"].items() if parse(v["t"]) > old}
            save_state(st)
            if t0 - last_commit > COMMIT_MIN * 60:
                report(st); write_status(st, games, start_code, t_start); git_commit(f"bot: {iso(now())}"); last_commit = t0
            if t0 - last_code > 600:
                last_code = t0
                if code_updated(start_code): log("new code pushed: ending this run so that the next run uses it"); break
        except Exception:
            log("loop error", traceback.format_exc(limit=3)); STATUS["errors"] += 1
        if not active:
            nxt = min((g.ko - dt.timedelta(hours=WINDOW_H) - now()).total_seconds() for g in games.values()) if games else 600
            time.sleep(max(POLL_SEC, min(300, nxt)))
        else:
            time.sleep(max(1.0, POLL_SEC - (time.time() - t0)))
    settle(st); save_state(st); report(st); write_status(st, games, start_code, t_start); git_commit(f"bot: end of run {iso(now())}")
    log("done")


if __name__ == "__main__":
    main()
