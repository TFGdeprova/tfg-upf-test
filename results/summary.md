# Paper-trading bot: status at 2026-11-23T05:57:53Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 379 / 379 |
| Realised profit | $-87,275.47 ≈ €-75,237.47 |
| … Polymarket/Kalshi only | $49.81 |
| … with bookmakers (all) | $-87,325.28 |
| … with bookmakers licensed in Spain only | $-2,172.29 |
| Open positions (cost) | $0.00 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $-54,795.47 ≈ €-47,237.47 |
| Return so far (realised / peak money in use) | -55.953% over 16.3 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 1063, executed 40, rounding 96, seen 1323, vanished 101.
Gaps using bookmakers: below_min_size 8, executed 339, no_cash 41, rounding 4, seen 443, vanished 42 (snapshots combined with Polymarket/Kalshi: 2401).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 37. **Add keys soon: below 3 days only the last 3 snapshots per kick-off are taken.**

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $13,822.24 | $0.00 | $4,486.78 | $2,369.73 |
| Kalshi | $5,800.00 | $7,127.99 | $0.00 | $2,216.01 | $2,967.42 |
| betanysports | $580.00 | $-585.80 | $0.00 | $4,190.72 | $-3,610.72 |
| betfair_ex_eu (Spain) | $580.00 | $2,123.90 | $0.00 | $2,139.00 | $-771.67 |
| betfair_ex_uk (Spain) | $580.00 | $117.16 | $0.00 | $388.80 | $117.16 |
| betfred_uk | $580.00 | $-768.02 | $0.00 | $1,348.02 | $-768.02 |
| betmgm | $580.00 | $7,821.78 | $0.00 | $5,577.36 | $-4,997.36 |
| betonlineag | $580.00 | $1,823.49 | $0.00 | $4,590.49 | $-10,211.76 |
| betrivers | $580.00 | $11,676.58 | $0.00 | $4,227.93 | $-1,141.39 |
| betsson | $580.00 | $2,119.70 | $0.00 | $986.99 | $-406.99 |
| betus | $580.00 | $-1,506.15 | $0.00 | $3,869.28 | $-3,289.28 |
| bovada | $580.00 | $-244.12 | $0.00 | $824.12 | $-244.12 |
| boylesports | $580.00 | $574.88 | $0.00 | $1,813.51 | $-1,233.51 |
| codere_it | $580.00 | $103.69 | $0.00 | $1,693.81 | $-715.21 |
| coolbet | $580.00 | $16,585.22 | $0.00 | $11,130.88 | $-8,022.38 |
| coral | $580.00 | $-4,370.81 | $0.00 | $6,136.50 | $-6,178.40 |
| draftkings | $580.00 | $-4,529.72 | $0.00 | $3,278.54 | $-4,529.72 |
| fanduel | $580.00 | $416.03 | $0.00 | $1,659.29 | $-2,247.51 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $-1,124.53 | $0.00 | $8,368.04 | $-7,633.02 |
| ladbrokes_uk | $580.00 | $-2,184.36 | $0.00 | $4,528.91 | $-7,734.96 |
| leovegas_se | $580.00 | $-20,519.71 | $0.00 | $47,555.97 | $-55,331.30 |
| lowvig | $580.00 | $-4,145.55 | $0.00 | $1,695.80 | $-6,543.63 |
| marathonbet (Spain) | $580.00 | $-8,298.35 | $0.00 | $12,666.27 | $-20,985.88 |
| matchbook | $580.00 | $12,295.84 | $0.00 | $12,468.15 | $-4,103.15 |
| mybookieag | $580.00 | $-7,038.42 | $0.00 | $4,422.60 | $-7,124.16 |
| nordicbet | $580.00 | $3,609.94 | $0.00 | $1,993.38 | $-1,413.38 |
| onexbet | $580.00 | $-68,743.79 | $0.00 | $69,050.38 | $-102,003.41 |
| pinnacle | $580.00 | $325.78 | $0.00 | $13,234.59 | $-12,586.95 |
| skybet | $580.00 | $-1,150.75 | $0.00 | $775.64 | $-1,150.75 |
| smarkets | $580.00 | $4,966.43 | $0.00 | $15,944.68 | $-12,057.08 |
| sport888 (Spain) | $580.00 | $1,775.90 | $0.00 | $1,314.18 | $-734.18 |
| tipico_de | $580.00 | $-1,205.07 | $0.00 | $5,851.05 | $-3,710.95 |
| unibet_nl | $580.00 | $-3,911.29 | $0.00 | $5,390.31 | $-16,211.87 |
| unibet_se | $580.00 | $-9,348.89 | $0.00 | $24,382.67 | $-28,469.93 |
| unibet_uk | $580.00 | $-1,287.96 | $0.00 | $1,340.27 | $-1,287.96 |
| williamhill (Spain) | $580.00 | $-2,842.88 | $0.00 | $1,686.02 | $-3,383.02 |
| winamax_de (Spain) | $580.00 | $1,144.17 | $0.00 | $805.80 | $-872.91 |

Peak money in use across all accounts at the same time: $155,979.62 ≈ €134,465.19.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 258 Polymarket/Kalshi and 490 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 257 | 190 | 125 | 1 | 0 |
| +1 min | 254 | 172 | 112 | 2 | 2 |
| +2 min | 248 | 156 | 98 | 5 | 5 |
| +5 min | 239 | 120 | 76 | 5 | 14 |
| bookmaker confirmation (~1 min) | 869 | 479 | 470 | 22 | 0 |
| next bookmaker snapshot | 702 | 181 | 172 | 23 | 0 |

