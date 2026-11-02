"""Fictional accounts, transfers between them and capital tracking.

Accounts: Polymarket ("PM") and Kalshi ("KS") in US dollars, and one account per bookmaker ("BK:<key>"), funded with
EUR 500 the first time the bot needs it. All amounts are kept in US dollars (EUR at a fixed rate for reporting).

Money moves only by transfer, with the delays and fees the venues document (checked 31 Oct 2026):
  * Polymarket: withdrawals "instant and free" (docs.polymarket.com/trading/bridge/withdraw); deposits are on-chain
    transfers (minutes).
  * Kalshi: crypto withdrawals "typically within 30 minutes", no fee; crypto deposits "typically up to 30 minutes",
    provider/network fees may apply (help.kalshi.com: Crypto Withdrawals, Crypto Deposits); crypto deposits carry no
    withdrawal hold (Security Holds). International accounts use card or crypto.
  * Bookmakers: deposits by card/PayPal are immediate; withdrawals take from a few hours (PayPal) to several days
    (bank transfer) plus the operator's review: 24 hours is assumed.
  * Dollars <-> euros (crypto exchange + SEPA instant): 2 hours and 0.5%.
Policy: every check of the accounts, an account whose free cash plus money already on its way is below LOW x its
target (its starting balance) is topped up to the target from accounts holding more than HIGH x their target,
fastest route first. Money in transit cannot be used.
"""
import os

E = lambda k, d: type(d)(os.environ.get(k, d))
FX = E("EUR_USD", 1.16)
BOOK_START = E("CASH_BOOK_EUR", 500.0) * FX           # EUR 500 per bookmaker, in dollars
LOW, HIGH, MIN_TRANSFER = E("REBAL_LOW", 0.5), E("REBAL_HIGH", 1.2), E("MIN_TRANSFER", 50.0)
# venue type -> (withdrawal hours, withdrawal fee rate, deposit hours, deposit fee rate, currency)
ROUTES = {"PM": (0.1, 0.0, 0.25, 0.0, "USD"), "KS": (0.5, 0.0, 0.5, 0.001, "USD"), "BK": (24.0, 0.0, 0.05, 0.0, "EUR")}
CONVERT_H, CONVERT_FEE = E("CONVERT_H", 2.0), E("CONVERT_FEE", 0.005)


def vtype(v): return "BK" if v.startswith("BK:") else v


def route(src, dst):
    """(hours, fee rate) of moving money from src to dst."""
    wo_h, wo_f, _, _, c1 = ROUTES[vtype(src)]
    _, _, de_h, de_f, c2 = ROUTES[vtype(dst)]
    conv = c1 != c2
    return wo_h + de_h + (CONVERT_H if conv else 0.0), wo_f + de_f + (CONVERT_FEE if conv else 0.0)


def init(st, start):
    """Add the account fields to a state (idempotent)."""
    st.setdefault("cash", dict(start)); st.setdefault("start_cash", dict(start))
    st.setdefault("locked", {v: 0.0 for v in st["cash"]})
    st.setdefault("peak_locked", {v: 0.0 for v in st["cash"]})
    st.setdefault("min_cash", {v: st["cash"][v] for v in st["cash"]})
    st.setdefault("transfers", [])                       # pending: {src, dst, amount, fee, depart, arrive}
    st.setdefault("transfer_stats", {"count": 0, "moved": 0.0, "fees": 0.0})
    st.setdefault("peak_total_locked", 0.0)


def open_book(st, key):
    """Bookmaker account, funded with EUR 500 the first time it is needed."""
    v = f"BK:{key}"
    if v not in st["cash"]:
        st["cash"][v] = BOOK_START; st["start_cash"][v] = BOOK_START
        st["locked"][v] = 0.0; st["peak_locked"][v] = 0.0; st["min_cash"][v] = BOOK_START
    return v


def lock(st, v, amount):
    st["cash"][v] -= amount; st["locked"][v] = st["locked"].get(v, 0.0) + amount
    st["peak_locked"][v] = max(st["peak_locked"].get(v, 0.0), st["locked"][v])
    st["min_cash"][v] = min(st["min_cash"].get(v, st["cash"][v]), st["cash"][v])
    st["peak_total_locked"] = max(st["peak_total_locked"], sum(st["locked"].values()) + in_transit(st))


def unlock(st, v, cost, payout):
    st["locked"][v] = max(0.0, st["locked"].get(v, 0.0) - cost); st["cash"][v] += payout


def in_transit(st): return sum(t["amount"] - t["fee"] for t in st.get("transfers", []))


def arrive(st, now_ts):
    """Credit the transfers that have arrived. Returns the list of arrived transfers."""
    done = [t for t in st["transfers"] if t["arrive"] <= now_ts]
    for t in done: st["cash"][t["dst"]] += t["amount"] - t["fee"]
    st["transfers"] = [t for t in st["transfers"] if t["arrive"] > now_ts]
    return done


def rebalance(st, now_ts):
    """Top up accounts below LOW x target from accounts above HIGH x target. Returns the transfers started."""
    started = []
    incoming = lambda v: sum(t["amount"] - t["fee"] for t in st["transfers"] if t["dst"] == v)
    target = st["start_cash"]
    low = sorted((v for v in st["cash"] if st["cash"][v] + incoming(v) < LOW * target[v]),
                 key=lambda v: (st["cash"][v] + incoming(v)) / target[v])
    for v in low:
        need = target[v] - st["cash"][v] - incoming(v)
        donors = [u for u in st["cash"] if u != v and st["cash"][u] > HIGH * target[u]]
        for u in sorted(donors, key=lambda u: (route(u, v)[0], -(st["cash"][u] - target[u]))):
            amt = min(need, st["cash"][u] - target[u])
            if amt < MIN_TRANSFER: continue
            hours, rate = route(u, v)
            st["cash"][u] -= amt
            st["min_cash"][u] = min(st["min_cash"].get(u, st["cash"][u]), st["cash"][u])
            t = {"src": u, "dst": v, "amount": round(amt, 2), "fee": round(amt * rate, 2), "depart": now_ts,
                 "arrive": now_ts + hours * 3600}
            st["transfers"].append(t); started.append(t)
            st["transfer_stats"]["count"] += 1; st["transfer_stats"]["moved"] += amt; st["transfer_stats"]["fees"] += t["fee"]
            need -= amt
            if need < MIN_TRANSFER: break
    return started
