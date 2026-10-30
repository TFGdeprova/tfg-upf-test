"""State space and payoffs for US team sports (NBA, NFL, NHL).

A state is the official final score (home h, away a) including overtime; NFL regular-season games can end tied,
NBA and NHL games cannot. NHL games decided by a shootout count the shootout as one goal for the winner (Kalshi rules).
Polymarket's NHL totals rules do not say how a shootout is counted, so every one-goal NHL result is duplicated with a
flag SO = 1 meaning "the shootout goal is NOT counted by contracts that may ignore it": an arbitrage has to pay in both
readings (conservative).

Payoffs are per share (YES pays 1, NO pays 1 - YES); NFL ties pay 0.5 to both sides of a winner market on both venues
("resolves 50-50"). States with identical payoffs for every contract of a match are merged (exact), so the LP has a
few hundred rows instead of tens of thousands.
"""
import numpy as np

MAXPTS = {"nba": 250, "nfl": 110, "nhl": 20}


class USGrid:
    def __init__(self, league, ties=None):
        n = MAXPTS[league]
        H, A = np.meshgrid(np.arange(n + 1), np.arange(n + 1), indexing="ij")
        H, A = H.ravel(), A.ravel()
        ties = (league == "nfl") if ties is None else ties
        keep = (H != A) | ties
        H, A = H[keep], A[keep]
        SO = np.zeros(H.size, bool)
        if league == "nhl":
            d = np.abs(H - A) == 1
            H, A, SO = np.r_[H, H[d]], np.r_[A, A[d]], np.r_[SO, np.ones(int(d.sum()), bool)]
        self.league, self.H, self.A, self.SO = league, H, A, SO

    def scores(self, counts_so=True):
        """(home, away) as seen by a contract; with counts_so=False the shootout goal is removed in SO states."""
        if counts_so or not self.SO.any(): return self.H, self.A
        h = self.H - (self.SO & (self.H > self.A)); a = self.A - (self.SO & (self.A > self.H))
        return h, a

    def payoff(self, c):
        """YES payoff per share of contract c (dict with kind, side, line, lo, hi, counts_so)."""
        h, a = self.scores(c.get("counts_so", True))
        kind, side, line = c["kind"], c.get("side"), c.get("line")
        mine, other = (h, a) if side == "home" else (a, h)
        if kind == "win":         return np.where(mine > other, 1.0, np.where(mine == other, 0.5, 0.0))
        if kind == "margin_over": return (mine - other > line).astype(float)
        if kind == "margin_band":
            m = mine - other; hi = c.get("hi")
            return ((m >= c["lo"]) & ((m <= hi) if hi is not None else True)).astype(float)
        if kind == "total_over":  return (h + a > line).astype(float)
        if kind == "team_over":   return (mine > line).astype(float)
        if kind == "tie":         return (h == a).astype(float)
        if kind == "odd":         return ((h + a) % 2 == 1).astype(float)
        if kind == "both_ge":     return ((h >= line) & (a >= line)).astype(float)
        raise ValueError(kind)

    def compressed(self, contracts):
        """Payoff matrix (unique states x contracts) for the given contracts; skipped contracts get None."""
        idx = [j for j, c in enumerate(contracts) if c.get("kind") not in (None, "skip")]
        if not idx: return {}, 0
        P = np.column_stack([self.payoff(contracts[j]) for j in idx])
        U = unique_rows(P)
        return {j: U[:, k] for k, j in enumerate(idx)}, U.shape[0]


_W1 = np.random.default_rng(12345).integers(1, 2 ** 62, size=8192, dtype=np.int64)
_W2 = np.random.default_rng(54321).integers(1, 2 ** 62, size=8192, dtype=np.int64)


def unique_rows(P, codes=False):
    """Distinct rows of a payoff matrix (values 0, 0.5, 1; or integer codes 0..255 with codes=True). Rows are hashed
    with two independent 64-bit hashes, column block by column block, so memory stays small even for NBA grids."""
    n = P.shape[1]; h1 = np.zeros(P.shape[0], np.int64); h2 = np.zeros(P.shape[0], np.int64)
    W1, W2 = np.resize(_W1, n), np.resize(_W2[::-1], n)
    for s in range(0, n, 64):
        c = P[:, s:s + 64].astype(np.int64) if codes else np.rint(P[:, s:s + 64] * 2).astype(np.int64)
        h1 += (c * W1[s:s + 64]).sum(axis=1); h2 += (c * W2[s:s + 64]).sum(axis=1)
    _, first = np.unique(h1 * 1000003 + h2, return_index=True)
    return P[np.sort(first)]
