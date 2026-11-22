# Paper-trading bot: status at 2026-11-22T20:05:12Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 368 / 351 |
| Realised profit | $-88,101.77 ≈ €-75,949.80 |
| … Polymarket/Kalshi only | $48.86 |
| … with bookmakers (all) | $-88,150.62 |
| … with bookmakers licensed in Spain only | $-2,285.19 |
| Open positions (cost) | $42,499.77 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $-56,201.76 ≈ €-48,449.79 |
| Return so far (realised / peak money in use) | -56.483% over 15.9 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 1019, executed 39, rounding 95, seen 1268, vanished 92.
Gaps using bookmakers: below_min_size 7, executed 329, no_cash 41, rounding 4, seen 429, vanished 39 (snapshots combined with Polymarket/Kalshi: 2346).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 303 (about 0.3 days at the current pace). **Add keys soon: below 3 days only the last 3 snapshots per kick-off are taken.**

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $14,136.71 | $122.90 | $4,486.78 | $2,369.73 |
| Kalshi | $5,800.00 | $7,246.40 | $3.61 | $2,216.01 | $2,967.42 |
| betanysports | $580.00 | $-585.80 | $0.00 | $4,190.72 | $-3,610.72 |
| betfair_ex_eu (Spain) | $580.00 | $1,737.81 | $0.00 | $837.89 | $-771.67 |
| betfair_ex_uk (Spain) | $580.00 | $117.16 | $0.00 | $388.80 | $117.16 |
| betfred_uk | $580.00 | $-768.02 | $0.00 | $1,348.02 | $-768.02 |
| betmgm | $580.00 | $7,821.78 | $0.00 | $5,577.36 | $-4,997.36 |
| betonlineag | $580.00 | $1,823.49 | $0.00 | $4,590.49 | $-10,211.76 |
| betrivers | $580.00 | $11,676.58 | $0.00 | $4,227.93 | $-1,141.39 |
| betsson | $580.00 | $2,119.70 | $0.00 | $986.99 | $-406.99 |
| betus | $580.00 | $-780.87 | $0.00 | $3,869.28 | $-3,289.28 |
| bovada | $580.00 | $-244.12 | $0.00 | $824.12 | $-244.12 |
| boylesports | $580.00 | $574.88 | $0.00 | $1,813.51 | $-1,233.51 |
| codere_it | $580.00 | $103.69 | $1,693.81 | $1,693.81 | $-715.21 |
| coolbet | $580.00 | $5,417.26 | $4,648.90 | $11,130.88 | $-8,022.38 |
| coral | $580.00 | $-4,370.81 | $3,346.44 | $6,136.50 | $-6,178.40 |
| draftkings | $580.00 | $-2,698.54 | $0.00 | $3,278.54 | $-2,698.54 |
| fanduel | $580.00 | $416.03 | $0.00 | $1,659.29 | $-2,247.51 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $-1,124.53 | $0.00 | $8,368.04 | $-7,633.02 |
| ladbrokes_uk | $580.00 | $-2,184.36 | $0.00 | $4,528.91 | $-7,734.96 |
| leovegas_se | $580.00 | $-20,519.71 | $0.00 | $47,555.97 | $-55,331.30 |
| lowvig | $580.00 | $-4,145.55 | $0.00 | $1,695.80 | $-6,543.63 |
| marathonbet (Spain) | $580.00 | $-19,635.57 | $11,315.96 | $11,315.96 | $-19,635.57 |
| matchbook | $580.00 | $14,571.96 | $0.00 | $12,468.15 | $-4,103.15 |
| mybookieag | $580.00 | $-7,038.42 | $2,492.01 | $4,422.60 | $-7,124.16 |
| nordicbet | $580.00 | $3,609.94 | $0.00 | $1,993.38 | $-1,413.38 |
| onexbet | $580.00 | $-73,793.66 | $3,176.06 | $69,050.38 | $-102,003.41 |
| pinnacle | $580.00 | $-10,445.46 | $11,416.48 | $12,018.68 | $-12,586.95 |
| skybet | $580.00 | $-1,150.75 | $0.00 | $775.64 | $-1,150.75 |
| smarkets | $580.00 | $4,966.43 | $1,192.69 | $15,944.68 | $-12,057.08 |
| tipico_de | $580.00 | $-1,205.07 | $0.00 | $5,851.05 | $-3,710.95 |
| unibet_nl | $580.00 | $-5,685.01 | $0.00 | $5,390.31 | $-16,211.87 |
| unibet_se | $580.00 | $-16,909.13 | $3,090.91 | $24,382.67 | $-28,469.93 |
| unibet_uk | $580.00 | $-1,287.96 | $0.00 | $1,340.27 | $-1,287.96 |
| williamhill (Spain) | $580.00 | $-2,192.18 | $0.00 | $1,686.02 | $-3,383.02 |
| winamax_de (Spain) | $580.00 | $1,144.17 | $0.00 | $805.80 | $-872.91 |

Peak money in use across all accounts at the same time: $155,979.62 ≈ €134,465.19.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 240 Polymarket/Kalshi and 476 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 239 | 183 | 119 | 1 | 0 |
| +1 min | 237 | 168 | 108 | 2 | 1 |
| +2 min | 232 | 153 | 95 | 5 | 3 |
| +5 min | 222 | 118 | 75 | 5 | 12 |
| bookmaker confirmation (~1 min) | 852 | 469 | 461 | 18 | 0 |
| next bookmaker snapshot | 694 | 179 | 170 | 20 | 0 |

