# Paper-trading bot: status at 2026-11-08T22:04:31Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 77 / 70 |
| Realised profit | $1,481.08 ≈ €1,276.79 |
| … Polymarket/Kalshi only | $1.25 |
| … with bookmakers (all) | $1,479.83 |
| … with bookmakers licensed in Spain only | $0.00 |
| Open positions (cost) | $12,829.97 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $28,741.08 ≈ €24,776.80 |
| Return so far (realised / peak money in use) | 2.458% over 2.0 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 183, executed 6, rounding 18, seen 219, vanished 10.
Gaps using bookmakers: executed 71, no_cash 41, rounding 1, seen 131, vanished 18 (snapshots combined with Polymarket/Kalshi: 652).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 909 (about 1.8 days at the current pace). **Add keys soon: below 3 days only the last 3 snapshots per kick-off are taken.**

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $5,235.87 | $313.65 | $402.95 | $5,235.87 |
| Kalshi | $5,800.00 | $6,206.39 | $16.38 | $400.96 | $5,231.94 |
| betanysports | $580.00 | $-2,144.93 | $0.00 | $4,190.72 | $-3,610.72 |
| betfair_ex_eu (Spain) | $580.00 | $453.07 | $0.00 | $126.93 | $453.07 |
| betfair_ex_uk (Spain) | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| betfred_uk | $580.00 | $-768.02 | $0.00 | $1,348.02 | $-768.02 |
| betmgm | $580.00 | $5,041.89 | $0.00 | $5,577.36 | $-4,997.36 |
| betonlineag | $580.00 | $-4,391.48 | $1,314.81 | $4,590.49 | $-4,391.48 |
| betrivers | $580.00 | $1,389.05 | $0.00 | $1,721.39 | $-1,141.39 |
| betsson | $580.00 | $2,119.70 | $0.00 | $986.99 | $-406.99 |
| boylesports | $580.00 | $1,315.03 | $0.00 | $1,813.51 | $-1,233.51 |
| codere_it | $580.00 | $1,797.50 | $0.00 | $1,295.21 | $-715.21 |
| coolbet | $580.00 | $1,990.70 | $2,597.47 | $7,199.91 | $-8,022.38 |
| coral | $580.00 | $1,338.67 | $0.00 | $1,948.91 | $-1,194.91 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $5,009.94 | $0.00 | $6,720.04 | $-7,633.02 |
| leovegas_se | $580.00 | $5,327.11 | $1,067.44 | $2,971.13 | $-1,181.83 |
| lowvig | $580.00 | $-198.60 | $0.00 | $778.60 | $-198.60 |
| marathonbet (Spain) | $580.00 | $2,060.64 | $672.08 | $2,789.53 | $-1,673.21 |
| matchbook | $580.00 | $5,371.57 | $0.00 | $4,155.10 | $-3,925.78 |
| mybookieag | $580.00 | $-3,038.31 | $0.00 | $4,422.60 | $-5,553.85 |
| onexbet | $580.00 | $96.36 | $3,157.93 | $22,357.23 | $-20,246.55 |
| pinnacle | $580.00 | $-4,296.42 | $1,313.20 | $3,723.57 | $-6,879.02 |
| skybet | $580.00 | $-375.11 | $0.00 | $567.67 | $-375.11 |
| smarkets | $580.00 | $-8,947.57 | $782.68 | $4,070.28 | $-8,947.57 |
| tipico_de | $580.00 | $2,622.00 | $0.00 | $486.19 | $93.81 |
| unibet_nl | $580.00 | $-7,801.68 | $1,594.33 | $4,157.51 | $-7,801.68 |
| unibet_se | $580.00 | $-403.85 | $0.00 | $7,330.64 | $-5,486.19 |
| winamax_de (Spain) | $580.00 | $-258.41 | $0.00 | $805.80 | $-258.41 |

Peak money in use across all accounts at the same time: $60,263.56 ≈ €51,951.34.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 32 Polymarket/Kalshi and 150 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 32 | 28 | 20 | 0 | 0 |
| +1 min | 31 | 25 | 16 | 0 | 1 |
| +2 min | 31 | 23 | 13 | 0 | 1 |
| +5 min | 30 | 17 | 10 | 0 | 2 |
| bookmaker confirmation (~1 min) | 272 | 105 | 100 | 5 | 0 |
| next bookmaker snapshot | 248 | 23 | 18 | 4 | 0 |

