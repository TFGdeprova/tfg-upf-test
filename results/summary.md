# Paper-trading bot: status at 2026-11-08T18:31:38Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 71 / 56 |
| Realised profit | $1,167.25 ≈ €1,006.25 |
| … Polymarket/Kalshi only | $0.00 |
| … with bookmakers (all) | $1,167.25 |
| … with bookmakers licensed in Spain only | $0.00 |
| Open positions (cost) | $25,550.90 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $28,427.25 ≈ €24,506.25 |
| Return so far (realised / peak money in use) | 1.937% over 1.8 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 165, executed 5, rounding 18, seen 199, vanished 9.
Gaps using bookmakers: executed 66, no_cash 41, rounding 1, seen 125, vanished 17 (snapshots combined with Polymarket/Kalshi: 619).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 1,013 (about 2.0 days at the current pace). **Add keys soon: below 3 days only the last 3 snapshots per kick-off are taken.**

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $5,256.25 | $402.95 | $402.95 | $5,256.25 |
| Kalshi | $5,800.00 | $5,963.77 | $148.24 | $400.96 | $5,231.94 |
| betanysports | $580.00 | $-2,144.93 | $1,047.45 | $4,190.72 | $-3,610.72 |
| betfair_ex_eu (Spain) | $580.00 | $453.07 | $0.00 | $126.93 | $453.07 |
| betfair_ex_uk (Spain) | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| betfred_uk | $580.00 | $-768.02 | $0.00 | $1,348.02 | $-768.02 |
| betmgm | $580.00 | $5,041.89 | $0.00 | $5,577.36 | $-4,997.36 |
| betonlineag | $580.00 | $-3,076.67 | $4,590.49 | $4,590.49 | $-3,520.56 |
| betrivers | $580.00 | $1,389.05 | $0.00 | $1,721.39 | $-1,141.39 |
| betsson | $580.00 | $2,119.70 | $0.00 | $986.99 | $-406.99 |
| boylesports | $580.00 | $1,315.03 | $0.00 | $1,813.51 | $-1,233.51 |
| codere_it | $580.00 | $1,797.50 | $0.00 | $1,295.21 | $-715.21 |
| coolbet | $580.00 | $-455.65 | $2,683.08 | $7,199.91 | $-8,022.38 |
| coral | $580.00 | $1,338.67 | $0.00 | $1,948.91 | $-1,194.91 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $5,009.94 | $0.00 | $6,720.04 | $-7,633.02 |
| leovegas_se | $580.00 | $-1,181.83 | $2,971.13 | $2,971.13 | $-1,181.83 |
| lowvig | $580.00 | $-198.60 | $0.00 | $778.60 | $-198.60 |
| marathonbet (Spain) | $580.00 | $2,732.72 | $650.95 | $2,789.53 | $-1,673.21 |
| matchbook | $580.00 | $5,371.57 | $0.00 | $4,155.10 | $-3,925.78 |
| mybookieag | $580.00 | $-5,553.85 | $1,711.25 | $4,422.60 | $-5,553.85 |
| onexbet | $580.00 | $742.52 | $5,662.28 | $22,357.23 | $-20,246.55 |
| pinnacle | $580.00 | $-5,565.82 | $1,195.65 | $3,723.57 | $-5,565.82 |
| skybet | $580.00 | $-375.11 | $0.00 | $567.67 | $-375.11 |
| smarkets | $580.00 | $-8,164.89 | $1,184.55 | $4,070.28 | $-8,164.89 |
| tipico_de | $580.00 | $2,622.00 | $0.00 | $486.19 | $93.81 |
| unibet_nl | $580.00 | $-6,207.35 | $0.00 | $4,157.51 | $-6,207.35 |
| unibet_se | $580.00 | $-5,486.19 | $3,302.88 | $7,330.64 | $-5,486.19 |
| winamax_de (Spain) | $580.00 | $-258.41 | $0.00 | $805.80 | $-258.41 |

Peak money in use across all accounts at the same time: $60,263.56 ≈ €51,951.34.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 30 Polymarket/Kalshi and 144 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 30 | 26 | 18 | 0 | 0 |
| +1 min | 29 | 23 | 14 | 0 | 1 |
| +2 min | 29 | 21 | 11 | 0 | 1 |
| +5 min | 28 | 15 | 8 | 0 | 2 |
| bookmaker confirmation (~1 min) | 263 | 102 | 97 | 5 | 0 |
| next bookmaker snapshot | 245 | 22 | 17 | 4 | 0 |

