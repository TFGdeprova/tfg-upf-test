# Paper-trading bot: status at 2026-11-22T14:54:06Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 347 / 320 |
| Realised profit | $-88,909.18 ≈ €-76,645.84 |
| … Polymarket/Kalshi only | $48.48 |
| … with bookmakers (all) | $-88,957.65 |
| … with bookmakers licensed in Spain only | $-2,285.19 |
| Open positions (cost) | $64,986.61 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $-57,009.18 ≈ €-49,145.84 |
| Return so far (realised / peak money in use) | -57.001% over 15.7 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 989, executed 38, rounding 95, seen 1222, vanished 77.
Gaps using bookmakers: below_min_size 4, executed 309, no_cash 41, rounding 4, seen 404, vanished 37 (snapshots combined with Polymarket/Kalshi: 2265).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 621 (about 0.6 days at the current pace). **Add keys soon: below 3 days only the last 3 snapshots per kick-off are taken.**

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $9,212.61 | $2,225.85 | $4,486.78 | $2,369.73 |
| Kalshi | $5,800.00 | $7,250.01 | $3.42 | $2,216.01 | $2,967.42 |
| betanysports | $580.00 | $-585.80 | $0.00 | $4,190.72 | $-3,610.72 |
| betfair_ex_eu (Spain) | $580.00 | $-771.67 | $837.89 | $837.89 | $-771.67 |
| betfair_ex_uk (Spain) | $580.00 | $117.16 | $0.00 | $388.80 | $117.16 |
| betfred_uk | $580.00 | $-768.02 | $0.00 | $1,348.02 | $-768.02 |
| betmgm | $580.00 | $5,308.69 | $1,978.81 | $5,577.36 | $-4,997.36 |
| betonlineag | $580.00 | $1,823.49 | $629.04 | $4,590.49 | $-10,211.76 |
| betrivers | $580.00 | $11,676.58 | $0.00 | $4,227.93 | $-1,141.39 |
| betsson | $580.00 | $2,119.70 | $0.00 | $986.99 | $-406.99 |
| betus | $580.00 | $-780.87 | $0.00 | $3,869.28 | $-3,289.28 |
| bovada | $580.00 | $-244.12 | $0.00 | $824.12 | $-244.12 |
| boylesports | $580.00 | $574.88 | $740.15 | $1,813.51 | $-1,233.51 |
| codere_it | $580.00 | $1,797.50 | $0.00 | $1,295.21 | $-715.21 |
| coolbet | $580.00 | $7,559.10 | $7,308.16 | $11,130.88 | $-8,022.38 |
| coral | $580.00 | $-6,178.40 | $5,450.79 | $6,136.50 | $-6,178.40 |
| draftkings | $580.00 | $-2,698.54 | $0.00 | $3,278.54 | $-2,698.54 |
| fanduel | $580.00 | $416.03 | $0.00 | $1,659.29 | $-2,247.51 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $-1,124.53 | $1,058.85 | $8,368.04 | $-7,633.02 |
| ladbrokes_uk | $580.00 | $-4,760.14 | $2,060.63 | $4,528.91 | $-7,734.96 |
| leovegas_se | $580.00 | $-20,519.71 | $0.00 | $47,555.97 | $-55,331.30 |
| lowvig | $580.00 | $-4,145.55 | $0.00 | $1,695.80 | $-6,543.63 |
| marathonbet (Spain) | $580.00 | $-8,319.61 | $0.00 | $8,525.07 | $-13,349.34 |
| matchbook | $580.00 | $2,557.47 | $4,527.94 | $12,468.15 | $-4,103.15 |
| mybookieag | $580.00 | $-4,546.41 | $0.00 | $4,422.60 | $-7,124.16 |
| nordicbet | $580.00 | $3,609.94 | $0.00 | $1,993.38 | $-1,413.38 |
| onexbet | $580.00 | $-81,356.07 | $18,541.21 | $69,050.38 | $-102,003.41 |
| pinnacle | $580.00 | $-943.31 | $2,630.82 | $10,216.96 | $-12,586.95 |
| skybet | $580.00 | $-1,150.75 | $0.00 | $775.64 | $-1,150.75 |
| smarkets | $580.00 | $-1,396.83 | $6,392.67 | $15,944.68 | $-12,057.08 |
| tipico_de | $580.00 | $-1,205.07 | $0.00 | $5,851.05 | $-3,710.95 |
| unibet_nl | $580.00 | $-4,297.62 | $667.64 | $5,390.31 | $-16,211.87 |
| unibet_se | $580.00 | $-28,469.93 | $9,405.05 | $24,382.67 | $-28,469.93 |
| unibet_uk | $580.00 | $-1,287.96 | $527.69 | $1,340.27 | $-1,287.96 |
| williamhill (Spain) | $580.00 | $-2,192.18 | $0.00 | $1,686.02 | $-3,383.02 |
| winamax_de (Spain) | $580.00 | $1,144.17 | $0.00 | $805.80 | $-872.91 |

Peak money in use across all accounts at the same time: $155,979.62 ≈ €134,465.19.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 191 Polymarket/Kalshi and 450 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 190 | 151 | 112 | 1 | 0 |
| +1 min | 189 | 141 | 103 | 1 | 1 |
| +2 min | 186 | 124 | 85 | 2 | 3 |
| +5 min | 176 | 90 | 65 | 4 | 11 |
| bookmaker confirmation (~1 min) | 813 | 441 | 435 | 15 | 0 |
| next bookmaker snapshot | 671 | 166 | 157 | 20 | 0 |

