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
   gone), at least the venue's minimum order size, at most $250 per trade, and only with the cash it holds on each
   venue (fictional $5,800 on Polymarket and $5,800 on Kalshi, about €10,000 in total).
4. After the game, positions are settled from the official resolutions and the cash returns to each venue.
5. Bookmakers (measurement only for now): 3 h, 2 h, 1 h, 30, 15 and 5 minutes before each kick-off the bot takes a snapshot of bookmaker odds
   (The Odds API: winner and totals for football; winner, spreads and totals for the US leagues) and solves the same
   linear program with Polymarket, Kalshi and the best bookmaker odds together. These are logged separately and not
   paper-traded: one snapshot cannot pass the persistence check, and bookmaker stake limits are unknown.

## Results
- [`results/summary.md`](results/summary.md): balances, trades and realised profit (updated every 20 minutes)
- `results/trades.csv` / `trades.jsonl`: every paper trade with its legs, prices, sizes and fees
- `results/opportunities.csv`: every gap above the threshold (seen / executed / vanished / too small)
- `results/opportunities_books.csv`: each bookmaker snapshot combined with Polymarket and Kalshi (gaps above 0.2% listed with their legs)
- `results/polls/<date>.csv`: the best guaranteed return found at every check of every game
- `results/status.json`: health of the current run (checks, errors, pushes)

Raw order-book snapshots are stored in a private research repository, not here.

## Switching it on and off
The bot runs only while the repository variable `BOT_ENABLED` is `true` (Settings → Secrets and variables → Actions →
Variables). A run that is already going can be stopped from the Actions tab (Cancel workflow run).

## Running locally
```
pip install -r requirements.txt
python -m bot.bot          # MAX_RUNTIME_MIN, POLL_SEC, WINDOW_H, THRESH, CAP_PER_TRADE are environment variables
```
