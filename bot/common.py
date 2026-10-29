"""HTTP helpers, time helpers and the arbitrage linear program shared by the bot."""
import json, time, datetime as dt, urllib.request, urllib.parse, urllib.error
import numpy as np
from scipy.optimize import linprog

UA = {"User-Agent": "Mozilla/5.0 (academic research; UPF TFG paper-trading bot)", "Accept": "application/json"}
KS = "https://api.elections.kalshi.com/trade-api/v2"
GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"
KS_FEE = 0.07                      # Kalshi taker fee: ceil(0.07 * C * P * (1 - P)) cents per order


def get(url, params=None, retries=3, timeout=30):
    if params: url += ("&" if "?" in url else "?") + urllib.parse.urlencode(params, doseq=True)
    for i in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and i < retries - 1: time.sleep(2 ** (i + 1)); continue
            raise
        except Exception:
            if i < retries - 1: time.sleep(2 ** (i + 1)); continue
            raise


def post(url, body, retries=3, timeout=30):
    data = json.dumps(body).encode()
    for i in range(retries):
        try:
            req = urllib.request.Request(url, data=data, headers={**UA, "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read())
        except Exception:
            if i < retries - 1: time.sleep(2 ** (i + 1)); continue
            raise


def now(): return dt.datetime.now(dt.timezone.utc)
def iso(t): return t.strftime("%Y-%m-%dT%H:%M:%SZ")
def parse(s): return dt.datetime.fromisoformat(s.replace("Z", "+00:00").replace(" ", "T"))


def pm_books(tokens):
    """Best ask / best bid (price, size) of Polymarket tokens: {token: (ask, ask_size, bid, bid_size)}."""
    out = {}
    for i in range(0, len(tokens), 50):
        try: books = post(f"{CLOB}/books", [{"token_id": t} for t in tokens[i:i + 50]])
        except Exception: continue
        for b in books:
            asks = sorted(((float(x["price"]), float(x["size"])) for x in b.get("asks", [])), key=lambda z: z[0])
            bids = sorted(((float(x["price"]), float(x["size"])) for x in b.get("bids", [])), key=lambda z: -z[0])
            out[b.get("asset_id")] = (asks[0] if asks else (None, 0.0)) + (bids[0] if bids else (None, 0.0))
    return out


def ks_event_markets(event_ticker):
    try: return get(f"{KS}/markets", {"event_ticker": event_ticker, "limit": 500}).get("markets", [])
    except Exception: return []


def fnum(x):
    try: return float(x)
    except (TypeError, ValueError): return None


def ks_quote(m):
    """(yes_ask, yes_ask_size, no_ask, no_ask_size) of a Kalshi market from the market list (dollars, contracts)."""
    ya, ys = fnum(m.get("yes_ask_dollars")), fnum(m.get("yes_ask_size_fp")) or 0.0
    yb, bs = fnum(m.get("yes_bid_dollars")), fnum(m.get("yes_bid_size_fp")) or 0.0
    na = fnum(m.get("no_ask_dollars"))
    if na is None and yb: na = 1 - yb
    return (ya if ya and 0 < ya < 1 else None, ys, na if na and 0 < na < 1 else None, bs)


def solve(R):
    """max t s.t. R x >= 1 + t (every state), sum x = 1, x >= 0.  R: states x tickets gross returns per unit invested."""
    if R.shape[1] < 2: return np.nan, None
    ns, n = R.shape
    c = np.zeros(n + 1); c[-1] = -1.0
    A_ub = np.hstack([-R, np.ones((ns, 1))]); b_ub = -np.ones(ns)
    A_eq = np.zeros((1, n + 1)); A_eq[0, :n] = 1.0
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=[1.0], bounds=[(0, 1)] * n + [(None, None)], method="highs")
    if res.status != 0: return np.nan, None
    return float(res.x[-1]), res.x[:n]
