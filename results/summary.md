# Paper-trading bot: status at 2026-11-07T11:57:19Z

Started 2026-11-06T22:51:30Z. Fictional capital: Polymarket $5,800.00 + Kalshi $5,800.00 (≈ €10,000) and €500 at each bookmaker the bot has used (7 so far): $15,660.00 ≈ €13,500.00 in total. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 4 / 0 |
| Realised profit | $0.00 ≈ €0.00 |
| … Polymarket/Kalshi only | $0.00 |
| … with bookmakers (all) | $0.00 |
| … with bookmakers licensed in Spain only | $0.00 |
| Open positions (cost) | $2,698.65 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $15,660.00 ≈ €13,500.00 |
| Return so far (realised / capital) | 0.000% over 0.5 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 1, seen 2, vanished 1.
Gaps using bookmakers: executed 4, no_cash 3, seen 9, vanished 2 (snapshots combined with Polymarket/Kalshi: 85).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 2,271 (about 46.1 days at the current pace).

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $5,800.00 | $0.00 | $0.00 | $5,800.00 |
| Kalshi | $5,800.00 | $5,800.00 | $0.00 | $0.00 | $5,800.00 |
| gtbets | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| leovegas_se | $580.00 | $0.01 | $579.99 | $579.99 | $0.01 |
| matchbook | $580.00 | $233.95 | $346.05 | $346.05 | $233.95 |
| onexbet | $580.00 | $0.00 | $580.00 | $580.00 | $0.00 |
| pinnacle | $580.00 | $0.00 | $580.00 | $580.00 | $0.00 |
| smarkets | $580.00 | $0.00 | $580.00 | $580.00 | $0.00 |
| winamax_de (Spain) | $580.00 | $547.39 | $32.61 | $32.61 | $547.39 |

Peak money in use across all accounts at the same time: $2,698.65 ≈ €2,326.42.

Transfers between accounts: 0 ($0.00 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 7 Polymarket/Kalshi and 12 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 7 | 5 | 0 | 0 | 0 |
| +1 min | 6 | 4 | 0 | 0 | 1 |
| +2 min | 6 | 5 | 0 | 0 | 1 |
| +5 min | 6 | 3 | 0 | 0 | 1 |
| bookmaker confirmation (~1 min) | 8 | 6 | 6 | 2 | 0 |
| next bookmaker snapshot | 3 | 0 | 0 | 0 | 0 |

Depth at detection (19 gaps with full order books): median capacity (largest size still profitable after walking the order books) $20,000; median largest guaranteed profit $27.66. Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 4 | 11-07T11:32 | RB Leipzig v FC Augsburg | 177.9 | matchbook, onexbet, winamax_de | 0.84% | $184.36 | $1.52 | open |  |
| 3 | 11-07T11:32 | SC Paderborn 07 v Eintracht Frankfurt | 178.0 | matchbook, onexbet, smarkets | 0.65% | $101.15 | $0.63 | open |  |
| 2 | 11-07T10:31 | Bristol City FC v Norwich City FC | 118.1 | leovegas_se, matchbook | 0.43% | $857.01 | $3.69 | open |  |
| 1 | 11-07T10:31 | Leeds United FC v Tottenham Hotspur FC | 118.1 | onexbet, pinnacle, smarkets | 0.26% | $1556.13 | $4.05 | open |  |
