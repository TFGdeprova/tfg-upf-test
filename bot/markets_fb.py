"""Live football matches listed on both Polymarket and Kalshi, contracts mapped onto the final-score grid (grid.py).

Contracts: 1X2, totals, spreads, both-teams-to-score, team totals, exact scores (90 minutes + stoppage time).
"""
import re, json, unicodedata, difflib, datetime as dt
from .common import get, GAMMA, KS, parse, now, ks_event_markets
from .grid import predicate

LEAGUES = {"epl": (10188, "EPL"), "lal": (10193, "LALIGA"), "sea": (10203, "SERIEA"), "bun": (10194, "BUNDESLIGA"),
           "fl1": (10195, "LIGUE1"), "ere": (10286, "EREDIVISIE"), "elc": (10355, "EFLCHAMPIONSHIP"),
           "scop": (10674, "SCOTTISHPREM"), "ucl": (10204, "UCL"), "uel": (10209, "UEL")}
KS_KINDS = ["GAME", "TOTAL", "SPREAD", "BTTS", "SCORE", "TEAMTOTAL"]
STOP = {"fc", "afc", "cf", "sc", "ac", "as", "ss", "us", "ssc", "rc", "rcd", "cd", "ud", "sd", "ca", "club", "de", "la", "the",
        "calcio", "vs", "sv", "fsv", "tsg", "vfl", "vfb", "bc", "1", "1899", "1846", "04", "05", "09", "sk", "fk", "bk", "kv"}
ALIAS = {"wolves": "wolverhampton", "man": "manchester", "utd": "united", "nott": "nottingham", "forest": "nottingham",
         "spurs": "tottenham", "ath": "athletic", "bilbao": "athletic", "m'gladbach": "monchengladbach",
         "gladbach": "monchengladbach", "psg": "paris", "st": "saint", "cologne": "koln", "qpr": "queens"}


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower().replace(".", " ").replace("-", " ")
    toks = [ALIAS.get(t, t) for t in re.findall(r"[a-z0-9']+", s)]
    return " ".join(t for t in toks if t not in STOP) or s


def sim(a, b):
    a, b = norm(a), norm(b)
    if a in b or b in a: return 1.0
    ta, tb = set(a.split()), set(b.split())
    return max(difflib.SequenceMatcher(None, a, b).ratio(), len(ta & tb) / max(1, min(len(ta), len(tb))))


def split_title(t):
    t = re.sub(r"\s*\(.*?\)\s*$", "", t or "")
    p = re.split(r"\s+vs\.?\s+|\s+v\s+|\s+at\s+", t, maxsplit=1)
    return (p[0].strip(), p[1].strip()) if len(p) == 2 else None


def resolver(names):
    def side(name):
        n = norm(name)
        exact = [s for s, L in names.items() if any(norm(x) == n for x in L)]
        if len(exact) == 1: return exact[0]
        sub = [s for s, L in names.items() if any(norm(x) in n or n in norm(x) for x in L if len(norm(x)) > 2)]
        if len(sub) == 1: return sub[0]
        sc = {s: max(sim(name, x) for x in L) for s, L in names.items()}
        (b, vb), (o, vo) = sorted(sc.items(), key=lambda kv: -kv[1])
        return b if vb >= 0.6 and vb - vo >= 0.15 else None
    return side


