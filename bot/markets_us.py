"""Live NBA / NFL / NHL games on both Polymarket and Kalshi, with every full-game contract mapped onto grid_us.

Same mapping as the historical study (audited against 147,719 resolutions): games matched on date and team codes;
contracts = winner, spreads, totals, team totals, winning-margin bands, odd/even, tie, both-teams-score.
"""
import re, json, datetime as dt
from .common import get, GAMMA, KS, parse, now, ks_event_markets

LEAGUES = {"nba": {"pm_series": 10345, "ks": ["GAME", "SPREAD", "TOTAL", "TEAMTOTAL", "WINMARGIN"]},
           "nfl": {"pm_series": 12185, "ks": ["GAME", "SPREAD", "TOTAL", "TEAMTOTAL", "WINMARGIN", "TIE", "BOTH"]},
           "nhl": {"pm_series": 10346, "ks": ["GAME", "SPREAD", "TOTAL", "TEAMTOTAL"]}}
ALIAS = {"nhl": {"MON": "MTL", "LAS": "VGK", "LAK": "LA", "CAL": "CGY", "UTAH": "UTA"}, "nfl": {"JAX": "JAC"}, "nba": {}}
PM_TYPES = {"moneyline", "spreads", "totals", "team_totals", "exact_margin", "basketball_odd_even"}
MON = {m: i + 1 for i, m in enumerate("JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split())}


def norm(s): return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def ks_games(lg):
    ev = get(f"{KS}/events", {"series_ticker": f"KX{lg.upper()}GAME", "status": "open", "limit": 200}).get("events", [])
    out = []
    for e in ev:
        suf = e["event_ticker"].split("-", 1)[1]
        m = re.match(r"(\w+) (?:at|vs) (\w+)", e.get("sub_title") or "")
        if not m: continue
        d = dt.date(2000 + int(suf[:2]), MON[suf[2:5]], int(suf[5:7]))
        out.append({"suffix": suf, "date": d, "away": m.group(1), "home": m.group(2)})
    return out


def pm_events(lg, horizon_h):
    t0 = now()
    ev = get(f"{GAMMA}/events", {"series_id": LEAGUES[lg]["pm_series"], "closed": "false", "limit": 300,
                                 "end_date_min": (t0 - dt.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")})
    out = []
    for e in ev:
        st = e.get("startTime")
        m = re.match(rf"{lg}-([a-z0-9]+)-([a-z0-9]+)-(\d{{4}}-\d{{2}}-\d{{2}})$", e.get("slug", ""))
        ml = next((x for x in e.get("markets", []) if x.get("sportsMarketType") == "moneyline"), None)
        if not (st and m and ml): continue
        mins = (parse(st) - t0).total_seconds() / 60
        if not (-5 <= mins <= horizon_h * 60): continue
        names = json.loads(ml["outcomes"]) if isinstance(ml["outcomes"], str) else ml["outcomes"]
        out.append({"slug": e["slug"], "codes": (m.group(1).upper(), m.group(2).upper()), "names": names,
                    "date": dt.date.fromisoformat(m.group(3)), "start": st})
    return out


def discover(lg, horizon_h):
    """Games starting within `horizon_h` hours that are listed on both venues."""
    ks = ks_games(lg); al = ALIAS[lg]; games = []
    for p in pm_events(lg, horizon_h):
        a1, a2 = (al.get(c, c) for c in p["codes"])
        g = next((g for g in ks if {a1, a2} == {g["away"], g["home"]} and abs((g["date"] - p["date"]).days) <= 1), None)
        if not g: continue
        side = {}
        for nm, code in zip(p["names"], p["codes"]):
            kc = al.get(code, code); side[norm(nm)] = "home" if kc == g["home"] else "away"
        games.append({"id": f"{lg}:{g['suffix']}", "league": lg, "sport": lg, "kickoff": p["start"], "pm_slug": p["slug"],
                      "ks_events": [f"KX{lg.upper()}{s}-{g['suffix']}" for s in LEAGUES[lg]["ks"]],
                      "home": g["home"], "away": g["away"], "side": side, "title": f"{g['away']} at {g['home']}"})
    return games


def pm_contracts(game):
    """Polymarket contracts of the game (refreshed: lines are added during the day)."""
    ev = get(f"{GAMMA}/events", {"slug": game["pm_slug"]})
    if not ev: return []
    side = lambda name: game["side"].get(norm(name))
    out = []
    for m in ev[0].get("markets", []):
        t = m.get("sportsMarketType"); q = m.get("question", "")
        if t not in PM_TYPES or not m.get("clobTokenIds") or not m.get("acceptingOrders"): continue
        toks = json.loads(m["clobTokenIds"]); outs = json.loads(m["outcomes"]) if isinstance(m["outcomes"], str) else m["outcomes"]
        fs = m.get("feeSchedule") or {}
        c = {"venue": "PM", "id": m["conditionId"], "token": toks[0], "label": q,
             "fee": float(fs.get("rate") or 0.0) if m.get("feesEnabled") else 0.0,
             "min_size": float(m.get("orderMinSize") or 5), "counts_so": game["sport"] != "nhl"}
        if t == "moneyline": c.update(kind="win", side=side(outs[0]))
        elif t == "spreads":
            r = re.match(r"Spread:\s*(.+?)\s*\(([-+]?[\d.]+)\)", q)
            if not r or norm(outs[0]) != norm(r.group(1)): continue
            c.update(kind="margin_over", side=side(r.group(1)), line=-float(r.group(2)))
        elif t == "totals":
            r = re.search(r"O/U\s*([\d.]+)", q)
            if not r or norm(outs[0]) != "over": continue
            c.update(kind="total_over", line=float(r.group(1)))
        elif t == "team_totals":
            r = re.match(r"(.+?) Team Total:\s*O/U\s*([\d.]+)", q)
            if not r or norm(outs[0]) != "over": continue
            c.update(kind="team_over", side=side(r.group(1)), line=float(r.group(2)))
        elif t == "exact_margin":
            r = re.match(r"Exact Margin:\s*(.+?) by (\d+)(?:-(\d+)|\+)", q)
            if not r or norm(outs[0]) != "yes": continue
            c.update(kind="margin_band", side=side(r.group(1)), lo=int(r.group(2)), hi=int(r.group(3)) if r.group(3) else None)
        elif t == "basketball_odd_even":
            if norm(outs[0]) != "odd": continue
            c.update(kind="odd")
        if c.get("kind") in ("win", "margin_over", "team_over", "margin_band") and c.get("side") is None: continue
        out.append(c)
    return out


def ks_contracts(game):
    """Kalshi contracts of the game with their current top of book (one request per series event)."""
    out = []
    for ev in game["ks_events"]:
        s = ev.split("-", 1)[0][len("KX") + len(game["sport"]):]
        for m in ks_event_markets(ev):
            if m.get("status") not in ("active", "open"): continue
            code = m["ticker"].rsplit("-", 1)[1]
            team = next((x for x in sorted((game["away"], game["home"]), key=len, reverse=True) if code.startswith(x)), None)
            sd = "home" if team == game["home"] else "away" if team == game["away"] else None
            k = m.get("floor_strike")
            c = {"venue": "KS", "id": m["ticker"], "label": m.get("yes_sub_title"), "counts_so": True, "market": m}
            if s == "GAME" and sd: c.update(kind="win", side=sd)
            elif s == "SPREAD" and sd and k is not None: c.update(kind="margin_over", side=sd, line=float(k))
            elif s == "TOTAL" and k is not None: c.update(kind="total_over", line=float(k))
            elif s == "TEAMTOTAL" and sd and k is not None: c.update(kind="team_over", side=sd, line=float(k))
            elif s == "WINMARGIN" and sd:
                r = re.match(r"(\d+)(?:TO(\d+)|PLUS)$", code[len(team):])
                if not r: continue
                c.update(kind="margin_band", side=sd, lo=int(r.group(1)), hi=int(r.group(2)) if r.group(2) else None)
            elif s == "TIE": c.update(kind="tie")
            elif s == "BOTH" and k is not None and m.get("strike_type") == "greater_or_equal": c.update(kind="both_ge", line=float(k))
            else: continue
            out.append(c)
    return out
