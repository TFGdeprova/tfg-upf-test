"""Paper-trading bot: deterministic arbitrage between Polymarket and Kalshi, with fictional money.

Loop (until MAX_RUNTIME_MIN):
  * every DISCOVER_MIN: find games (football, NBA, NFL, NHL) listed on both venues that start within WINDOW_H hours;
  * every POLL_SEC, for each game between KO - WINDOW_H and KO - 1 min (pre-game only): read Polymarket order books
    and Kalshi top of book, solve the arbitrage LP over the game's final-score states, net of each market's taker fee;
  * a gap above THRESH must still be there at the next check (one polling interval of reaction time); the bot then
    "buys" at that moment's best prices, never more than the displayed size (minus what it already took), at least the
    venue's minimum order size, at most CAP_PER_TRADE, and only with the cash it has on each venue;
  * positions settle from the venues' official resolutions; cash returns to each venue;
  * every gap above WATCH_THRESH (traded or not) is followed: the same portfolio is re-priced RECHECK_SEC later and the
    order-book depth of its contracts gives the guaranteed profit at larger sizes (rechecks.csv, depth.csv).
No order is ever sent: this is a simulation on live public data.
Outputs (results/): trades.jsonl, trades.csv, opportunities.csv, opportunities_books.csv, rechecks.csv, depth.csv,
transfers.csv, polls/<date>.csv, state.json, status.json, summary.md
"""
import os, sys, json, csv, math, time, gzip, subprocess, threading, traceback, datetime as dt
from concurrent.futures import ThreadPoolExecutor
import numpy as np
from .common import get, GAMMA, KS, now, iso, parse, pm_books, ks_quote, ks_ladders, solve, KS_FEE, odds_key_check
from . import markets_us, markets_fb, books as bk, accounts as ac, depth as dp
from .grid_us import USGrid, unique_rows

ROOT = os.path.join(os.path.dirname(__file__), "..")
RES = os.environ.get("BOT_RESULTS_DIR") or os.path.join(ROOT, "results")
RAW = os.environ.get("BOT_RAW_DIR")                      # raw top-of-book snapshots (kept out of the public repo)
E = lambda k, d: type(d)(os.environ.get(k, d))
POLL_SEC, WINDOW_H, DISCOVER_MIN = E("POLL_SEC", 30), E("WINDOW_H", 3.0), E("DISCOVER_MIN", 10)
MAX_RUNTIME_MIN, COMMIT_MIN = E("MAX_RUNTIME_MIN", 340), E("COMMIT_MIN", 20)
THRESH, MIN_PROFIT, CAP_PER_TRADE = E("THRESH", 0.002), E("MIN_PROFIT", 0.02), E("CAP_PER_TRADE", 2500.0)
# Unlimited capital (default, for the test of the opportunities): cash never limits a trade. Polymarket/Kalshi trades
# take the full size shown at the best prices; trades that use bookmakers (which publish no depth) are capped at
# CAP_BOOK_TRADE in total. The capital needed is then a result: the peak money in use per account. UNLIMITED_CAPITAL=0
# restores the bankroll design (EUR 10,000 on Polymarket + Kalshi, EUR 500 per bookmaker, CAP_PER_TRADE, transfers).
UNLIMITED, CAP_BOOK_TRADE = E("UNLIMITED_CAPITAL", 1) == 1, E("CAP_BOOK_TRADE", 2500.0)
FX = E("EUR_USD", 1.16)                 # reporting only: the venues trade in US dollars
START_CASH = {"PM": E("CASH_PM", 5800.0), "KS": E("CASH_KS", 5800.0)}   # = EUR 10,000 at 1.16
RAW_EVERY = E("RAW_EVERY", 10)          # raw snapshot every 10th check of a game (~5 min) + every check with t* > -0.5%
CONFIRM_SEC = E("CONFIRM_SEC", 60)       # a gap that uses a bookmaker is re-checked with fresh odds this much later
MIN_BOOK_STAKE = E("MIN_BOOK_STAKE", 1.0)
WATCH_THRESH = E("WATCH_THRESH", 0.001)  # gaps above 0.1% are followed (re-checks and depth), whether traded or not
RECHECK_SEC = [int(v) for v in os.environ.get("RECHECK_SEC", "30,60,120,300").split(",")]  # re-check delays (seconds)
SETTLE_AFTER_H = {"nba": 3.0, "nhl": 3.0, "nfl": 4.0, "football": 2.5}
US = ("nba", "nfl", "nhl")
GRIDS = {}
LOCK = threading.Lock()                  # games are checked in parallel threads: file appends must not interleave
STATUS = {"checks": 0, "errors": 0, "raw_snapshots": 0, "results_pushes": 0, "raw_pushes": 0, "book_calls": 0, "book_games": 0,
          "book_confirm_calls": 0, "score_calls": 0, "watches": 0, "rechecks": 0, "depth_rows": 0, "ks_depth_calls": 0,
          "discover_errors": 0, "last_discover_error": None}
CONFIRM = {}                             # league -> time after which a confirmation snapshot is taken
ODDS_KEYS = {i: os.environ.get(f"ODDS_API_KEY_{i}", "").strip() for i in range(1, 11)}  # GitHub secrets; never logged


def log(*a): print(iso(now()), *a, flush=True)


