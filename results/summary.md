# Paper-trading bot: status at 2026-11-22T11:13:04Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 321 / 316 |
| Realised profit | $-89,077.83 ≈ €-76,791.23 |
| … Polymarket/Kalshi only | $48.48 |
| … with bookmakers (all) | $-89,126.30 |
| … with bookmakers licensed in Spain only | $-2,285.19 |
| Open positions (cost) | $12,499.92 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $-57,177.83 ≈ €-49,291.23 |
| Return so far (realised / peak money in use) | -57.109% over 15.5 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 982, executed 37, rounding 95, seen 1213, vanished 76.
Gaps using bookmakers: below_min_size 4, executed 284, no_cash 41, rounding 3, seen 377, vanished 36 (snapshots combined with Polymarket/Kalshi: 2188).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 1,039 (about 1.2 days at the current pace). **Add keys soon: below 3 days only the last 3 snapshots per kick-off are taken.**

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $11,438.46 | $0.00 | $4,486.78 | $2,369.73 |
| Kalshi | $5,800.00 | $7,253.43 | $0.00 | $2,216.01 | $2,967.42 |
| betanysports | $580.00 | $-585.80 | $0.00 | $4,190.72 | $-3,610.72 |
| betfair_ex_eu (Spain) | $580.00 | $66.22 | $0.00 | $386.85 | $66.22 |
| betfair_ex_uk (Spain) | $580.00 | $117.16 | $0.00 | $388.80 | $117.16 |
| betfred_uk | $580.00 | $-768.02 | $0.00 | $1,348.02 | $-768.02 |
| betmgm | $580.00 | $7,287.50 | $0.00 | $5,577.36 | $-4,997.36 |
| betonlineag | $580.00 | $2,452.53 | $0.00 | $4,590.49 | $-10,211.76 |
| betrivers | $580.00 | $11,676.58 | $0.00 | $4,227.93 | $-1,141.39 |
| betsson | $580.00 | $2,119.70 | $0.00 | $986.99 | $-406.99 |
| betus | $580.00 | $-780.87 | $0.00 | $3,869.28 | $-3,289.28 |
| bovada | $580.00 | $-244.12 | $0.00 | $824.12 | $-244.12 |
| boylesports | $580.00 | $1,315.03 | $0.00 | $1,813.51 | $-1,233.51 |
| codere_it | $580.00 | $1,797.50 | $0.00 | $1,295.21 | $-715.21 |
| coolbet | $580.00 | $14,697.82 | $169.44 | $11,130.88 | $-8,022.38 |
| coral | $580.00 | $-727.61 | $0.00 | $6,136.50 | $-3,247.13 |
| draftkings | $580.00 | $-2,698.54 | $0.00 | $3,278.54 | $-2,698.54 |
| fanduel | $580.00 | $416.03 | $0.00 | $1,659.29 | $-2,247.51 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $-65.68 | $0.00 | $8,368.04 | $-7,633.02 |
| ladbrokes_uk | $580.00 | $-2,699.51 | $0.00 | $4,528.91 | $-7,734.96 |
| leovegas_se | $580.00 | $-16,543.03 | $0.00 | $47,555.97 | $-55,331.30 |
| lowvig | $580.00 | $-4,145.55 | $0.00 | $1,695.80 | $-6,543.63 |
| marathonbet (Spain) | $580.00 | $-8,319.61 | $0.00 | $8,525.07 | $-13,349.34 |
| matchbook | $580.00 | $6,673.69 | $166.89 | $12,468.15 | $-4,103.15 |
| mybookieag | $580.00 | $-4,546.41 | $0.00 | $4,422.60 | $-7,124.16 |
| nordicbet | $580.00 | $3,609.94 | $0.00 | $1,993.38 | $-1,413.38 |
| onexbet | $580.00 | $-76,076.18 | $8,596.56 | $69,050.38 | $-102,003.41 |
| pinnacle | $580.00 | $820.07 | $867.44 | $10,216.96 | $-12,586.95 |
| skybet | $580.00 | $-1,150.75 | $0.00 | $775.64 | $-1,150.75 |
| smarkets | $580.00 | $3,981.57 | $1,014.27 | $15,944.68 | $-12,057.08 |
| tipico_de | $580.00 | $-1,205.07 | $0.00 | $5,851.05 | $-3,710.95 |
| unibet_nl | $580.00 | $-3,629.98 | $0.00 | $5,390.31 | $-16,211.87 |
| unibet_se | $580.00 | $-19,985.94 | $1,685.32 | $24,382.67 | $-28,095.54 |
| unibet_uk | $580.00 | $-760.27 | $0.00 | $1,340.27 | $-760.27 |
| williamhill (Spain) | $580.00 | $-2,192.18 | $0.00 | $1,686.02 | $-3,383.02 |
| winamax_de (Spain) | $580.00 | $1,144.17 | $0.00 | $805.80 | $-872.91 |

Peak money in use across all accounts at the same time: $155,979.62 ≈ €134,465.19.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 188 Polymarket/Kalshi and 420 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 187 | 149 | 110 | 1 | 0 |
| +1 min | 186 | 140 | 102 | 1 | 1 |
| +2 min | 183 | 123 | 84 | 2 | 3 |
| +5 min | 173 | 89 | 64 | 4 | 11 |
| bookmaker confirmation (~1 min) | 739 | 409 | 403 | 15 | 0 |
| next bookmaker snapshot | 600 | 157 | 149 | 19 | 0 |

Depth at detection (capacity = largest size still profitable after walking the order books):

