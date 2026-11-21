# Paper-trading bot: status at 2026-11-21T22:06:11Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 312 / 295 |
| Realised profit | $-89,611.34 ≈ €-77,251.16 |
| … Polymarket/Kalshi only | $48.43 |
| … with bookmakers (all) | $-89,659.78 |
| … with bookmakers licensed in Spain only | $-2,285.19 |
| Open positions (cost) | $42,499.77 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $-57,711.34 ≈ €-49,751.15 |
| Return so far (realised / peak money in use) | -57.451% over 15.0 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 971, executed 36, rounding 90, seen 1194, vanished 74.
Gaps using bookmakers: below_min_size 4, executed 276, no_cash 41, rounding 3, seen 369, vanished 36 (snapshots combined with Polymarket/Kalshi: 2090).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 1,327 (about 1.8 days at the current pace). **Add keys soon: below 3 days only the last 3 snapshots per kick-off are taken.**

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $11,382.10 | $2,446.02 | $4,486.78 | $2,369.73 |
| Kalshi | $5,800.00 | $7,254.92 | $0.00 | $2,216.01 | $2,967.42 |
| betanysports | $580.00 | $-585.80 | $0.00 | $4,190.72 | $-3,610.72 |
| betfair_ex_eu (Spain) | $580.00 | $66.22 | $0.00 | $386.85 | $66.22 |
| betfair_ex_uk (Spain) | $580.00 | $117.16 | $388.80 | $388.80 | $117.16 |
| betfred_uk | $580.00 | $-768.02 | $0.00 | $1,348.02 | $-768.02 |
| betmgm | $580.00 | $7,287.50 | $0.00 | $5,577.36 | $-4,997.36 |
| betonlineag | $580.00 | $2,452.53 | $0.00 | $4,590.49 | $-10,211.76 |
| betrivers | $580.00 | $11,676.58 | $0.00 | $4,227.93 | $-1,141.39 |
| betsson | $580.00 | $2,119.70 | $0.00 | $986.99 | $-406.99 |
| betus | $580.00 | $-780.87 | $0.00 | $3,869.28 | $-3,289.28 |
| bovada | $580.00 | $-244.12 | $0.00 | $824.12 | $-244.12 |
| boylesports | $580.00 | $1,315.03 | $0.00 | $1,813.51 | $-1,233.51 |
| codere_it | $580.00 | $1,797.50 | $0.00 | $1,295.21 | $-715.21 |
| coolbet | $580.00 | $10,223.56 | $851.25 | $11,130.88 | $-8,022.38 |
| coral | $580.00 | $-727.61 | $0.00 | $6,136.50 | $-3,247.13 |
| draftkings | $580.00 | $-2,698.54 | $0.00 | $3,278.54 | $-2,698.54 |
| fanduel | $580.00 | $416.03 | $0.00 | $1,659.29 | $-2,247.51 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $-65.68 | $0.00 | $8,368.04 | $-7,633.02 |
| ladbrokes_uk | $580.00 | $-2,699.51 | $0.00 | $4,528.91 | $-7,734.96 |
| leovegas_se | $580.00 | $-16,543.03 | $0.00 | $47,555.97 | $-55,331.30 |
| lowvig | $580.00 | $-4,145.55 | $0.00 | $1,695.80 | $-6,543.63 |
| marathonbet (Spain) | $580.00 | $-13,349.34 | $4,226.66 | $8,525.07 | $-13,349.34 |
| matchbook | $580.00 | $3,720.03 | $3,806.50 | $12,468.15 | $-4,103.15 |
| mybookieag | $580.00 | $-4,546.41 | $0.00 | $4,422.60 | $-7,124.16 |
| nordicbet | $580.00 | $-1,413.38 | $1,993.38 | $1,993.38 | $-1,413.38 |
| onexbet | $580.00 | $-77,646.42 | $8,402.31 | $69,050.38 | $-102,003.41 |
| pinnacle | $580.00 | $-2,061.17 | $3,543.04 | $10,216.96 | $-12,586.95 |
| skybet | $580.00 | $-1,150.75 | $0.00 | $775.64 | $-1,150.75 |
| smarkets | $580.00 | $-2,559.19 | $5,175.10 | $15,944.68 | $-12,057.08 |
| tipico_de | $580.00 | $-3,710.95 | $481.90 | $5,851.05 | $-3,710.95 |
| unibet_nl | $580.00 | $-6,152.91 | $4,197.82 | $5,390.31 | $-16,211.87 |
| unibet_se | $580.00 | $-18,300.62 | $6,986.99 | $24,382.67 | $-28,095.54 |
| unibet_uk | $580.00 | $-760.27 | $0.00 | $1,340.27 | $-760.27 |
| williamhill (Spain) | $580.00 | $-853.99 | $0.00 | $1,686.02 | $-3,383.02 |
| winamax_de (Spain) | $580.00 | $1,144.17 | $0.00 | $805.80 | $-872.91 |

Peak money in use across all accounts at the same time: $155,979.62 ≈ €134,465.19.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 183 Polymarket/Kalshi and 410 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 182 | 146 | 107 | 1 | 0 |
| +1 min | 181 | 137 | 99 | 1 | 1 |
| +2 min | 178 | 120 | 81 | 2 | 3 |
| +5 min | 169 | 87 | 62 | 4 | 10 |
| bookmaker confirmation (~1 min) | 731 | 402 | 396 | 14 | 0 |
| next bookmaker snapshot | 595 | 157 | 149 | 19 | 0 |

