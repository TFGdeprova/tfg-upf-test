"""Order-book depth: how much money a detected gap can absorb before prices move against it (slippage).

A gap is a portfolio found by the linear program at the best prices: n_i shares (or dollars staked, for a bookmaker)
per unit of budget, with a guaranteed payout g per unit of budget in every final score. Investing S units means buying
S * n_i shares of each leg. Walking each leg's order book (price levels, cheapest first, with the venue's fee at each
level) gives the real cost of those shares, so the guaranteed profit at size S is S * g - cost(S). Bookmaker legs have no
public depth and are taken at fixed odds (their limit is the bookmaker account). Polymarket and Kalshi books come from
the venues' public endpoints; the ladders are kept up to 60 levels or USD 20,000 per side (common.trim).
"""
import math
import numpy as np
from .common import KS_FEE

SIZES = (50, 100, 250, 500, 1000, 2500, 5000, 10000)           # budget sizes reported (US dollars at best prices)
GRID = np.unique(np.round(np.geomspace(5, 20000, 90), 2))       # sizes searched for the best size and the capacity


EMPTY = {k: "" for S in SIZES for k in (f"profit_{S}", f"ret_{S}")} | {"best_size": "", "best_profit": "", "capacity": "",
                                                                        "book_exhausted": ""}   # same columns as curve()


def fee_pm(rate):
    return lambda q, p: rate * q * p * (1 - p)                  # Polymarket taker fee: rate * shares * p * (1 - p)


def fee_ks(q, p):
    return math.ceil(KS_FEE * q * p * (1 - p) * 100 - 1e-9) / 100   # Kalshi: rounded up to the cent on each fill


def walk(ladder, n, fee):
    """Cost of buying n shares by walking the ladder [(price, shares)], fees included; None if the book is too thin."""
    cost, left = 0.0, n
    for p, s in ladder:
        q = min(left, s)
        cost += q * p + (fee(q, p) if fee else 0.0); left -= q
        if left <= 1e-9: return cost
    return None if left > 1e-9 else cost


def cost_at(legs, S):
    """Cost of S budget units of the portfolio, or None if some order book is too thin."""
    total = 0.0
    for L in legs:
        n = S * L["n"]
        if L.get("ladder") is None: total += n * L["price"]; continue     # bookmaker stake (fixed odds) or fixed price
        c = walk(L["ladder"], n, L.get("fee"))
        if c is None: return None
        total += c
    return total


def curve(legs, g):
    """Guaranteed profit and return of the portfolio at each reported size, the size with the largest profit, and the
    largest size that still has a guaranteed profit (capacity).

    legs: [{"n": shares per budget unit, "ladder": [(price, shares)] or None, "price": fixed price if no ladder,
            "fee": fee function or None}]; g: guaranteed payout per budget unit."""
    out = {}
    for S in SIZES:
        c = cost_at(legs, S)
        out[f"profit_{S}"] = "" if c is None else round(S * g - c, 4)
        out[f"ret_{S}"] = "" if c is None or c <= 0 else round((S * g - c) / c, 6)
    best_S, best_p, cap, exhausted = 0.0, 0.0, 0.0, False
    for S in GRID:
        c = cost_at(legs, S)
        if c is None: exhausted = True; break
        p = S * g - c
        if p > best_p: best_S, best_p = S, p
        if p > 0: cap = S
        elif cap > 0: break                                            # profit has turned negative: capacity found
    out.update(best_size=round(float(best_S), 2), best_profit=round(float(best_p), 4), capacity=round(float(cap), 2),
               book_exhausted=exhausted)
    return out