Depth at detection (174 gaps with full order books): median capacity (largest size still profitable after walking the order books) $20,000; median largest guaranteed profit $90.33. Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 71 | 11-08T18:26 | LV at SF | 178.9 | no | 0.30% | $287.11 | $0.86 | open |  |
| 70 | 11-08T17:57 | CLE at NO | 2.8 | betonlineag, mybookieag | 0.62% | $2499.99 | $14.83 | open |  |
| 69 | 11-08T17:26 | Villarreal CF v Getafe CF | 3.1 | onexbet, pinnacle | 3.30% | $2499.99 | $82.60 | open |  |
| 68 | 11-08T16:26 | Manchester United FC v Aston Villa FC | 3.2 | betanysports, coolbet, onexbet | 1.25% | $2499.99 | $31.17 | open |  |
| 67 | 11-08T16:16 | SC Freiburg v 1. FC Union Berlin | 13.2 | onexbet, unibet_se | 0.47% | $2499.98 | $11.76 | open |  |
| 66 | 11-08T16:12 | Angers SCO v OGC Nice | 2.7 | coolbet, marathonbet, smarkets | 0.51% | $2499.99 | $12.66 | open |  |
| 65 | 11-08T16:12 | Le Havre AC v FC Lorient | 2.7 | betonlineag, leovegas_se | 0.79% | $2499.99 | $19.74 | open |  |
| 64 | 11-08T16:02 | Angers SCO v OGC Nice | 12.9 | onexbet, smarkets, unibet_se | 2.38% | $2499.99 | $59.57 | open |  |
| 63 | 11-08T16:02 | Le Havre AC v FC Lorient | 12.9 | betonlineag, leovegas_se | 0.79% | $2499.99 | $19.74 | open |  |
| 62 | 11-08T15:47 | Le Mans FC v AS Monaco FC | 27.8 | onexbet, unibet_se | 0.91% | $2499.99 | $22.77 | open |  |
| 61 | 11-08T15:47 | Le Havre AC v FC Lorient | 27.8 | betonlineag, leovegas_se, onexbet | 1.48% | $2499.98 | $36.94 | open |  |
| 60 | 11-08T14:26 | 1. FC Köln v Bayer 04 Leverkusen | 3.0 | coolbet, skybet, smarkets | 2.18% | $2499.99 | $54.50 | settled | $+54.53 |
| 59 | 11-08T14:20 | CIN at ATL | 9.0 | no | 0.58% | $29.85 | $0.15 | open |  |
| 58 | 11-08T14:16 | 1. FC Köln v Bayer 04 Leverkusen | 13.0 | gtbets, matchbook, smarkets | 3.22% | $2499.99 | $80.51 | settled | $+80.51 |
| 57 | 11-08T14:14 | CIN at ATL | 15.6 | no | 0.58% | $80.98 | $0.02 | open |  |
| 56 | 11-08T13:57 | AC Monza v Atalanta BC | 2.7 | matchbook, pinnacle, unibet_se | 1.31% | $2499.98 | $32.79 | settled | $+32.82 |
| 55 | 11-08T13:57 | Genoa CFC v AC Milan | 2.9 | coolbet, pinnacle, unibet_se | 0.24% | $2499.98 | $6.08 | settled | $+6.12 |
| 54 | 11-08T13:57 | Sunderland AFC v Chelsea FC | 2.9 | boylesports, marathonbet | 1.29% | $2499.99 | $32.18 | settled | $+32.18 |
| 53 | 11-08T13:57 | Crystal Palace FC v Liverpool FC | 2.9 | gtbets, onexbet, smarkets | 0.52% | $2499.98 | $12.90 | settled | $+12.95 |
| 52 | 11-08T13:47 | AC Monza v Atalanta BC | 13.0 | gtbets, smarkets, unibet_se | 0.98% | $2499.98 | $24.50 | settled | $+24.52 |
| 51 | 11-08T13:47 | Genoa CFC v AC Milan | 13.0 | coolbet, pinnacle, unibet_se | 0.24% | $2499.98 | $6.08 | settled | $+6.12 |
| 50 | 11-08T13:47 | Sunderland AFC v Chelsea FC | 13.0 | betfred_uk, boylesports, unibet_se | 1.94% | $2499.99 | $48.54 | settled | $+48.55 |
| 49 | 11-08T13:33 | CIN at ATL | 56.6 | no | 10.71% | $5.57 | $0.43 | open |  |
| 48 | 11-08T13:32 | Brighton & Hove Albion FC v Brentford FC | 27.6 | codere_it, coolbet, unibet_se | 0.51% | $2499.98 | $12.72 | settled | $+12.73 |
| 47 | 11-08T13:32 | Sunderland AFC v Chelsea FC | 27.6 | betfred_uk, matchbook, pinnacle | 0.26% | $2499.98 | $6.56 | settled | $+6.56 |
