# Paper-trading bot: status at 2026-11-07T10:57:07Z

Started 2026-11-06T22:51:30Z. Fictional capital: Polymarket $5,800.00 + Kalshi $5,800.00 (≈ €10,000) and €500 at each bookmaker the bot has used (5 so far): $14,500.00 ≈ €12,500.00 in total. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 2 / 0 |
| Realised profit | $0.00 ≈ €0.00 |
| … Polymarket/Kalshi only | $0.00 |
| … with bookmakers (all) | $0.00 |
| … with bookmakers licensed in Spain only | $0.00 |
| Open positions (cost) | $2,413.14 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $14,500.00 ≈ €12,500.00 |
| Return so far (realised / capital) | 0.000% over 0.5 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 1, seen 2, vanished 1.
Gaps using bookmakers: executed 2, seen 4, vanished 2 (snapshots combined with Polymarket/Kalshi: 70).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 2,295 (about 56.9 days at the current pace).

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $5,800.00 | $0.00 | $0.00 | $5,800.00 |
| Kalshi | $5,800.00 | $5,800.00 | $0.00 | $0.00 | $5,800.00 |
| leovegas_se | $580.00 | $0.01 | $579.99 | $579.99 | $0.01 |
| matchbook | $580.00 | $302.98 | $277.02 | $277.02 | $302.98 |
| onexbet | $580.00 | $149.01 | $430.99 | $430.99 | $149.01 |
| pinnacle | $580.00 | $0.00 | $580.00 | $580.00 | $0.00 |
| smarkets | $580.00 | $34.86 | $545.14 | $545.14 | $34.86 |

Peak money in use across all accounts at the same time: $2,413.14 ≈ €2,080.29.

Transfers between accounts: 0 ($0.00 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 7 Polymarket/Kalshi and 7 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 7 | 5 | 0 | 0 | 0 |
| +1 min | 6 | 4 | 0 | 0 | 1 |
| +2 min | 6 | 5 | 0 | 0 | 1 |
| +5 min | 6 | 3 | 0 | 0 | 1 |
| bookmaker confirmation (~1 min) | 2 | 2 | 2 | 2 | 0 |

Depth at detection (14 gaps with full order books): median capacity (largest size still profitable after walking the order books) $20,000; median largest guaranteed profit $22.38. Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 11-07T10:31 | Bristol City FC v Norwich City FC | 118.1 | leovegas_se, matchbook | 0.43% | $857.01 | $3.69 | open |  |
| 1 | 11-07T10:31 | Leeds United FC v Tottenham Hotspur FC | 118.1 | onexbet, pinnacle, smarkets | 0.26% | $1556.13 | $4.05 | open |  |