Depth at detection (capacity = largest size still profitable after walking the order books):

- Polymarket/Kalshi gaps (240): median capacity $0 (maximum $2,826); still profitable with a $50 stake: 39 of 238; median largest guaranteed profit $0.00.
- Gaps with bookmakers (476): median capacity $20,000 (maximum $20,000); still profitable with a $50 stake: 461 of 476; median largest guaranteed profit $152.97. Bookmakers publish no order-book depth, so only the Polymarket/Kalshi legs limit these sizes and the capacity stops at the search limit of $20,000; the bot's bets with bookmakers are capped at $2,500.

Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 368 | 11-22T19:46 | Getafe CF v Club Atlético de Madrid | 13.5 | onexbet, smarkets, unibet_se | 0.59% | $2499.98 | $14.82 | open |  |
| 367 | 11-22T19:42 | Olympique de Marseille v Le Mans FC | 3.0 | coral, unibet_se | 0.39% | $2499.98 | $9.82 | open |  |
| 366 | 11-22T19:32 | Olympique de Marseille v Le Mans FC | 12.9 | coral, unibet_se | 0.39% | $2499.98 | $9.82 | open |  |
| 365 | 11-22T19:32 | Getafe CF v Club Atlético de Madrid | 27.9 | onexbet, smarkets, unibet_se | 1.40% | $2499.99 | $34.97 | open |  |
| 364 | 11-22T19:16 | Olympique de Marseille v Le Mans FC | 28.5 | codere_it, unibet_se | 1.63% | $2499.98 | $40.66 | open |  |
| 363 | 11-22T17:56 | PIT at PHI | 3.1 | coolbet, marathonbet | 2.04% | $2499.99 | $50.45 | open |  |
| 362 | 11-22T17:56 | ARI at KC | 3.1 | coolbet, pinnacle | 0.39% | $2499.98 | $8.90 | open |  |
| 361 | 11-22T17:56 | TB at DET | 3.1 | marathonbet, mybookieag | 2.08% | $2499.99 | $52.06 | open |  |
| 360 | 11-22T17:56 | NO at CHI | 3.1 | coolbet, pinnacle | 0.97% | $2499.99 | $23.74 | open |  |
| 359 | 11-22T17:56 | MIA at BUF | 3.2 | coolbet, pinnacle | 0.74% | $2499.99 | $17.80 | open |  |
| 358 | 11-22T17:47 | PIT at PHI | 12.8 | coolbet, marathonbet | 1.63% | $2499.99 | $40.56 | open |  |
| 357 | 11-22T17:47 | TB at DET | 12.8 | marathonbet, mybookieag | 2.20% | $2499.99 | $54.41 | open |  |
| 356 | 11-22T17:47 | MIA at BUF | 12.8 | coolbet, pinnacle | 0.74% | $2499.99 | $17.80 | open |  |
| 355 | 11-22T17:31 | PIT at PHI | 28.1 | coolbet, marathonbet | 1.22% | $2499.99 | $29.67 | open |  |
| 354 | 11-22T17:31 | TB at DET | 28.1 | marathonbet, mybookieag | 1.78% | $2499.98 | $43.52 | open |  |
| 353 | 11-22T17:31 | MIA at BUF | 28.1 | coolbet, pinnacle | 0.74% | $2499.99 | $17.80 | open |  |
| 352 | 11-22T16:32 | AC Milan v Frosinone Calcio | 27.8 | matchbook, onexbet, unibet_se | 0.41% | $2499.99 | $10.25 | settled | $+10.29 |
| 351 | 11-22T16:27 | Liverpool FC v Manchester United FC | 2.8 | matchbook, onexbet | 0.78% | $2499.99 | $19.55 | settled | $+19.56 |
| 350 | 11-22T15:52 | Trabzonspor v Eyüpspor | 7.4 | no | 0.54% | $26.75 | $0.15 | settled | $+0.15 |
| 349 | 11-22T15:42 | Go Ahead Eagles v Fortuna Sittard | 2.7 | matchbook, pinnacle, unibet_nl | 0.45% | $2499.99 | $11.18 | settled | $+11.18 |
| 348 | 11-22T15:05 | PIT at PHI | 174.2 | coolbet, marathonbet | 0.97% | $2499.99 | $23.74 | open |  |
| 347 | 11-22T14:47 | Go Ahead Eagles v Fortuna Sittard | 57.1 | coral | 1.43% | $2500.00 | $35.66 | settled | $+35.66 |
| 346 | 11-22T14:31 | CA Osasuna v Málaga CF | 178.1 | coolbet, onexbet, unibet_se | 0.28% | $2499.98 | $7.07 | settled | $+7.09 |
| 345 | 11-22T13:56 | Paris FC v Angers SCO | 3.1 | betonlineag, unibet_se | 0.28% | $2499.99 | $7.02 | settled | $+7.08 |
| 344 | 11-22T13:56 | US Sassuolo Calcio v Genoa CFC | 3.1 | boylesports, coolbet, pinnacle | 0.66% | $2499.98 | $16.53 | settled | $+16.55 |
