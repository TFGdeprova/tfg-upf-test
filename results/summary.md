# Paper-trading bot: status at 2026-11-07T23:38:23Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 26 / 24 |
| Realised profit | $524.67 ≈ €452.30 |
| … Polymarket/Kalshi only | $0.00 |
| … with bookmakers (all) | $524.67 |
| … with bookmakers licensed in Spain only | $0.00 |
| Open positions (cost) | $2,788.21 |
| Money in transit between accounts | $1,399.69 |
| Equity (cash + open at cost + in transit) | $23,144.67 ≈ €19,952.30 |
| Return so far (realised / peak money in use) | 1.124% over 1.0 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 1, seen 2, vanished 1.
Gaps using bookmakers: executed 26, no_cash 41, seen 79, vanished 12 (snapshots combined with Polymarket/Kalshi: 403).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 1,521 (about 5.2 days at the current pace).

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $5,659.20 | $140.80 | $140.80 | $5,659.20 |
| Kalshi | $5,800.00 | $5,632.90 | $0.00 | $167.10 | $5,632.90 |
| betfair_ex_eu (Spain) | $580.00 | $453.07 | $0.00 | $126.93 | $453.07 |
| betfair_ex_uk (Spain) | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| betfred_uk | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| betonlineag | $580.00 | $-87.62 | $0.00 | $667.62 | $-87.62 |
| coolbet | $580.00 | $-89.73 | $0.00 | $669.73 | $-89.73 |
| coral | $580.00 | $1,338.67 | $0.00 | $1,948.91 | $-1,194.91 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $-912.98 | $0.00 | $1,492.98 | $-912.98 |
| leovegas_se | $580.00 | $1,789.30 | $0.00 | $1,403.00 | $-722.07 |
| marathonbet (Spain) | $580.00 | $1,116.32 | $0.00 | $1,986.36 | $-1,406.36 |
| matchbook | $580.00 | $3,632.14 | $0.00 | $2,789.92 | $-3,925.78 |
| onexbet | $580.00 | $2,567.02 | $2,414.65 | $22,357.23 | $-20,246.55 |
| pinnacle | $580.00 | $-1,226.60 | $0.00 | $1,226.60 | $-1,226.60 |
| skybet | $580.00 | $192.56 | $0.00 | $387.44 | $192.56 |
| smarkets | $580.00 | $-2,181.58 | $232.76 | $2,761.58 | $-2,181.58 |
| tipico_de | $580.00 | $2,622.00 | $0.00 | $486.19 | $93.81 |
| unibet_nl | $580.00 | $-4,248.48 | $0.00 | $4,157.51 | $-4,248.48 |
| unibet_se | $580.00 | $1,218.99 | $0.00 | $1,879.37 | $-1,299.37 |
| winamax_de (Spain) | $580.00 | $-258.41 | $0.00 | $805.80 | $-258.41 |

Peak money in use across all accounts at the same time: $46,687.66 ≈ €40,247.99.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 4 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 7 Polymarket/Kalshi and 91 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 7 | 5 | 0 | 0 | 0 |
| +1 min | 6 | 4 | 0 | 0 | 1 |
| +2 min | 6 | 5 | 0 | 0 | 1 |
| +5 min | 6 | 3 | 0 | 0 | 1 |
| bookmaker confirmation (~1 min) | 179 | 64 | 62 | 2 | 0 |
| next bookmaker snapshot | 189 | 12 | 11 | 0 | 0 |

