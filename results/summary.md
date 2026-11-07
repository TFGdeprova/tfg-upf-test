# Paper-trading bot: status at 2026-11-07T18:42:58Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 15 / 7 |
| Realised profit | $38.75 ≈ €33.41 |
| … Polymarket/Kalshi only | $0.00 |
| … with bookmakers (all) | $38.75 |
| … with bookmakers licensed in Spain only | $0.00 |
| Open positions (cost) | $19,999.88 |
| Money in transit between accounts | $1,399.69 |
| Equity (cash + open at cost + in transit) | $21,498.76 ≈ €18,533.41 |
| Return so far (realised / peak money in use) | 0.181% over 0.8 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 1, seen 2, vanished 1.
Gaps using bookmakers: executed 15, no_cash 41, seen 67, vanished 11 (snapshots combined with Polymarket/Kalshi: 329).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 1,722 (about 7.1 days at the current pace).

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $5,800.00 | $0.00 | $0.00 | $5,800.00 |
| Kalshi | $5,800.00 | $5,632.90 | $0.00 | $167.10 | $5,632.90 |
| betfair_ex_eu (Spain) | $580.00 | $453.07 | $126.93 | $126.93 | $453.07 |
| betfair_ex_uk (Spain) | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| betfred_uk | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| coolbet | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| coral | $580.00 | $754.00 | $0.00 | $580.00 | $0.00 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $-912.98 | $1,492.98 | $1,492.98 | $-912.98 |
| leovegas_se | $580.00 | $-722.07 | $1,403.00 | $1,403.00 | $-722.07 |
| marathonbet (Spain) | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| matchbook | $580.00 | $-1,882.36 | $746.50 | $1,882.36 | $-1,882.36 |
| onexbet | $580.00 | $-9,884.47 | $11,995.15 | $11,995.15 | $-10,302.54 |
| pinnacle | $580.00 | $-1,226.60 | $1,226.60 | $1,226.60 | $-1,226.60 |
| smarkets | $580.00 | $-591.14 | $1,171.14 | $1,171.14 | $-591.14 |
| tipico_de | $580.00 | $93.81 | $486.19 | $486.19 | $93.81 |
| unibet_nl | $580.00 | $-1,039.88 | $948.91 | $1,619.88 | $-1,039.88 |
| unibet_se | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| winamax_de (Spain) | $580.00 | $144.91 | $402.48 | $402.48 | $144.91 |

Peak money in use across all accounts at the same time: $21,399.57 ≈ €18,447.91.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 4 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 7 Polymarket/Kalshi and 79 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 7 | 5 | 0 | 0 | 0 |
| +1 min | 6 | 4 | 0 | 0 | 1 |
| +2 min | 6 | 5 | 0 | 0 | 1 |
| +5 min | 6 | 3 | 0 | 0 | 1 |
| bookmaker confirmation (~1 min) | 145 | 52 | 52 | 2 | 0 |
| next bookmaker snapshot | 156 | 8 | 8 | 0 | 0 |

Depth at detection (86 gaps with full order books): median capacity (largest size still profitable after walking the order books) $20,000; median largest guaranteed profit $109.41. Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 15 | 11-07T18:06 | Paris Saint-Germain FC v ES Troyes AC | 118.0 | betfair_ex_eu, onexbet, smarkets | 1.55% | $2499.98 | $38.62 | open |  |
| 14 | 11-07T17:47 | AS Roma v US Sassuolo Calcio | 118.0 | matchbook, onexbet, winamax_de | 0.62% | $2499.98 | $15.44 | open |  |
| 13 | 11-07T17:42 | ADO Den Haag v Sparta Rotterdam | 3.0 | onexbet, pinnacle, unibet_nl | 0.59% | $2499.98 | $14.63 | open |  |
| 12 | 11-07T17:27 | Nottingham Forest FC v Manchester City FC | 3.0 | gtbets, onexbet, pinnacle | 1.52% | $2499.99 | $38.06 | open |  |
| 11 | 11-07T17:06 | Paris Saint-Germain FC v ES Troyes AC | 178.0 | onexbet, smarkets | 2.69% | $2499.99 | $67.09 | open |  |
| 10 | 11-07T16:31 | Nottingham Forest FC v Manchester City FC | 58.3 | onexbet, tipico_de | 1.13% | $2499.99 | $28.19 | open |  |
| 9 | 11-07T16:02 | AJ Auxerre v Paris FC | 117.9 | leovegas_se, onexbet, smarkets | 0.45% | $2499.99 | $11.36 | open |  |
| 8 | 11-07T15:32 | Nottingham Forest FC v Manchester City FC | 117.9 | matchbook, onexbet | 1.18% | $2499.98 | $29.49 | open |  |
| 7 | 11-07T15:27 | Fortuna Sittard v Telstar 1963 | 2.9 | matchbook, onexbet, unibet_nl | 0.65% | $2499.98 | $16.15 | settled | $+16.15 |
| 6 | 11-07T14:26 | 1. FSV Mainz 05 v FC Bayern München | 3.2 | coral | 0.92% | $747.10 | $6.90 | settled | $+6.90 |
| 5 | 11-07T12:02 | Wrexham AFC v Wolverhampton Wanderers FC | 27.8 | grosvenor, matchbook | 1.09% | $526.25 | $5.74 | settled | $+5.74 |
| 4 | 11-07T11:32 | RB Leipzig v FC Augsburg | 177.9 | matchbook, onexbet, winamax_de | 0.84% | $184.36 | $1.52 | settled | $+1.55 |
| 3 | 11-07T11:32 | SC Paderborn 07 v Eintracht Frankfurt | 178.0 | matchbook, onexbet, smarkets | 0.65% | $101.15 | $0.63 | settled | $+0.63 |
| 2 | 11-07T10:31 | Bristol City FC v Norwich City FC | 118.1 | leovegas_se, matchbook | 0.43% | $857.01 | $3.69 | settled | $+3.72 |
| 1 | 11-07T10:31 | Leeds United FC v Tottenham Hotspur FC | 118.1 | onexbet, pinnacle, smarkets | 0.26% | $1556.13 | $4.05 | settled | $+4.06 |