Depth at detection (182 gaps with full order books): median capacity (largest size still profitable after walking the order books) $20,000; median largest guaranteed profit $90.98. Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 77 | 11-08T21:12 | GB at NE | 12.1 | no | 0.22% | $42.92 | $0.08 | open |  |
| 76 | 11-08T19:56 | Club Atlético de Madrid v FC Barcelona | 3.1 | onexbet, pinnacle, unibet_nl | 1.38% | $2499.98 | $34.47 | open |  |
| 75 | 11-08T19:46 | Club Atlético de Madrid v FC Barcelona | 13.2 | coolbet, marathonbet, unibet_nl | 1.08% | $2499.99 | $27.01 | open |  |
| 74 | 11-08T19:41 | ACF Fiorentina v Juventus FC | 3.1 | betonlineag, onexbet | 0.98% | $2499.99 | $24.44 | open |  |
| 73 | 11-08T19:31 | Club Atlético de Madrid v FC Barcelona | 28.1 | coolbet, onexbet, unibet_nl | 1.52% | $2499.99 | $38.05 | open |  |
| 72 | 11-08T19:17 | Racing Club de Lens v Olympique de Marseille | 27.8 | leovegas_se, onexbet, smarkets | 0.34% | $2499.99 | $8.49 | open |  |
| 71 | 11-08T18:26 | LV at SF | 178.9 | no | 0.30% | $287.11 | $0.86 | open |  |
| 70 | 11-08T17:57 | CLE at NO | 2.8 | betonlineag, mybookieag | 0.62% | $2499.99 | $14.83 | settled | $+15.55 |
| 69 | 11-08T17:26 | Villarreal CF v Getafe CF | 3.1 | onexbet, pinnacle | 3.30% | $2499.99 | $82.60 | settled | $+82.61 |
| 68 | 11-08T16:26 | Manchester United FC v Aston Villa FC | 3.2 | betanysports, coolbet, onexbet | 1.25% | $2499.99 | $31.17 | settled | $+31.18 |
| 67 | 11-08T16:16 | SC Freiburg v 1. FC Union Berlin | 13.2 | onexbet, unibet_se | 0.47% | $2499.98 | $11.76 | settled | $+11.79 |
| 66 | 11-08T16:12 | Angers SCO v OGC Nice | 2.7 | coolbet, marathonbet, smarkets | 0.51% | $2499.99 | $12.66 | settled | $+12.67 |
| 65 | 11-08T16:12 | Le Havre AC v FC Lorient | 2.7 | betonlineag, leovegas_se | 0.79% | $2499.99 | $19.74 | settled | $+19.74 |
| 64 | 11-08T16:02 | Angers SCO v OGC Nice | 12.9 | onexbet, smarkets, unibet_se | 2.38% | $2499.99 | $59.57 | settled | $+59.58 |
| 63 | 11-08T16:02 | Le Havre AC v FC Lorient | 12.9 | betonlineag, leovegas_se | 0.79% | $2499.99 | $19.74 | settled | $+19.74 |
| 62 | 11-08T15:47 | Le Mans FC v AS Monaco FC | 27.8 | onexbet, unibet_se | 0.91% | $2499.99 | $22.77 | settled | $+22.78 |
| 61 | 11-08T15:47 | Le Havre AC v FC Lorient | 27.8 | betonlineag, leovegas_se, onexbet | 1.48% | $2499.98 | $36.94 | settled | $+36.94 |
| 60 | 11-08T14:26 | 1. FC Köln v Bayer 04 Leverkusen | 3.0 | coolbet, skybet, smarkets | 2.18% | $2499.99 | $54.50 | settled | $+54.53 |
| 59 | 11-08T14:20 | CIN at ATL | 9.0 | no | 0.58% | $29.85 | $0.15 | settled | $+0.15 |
| 58 | 11-08T14:16 | 1. FC Köln v Bayer 04 Leverkusen | 13.0 | gtbets, matchbook, smarkets | 3.22% | $2499.99 | $80.51 | settled | $+80.51 |
| 57 | 11-08T14:14 | CIN at ATL | 15.6 | no | 0.58% | $80.98 | $0.02 | settled | $+0.02 |
| 56 | 11-08T13:57 | AC Monza v Atalanta BC | 2.7 | matchbook, pinnacle, unibet_se | 1.31% | $2499.98 | $32.79 | settled | $+32.82 |
| 55 | 11-08T13:57 | Genoa CFC v AC Milan | 2.9 | coolbet, pinnacle, unibet_se | 0.24% | $2499.98 | $6.08 | settled | $+6.12 |
| 54 | 11-08T13:57 | Sunderland AFC v Chelsea FC | 2.9 | boylesports, marathonbet | 1.29% | $2499.99 | $32.18 | settled | $+32.18 |
| 53 | 11-08T13:57 | Crystal Palace FC v Liverpool FC | 2.9 | gtbets, onexbet, smarkets | 0.52% | $2499.98 | $12.90 | settled | $+12.95 |
