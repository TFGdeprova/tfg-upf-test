"""Bookmaker odds (The Odds API) for the games the bot follows: one snapshot per sport shortly before each kick-off.

Bookmaker legs are a *measurement*, not paper trades: one snapshot per kick-off cannot pass the bot's persistence check,
stake limits are unknown and several books are offshore. Each snapshot is combined with the Polymarket and Kalshi prices
of the same minute and the result is logged separately (results/opportunities_books.csv).

Credits: one /odds call per sport returns every upcoming event of that sport and costs (markets x regions) credits.
Keys: ODDS_API_KEY_1..5 (GitHub secrets). They are never printed: request URLs and exceptions are not logged.
Raw odds go only to the private repository (The Odds API terms forbid redistributing raw data); the public results
contain only the few odds used in a detected opportunity (derived data, which the terms allow).
"""
import os, json, gzip, urllib.request, urllib.error, datetime as dt
import numpy as np
from .common import UA, now, iso, parse
from .grid import predicate, asian_total

SPORTS = {"epl": "soccer_epl", "lal": "soccer_spain_la_liga", "sea": "soccer_italy_serie_a", "bun": "soccer_germany_bundesliga",
          "fl1": "soccer_france_ligue_one", "ere": "soccer_netherlands_eredivisie", "elc": "soccer_efl_champ",
          "scop": "soccer_spl", "ucl": "soccer_uefa_champs_league", "uel": "soccer_uefa_europa_league",
          "nba": "basketball_nba", "nfl": "americanfootball_nfl", "nhl": "icehockey_nhl"}
US = ("nba", "nfl", "nhl")
COMMISSION = {"betfair_ex_uk": 0.05, "betfair_ex_eu": 0.05, "betfair_ex_au": 0.05, "matchbook": 0.02, "smarkets": 0.02}
SKIP_BOOKS = ("kalshi", "polymarket")                          # already covered directly by the bot
E = lambda k, d: type(d)(os.environ.get(k, d))
RESERVE = E("ODDS_RESERVE", 20)                                # never spend the last credits of a key
RESET_DAY = E("ODDS_RESET_DAY", 29)                            # day of the month the free credits renew
SNAP_MIN, SNAP_MAX = E("BOOK_SNAP_MIN", 8), E("BOOK_SNAP_MAX", 30)   # snapshot window: minutes before kick-off


def params(league):
    return ("h2h,spreads,totals", "us") if league in US else ("h2h,totals", "uk,eu")


def cost(league):
    m, r = params(league); return len(m.split(",")) * len(r.split(","))


class Keys:
    """The five keys, their remaining credits (persisted in state.json) and a daily budget."""
    def __init__(self, st):
        self.keys = {str(i): os.environ.get(f"ODDS_API_KEY_{i}", "").strip() for i in range(1, 6)}
        self.keys = {i: k for i, k in self.keys.items() if k}
        self.st = st.setdefault("odds", {"remaining": {}, "spent": {}})

    def remaining(self): return {i: self.st["remaining"].get(i, 500) for i in self.keys}

    def daily_cap(self):
        t = now().date()
        nxt = t.replace(day=RESET_DAY) if t.day < RESET_DAY else (t.replace(day=1) + dt.timedelta(days=32)).replace(day=RESET_DAY)
        left = sum(max(0, r - RESERVE) for r in self.remaining().values())
        return max(8, int(1.5 * left / max(1, (nxt - t).days)))

    def call(self, sport, markets, regions, credits):
        today = now().strftime("%Y-%m-%d")
        if self.st["spent"].get(today, 0) + credits > self.daily_cap(): return None, "daily budget reached"
        cands = [(r, i) for i, r in self.remaining().items() if r - credits >= RESERVE]
        if not cands: return None, "no credits left"
        i = max(cands)[1]
        url = (f"https://api.the-odds-api.com/v4/sports/{sport}/odds?regions={regions}&markets={markets}"
               f"&oddsFormat=decimal&apiKey={self.keys[i]}")
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
                data = json.loads(r.read())
                rem = r.headers.get("x-requests-remaining")
            self.st["remaining"][i] = int(float(rem)) if rem is not None else self.remaining()[i] - credits
            self.st["spent"][today] = self.st["spent"].get(today, 0) + credits
            self.st["spent"] = {d: v for d, v in self.st["spent"].items() if d >= (now() - dt.timedelta(days=40)).strftime("%Y-%m-%d")}
            return data, f"ok (key slot {i})"
        except urllib.error.HTTPError as e:                     # never log the exception text (it could carry the URL)
            if e.code in (401, 429): self.st["remaining"][i] = 0
            return None, f"HTTP {e.code} (key slot {i})"
        except Exception:
            return None, f"network error (key slot {i})"


