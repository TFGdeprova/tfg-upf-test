# Paper-trading bot: status at 2026-11-07T15:22:49Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 6 / 3 |
| Realised profit | $13.51 ≈ €11.65 |
| … Polymarket/Kalshi only | $0.00 |
| … with bookmakers (all) | $13.51 |
| … with bookmakers licensed in Spain only | $0.00 |
| Open positions (cost) | $1,032.61 |
| Money in transit between accounts | $1,399.69 |
| Equity (cash + open at cost + in transit) | $20,893.52 ≈ €18,011.65 |
| Return so far (realised / peak money in use) | 0.340% over 0.7 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 1, seen 2, vanished 1.
Gaps using bookmakers: executed 6, no_cash 41, seen 54, vanished 7 (snapshots combined with Polymarket/Kalshi: 264).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 1,969 (about 12.2 days at the current pace).

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $5,800.00 | $0.00 | $0.00 | $5,800.00 |
| Kalshi | $5,800.00 | $5,632.90 | $167.10 | $167.10 | $5,632.90 |
| betfair_ex_uk (Spain) | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| betfred_uk | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| coolbet | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| coral | $580.00 | $0.00 | $580.00 | $580.00 | $0.00 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| leovegas_se | $580.00 | $680.93 | $0.00 | $579.99 | $0.01 |
| marathonbet (Spain) | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| matchbook | $580.00 | $0.00 | $69.03 | $580.00 | $0.00 |
| onexbet | $580.00 | $0.00 | $149.01 | $580.00 | $0.00 |
| pinnacle | $580.00 | $0.00 | $0.00 | $580.00 | $0.00 |
| smarkets | $580.00 | $580.00 | $34.86 | $580.00 | $0.00 |
| tipico_de | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| unibet_nl | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| unibet_se | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| winamax_de (Spain) | $580.00 | $547.39 | $32.61 | $32.61 | $547.39 |

Peak money in use across all accounts at the same time: $3,972.00 ≈ €3,424.14.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 4 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 7 Polymarket/Kalshi and 63 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 7 | 5 | 0 | 0 | 0 |
| +1 min | 6 | 4 | 0 | 0 | 1 |
| +2 min | 6 | 5 | 0 | 0 | 1 |
| +5 min | 6 | 3 | 0 | 0 | 1 |
| bookmaker confirmation (~1 min) | 124 | 47 | 47 | 2 | 0 |
| next bookmaker snapshot | 134 | 7 | 7 | 0 | 0 |

Depth at detection (70 gaps with full order books): median capacity (largest size still profitable after walking the order books) $20,000; median largest guaranteed profit $105.38. Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 6 | 11-07T14:26 | 1. FSV Mainz 05 v FC Bayern München | 3.2 | coral | 0.92% | $747.10 | $6.90 | open |  |
| 5 | 11-07T12:02 | Wrexham AFC v Wolverhampton Wanderers FC | 27.8 | grosvenor, matchbook | 1.09% | $526.25 | $5.74 | settled | $+5.74 |
| 4 | 11-07T11:32 | RB Leipzig v FC Augsburg | 177.9 | matchbook, onexbet, winamax_de | 0.84% | $184.36 | $1.52 | open |  |
| 3 | 11-07T11:32 | SC Paderborn 07 v Eintracht Frankfurt | 178.0 | matchbook, onexbet, smarkets | 0.65% | $101.15 | $0.63 | open |  |
| 2 | 11-07T10:31 | Bristol City FC v Norwich City FC | 118.1 | leovegas_se, matchbook | 0.43% | $857.01 | $3.69 | settled | $+3.72 |
| 1 | 11-07T10:31 | Leeds United FC v Tottenham Hotspur FC | 118.1 | onexbet, pinnacle, smarkets | 0.26% | $1556.13 | $4.05 | settled | $+4.06 |