Depth at detection (capacity = largest size still profitable after walking the order books):

- Polymarket/Kalshi gaps (183): median capacity $0 (maximum $2,826); still profitable with a $50 stake: 31 of 181; median largest guaranteed profit $0.00.
- Gaps with bookmakers (410): median capacity $20,000 (maximum $20,000); still profitable with a $50 stake: 397 of 410; median largest guaranteed profit $158.03. Bookmakers publish no order-book depth, so only the Polymarket/Kalshi legs limit these sizes and the capacity stops at the search limit of $20,000; the bot's bets with bookmakers are capped at $2,500.

Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 312 | 11-21T19:56 | Real Madrid CF v RC Celta de Vigo | 3.2 | betfair_ex_uk, marathonbet, matchbook | 0.79% | $2499.99 | $19.61 | open |  |
| 311 | 11-21T19:46 | Real Madrid CF v RC Celta de Vigo | 13.2 | betfair_ex_uk, marathonbet, smarkets | 0.40% | $2499.99 | $9.94 | open |  |
| 310 | 11-21T19:41 | AS Monaco FC v AJ Auxerre | 3.0 | smarkets, unibet_se | 0.64% | $2499.99 | $16.04 | open |  |
| 309 | 11-21T19:31 | FC Groningen v SC Heerenveen | 28.1 | matchbook, pinnacle, unibet_nl | 0.63% | $2499.99 | $15.64 | open |  |
| 308 | 11-21T19:31 | AS Monaco FC v AJ Auxerre | 13.1 | smarkets, unibet_se | 1.01% | $2499.98 | $25.31 | open |  |
| 307 | 11-21T19:31 | Real Madrid CF v RC Celta de Vigo | 28.1 | onexbet | 1.75% | $2499.99 | $43.70 | open |  |
| 306 | 11-21T19:16 | AS Monaco FC v AJ Auxerre | 28.1 | smarkets, unibet_se | 0.55% | $2499.98 | $13.62 | open |  |
| 305 | 11-21T19:16 | SSC Napoli v Torino FC | 28.1 | coolbet, pinnacle | 0.41% | $2499.99 | $10.32 | open |  |
| 304 | 11-21T19:01 | FC Groningen v SC Heerenveen | 58.2 | matchbook, nordicbet, unibet_nl | 0.47% | $2499.99 | $11.67 | open |  |
| 303 | 11-21T19:01 | Real Madrid CF v RC Celta de Vigo | 58.2 | matchbook, onexbet | 1.45% | $2499.98 | $36.10 | open |  |
| 302 | 11-21T18:02 | FC Groningen v SC Heerenveen | 117.9 | nordicbet, smarkets, unibet_nl | 0.47% | $2499.99 | $11.67 | open |  |
| 301 | 11-21T18:02 | Real Madrid CF v RC Celta de Vigo | 117.9 | matchbook, onexbet, smarkets | 1.54% | $2499.99 | $38.56 | open |  |
| 300 | 11-21T17:56 | EDM at CAR | 3.0 | matchbook, williamhill | 1.16% | $2499.99 | $29.01 | settled | $+29.04 |
| 299 | 11-21T17:47 | AS Monaco FC v AJ Auxerre | 117.9 | smarkets, tipico_de, unibet_se | 0.24% | $2499.98 | $5.83 | open |  |
| 298 | 11-21T17:41 | FC Utrecht v SC Cambuur-Leeuwarden | 3.0 | matchbook, pinnacle | 0.98% | $2499.99 | $24.54 | open |  |
| 297 | 11-21T17:31 | FC Utrecht v SC Cambuur-Leeuwarden | 13.1 | matchbook, onexbet | 1.70% | $2499.99 | $42.38 | settled | $+42.38 |
| 296 | 11-21T17:31 | MIL at PHI | 28.1 | lowvig | 2.32% | $2343.79 | $54.28 | settled | $+54.29 |
| 295 | 11-21T17:26 | Sevilla FC v Real Betis Balompié | 3.2 | smarkets, unibet_se | 1.79% | $2499.99 | $44.69 | settled | $+44.70 |
| 294 | 11-21T17:26 | Newcastle United FC v Arsenal FC | 3.2 | betonlineag, gtbets | 2.02% | $2499.98 | $50.35 | settled | $+50.38 |
| 293 | 11-21T17:17 | Feyenoord Rotterdam v SBV Excelsior | 27.8 | matchbook, onexbet | 2.85% | $2499.99 | $71.33 | settled | $+71.33 |
| 292 | 11-21T17:17 | FC Schalke 04 v VfB Stuttgart | 12.8 | matchbook, onexbet, unibet_uk | 0.76% | $2499.99 | $19.03 | settled | $+19.03 |
| 291 | 11-21T17:17 | Sevilla FC v Real Betis Balompié | 12.8 | matchbook, onexbet | 0.26% | $2499.98 | $6.40 | settled | $+6.41 |
| 290 | 11-21T17:17 | Newcastle United FC v Arsenal FC | 12.8 | betonlineag, gtbets | 2.02% | $2499.98 | $50.35 | settled | $+50.38 |
| 289 | 11-21T17:02 | FC Groningen v SC Heerenveen | 177.7 | matchbook, smarkets, unibet_nl | 0.30% | $2499.99 | $7.37 | open |  |
| 288 | 11-21T17:02 | FC Schalke 04 v VfB Stuttgart | 27.7 | onexbet, smarkets, unibet_uk | 0.28% | $2499.99 | $7.00 | settled | $+7.00 |