# ---------------------------------------------------------------- persistence
def load_state():
    p = os.path.join(RES, "state.json")
    if os.path.exists(p):
        st = json.load(open(p))
        same = all(st.get("start_cash", {}).get(v) == START_CASH[v] for v in START_CASH)
        if st.get("n_trades", 0) > 0 or same:
            ac.init(st, START_CASH); return st
        log("starting capital changed and no trade yet: fresh state")      # e.g. test runs before the real start
    st = {"cash": dict(START_CASH), "start_cash": dict(START_CASH), "open": [], "consumed": {}, "started": iso(now()),
          "n_trades": 0, "n_settled": 0, "realized_pnl": 0.0, "runs": 0}
    ac.init(st, START_CASH); return st


def save_state(st):
    os.makedirs(RES, exist_ok=True)
    json.dump(st, open(os.path.join(RES, "state.json"), "w"), indent=1)


HEADERS = {}                             # csv path -> column order (rows are always written in the file's own order)


def append_csv(path, row):
    with LOCK:
        new = not os.path.exists(path) or os.path.getsize(path) == 0
        if new: HEADERS[path] = list(row)
        elif path not in HEADERS:
            with open(path, newline="") as f: HEADERS[path] = next(csv.reader(f), None) or list(row)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=HEADERS[path], restval="", extrasaction="ignore")
            new and w.writeheader(); w.writerow(row)


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
        self.book_pend = None                             # gap with a bookmaker waiting for its confirmation snapshot
        self.depth, self.ksm = {}, {}                     # last poll: Polymarket ladders by token, Kalshi markets by ticker
        self.qage = {}                                    # (venue, id, side) -> (price, time the price was first seen)
        self.t_first = None                               # first check of the game (price ages cannot be longer)
        self.watches, self.wid = [], None                 # gaps being followed; id of the current Polymarket/Kalshi episode

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
        except Exception as e:
            log("discover error", lg, e)
            with LOCK: STATUS["errors"] += 1; STATUS["discover_errors"] += 1; STATUS["last_discover_error"] = f"{iso(now())} {lg}: {e}"
            continue
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
    dep = {}
    books = pm_books([c["token"] for c in game.pm], dep) if game.pm else {}
    game.depth, game.ksm = dep, {c["id"]: c["market"] for c in ks}
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
    tq = time.time()
    if game.t_first is None: game.t_first = tq
    for t in T:                                                   # how long each best price has been unchanged
        k = (t[6], t[7], t[1])
        if k not in game.qage or game.qage[k][0] != t[3]: game.qage[k] = (t[3], tq)
    t_star, x, W = np.nan, None, None
    if len(T) >= 2:
        P = game.payoffs(contracts)                               # states x contracts
        W = np.column_stack([P[:, j] if s == "YES" else 1.0 - P[:, j] for j, s, *_ in T])   # payoff per share of each ticket
        cost = np.array([t[2] for t in T])
        t_star, x = solve(W / cost)
    if game.n % RAW_EVERY == 1 or (np.isfinite(t_star) and t_star > -0.005):
        raw_write(game.m, {c["token"]: books.get(c["token"]) for c in game.pm}, {c["id"]: ks_quote(c["market"]) for c in ks})
    try:                                                          # follow gaps above WATCH_THRESH (traded or not)
        run_watches(game, t_star)
        if np.isfinite(t_star) and t_star > WATCH_THRESH and x is not None:
            if game.wid is None: game.wid = watch_start(game, "pm_ks", t_star, x, T, W, contracts)
        else: game.wid = None
    except Exception:
        log("watch error", game.m["id"], traceback.format_exc(limit=2))
        with LOCK: STATUS["errors"] += 1
    if W is None: return None
    book_res = None
    if game.book is not None:
        try: book_res = books_eval(game, contracts, T, P, t_star)
        except Exception: log("books error", game.m["id"], traceback.format_exc(limit=2)); STATUS["errors"] += 1
    row = {"time": iso(now()), "game": game.m["id"], "title": game.m["title"], "min_to_ko": round((game.ko - now()).total_seconds() / 60, 1),
           "n_pm": len(game.pm), "n_ks": len(ks), "n_states": P.shape[0], "n_tickets": len(T),
           "t_star": round(t_star, 6) if np.isfinite(t_star) else ""}
    append_csv(os.path.join(RES, "polls", now().strftime("%Y-%m-%d") + ".csv"), row)
    return t_star, x, T, W, contracts, book_res


# ---------------------------------------------------------------- bookmakers
BOOK_CACHE = {}                          # league -> (time, data): one call serves every game of that league due now


def fetch_books(games, keys, st):
    """Bookmaker snapshots at fixed minutes before each kick-off (bk.OFFSETS), plus confirmation snapshots about a minute
    after a gap that uses a bookmaker. One call per sport serves all its games. If the credits left would last less than
    3 days at the current pace, only the late scheduled snapshots are taken (confirmations are always taken)."""
    if not keys.keys: return
    slots = st.setdefault("book_slots", {})
    offsets = bk.OFFSETS if keys.days_left() >= 3 else [o for o in bk.OFFSETS if o in bk.LATE]
    due = {}
    for g in games.values():
        mins = (g.ko - now()).total_seconds() / 60
        if g.m["league"] not in bk.SPORTS or mins < 1: continue
        for o in offsets:
            slot = f"{g.m['league']}|{g.m['kickoff'][:16]}|{o}"
            if o - 8 < mins <= o and slot not in slots: due.setdefault(g.m["league"], []).append((slot, g, False))
        if g.book_pend and g.m["league"] in CONFIRM and time.time() >= CONFIRM[g.m["league"]]:
            due.setdefault(g.m["league"], []).append((None, g, True))
    for lg, items in due.items():
        confirm = any(c for _, _, c in items)
        cached = BOOK_CACHE.get(lg)
        if cached and time.time() - cached[0] < 180 and not (confirm and cached[0] < CONFIRM.get(lg, 0) - 5):
            data, msg = cached[1], "reused a snapshot taken less than 3 minutes ago"
        else:
            markets, regions = bk.params(lg)
            data, msg = keys.call(bk.SPORTS[lg], markets, regions, bk.cost(lg))
            if data is not None:
                BOOK_CACHE[lg] = (time.time(), data); STATUS["book_calls"] += 1
                if confirm: STATUS["book_confirm_calls"] += 1
                with LOCK: bk.raw_write(RAW, bk.SPORTS[lg], data)
        log(f"odds {lg}{' (confirmation)' if confirm else ''}: {msg}")     # msg never contains a key
        if confirm: CONFIRM.pop(lg, None)
        for slot, g, c in items:
            if slot: slots[slot] = iso(now())
        if data is None:
            for _, g, c in items:
                if c: g.book_pend = None
            continue
        for slot, g, c in {id(g): (slot, g, c) for slot, g, c in sorted(items, key=lambda z: z[2])}.values():
            ev, side = bk.match_event(g.m, data, markets_fb.sim)
            if ev: g.book = (ev, side, c)
            else:
                log("odds: game not found at the bookmakers", g.m["id"])
                if c: g.book_pend = None
    old = (now() - dt.timedelta(days=2)).strftime("%Y-%m-%d")
    st["book_slots"] = {k: v for k, v in slots.items() if v >= old}