def discover(lg, horizon_h):
    sid, pref = LEAGUES[lg]; t0 = now()
    evs = get(f"{GAMMA}/events", {"series_id": sid, "closed": "false", "limit": 300,
                                  "end_date_min": (t0 - dt.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")})
    try: ks = get(f"{KS}/events", {"series_ticker": f"KX{pref}GAME", "status": "open", "limit": 200}).get("events", [])
    except Exception: ks = []
    games = []
    for e in evs:
        st = e.get("startTime"); tm = split_title((e.get("title") or "").split(" - ")[0])
        if not st or not tm or not re.match(r"^[a-z0-9]+-[a-z0-9]+-[a-z0-9]+-\d{4}-\d{2}-\d{2}$", e.get("slug", "")): continue
        if not (-5 <= (parse(st) - t0).total_seconds() / 60 <= horizon_h * 60): continue
        best, bs = None, 0
        for g in ks:
            t = split_title(g.get("title", ""))
            if not t: continue
            d = dt.datetime.strptime(g["event_ticker"].split("-")[1][:7], "%y%b%d").date()
            if abs((d - parse(st).date()).days) > 1: continue
            s = max(min(sim(t[0], tm[0]), sim(t[1], tm[1])), min(sim(t[1], tm[0]), sim(t[0], tm[1])))
            if s > bs: best, bs = g, s
        if not best or bs < 0.6: continue
        suf = best["event_ticker"].split("-", 1)[1]
        games.append({"id": f"{lg}:{suf}", "league": lg, "sport": "football", "kickoff": st, "pm_slug": e["slug"],
                      "ks_events": [f"KX{pref}{k}-{suf}" for k in KS_KINDS], "home": tm[0], "away": tm[1],
                      "title": f"{tm[0]} v {tm[1]}"})
    return games


def _side(game, extra=()):
    return resolver({"home": [game["home"], *[x[0] for x in extra]], "away": [game["away"], *[x[1] for x in extra]]})


def pm_contracts(game):
    ev = get(f"{GAMMA}/events", {"slug": game["pm_slug"]})
    if not ev: return []
    side = _side(game); out = []
    for m in ev[0].get("markets", []):
        if not m.get("clobTokenIds") or not m.get("acceptingOrders"): continue
        q, t, g = m.get("question", ""), m.get("sportsMarketType"), m.get("groupItemTitle") or ""
        pred = None
        if t == "moneyline" or (t is None and " win" in q):
            if "draw" in q.lower(): pred = predicate("draw")
            else:
                r = re.match(r"Will (.+?) win on", q); s = side(r.group(1)) if r else None
                pred = predicate(f"{s}_win") if s else None
        elif t == "totals" and m.get("line") is not None: pred = predicate("total_over", line=float(m["line"]))
        elif t == "both_teams_to_score": pred = predicate("btts")
        elif t == "spreads":
            r = re.match(r"Spread:\s*(.+?)\s*\(-([\d.]+)\)", q); s = side(r.group(1)) if r else None
            pred = predicate("margin_over", side=s, line=float(r.group(2))) if s else None
        elif t == "soccer_team_totals":
            r = re.search(r":\s*(.+?)\s+O/U\s+([\d.]+)", q); s = side(r.group(1)) if r else None
            pred = predicate("team_over", side=s, line=float(r.group(2))) if s else None
        elif t == "soccer_exact_score":
            r = re.search(r"(\d+)\s*-\s*(\d+)", g)
            pred = predicate("exact", h=int(r.group(1)), a=int(r.group(2))) if r else None
        if pred is None: continue
        fs = m.get("feeSchedule") or {}
        out.append({"venue": "PM", "id": m["conditionId"], "token": json.loads(m["clobTokenIds"])[0], "label": q,
                    "fee": float(fs.get("rate") or 0.0) if m.get("feesEnabled") else 0.0,
                    "min_size": float(m.get("orderMinSize") or 5), "payoff": pred.astype(float)})
    return out


def ks_contracts(game):
    side = _side(game); out = []
    for ev in game["ks_events"]:
        kind = ev.split("-", 1)[0]
        for m in ks_event_markets(ev):
            if m.get("status") not in ("active", "open"): continue
            y = re.sub(r"^(Goal Diff )?Reg Time:\s*", "", m.get("yes_sub_title") or "").replace("more than", "over")
            pred = None
            if kind.endswith("GAME"):
                if y.lower() in ("tie", "draw"): pred = predicate("draw")
                else:
                    s = side(y); pred = predicate(f"{s}_win") if s else None
            elif kind.endswith("TEAMTOTAL"):
                r = re.match(r"(.+?) over ([\d.]+)", y); s = side(r.group(1)) if r else None
                pred = predicate("team_over", side=s, line=float(r.group(2))) if s else None
            elif kind.endswith("TOTAL"):
                pred = predicate("total_over", line=float(m["floor_strike"])) if m.get("floor_strike") is not None else None
            elif kind.endswith("BTTS"): pred = predicate("btts")
            elif kind.endswith("SPREAD"):
                r = re.match(r"(.+?) wins by over ([\d.]+)", y); s = side(r.group(1)) if r else None
                pred = predicate("margin_over", side=s, line=float(r.group(2))) if s else None
            elif kind.endswith("SCORE"):
                r = re.search(r"(\d+)-(\d+)", y)
                if r:
                    a, b = int(r.group(1)), int(r.group(2))
                    if y.lower().startswith(("draw", "tie")): pred = predicate("exact", h=a, a=b)
                    else:
                        s = side(y.split(" wins")[0])
                        pred = predicate("exact", h=a, a=b) if s == "home" else predicate("exact", h=b, a=a) if s == "away" else None
            if pred is None: continue
            out.append({"venue": "KS", "id": m["ticker"], "label": m.get("yes_sub_title"), "market": m, "payoff": pred.astype(float)})
    return out
