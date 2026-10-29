"""State space of a football match (final score after 90' + stoppage) and payoff functions.

Each outcome is a final score (h, a) with 0 <= h, a <= MAXG. The last value MAXG means "MAXG or more",
which is exact for all contracts whose lines are below MAXG - 0.5 (true for every line we use).
"""
import numpy as np

MAXG = 12
H, A = np.meshgrid(np.arange(MAXG + 1), np.arange(MAXG + 1), indexing="ij")
H, A = H.ravel(), A.ravel()          # one entry per state
N_STATES = H.size


def predicate(kind, side=None, line=None, h=None, a=None, listed=None):
    """Boolean vector over states for a binary event.

    kind: home_win | draw | away_win | total_over | team_over | margin_over | btts | exact | exact_other
    side: 'home' | 'away' (for team_over / margin_over)
    line: e.g. 2.5
    """
    if kind == "home_win":   return H > A
    if kind == "away_win":   return A > H
    if kind == "draw":       return H == A
    if kind == "total_over": return H + A > line
    if kind == "btts":       return (H > 0) & (A > 0)
    if kind == "team_over":  return (H if side == "home" else A) > line
    if kind == "margin_over":                       # side wins by more than `line` goals
        m = H - A if side == "home" else A - H
        return m > line
    if kind == "exact":      return (H == h) & (A == a)
    if kind == "exact_other":                       # complement of a listed set of exact scores
        hit = np.zeros(N_STATES, bool)
        for (x, y) in listed: hit |= (H == x) & (A == y)
        return ~hit
    raise ValueError(kind)


def asian_handicap(side, hcap, odds):
    """Gross return per 1 unit staked on an Asian handicap bet (stake included), per state.

    hcap is the handicap applied to `side` (e.g. -0.75). Quarter lines are split in two half-stakes.
    Whole lines can push (stake returned).
    """
    q = hcap * 4
    parts = [hcap] if abs(q - round(q)) < 1e-9 and round(q) % 2 == 0 else [hcap - 0.25, hcap + 0.25]
    m = (H - A) if side == "home" else (A - H)
    out = np.zeros(N_STATES)
    for L in parts:
        adj = m + L
        out += np.where(adj > 1e-9, odds, np.where(np.abs(adj) <= 1e-9, 1.0, 0.0)) / len(parts)
    return out


def asian_total(over, line, odds):
    """Gross return per 1 unit staked on an (Asian) total: half lines win/lose, whole lines push at equality,
    quarter lines are split in two half-stakes (e.g. 2.25 = half on 2.0 and half on 2.5)."""
    q = line * 4
    parts = [line] if abs(q - round(q)) < 1e-9 and round(q) % 2 == 0 else [line - 0.25, line + 0.25]
    tot = H + A
    out = np.zeros(N_STATES)
    for L in parts:
        diff = (tot - L) if over else (L - tot)
        out += np.where(diff > 1e-9, odds, np.where(np.abs(diff) <= 1e-9, 1.0, 0.0)) / len(parts)
    return out