Depth at detection (capacity = largest size still profitable after walking the order books):

- Polymarket/Kalshi gaps (191): median capacity $0 (maximum $2,826); still profitable with a $50 stake: 32 of 189; median largest guaranteed profit $0.00.
- Gaps with bookmakers (450): median capacity $20,000 (maximum $20,000); still profitable with a $50 stake: 437 of 450; median largest guaranteed profit $154.57. Bookmakers publish no order-book depth, so only the Polymarket/Kalshi legs limit these sizes and the capacity stops at the search limit of $20,000; the bot's bets with bookmakers are capped at $2,500.

Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 347 | 11-22T14:47 | Go Ahead Eagles v Fortuna Sittard | 57.1 | coral | 1.43% | $2500.00 | $35.66 | open |  |
| 346 | 11-22T14:31 | CA Osasuna v Málaga CF | 178.1 | coolbet, onexbet, unibet_se | 0.28% | $2499.98 | $7.07 | open |  |
| 345 | 11-22T13:56 | Paris FC v Angers SCO | 3.1 | betonlineag, unibet_se | 0.28% | $2499.99 | $7.02 | open |  |
| 344 | 11-22T13:56 | US Sassuolo Calcio v Genoa CFC | 3.1 | boylesports, coolbet, pinnacle | 0.66% | $2499.98 | $16.53 | open |  |
| 343 | 11-22T13:56 | Bologna FC 1909 v Udinese Calcio | 3.1 | smarkets, unibet_se | 1.55% | $2499.99 | $38.82 | open |  |
| 342 | 11-22T13:47 | Paris FC v Angers SCO | 12.8 | onexbet | 1.00% | $2407.21 | $23.99 | open |  |
| 341 | 11-22T13:47 | US Sassuolo Calcio v Genoa CFC | 12.8 | coolbet, onexbet, smarkets | 1.50% | $2499.99 | $37.38 | open |  |
| 340 | 11-22T13:47 | Hull City AFC v Brighton & Hove Albion FC | 12.9 | onexbet, smarkets, unibet_se | 0.48% | $2499.99 | $12.04 | open |  |
| 339 | 11-22T13:46 | Paris FC v Angers SCO | 13.9 | no | 0.30% | $79.75 | $0.24 | open |  |
| 338 | 11-22T13:32 | SV Werder Bremen v Hamburger SV | 177.9 | onexbet, smarkets, unibet_se | 0.35% | $2499.99 | $8.79 | open |  |
| 337 | 11-22T13:32 | FC Augsburg v 1. FSV Mainz 05 | 58.0 | betfair_ex_eu, gtbets, onexbet | 0.38% | $2499.98 | $9.49 | open |  |
| 336 | 11-22T13:32 | US Sassuolo Calcio v Genoa CFC | 28.0 | coolbet, matchbook, onexbet | 1.25% | $2499.99 | $31.28 | open |  |
| 335 | 11-22T13:32 | Hull City AFC v Brighton & Hove Albion FC | 28.0 | onexbet, smarkets, unibet_uk | 0.26% | $2499.99 | $6.52 | open |  |
| 334 | 11-22T13:16 | AFC Ajax v ADO Den Haag | 13.1 | betmgm, onexbet, unibet_nl | 0.52% | $2499.98 | $13.02 | open |  |
| 333 | 11-22T13:01 | US Sassuolo Calcio v Genoa CFC | 58.2 | matchbook, onexbet, pinnacle | 1.07% | $2499.99 | $26.63 | open |  |
| 332 | 11-22T13:01 | Bologna FC 1909 v Udinese Calcio | 58.2 | coolbet, onexbet, smarkets | 0.29% | $2499.99 | $7.13 | open |  |
| 331 | 11-22T13:01 | Hull City AFC v Brighton & Hove Albion FC | 58.2 | coolbet, onexbet | 2.93% | $2499.99 | $73.14 | open |  |
| 330 | 11-22T12:56 | FC Barcelona v Villarreal CF | 3.1 | coral, matchbook, smarkets | 3.13% | $2499.98 | $78.11 | open |  |
| 329 | 11-22T12:46 | FC Barcelona v Villarreal CF | 13.4 | coolbet, coral, matchbook | 3.03% | $2499.98 | $75.67 | open |  |
| 328 | 11-22T12:32 | AFC Ajax v ADO Den Haag | 57.8 | matchbook, unibet_nl | 1.26% | $2499.99 | $31.56 | open |  |
| 327 | 11-22T12:32 | FC Barcelona v Villarreal CF | 27.9 | coolbet, ladbrokes_uk, smarkets | 3.03% | $2499.98 | $75.67 | open |  |
| 326 | 11-22T12:02 | Paris FC v Angers SCO | 117.8 | onexbet, smarkets, unibet_se | 0.39% | $2499.98 | $9.72 | open |  |
| 325 | 11-22T12:02 | US Sassuolo Calcio v Genoa CFC | 117.8 | onexbet, smarkets, unibet_se | 0.77% | $2499.98 | $19.21 | open |  |
| 324 | 11-22T11:57 | Burnley FC v Blackburn Rovers FC | 2.9 | leovegas_se, matchbook, onexbet | 2.13% | $2499.99 | $53.24 | settled | $+53.24 |
| 323 | 11-22T11:46 | Burnley FC v Blackburn Rovers FC | 13.0 | leovegas_se, matchbook, onexbet | 2.25% | $2499.98 | $56.32 | settled | $+56.32 |