def raw_write(raw_dir, sport, data):
    if not raw_dir: return
    d = os.path.join(raw_dir, "books", now().strftime("%Y-%m-%d")); os.makedirs(d, exist_ok=True)
    with gzip.open(os.path.join(d, now().strftime("%H") + ".jsonl.gz"), "at") as f:
        f.write(json.dumps({"t": iso(now()), "sport": sport, "events": data}) + "\n")


def match_event(game, events, sim=None):
    """The Odds API event of this game: kick-off within 30 minutes and both teams recognised.
    Returns (event, {odds-api team name: 'home'|'away'}) or (None, None)."""
    ko = parse(game["kickoff"])
    for ev in events:
        if abs((parse(ev["commence_time"]) - ko).total_seconds()) > 1800: continue
        names = (ev["home_team"], ev["away_team"])
        if game["sport"] == "football":
            s1 = min(sim(names[0], game["home"]), sim(names[1], game["away"]))
            s2 = min(sim(names[0], game["away"]), sim(names[1], game["home"]))
            if max(s1, s2) < 0.6: continue
            return ev, ({names[0]: "home", names[1]: "away"} if s1 >= s2 else {names[0]: "away", names[1]: "home"})
        norm = lambda s: "".join(ch for ch in s.lower() if ch.isalnum())
        side = {}
        for nm in names:
            hit = [sd for nick, sd in game["side"].items() if nick and nick in norm(nm)]
            if len(set(hit)) == 1: side[nm] = hit[0]
        if len(side) == 2 and len(set(side.values())) == 2: return ev, side
    return None, None


def best_lines(ev, side):
    """Best odds per (market, outcome, line) across bookmakers, after exchange commission.
    Returns [{"market", "outcome", "side", "point", "odds", "eff", "book"}]."""
    best = {}
    for bk in ev.get("bookmakers", []):
        if any(s in bk["key"] for s in SKIP_BOOKS): continue
        c = COMMISSION.get(bk["key"], 0.0)
        for mk in bk.get("markets", []):
            if mk["key"] not in ("h2h", "spreads", "totals"): continue
            for o in mk.get("outcomes", []):
                d = float(o.get("price") or 0)
                if d <= 1.0: continue
                sd = side.get(o["name"]) if mk["key"] != "totals" else o["name"].lower()
                if mk["key"] == "h2h" and o["name"].lower() == "draw": sd = "draw"
                if sd is None: continue
                key = (mk["key"], sd, o.get("point"))
                eff = 1 + (d - 1) * (1 - c)
                if key not in best or eff > best[key]["eff"]:
                    best[key] = {"market": mk["key"], "outcome": o["name"], "side": sd, "point": o.get("point"),
                                 "odds": d, "eff": eff, "book": bk["key"]}
    return list(best.values())


def payoff_football(L):
    """Gross return per 1 staked over the football score grid (169 states)."""
    if L["market"] == "h2h":
        k = {"home": "home_win", "away": "away_win", "draw": "draw"}[L["side"]]
        return predicate(k).astype(float) * L["eff"]
    if L["market"] == "totals" and L["point"] is not None:
        return asian_total(L["side"] == "over", float(L["point"]), L["eff"])
    return None


def payoff_us(L, g):
    """Gross return per 1 staked over a US score grid (official score; pushes return the stake)."""
    h, a = g.scores(True)
    if L["market"] == "totals":
        if L["point"] is None: return None
        diff = (h + a - float(L["point"])) * (1 if L["side"] == "over" else -1)
    else:
        mine, other = (h, a) if L["side"] == "home" else (a, h)
        diff = (mine - other) + (float(L["point"]) if L["market"] == "spreads" and L["point"] is not None else 0.0)
        if L["market"] == "spreads" and L["point"] is None: return None
    return np.where(diff > 1e-9, L["eff"], np.where(np.abs(diff) <= 1e-9, 1.0, 0.0))
