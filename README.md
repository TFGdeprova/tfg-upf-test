# Paper-trading bot for deterministic arbitrage between Polymarket and Kalshi

Part 2 of a bachelor's thesis (TFG, Universitat Pompeu Fabra) on deterministic arbitrage in betting and prediction
markets. **No real money is used and no order is ever sent**: the bot reads public market data and records the trades
it *would* have made, then settles them with the venues' official results.

## What it does
1. Every 10 minutes it lists the games that start within the next 3 hours and are listed on **both** Polymarket and
   Kalshi: football (Premier League, LaLiga, Serie A, Bundesliga, Ligue 1, Eredivisie, Championship, Scottish
   Premiership, Champions League, Europa League), NBA, NFL and NHL.
2. Every 30 seconds, until one minute before kick-off (pre-game only), it reads the best prices and sizes of every
   full-game contract of each game (winner, spreads, totals, team totals, margins, exact scores, …) and solves a linear
   program over all possible final scores: is there a combination of purchases that pays more than it costs **whatever
   the result**? Each market's own taker fee is included.
3. A gap above 0.2 % must still be there at the next check (one polling interval of reaction time). The bot then
   "buys" at that moment's best prices, never more than the displayed size (liquidity it already took is treated as
   gone), at least the venue's minimum order size, at most $2,500 per trade, and only with the cash it holds on each
   venue.
4. Bookmakers: 3 h, 2 h, 1 h, 30, 15 and 5 minutes before each kick-off the bot takes a snapshot of bookmaker odds
   (The Odds API: winner and totals for football; winner, spreads and totals for the US leagues) and solves the same
   linear program with Polymarket, Kalshi and the best bookmaker odds together. A gap that uses a bookmaker must still
   be there in a confirmation snapshot taken about one minute later; the bot then bets at those odds (stake limited by
   the money in that bookmaker account) together with the Polymarket/Kalshi legs.
5. After the game, positions are settled from the official resolutions (Polymarket, Kalshi) and final scores
   (bookmakers), and the money returns to each account.
6. Every gap above 0.1 %, traded or not, is **followed** (the tests used in the finance literature on arbitrage):
   - *Re-checks (ex-ante test):* the same portfolio (same shares, same bookmaker stakes) is priced again 30 seconds and
     1, 2 and 5 minutes later; gaps that use a bookmaker are re-priced at that bookmaker's odds in the confirmation
     snapshot and in the next scheduled snapshot. A re-check that the kick-off or the end of a run comes before is
     recorded as *censored*.
   - *Depth (slippage and capacity):* at detection and at every re-check the bot reads the order books of the
     portfolio's contracts (Polymarket: every price level; Kalshi: the market's order book) and computes the guaranteed
     profit if $50, $100, $250, $500, $1,000, $2,500, $5,000 or $10,000 were invested, walking down the books with each
     venue's fee at every level; also the size with the largest profit and the largest size still profitable
     (capacity). Bookmaker bets are taken at fixed odds (no public depth).
   - *Freshness:* how long each price in the portfolio had been unchanged when the gap was seen.

## Money and transfers (all fictional)
- Starting capital: $5,800 on Polymarket and $5,800 on Kalshi (about €10,000), and €500 at each bookmaker, opened the
  first time the bot bets there. Results are shown for all bookmakers and for those whose operator holds a Spanish
  licence (DGOJ list).
- Money moves between accounts only by transfer, with the delays and fees the venues document: Polymarket withdrawals
  instant and free, deposits on-chain (~15 min); Kalshi crypto deposits and withdrawals about 30 minutes; bookmakers:
  deposits immediate, withdrawals 24 hours; dollars ↔ euros 2 hours and 0.5%. Money in transit cannot be used.
- When an account falls below half of its starting balance, it is topped up from accounts holding more than 120% of
  theirs (fastest route first). The summary reports the peak money in use per account, i.e. how much capital was
  really needed.

## Results
- [`results/summary.md`](results/summary.md): balances, trades and realised profit (updated every 20 minutes)
- `results/trades.csv` / `trades.jsonl`: every paper trade with its legs, prices, sizes and fees
- `results/opportunities.csv`: every gap above the threshold (seen / executed / vanished / too small)
- `results/opportunities_books.csv`: each bookmaker snapshot combined with Polymarket and Kalshi (seen / executed / vanished)
- `results/transfers.csv`: every transfer between accounts (amount, fee, delay)
- `results/rechecks.csv`: each followed gap re-priced later (same portfolio): delay, return then, still profitable or
  not, best return available then, censored re-checks
- `results/depth.csv`: each followed gap at detection and at every re-check: guaranteed profit and return at each size,
  best size, capacity, age of the prices
- `results/polls/<date>.csv`: the best guaranteed return found at every check of every game
- `results/status.json`: health of the current run (checks, errors, pushes)

Raw order-book snapshots (including the full depth of every followed gap) are stored in a private research
repository, not here.

## Switching it on and off
The bot runs unless the repository variable `BOT_ENABLED` is `false` (Settings → Secrets and variables → Actions →
Variables). To stop it, create that variable with the value `false` and cancel the run in progress from the Actions tab
(Cancel workflow run), or disable the workflow in the Actions tab.

## Running locally
```
pip install -r requirements.txt
python -m bot.bot          # MAX_RUNTIME_MIN, POLL_SEC, WINDOW_H, THRESH, CAP_PER_TRADE are environment variables
```
