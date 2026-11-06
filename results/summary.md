# Paper-trading bot: status at 2026-11-06T23:03:07Z

Started 2026-11-06T22:51:30Z. Fictional capital: Polymarket $5,800.00 + Kalshi $5,800.00 (≈ €10,000) and €500 at each bookmaker the bot has used (0 so far): $11,600.00 ≈ €10,000.00 in total. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 0 / 0 |
| Realised profit | $0.00 ≈ €0.00 |
| … Polymarket/Kalshi only | $0.00 |
| … with bookmakers (all) | $0.00 |
| … with bookmakers licensed in Spain only | $0.00 |
| Open positions (cost) | $0.00 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $11,600.00 ≈ €10,000.00 |
| Return so far (realised / capital) | 0.000% over 0.0 days |

Polymarket/Kalshi gaps above the threshold: none yet.
Gaps using bookmakers: none yet (snapshots combined with Polymarket/Kalshi: 9).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 2,388 (about 382.0 days at the current pace).

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $5,800.00 | $0.00 | $0.00 | $5,800.00 |
| Kalshi | $5,800.00 | $5,800.00 | $0.00 | $0.00 | $5,800.00 |

Peak money in use across all accounts at the same time: $0.00 ≈ €0.00.

Transfers between accounts: 0 ($0.00 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