def books_eval(game, contracts, T, P, t_pmks):
    """Combine the bookmaker snapshot with this minute's Polymarket/Kalshi prices in one LP (no state is changed here:
    the main thread decides what to do with the result)."""
    ev, side, confirm = game.book; game.book = None
    lines = bk.best_lines(ev, side)
    football = game.m["sport"] == "football"
    if football:
        bl = [(L, v) for L in lines if (v := bk.payoff_football(L)) is not None]
        if not bl: return None
        Pc, B = P, np.column_stack([v for _, v in bl])
    else:
        g = GRIDS.get(game.m["sport"]) or GRIDS.setdefault(game.m["sport"], USGrid(game.m["sport"]))
        bl = [(L, v) for L in lines if (v := bk.payoff_us(L, g)) is not None]
        if not bl: return None
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
    for L, _ in bl: L["three_way"] = football
    wid = None
    try:                     # earlier gaps with bookmakers: same bets re-priced at this snapshot; then follow a new gap
        for w in [w for w in game.watches if w["kind"] == "with_books"]:
            measure(game, w, time.time() - w["ts"], ["confirmation" if confirm else "scheduled"], "recheck", t_all, ev, side)
        uses = x is not None and np.isfinite(t_all) and any(x[len(T) + k] > 1e-6 for k in range(len(bl)))
        if uses and t_all > WATCH_THRESH and not confirm:
            wid = watch_start(game, "with_books", t_all, x, T, Wt, contracts, [L for L, _ in bl], B)
    except Exception:
        log("book watch error", game.m["id"], traceback.format_exc(limit=2))
        with LOCK: STATUS["errors"] += 1
    return {"t_all": t_all, "x": x, "Wt": Wt, "B": B, "bl": [L for L, _ in bl], "T": T, "contracts": contracts,
            "confirm": confirm, "t_pmks": t_pmks, "watch": wid, "ev": {"id": ev["id"], "sport": ev.get("sport_key"),
            "home": ev["home_team"], "away": ev["away_team"]}}


def handle_books(game, st, r):
    """Main thread: a gap that uses a bookmaker is first 'seen'; a confirmation snapshot is requested; if the gap is still
    there in the confirmation, the bot bets."""
    if r is None: return
    t_all, x, T, bl = r["t_all"], r["x"], r["T"], r["bl"]
    uses_book = x is not None and np.isfinite(t_all) and any(x[len(T) + k] > 1e-6 for k in range(len(bl)))
    gap = uses_book and t_all > THRESH
    if r["confirm"]:
        if gap: action, tr = execute_books(game, st, r)
        else: action, tr = "vanished", None
        game.book_pend = None
    elif gap:
        game.book_pend = {"ts": time.time(), "t": t_all}; CONFIRM[game.m["league"]] = time.time() + CONFIRM_SEC
        action = "seen"
    else:
        action = "no gap"
    legs, caps = [], []
    if x is not None and (gap or r["confirm"]):
        for i in np.where(x > 1e-6)[0]:
            if i < len(T):
                j, s_, allin, px, sz, fee, venue, cid, mn = T[i]
                legs.append(f"{venue} {s_} {px:.3f} x{x[i]:.3f} {r['contracts'][j]['label']}"); caps.append(sz * allin / x[i])
            else:
                L = bl[i - len(T)]
                legs.append(f"{L['book']} {L['market']} {L['outcome']} {'' if L['point'] is None else L['point']} @{L['odds']} x{x[i]:.3f}")
    append_csv(os.path.join(RES, "opportunities_books.csv"), {
        "time": iso(now()), "game": game.m["id"], "title": game.m["title"], "league": game.m["league"],
        "min_to_ko": round((game.ko - now()).total_seconds() / 60, 1), "snapshot": "confirmation" if r["confirm"] else "scheduled",
        "book_lines": len(bl), "t_pm_ks": round(r["t_pmks"], 6) if np.isfinite(r["t_pmks"]) else "",
        "t_with_books": round(t_all, 6) if np.isfinite(t_all) else "", "action": action,
        "pm_ks_capacity_usd": round(min(caps), 2) if caps else "", "watch": r.get("watch") or "", "legs": " | ".join(legs)})