Depth at detection (capacity = largest size still profitable after walking the order books):

- Polymarket/Kalshi gaps (258): median capacity $0 (maximum $2,826); still profitable with a $50 stake: 42 of 256; median largest guaranteed profit $0.00.
- Gaps with bookmakers (490): median capacity $20,000 (maximum $20,000); still profitable with a $50 stake: 474 of 490; median largest guaranteed profit $153.88. Bookmakers publish no order-book depth, so only the Polymarket/Kalshi legs limit these sizes and the capacity stops at the search limit of $20,000; the bot's bets with bookmakers are capped at $2,500.

Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 379 | 11-23T01:06 | MIN at SF | 13.4 | coolbet, unibet_nl | 1.17% | $2500.00 | $28.68 | settled | $+29.19 |
| 378 | 11-23T00:56 | IND at NYK | 3.4 | sport888 | 0.40% | $2500.00 | $10.09 | settled | $+10.09 |
| 377 | 11-23T00:51 | MIN at SF | 28.4 | coolbet, unibet_nl | 1.17% | $2500.00 | $28.68 | settled | $+29.19 |
| 376 | 11-23T00:46 | IND at NYK | 13.4 | betus, matchbook | 2.99% | $2499.99 | $74.75 | settled | $+74.76 |
| 375 | 11-23T00:31 | IND at NYK | 28.4 | williamhill | 4.11% | $2500.00 | $102.80 | settled | $+102.81 |
| 374 | 11-23T00:30 | IND at NYK | 29.1 | no | 0.24% | $406.06 | $0.94 | settled | $+0.95 |
| 373 | 11-22T21:22 | LV at DEN | 3.0 | betfair_ex_eu, coolbet | 1.00% | $2499.99 | $24.73 | settled | $+25.10 |
| 372 | 11-22T21:21 | JAC at NYG | 3.0 | marathonbet, pinnacle | 0.36% | $2500.00 | $8.90 | settled | $+8.99 |
| 371 | 11-22T21:11 | JAC at NYG | 13.0 | draftkings, marathonbet | 1.08% | $2499.99 | $26.71 | settled | $+27.02 |
| 370 | 11-22T21:02 | NYJ at LAC | 2.9 | coolbet, matchbook | 0.60% | $2499.99 | $14.83 | settled | $+14.88 |
| 369 | 11-22T20:51 | NYJ at LAC | 13.0 | coolbet, matchbook | 0.23% | $2499.99 | $4.94 | settled | $+5.71 |
| 368 | 11-22T19:46 | Getafe CF v Club Atlético de Madrid | 13.5 | onexbet, smarkets, unibet_se | 0.59% | $2499.98 | $14.82 | settled | $+14.86 |
| 367 | 11-22T19:42 | Olympique de Marseille v Le Mans FC | 3.0 | coral, unibet_se | 0.39% | $2499.98 | $9.82 | settled | $+9.82 |
| 366 | 11-22T19:32 | Olympique de Marseille v Le Mans FC | 12.9 | coral, unibet_se | 0.39% | $2499.98 | $9.82 | settled | $+9.82 |
| 365 | 11-22T19:32 | Getafe CF v Club Atlético de Madrid | 27.9 | onexbet, smarkets, unibet_se | 1.40% | $2499.99 | $34.97 | settled | $+35.03 |
| 364 | 11-22T19:16 | Olympique de Marseille v Le Mans FC | 28.5 | codere_it, unibet_se | 1.63% | $2499.98 | $40.66 | settled | $+40.66 |
| 363 | 11-22T17:56 | PIT at PHI | 3.1 | coolbet, marathonbet | 2.04% | $2499.99 | $50.45 | settled | $+50.96 |
| 362 | 11-22T17:56 | ARI at KC | 3.1 | coolbet, pinnacle | 0.39% | $2499.98 | $8.90 | settled | $+9.82 |
| 361 | 11-22T17:56 | TB at DET | 3.1 | marathonbet, mybookieag | 2.08% | $2499.99 | $52.06 | settled | $+52.06 |
| 360 | 11-22T17:56 | NO at CHI | 3.1 | coolbet, pinnacle | 0.97% | $2499.99 | $23.74 | settled | $+24.20 |
| 359 | 11-22T17:56 | MIA at BUF | 3.2 | coolbet, pinnacle | 0.74% | $2499.99 | $17.80 | settled | $+18.46 |
| 358 | 11-22T17:47 | PIT at PHI | 12.8 | coolbet, marathonbet | 1.63% | $2499.99 | $40.56 | settled | $+40.76 |
| 357 | 11-22T17:47 | TB at DET | 12.8 | marathonbet, mybookieag | 2.20% | $2499.99 | $54.41 | settled | $+55.01 |
| 356 | 11-22T17:47 | MIA at BUF | 12.8 | coolbet, pinnacle | 0.74% | $2499.99 | $17.80 | settled | $+18.46 |
| 355 | 11-22T17:31 | PIT at PHI | 28.1 | coolbet, marathonbet | 1.22% | $2499.99 | $29.67 | settled | $+30.50 |