- Polymarket/Kalshi gaps (188): median capacity $0 (maximum $2,826); still profitable with a $50 stake: 31 of 186; median largest guaranteed profit $0.00.
- Gaps with bookmakers (420): median capacity $20,000 (maximum $20,000); still profitable with a $50 stake: 407 of 420; median largest guaranteed profit $161.60. Bookmakers publish no order-book depth, so only the Polymarket/Kalshi legs limit these sizes and the capacity stops at the search limit of $20,000; the bot's bets with bookmakers are capped at $2,500.

Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 321 | 11-22T11:01 | US Sassuolo Calcio v Genoa CFC | 178.2 | onexbet, pinnacle, unibet_se | 1.32% | $2499.99 | $32.91 | open |  |
| 320 | 11-22T11:01 | Bologna FC 1909 v Udinese Calcio | 178.3 | onexbet, smarkets | 0.30% | $2499.99 | $7.53 | open |  |
| 319 | 11-22T11:01 | Juventus FC v Venezia FC | 28.3 | onexbet, unibet_se | 1.37% | $2499.98 | $34.14 | open |  |
| 318 | 11-22T11:01 | FC Barcelona v Villarreal CF | 118.3 | coolbet, onexbet, smarkets | 1.67% | $2499.98 | $41.62 | open |  |
| 317 | 11-22T10:02 | FC Barcelona v Villarreal CF | 177.9 | matchbook, onexbet, smarkets | 1.54% | $2499.98 | $38.42 | open |  |
| 316 | 11-22T02:56 | SEA at SJ | 3.3 | coolbet, matchbook | 2.84% | $2499.99 | $70.92 | settled | $+70.93 |
| 315 | 11-22T02:56 | MIN at VAN | 3.3 | coolbet, williamhill | 2.24% | $2499.99 | $55.95 | settled | $+55.97 |
| 314 | 11-22T00:07 | BOS at SAC | 172.3 | no | 0.49% | $9.95 | $0.04 | settled | $+0.04 |
| 313 | 11-21T22:31 | POR at NYK | 118.1 | pinnacle | 1.79% | $2499.99 | $44.82 | settled | $+44.82 |
| 312 | 11-21T19:56 | Real Madrid CF v RC Celta de Vigo | 3.2 | betfair_ex_uk, marathonbet, matchbook | 0.79% | $2499.99 | $19.61 | settled | $+19.74 |
| 311 | 11-21T19:46 | Real Madrid CF v RC Celta de Vigo | 13.2 | betfair_ex_uk, marathonbet, smarkets | 0.40% | $2499.99 | $9.94 | settled | $+10.01 |
| 310 | 11-21T19:41 | AS Monaco FC v AJ Auxerre | 3.0 | smarkets, unibet_se | 0.64% | $2499.99 | $16.04 | settled | $+16.04 |
| 309 | 11-21T19:31 | FC Groningen v SC Heerenveen | 28.1 | matchbook, pinnacle, unibet_nl | 0.63% | $2499.99 | $15.64 | settled | $+15.64 |
| 308 | 11-21T19:31 | AS Monaco FC v AJ Auxerre | 13.1 | smarkets, unibet_se | 1.01% | $2499.98 | $25.31 | settled | $+25.35 |
| 307 | 11-21T19:31 | Real Madrid CF v RC Celta de Vigo | 28.1 | onexbet | 1.75% | $2499.99 | $43.70 | settled | $+43.70 |
| 306 | 11-21T19:16 | AS Monaco FC v AJ Auxerre | 28.1 | smarkets, unibet_se | 0.55% | $2499.98 | $13.62 | settled | $+13.69 |
| 305 | 11-21T19:16 | SSC Napoli v Torino FC | 28.1 | coolbet, pinnacle | 0.41% | $2499.99 | $10.32 | settled | $+10.32 |
| 304 | 11-21T19:01 | FC Groningen v SC Heerenveen | 58.2 | matchbook, nordicbet, unibet_nl | 0.47% | $2499.99 | $11.67 | settled | $+11.67 |
| 303 | 11-21T19:01 | Real Madrid CF v RC Celta de Vigo | 58.2 | matchbook, onexbet | 1.45% | $2499.98 | $36.10 | settled | $+36.19 |
| 302 | 11-21T18:02 | FC Groningen v SC Heerenveen | 117.9 | nordicbet, smarkets, unibet_nl | 0.47% | $2499.99 | $11.67 | settled | $+11.67 |
| 301 | 11-21T18:02 | Real Madrid CF v RC Celta de Vigo | 117.9 | matchbook, onexbet, smarkets | 1.54% | $2499.99 | $38.56 | settled | $+38.63 |
| 300 | 11-21T17:56 | EDM at CAR | 3.0 | matchbook, williamhill | 1.16% | $2499.99 | $29.01 | settled | $+29.04 |
| 299 | 11-21T17:47 | AS Monaco FC v AJ Auxerre | 117.9 | smarkets, tipico_de, unibet_se | 0.24% | $2499.98 | $5.83 | settled | $+5.90 |
| 298 | 11-21T17:41 | FC Utrecht v SC Cambuur-Leeuwarden | 3.0 | matchbook, pinnacle | 0.98% | $2499.99 | $24.54 | settled | $+24.54 |
| 297 | 11-21T17:31 | FC Utrecht v SC Cambuur-Leeuwarden | 13.1 | matchbook, onexbet | 1.70% | $2499.99 | $42.38 | settled | $+42.38 |