def execute_books(game, st, r):
    """Paper bet on a confirmed gap that uses bookmakers: Polymarket/Kalshi legs at the best prices (displayed size,
    minimum order sizes, exact fees), bookmaker legs at the confirmation odds (stake limited by the bookmaker account)."""
    t_all, x, T, bl, Wt, B = r["t_all"], r["x"], r["T"], r["bl"], r["Wt"], r["B"]
    nT = len(T)
    used = [i for i in range(len(x)) if x[i] > 1e-6]
    for i in used:
        if i >= nT: ac.open_book(st, bl[i - nT]["book"])
    allin = lambda i: T[i][2] if i < nT else 1.0
    venue = lambda i: T[i][6] if i < nT else f"BK:{bl[i - nT]['book']}"
    caps = [T[i][4] * T[i][2] / x[i] for i in used if i < nT]                 # displayed size on Polymarket/Kalshi
    share = {}
    for i in used: share[venue(i)] = share.get(venue(i), 0.0) + x[i]
    cash = [] if UNLIMITED else [st["cash"][v] / s_ for v, s_ in share.items() if s_ > 1e-9]
    need = max((T[i][8] * T[i][2] / x[i]) if i < nT else MIN_BOOK_STAKE / x[i] for i in used)
    S = min([CAP_BOOK_TRADE if UNLIMITED else CAP_PER_TRADE] + caps + cash)
    if S < need:
        if need <= min(caps + cash): S = need
        else: return ("no_cash" if need <= min(caps or [float("inf")]) else "below_min_size"), None
    legs, payout, total = [], np.zeros(Wt.shape[0]), 0.0
    for i in used:
        if i < nT:
            j, side, al, px, sz, fee, v, cid, mn = T[i]
            n = math.floor(S * x[i] / al * 100) / 100 if v == "PM" else math.floor(S * x[i] / al)
            if n < mn: return "below_min_size", None
            f = round(fee * n * px * (1 - px), 5) if v == "PM" else ks_fee(n, px)
            c = n * px + f; total += c; payout += n * Wt[:, i]
            legs.append({"venue": v, "id": cid, "label": r["contracts"][j]["label"], "side": side, "price": px, "shares": n,
                         "fee": round(f, 5), "cost": round(c, 4)})
        else:
            L = bl[i - nT]; stake = math.floor(S * x[i] * 100) / 100
            if stake < MIN_BOOK_STAKE: return "below_min_size", None
            total += stake; payout += stake * B[:, i - nT]
            legs.append({"venue": f"BK:{L['book']}", "book": L["book"], "market": L["market"], "outcome": L["outcome"],
                         "side": L["side"], "point": L["point"], "odds": L["odds"], "eff": L["eff"],
                         "three_way": L.get("three_way", False), "stake": stake, "cost": stake,
                         "label": f"{L['market']} {L['outcome']} {'' if L['point'] is None else L['point']} @{L['odds']}"})
    guaranteed = float(payout.min())
    if guaranteed - total < MIN_PROFIT: return "rounding", None
    for L in legs:
        ac.lock(st, L["venue"], L["cost"])
        if not L["venue"].startswith("BK:"):
            k = f"{L['venue']}|{L['id']}|{L['side']}|{L['price']:.4f}"
            st["consumed"][k] = {"n": st["consumed"].get(k, {}).get("n", 0.0) + L["shares"], "t": iso(now())}
    st["n_trades"] += 1
    tr = {"trade_id": st["n_trades"], "time": iso(now()), "game": game.m["id"], "title": game.m["title"], "league": game.m["league"],
          "kickoff": game.m["kickoff"], "min_to_ko": round((game.ko - now()).total_seconds() / 60, 1), "t_lp": round(t_all, 6),
          "with_books": True, "books": sorted({L["book"] for L in legs if "book" in L}),
          "spain_only": all(L["book"] in bk.SPAIN for L in legs if "book" in L), "event": r["ev"],
          "cost": round(total, 4), "guaranteed_payout": round(guaranteed, 4), "guaranteed_profit": round(guaranteed - total, 4),
          "legs": legs, "status": "open"}
    st["open"].append(tr)
    with open(os.path.join(RES, "trades.jsonl"), "a") as f: f.write(json.dumps(tr) + "\n")
    log(f"TRADE #{tr['trade_id']} (with bookmakers) {game.m['title']} cost ${total:.2f} guaranteed +${guaranteed - total:.2f} ({100 * t_all:.2f}%)")
    return "executed", tr


# ---------------------------------------------------------------- paper execution
def ks_fee(n, p): return math.ceil(KS_FEE * n * p * (1 - p) * 100 - 1e-9) / 100


def execute(game, st, t_star, x, T, W, contracts):
    used = [i for i in range(len(T)) if x[i] > 1e-6]
    cap = min(T[i][4] * T[i][2] / x[i] for i in used)                     # displayed size
    cash = float("inf") if UNLIMITED else min(
        (st["cash"][v] / s) for v in ("PM", "KS") if (s := sum(x[i] for i in used if T[i][6] == v)) > 1e-9)
    need = max(T[i][8] * T[i][2] / x[i] for i in used)                    # minimum order sizes
    S = min(float("inf") if UNLIMITED else CAP_PER_TRADE, cap, cash)
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
        ac.lock(st, L["venue"], L["cost"])
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
    t_star, x, T, W, contracts, book_res = res
    try: handle_books(game, st, book_res)
    except Exception: log("books handling error", game.m["id"], traceback.format_exc(limit=2)); STATUS["errors"] += 1
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
        "action": action, "watch": game.wid or "",
        "legs": " | ".join(f"{T[i][6]} {T[i][1]} {T[i][3]:.3f} x{x[i]:.3f} {T[i][7]}" for i in used)})