Depth at detection (98 gaps with full order books): median capacity (largest size still profitable after walking the order books) $20,000; median largest guaranteed profit $124.72. Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 26 | 11-07T19:56 | Valencia CF v Real Madrid CF | 3.0 | marathonbet, matchbook, unibet_nl | 0.91% | $2499.98 | $22.57 | settled | $+22.70 |
| 25 | 11-07T19:52 | Paris Saint-Germain FC v ES Troyes AC | 13.0 | onexbet, smarkets | 0.55% | $2499.99 | $13.82 | open |  |
| 24 | 11-07T19:46 | Valencia CF v Real Madrid CF | 13.0 | onexbet, smarkets, unibet_nl | 1.91% | $2499.99 | $47.71 | settled | $+47.76 |
| 23 | 11-07T19:42 | AS Roma v US Sassuolo Calcio | 3.0 | skybet, smarkets, unibet_se | 0.73% | $2499.99 | $18.35 | settled | $+18.37 |
| 22 | 11-07T19:37 | Paris Saint-Germain FC v ES Troyes AC | 28.0 | onexbet, smarkets | 1.36% | $2499.99 | $34.01 | settled | $+34.08 |
| 21 | 11-07T19:32 | SBV Excelsior v Go Ahead Eagles | 27.9 | betonlineag, matchbook, unibet_nl | 0.68% | $2499.99 | $16.94 | settled | $+16.95 |
| 20 | 11-07T19:32 | Valencia CF v Real Madrid CF | 28.0 | onexbet, unibet_nl | 1.48% | $2499.98 | $36.84 | settled | $+36.92 |
| 19 | 11-07T19:07 | Paris Saint-Germain FC v ES Troyes AC | 58.0 | onexbet | 2.20% | $288.22 | $6.35 | open |  |
| 18 | 11-07T19:01 | SBV Excelsior v Go Ahead Eagles | 58.0 | coolbet, matchbook, unibet_nl | 0.46% | $2499.99 | $11.50 | settled | $+11.52 |
| 17 | 11-07T19:01 | Valencia CF v Real Madrid CF | 58.0 | coral, smarkets, unibet_nl | 1.34% | $2499.99 | $33.51 | settled | $+33.59 |
| 16 | 11-07T18:46 | AS Roma v US Sassuolo Calcio | 58.0 | onexbet, smarkets, winamax_de | 0.83% | $2499.98 | $20.72 | settled | $+20.78 |
| 15 | 11-07T18:06 | Paris Saint-Germain FC v ES Troyes AC | 118.0 | betfair_ex_eu, onexbet, smarkets | 1.55% | $2499.98 | $38.62 | settled | $+38.68 |
| 14 | 11-07T17:47 | AS Roma v US Sassuolo Calcio | 118.0 | matchbook, onexbet, winamax_de | 0.62% | $2499.98 | $15.44 | settled | $+15.52 |
| 13 | 11-07T17:42 | ADO Den Haag v Sparta Rotterdam | 3.0 | onexbet, pinnacle, unibet_nl | 0.59% | $2499.98 | $14.63 | settled | $+14.65 |
| 12 | 11-07T17:27 | Nottingham Forest FC v Manchester City FC | 3.0 | gtbets, onexbet, pinnacle | 1.52% | $2499.99 | $38.06 | settled | $+38.07 |
| 11 | 11-07T17:06 | Paris Saint-Germain FC v ES Troyes AC | 178.0 | onexbet, smarkets | 2.69% | $2499.99 | $67.09 | settled | $+67.26 |
| 10 | 11-07T16:31 | Nottingham Forest FC v Manchester City FC | 58.3 | onexbet, tipico_de | 1.13% | $2499.99 | $28.19 | settled | $+28.20 |
| 9 | 11-07T16:02 | AJ Auxerre v Paris FC | 117.9 | leovegas_se, onexbet, smarkets | 0.45% | $2499.99 | $11.36 | settled | $+11.38 |
| 8 | 11-07T15:32 | Nottingham Forest FC v Manchester City FC | 117.9 | matchbook, onexbet | 1.18% | $2499.98 | $29.49 | settled | $+29.49 |
| 7 | 11-07T15:27 | Fortuna Sittard v Telstar 1963 | 2.9 | matchbook, onexbet, unibet_nl | 0.65% | $2499.98 | $16.15 | settled | $+16.15 |
| 6 | 11-07T14:26 | 1. FSV Mainz 05 v FC Bayern München | 3.2 | coral | 0.92% | $747.10 | $6.90 | settled | $+6.90 |
| 5 | 11-07T12:02 | Wrexham AFC v Wolverhampton Wanderers FC | 27.8 | grosvenor, matchbook | 1.09% | $526.25 | $5.74 | settled | $+5.74 |
| 4 | 11-07T11:32 | RB Leipzig v FC Augsburg | 177.9 | matchbook, onexbet, winamax_de | 0.84% | $184.36 | $1.52 | settled | $+1.55 |
| 3 | 11-07T11:32 | SC Paderborn 07 v Eintracht Frankfurt | 178.0 | matchbook, onexbet, smarkets | 0.65% | $101.15 | $0.63 | settled | $+0.63 |
| 2 | 11-07T10:31 | Bristol City FC v Norwich City FC | 118.1 | leovegas_se, matchbook | 0.43% | $857.01 | $3.69 | settled | $+3.72 |