# ---------------------------------------------------------------- following a gap: re-checks and order-book depth
def rescale(v, e0, e1):
    """Payoff per unit staked with a bookmaker at new odds: win e0 -> e1, half win (1+e0)/2 -> (1+e1)/2."""
    out = v.copy()
    out[np.isclose(v, e0)] = e1
    out[np.isclose(v, (1 + e0) / 2)] = (1 + e1) / 2
    return out


def watch_start(game, kind, t0, x, T, W, contracts, bl=(), B=None):
    """Follow a gap found now: the SAME portfolio (same shares, same stakes) is re-priced later (re-checks, the
    ex-ante test) and its order-book depth is measured now and at every re-check. Returns the gap's id."""
    nT, legs, cols = len(T), [], []
    for i in [i for i in range(len(x)) if x[i] > 1e-6]:
        if i < nT:
            j, side, allin, px, sz, fee, venue, cid, mn = T[i]
            L = {"venue": venue, "id": cid, "side": side, "n": float(x[i] / allin), "px0": px, "fee": fee,
                 "label": contracts[j]["label"]}
            if venue == "PM": L["token"] = contracts[j]["token"]
            legs.append(L); cols.append(W[:, i])
        else:
            b = bl[i - nT]
            legs.append({"venue": f"BK:{b['book']}", "book": b["book"], "market": b["market"], "side": b["side"],
                         "point": b["point"], "n": float(x[i]), "eff0": b["eff"], "odds0": b["odds"],
                         "label": f"{b['market']} {b['outcome']} {'' if b['point'] is None else b['point']} @{b['odds']}"})
            cols.append(B[:, i - nT])
    W0 = np.column_stack(cols).astype(float)                   # payoff per share / per unit staked, in every state
    n = np.array([L["n"] for L in legs])
    w = {"id": f"{game.m['id']}|{iso(now())}|{kind}", "kind": kind, "t0": float(t0), "ts": time.time(),
         "detected": iso(now()), "legs": legs, "W0": W0, "g0": float((W0 @ n).min()),
         "lags": list(RECHECK_SEC) if kind == "pm_ks" else []}
    game.watches.append(w)
    with LOCK: STATUS["watches"] += 1
    measure(game, w, 0.0, [], "detection", float(t0))
    return w["id"]


def leg_now(game, L, ev=None, side=None):
    """Current best all-in price and order-book ladder of one leg (bookmaker legs: current odds), or None if the leg
    is no longer quoted. Polymarket ladders come from this poll's books; Kalshi ladders cost one request."""
    if L["venue"] == "PM":
        lad = (game.depth.get(L["token"]) or {}).get(L["side"]) or []
        if not lad: return None
        p = lad[0][0]
        return {"allin": p + L["fee"] * p * (1 - p), "price": p, "ladder": lad, "fee": dp.fee_pm(L["fee"])}
    if L["venue"] == "KS":
        m = game.ksm.get(L["id"])
        if m is None: return None
        ya, ys, na, ns = ks_quote(m); p = ya if L["side"] == "YES" else na
        if p is None: return None
        try:
            lad = ks_ladders(L["id"])[L["side"]]
            with LOCK: STATUS["ks_depth_calls"] += 1
        except Exception: lad = None
        return {"allin": p + KS_FEE * p * (1 - p), "price": p, "ladder": lad, "fee": dp.fee_ks}
    if ev is None: return {"eff": L["eff0"], "odds": L["odds0"]}           # bookmaker leg at detection
    return bk.book_line(ev, side, L["book"], L["market"], L["side"], L["point"])


def measure(game, w, lag, targets, label, t_reopt, ev=None, side=None):
    """Price the followed portfolio now: guaranteed return at the best prices (t_fixed) and, walking the order books,
    the guaranteed profit at larger sizes. Writes rechecks.csv (one row per re-check delay due) and depth.csv."""
    tnow, cur = time.time(), [leg_now(game, L, ev, side) for L in w["legs"]]
    ok = all(c is not None for c in cur)
    t_fixed = g = None
    if ok:
        cols = w["W0"].copy()
        for k, (L, c) in enumerate(zip(w["legs"], cur)):
            if L["venue"].startswith("BK:"): cols[:, k] = rescale(w["W0"][:, k], L["eff0"], c["eff"])
        g = float((cols @ np.array([L["n"] for L in w["legs"]])).min())          # guaranteed payout per unit
        cost = sum(L["n"] * c.get("allin", 1.0) for L, c in zip(w["legs"], cur))  # stakes cost 1 per unit
        t_fixed = g / cost - 1
    ages = [tnow - game.qage[k][1] for L in w["legs"] if (k := (L["venue"], L["id"] if "id" in L else "", L["side"])) in game.qage]
    base = {"time": iso(now()), "watch": w["id"], "kind": w["kind"], "game": game.m["id"], "title": game.m["title"],
            "league": game.m["league"], "min_to_ko": round((game.ko - now()).total_seconds() / 60, 1), "lag_s": round(lag, 1)}
    for tg in targets:
        append_csv(os.path.join(RES, "rechecks.csv"), {**base, "detected": w["detected"], "recheck": tg, "t_detected": round(w["t0"], 6),
                   "t_same_portfolio": "" if t_fixed is None else round(t_fixed, 6),
                   "legs_quoted": f"{sum(c is not None for c in cur)}/{len(cur)}",
                   "t_best_now": round(t_reopt, 6) if t_reopt is not None and np.isfinite(t_reopt) else "",
                   "still_profitable": "" if t_fixed is None else t_fixed > 0, "above_threshold": "" if t_fixed is None else t_fixed > THRESH,
                   "status": "ok" if ok else "leg_not_quoted"})
        with LOCK: STATUS["rechecks"] += 1
    row = {**base, "measure": label, "t_same_portfolio": "" if t_fixed is None else round(t_fixed, 6)}
    if ok and all(c.get("ladder") is not None or "eff" in c for c in cur):
        legs = [{"n": L["n"], "ladder": None, "price": 1.0} if "eff" in c else {"n": L["n"], "ladder": c["ladder"], "fee": c["fee"]}
                for L, c in zip(w["legs"], cur)]
        row.update(dp.curve(legs, g))
    else:
        row.update(dp.EMPTY)
    row.update(max_quote_age_s=round(max(ages), 1) if ages else "", min_quote_age_s=round(min(ages), 1) if ages else "",
               game_watched_s=round(tnow - game.t_first, 1) if game.t_first else "", n_legs=len(w["legs"]), legs=" | ".join(f"{L['venue']} {L['side']} x{L['n']:.4f} {L['label']}" for L in w["legs"]))
    append_csv(os.path.join(RES, "depth.csv"), row)
    with LOCK: STATUS["depth_rows"] += 1
    if RAW:                                                         # full ladders: private repository only
        rec = {"t": iso(now()), "watch": w["id"], "lag_s": round(lag, 1), "measure": label,
               "legs": [{"venue": L["venue"], "id": L.get("id") or L.get("book"), "side": L["side"],
                         "price": c.get("price") if c else None, "ladder": c.get("ladder") if c else None,
                         "odds": c.get("odds") if c else None} for L, c in zip(w["legs"], cur)]}
        with LOCK:
            d = os.path.join(RAW, now().strftime("%Y-%m-%d")); os.makedirs(d, exist_ok=True)
            with gzip.open(os.path.join(d, "depth_" + now().strftime("%H") + ".jsonl.gz"), "at") as f: f.write(json.dumps(rec) + "\n")


def run_watches(game, t_reopt):
    """Re-check the followed Polymarket/Kalshi gaps of this game whose next delay (30 s, 1, 2, 5 min) has come."""
    for w in [w for w in game.watches if w["kind"] == "pm_ks"]:
        el = time.time() - w["ts"]
        due = [l for l in w["lags"] if el >= l - 5]
        if not due: continue
        w["lags"] = [l for l in w["lags"] if l not in due]
        measure(game, w, el, due, "recheck", t_reopt)
        if not w["lags"]: game.watches.remove(w)


def close_watches(game, reason):
    """The game left the window (kick-off) or the run ended: delays not reached are recorded as censored."""
    for w in game.watches:
        for l in w["lags"]:
            append_csv(os.path.join(RES, "rechecks.csv"), {"time": iso(now()), "watch": w["id"], "kind": w["kind"],
                       "game": game.m["id"], "title": game.m["title"], "league": game.m["league"],
                       "min_to_ko": round((game.ko - now()).total_seconds() / 60, 1), "lag_s": round(time.time() - w["ts"], 1),
                       "detected": w["detected"], "recheck": l, "t_detected": round(w["t0"], 6), "t_same_portfolio": "",
                       "legs_quoted": "", "t_best_now": "", "still_profitable": "", "above_threshold": "",
                       "status": f"censored ({reason})"})
    game.watches, game.wid = [], None


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


def leg_payout(L, tr, keys):
    """Payout of one leg once known, else None. Polymarket/Kalshi: official resolution; bookmakers: final score."""
    if not L["venue"].startswith("BK:"):
        p = resolution(L)
        return None if p is None else L["shares"] * (p if L["side"] == "YES" else 1 - p)
    ev = tr.get("event") or {}
    if not keys or not keys.keys or not ev.get("sport"): return None
    events = bk.scores(keys, ev["sport"], time.time())
    sc = bk.final_score(events, ev["id"], ev["home"], ev["away"])
    return None if sc is None else L["stake"] * bk.leg_return(L, sc[0], sc[1])


def settle(st, keys=None):
    keep = []
    for tr in st["open"]:
        sport = "football" if tr["league"] not in US else tr["league"]
        if now() < parse(tr["kickoff"]) + dt.timedelta(hours=SETTLE_AFTER_H[sport]): keep.append(tr); continue
        pays = [leg_payout(L, tr, keys) for L in tr["legs"]]
        if any(p is None for p in pays): keep.append(tr); continue
        total = 0.0
        for L, v in zip(tr["legs"], pays):
            total += v; ac.unlock(st, L["venue"], L["cost"], v)
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
    rows = [{k: v for k, v in t.items() if k not in ("legs", "event")} | {"n_legs": len(t["legs"])} for t in trades.values()]
    if rows:
        cols = list(dict.fromkeys(k for r in rows for k in r))
        with open(os.path.join(RES, "trades.csv"), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    count = lambda path: (lambda rs: {a: sum(1 for r in rs if r["action"] == a) for a in sorted({r["action"] for r in rs})})(
        list(csv.DictReader(open(path))) if os.path.exists(path) else [])
    acts, bacts = count(os.path.join(RES, "opportunities.csv")), count(os.path.join(RES, "opportunities_books.csv"))
    usd = lambda v: f"${v:,.2f}"
    eur = lambda v: f"€{v / FX:,.2f}"
    start = sum(st["start_cash"].values()); locked = sum(st["locked"].values()); transit = ac.in_transit(st)
    equity = sum(st["cash"].values()) + locked + transit
    days = max(1e-9, (now() - parse(st["started"])).total_seconds() / 86400)
    books = sorted(v for v in st["start_cash"] if v.startswith("BK:"))
    done = [t for t in trades.values() if t["status"] == "settled"]
    pnl = lambda ts: sum(t.get("pnl", 0.0) for t in ts)
    wb = [t for t in done if t.get("with_books")]; sp = [t for t in wb if t.get("spain_only")]
    peak = st["peak_total_locked"]
    capital = (f"Started {st['started']}. **Unlimited capital** (test of the opportunities): cash never limits a trade; "
               "Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers "
               f"(which publish no depth) are capped at {usd(CAP_BOOK_TRADE)}. The capital the strategy needed is the peak money "
               f"in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi "
               f"{usd(st['start_cash']['PM'])} each, €{ac.BOOK_START / FX:,.0f} per bookmaker) and may go below zero. "
               f"Euro amounts at {FX} USD/EUR." if UNLIMITED else
               f"Started {st['started']}. Fictional capital: Polymarket {usd(st['start_cash']['PM'])} + Kalshi "
               f"{usd(st['start_cash']['KS'])} (≈ €10,000) and €{ac.BOOK_START / FX:,.0f} at each bookmaker the bot has used "
               f"({len(books)} so far): {usd(start)} ≈ {eur(start)} in total. Euro amounts at {FX} USD/EUR.")
    ret = (f"| Return so far (realised / peak money in use) | {100 * st['realized_pnl'] / peak:.3f}% over {days:.1f} days |"
           if UNLIMITED and peak > 0 else
           f"| Return so far (realised / capital) | {100 * st['realized_pnl'] / start:.3f}% over {days:.1f} days |")
    lines = [f"# Paper-trading bot: status at {iso(now())}", "", capital, "",
             "| | |", "|---|---|",
             f"| Trades executed / settled | {st['n_trades']} / {st['n_settled']} |",
             f"| Realised profit | {usd(st['realized_pnl'])} ≈ {eur(st['realized_pnl'])} |",
             f"| … Polymarket/Kalshi only | {usd(pnl([t for t in done if not t.get('with_books')]))} |",
             f"| … with bookmakers (all) | {usd(pnl(wb))} |",
             f"| … with bookmakers licensed in Spain only | {usd(pnl(sp))} |",
             f"| Open positions (cost) | {usd(locked)} |",
             f"| Money in transit between accounts | {usd(transit)} |",
             f"| Equity (cash + open at cost + in transit) | {usd(equity)} ≈ {eur(equity)} |",
             ret, "",
             "Polymarket/Kalshi gaps above the threshold: " + (", ".join(f"{k} {v}" for k, v in acts.items()) or "none yet") + ".",
             "Gaps using bookmakers: " + (", ".join(f"{k} {v}" for k, v in bacts.items() if k != "no gap") or "none yet") +
             f" (snapshots combined with Polymarket/Kalshi: {sum(bacts.values())}).", "",
             "`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation",
             "snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to",
             "fill, or not enough cash on an account.", ""]
    dl = STATUS.get("odds_days_left")
    if STATUS.get("odds_credits_usable") is not None:
        lines += [f"The Odds API credits left: {STATUS['odds_credits_usable']:,}" + (f" (about {dl:.1f} days at the current pace)" if dl else "")
                  + (". **Add keys soon: below 3 days only the last 3 snapshots per kick-off are taken.**" if dl is not None and dl < 4 else "."), ""]
    lines += ["## Capital by account", "", "Peak in use = the most money that was tied up in open positions at the same time.",
              "", "| account | start | cash now | in open positions | peak in use | lowest cash |", "|---|---|---|---|---|---|"]
    for v in ["PM", "KS"] + books:
        name = {"PM": "Polymarket", "KS": "Kalshi"}.get(v, v[3:] + (" (Spain)" if v[3:] in bk.SPAIN else ""))
        lines.append(f"| {name} | {usd(st['start_cash'][v])} | {usd(st['cash'][v])} | {usd(st['locked'].get(v, 0.0))} | "
                     f"{usd(st['peak_locked'].get(v, 0.0))} | {usd(st['min_cash'].get(v, st['cash'][v]))} |")
    ts = st["transfer_stats"]
    lines += ["", f"Peak money in use across all accounts at the same time: {usd(st['peak_total_locked'])} ≈ "
              f"{eur(st['peak_total_locked'])}.", "",
              f"Transfers between accounts: {ts['count']} ({usd(ts['moved'])} moved, {usd(ts['fees'])} in fees; "
              f"{len(st['transfers'])} still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min "
              "each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).", ""]
    lines += follow_summary()
    if rows:
        lines += ["## Last trades", "", "| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |",
                  "|---|---|---|---|---|---|---|---|---|---|"]
        for t in sorted(trades.values(), key=lambda t: -t["trade_id"])[:25]:
            pl = "" if t.get("pnl") is None else f"${t['pnl']:+.2f}"
            wbk = ", ".join(t.get("books", [])) if t.get("with_books") else "no"
            lines.append(f"| {t['trade_id']} | {t['time'][5:16]} | {t['title']} | {t['min_to_ko']} | {wbk} | {100 * t['t_lp']:.2f}% | "
                         f"${t['cost']:.2f} | ${t['guaranteed_profit']:.2f} | {t['status']} | {pl} |")
    open(os.path.join(RES, "summary.md"), "w").write("\n".join(lines) + "\n")


def follow_summary():
    """Followed gaps: how many are still profitable when the same portfolio is re-priced later, and their depth."""
    read = lambda n: list(csv.DictReader(open(os.path.join(RES, n)))) if os.path.exists(os.path.join(RES, n)) else []
    rc, det = read("rechecks.csv"), [r for r in read("depth.csv") if r["measure"] == "detection"]
    if not det: return []
    lines = ["## Gaps followed: the same portfolio re-checked later, and order-book depth", "",
             f"Gaps above {100 * WATCH_THRESH:.1f}% followed: {sum(r['kind'] == 'pm_ks' for r in det)} Polymarket/Kalshi and "
             f"{sum(r['kind'] == 'with_books' for r in det)} with bookmakers. A re-check prices the same shares and stakes at the "
             "later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.", "",
             "| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |", "|---|---|---|---|---|---|"]
    names = {**{str(l): (f"+{l} s" if l < 60 else f"+{l // 60} min") for l in RECHECK_SEC},
             "confirmation": "bookmaker confirmation (~1 min)", "scheduled": "next bookmaker snapshot"}
    for tg, name in names.items():
        rows = [r for r in rc if r["recheck"] == tg]
        if not rows: continue
        ok = [r for r in rows if r["status"] == "ok"]
        lines.append(f"| {name} | {len(ok)} | {sum(r['still_profitable'] == 'True' for r in ok)} | "
                     f"{sum(r['above_threshold'] == 'True' for r in ok)} | {sum(r['status'] == 'leg_not_quoted' for r in rows)} | "
                     f"{sum(r['status'].startswith('censored') for r in rows)} |")
    med = lambda v: sorted(v)[len(v) // 2] if v else None
    caps = [float(r["capacity"]) for r in det if r["capacity"] not in ("", None)]
    bp = [float(r["best_profit"]) for r in det if r["best_profit"] not in ("", None)]
    if caps:
        lines += ["", f"Depth at detection ({len(caps)} gaps with full order books): median capacity (largest size still "
                  f"profitable after walking the order books) ${med(caps):,.0f}; median largest guaranteed profit "
                  f"${med(bp):,.2f}. Details: `results/rechecks.csv`, `results/depth.csv`."]
    return lines + [""]


def write_status(st, games, start_code, t_start):
    """Public health file (no secrets): lets the run be checked without access to the Actions logs."""
    STATUS["score_calls"] = bk.SCORE_CALLS[0]
    json.dump({"run": st["runs"], "run_started": iso(dt.datetime.fromtimestamp(t_start, dt.timezone.utc)),
               "last_update": iso(now()), "code_version": (start_code[0] or "")[:12],
               "private_raw_storage": bool(RAW), "odds_api_keys": STATUS.get("odds_keys", {}),
               "odds_credits_remaining": {f"ODDS_API_KEY_{i}": r for i, r in sorted(st.get("odds", {}).get("remaining", {}).items())},
               "odds_credits_spent_today": st.get("odds", {}).get("spent", {}).get(now().strftime("%Y-%m-%d"), 0),
               "odds_credits_days_left_at_current_pace": STATUS.get("odds_days_left"),
               "bookmaker_accounts_opened": sum(1 for v in st["start_cash"] if v.startswith("BK:")),
               "transfers_in_transit": len(st["transfers"]),
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
    log(f"run {st['runs']} | window {WINDOW_H} h | poll {POLL_SEC} s | threshold {100 * THRESH:.2f}% | "
        + (f"unlimited capital (bookmaker trades up to ${CAP_BOOK_TRADE:.0f})" if UNLIMITED else f"cap ${CAP_PER_TRADE:.0f}")
        + f" | private raw storage: {'yes' if RAW else 'no'}")
    pool = ThreadPoolExecutor(int(os.environ.get("WORKERS", 8)))
    while time.time() - t_start < MAX_RUNTIME_MIN * 60:
        t0 = time.time(); active = []
        try:
            if t0 - last_disc > DISCOVER_MIN * 60: discover(games); last_disc = t0
            fetch_books(games, keys, st)
            d = keys.days_left(); STATUS["odds_credits_usable"] = keys.usable()
            STATUS["odds_days_left"] = round(d, 1) if d != float("inf") else None
            active = [g for g in games.values() if g.ko - dt.timedelta(hours=WINDOW_H) <= now() < g.ko - dt.timedelta(minutes=1)]
            for g, res in zip(active, pool.map(lambda g: check(g, st), active)):
                try: handle(g, st, res)
                except Exception: log("handle error", g.m["id"], traceback.format_exc(limit=2)); STATUS["errors"] += 1
            for g in games.values():                                  # followed gaps of games that left the window
                if g.watches and g not in active: close_watches(g, "kick-off")
            for t in ac.arrive(st, time.time()):
                log(f"transfer arrived: {t['src']} -> {t['dst']} ${t['amount'] - t['fee']:,.2f}")
            if t0 - last_settle > 600:
                settle(st, keys); last_settle = t0
                for t in ([] if UNLIMITED else ac.rebalance(st, time.time())):   # no transfers needed if unlimited
                    log(f"transfer started: {t['src']} -> {t['dst']} ${t['amount']:,.2f} (fee ${t['fee']:,.2f}, "
                        f"{(t['arrive'] - t['depart']) / 3600:.2f} h)")
                    append_csv(os.path.join(RES, "transfers.csv"), {"time": iso(now()), "from": t["src"], "to": t["dst"],
                               "amount_usd": t["amount"], "fee_usd": t["fee"], "hours": round((t["arrive"] - t["depart"]) / 3600, 2)})
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
    for g in games.values():
        if g.watches: close_watches(g, "end of run")
    settle(st, keys); save_state(st); report(st); write_status(st, games, start_code, t_start); git_commit(f"bot: end of run {iso(now())}")
    log("done")


if __name__ == "__main__":
    main()
