# Paper-trading bot: status at 2026-11-08T15:30:13Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 60 / 40 |
| Realised profit | $791.80 ≈ €682.59 |
| … Polymarket/Kalshi only | $0.00 |
| … with bookmakers (all) | $791.80 |
| … with bookmakers licensed in Spain only | $0.00 |
| Open positions (cost) | $40,263.66 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $28,051.80 ≈ €24,182.59 |
| Return so far (realised / peak money in use) | 1.368% over 1.7 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 64, executed 4, rounding 17, seen 93, vanished 6.
Gaps using bookmakers: executed 56, no_cash 41, rounding 1, seen 113, vanished 15 (snapshots combined with Polymarket/Kalshi: 553).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 1,157 (about 2.5 days at the current pace). **Add keys soon: below 3 days only the last 3 snapshots per kick-off are taken.**

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $5,543.36 | $115.84 | $140.80 | $5,543.36 |
| Kalshi | $5,800.00 | $5,963.94 | $148.07 | $400.96 | $5,231.94 |
| betanysports | $580.00 | $-1,097.48 | $1,224.13 | $4,190.72 | $-3,610.72 |
| betfair_ex_eu (Spain) | $580.00 | $453.07 | $0.00 | $126.93 | $453.07 |
| betfair_ex_uk (Spain) | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| betfred_uk | $580.00 | $-768.02 | $1,348.02 | $1,348.02 | $-768.02 |
| betmgm | $580.00 | $5,041.89 | $0.00 | $5,577.36 | $-4,997.36 |
| betonlineag | $580.00 | $1,513.82 | $0.00 | $3,432.94 | $-3,520.56 |
| betrivers | $580.00 | $1,389.05 | $0.00 | $1,721.39 | $-1,141.39 |
| betsson | $580.00 | $2,119.70 | $0.00 | $986.99 | $-406.99 |
| boylesports | $580.00 | $-1,233.51 | $1,813.51 | $1,813.51 | $-1,233.51 |
| codere_it | $580.00 | $-715.21 | $1,295.21 | $1,295.21 | $-715.21 |
| coolbet | $580.00 | $-5,339.30 | $4,516.83 | $5,249.57 | $-5,339.30 |
| coral | $580.00 | $1,338.67 | $0.00 | $1,948.91 | $-1,194.91 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $-7,633.02 | $6,720.04 | $6,720.04 | $-7,633.02 |
| leovegas_se | $580.00 | $1,789.30 | $0.00 | $1,403.00 | $-722.07 |
| lowvig | $580.00 | $-198.60 | $0.00 | $778.60 | $-198.60 |
| marathonbet (Spain) | $580.00 | $851.50 | $1,436.05 | $2,789.53 | $-1,673.21 |
| matchbook | $580.00 | $332.23 | $3,810.09 | $4,155.10 | $-3,925.78 |
| mybookieag | $580.00 | $-3,842.60 | $0.00 | $4,422.60 | $-3,842.60 |
| onexbet | $580.00 | $-1,127.97 | $5,933.96 | $22,357.23 | $-20,246.55 |
| pinnacle | $580.00 | $-4,370.17 | $3,113.47 | $3,723.57 | $-4,950.17 |
| skybet | $580.00 | $-375.11 | $567.67 | $567.67 | $-375.11 |
| smarkets | $580.00 | $-6,980.34 | $2,848.34 | $4,070.28 | $-6,980.34 |
| tipico_de | $580.00 | $2,622.00 | $0.00 | $486.19 | $93.81 |
| unibet_nl | $580.00 | $-6,207.35 | $1,344.67 | $4,157.51 | $-6,207.35 |
| unibet_se | $580.00 | $-2,183.31 | $4,027.76 | $5,913.30 | $-4,694.31 |
| winamax_de (Spain) | $580.00 | $-258.41 | $0.00 | $805.80 | $-258.41 |

Peak money in use across all accounts at the same time: $57,883.06 ≈ €49,899.19.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 24 Polymarket/Kalshi and 129 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 24 | 21 | 14 | 0 | 0 |
| +1 min | 23 | 18 | 10 | 0 | 1 |
| +2 min | 23 | 17 | 8 | 0 | 1 |
| +5 min | 23 | 12 | 6 | 0 | 1 |
| bookmaker confirmation (~1 min) | 244 | 94 | 89 | 5 | 0 |
| next bookmaker snapshot | 230 | 21 | 16 | 4 | 0 |

Depth at detection (153 gaps with full order books): median capacity (largest size still profitable after walking the order books) $20,000; median largest guaranteed profit $90.98. Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 60 | 11-08T14:26 | 1. FC Köln v Bayer 04 Leverkusen | 3.0 | coolbet, skybet, smarkets | 2.18% | $2499.99 | $54.50 | open |  |
| 59 | 11-08T14:20 | CIN at ATL | 9.0 | no | 0.58% | $29.85 | $0.15 | open |  |
| 58 | 11-08T14:16 | 1. FC Köln v Bayer 04 Leverkusen | 13.0 | gtbets, matchbook, smarkets | 3.22% | $2499.99 | $80.51 | open |  |
| 57 | 11-08T14:14 | CIN at ATL | 15.6 | no | 0.58% | $80.98 | $0.02 | open |  |
| 56 | 11-08T13:57 | AC Monza v Atalanta BC | 2.7 | matchbook, pinnacle, unibet_se | 1.31% | $2499.98 | $32.79 | open |  |
| 55 | 11-08T13:57 | Genoa CFC v AC Milan | 2.9 | coolbet, pinnacle, unibet_se | 0.24% | $2499.98 | $6.08 | open |  |
| 54 | 11-08T13:57 | Sunderland AFC v Chelsea FC | 2.9 | boylesports, marathonbet | 1.29% | $2499.99 | $32.18 | open |  |
| 53 | 11-08T13:57 | Crystal Palace FC v Liverpool FC | 2.9 | gtbets, onexbet, smarkets | 0.52% | $2499.98 | $12.90 | open |  |
| 52 | 11-08T13:47 | AC Monza v Atalanta BC | 13.0 | gtbets, smarkets, unibet_se | 0.98% | $2499.98 | $24.50 | open |  |
| 51 | 11-08T13:47 | Genoa CFC v AC Milan | 13.0 | coolbet, pinnacle, unibet_se | 0.24% | $2499.98 | $6.08 | open |  |
| 50 | 11-08T13:47 | Sunderland AFC v Chelsea FC | 13.0 | betfred_uk, boylesports, unibet_se | 1.94% | $2499.99 | $48.54 | open |  |
| 49 | 11-08T13:33 | CIN at ATL | 56.6 | no | 10.71% | $5.57 | $0.43 | open |  |
| 48 | 11-08T13:32 | Brighton & Hove Albion FC v Brentford FC | 27.6 | codere_it, coolbet, unibet_se | 0.51% | $2499.98 | $12.72 | open |  |
| 47 | 11-08T13:32 | Sunderland AFC v Chelsea FC | 27.6 | betfred_uk, matchbook, pinnacle | 0.26% | $2499.98 | $6.56 | open |  |
| 46 | 11-08T13:32 | Crystal Palace FC v Liverpool FC | 27.6 | onexbet, unibet_nl | 0.22% | $2499.99 | $5.40 | open |  |
| 45 | 11-08T12:57 | Elche CF v Real Betis Balompié | 3.0 | coolbet, matchbook | 1.30% | $1330.64 | $16.86 | settled | $+16.86 |
| 44 | 11-08T12:46 | Elche CF v Real Betis Balompié | 13.2 | marathonbet, smarkets, unibet_se | 0.99% | $2499.98 | $24.71 | settled | $+24.74 |
| 43 | 11-08T12:36 | CIN at ATL | 113.7 | no | 0.58% | $147.50 | $0.50 | open |  |
| 42 | 11-08T12:32 | Elche CF v Real Betis Balompié | 28.0 | onexbet, pinnacle, unibet_se | 1.28% | $2499.98 | $31.93 | settled | $+31.96 |
| 41 | 11-08T12:01 | AC Monza v Atalanta BC | 118.2 | betanysports, gtbets, matchbook | 0.47% | $2499.98 | $11.77 | open |  |
| 40 | 11-08T11:26 | SSC Napoli v SS Lazio | 3.1 | betanysports, betonlineag, marathonbet | 0.69% | $2499.99 | $17.18 | settled | $+17.20 |
| 39 | 11-08T11:16 | SSC Napoli v SS Lazio | 13.1 | betanysports, betonlineag, marathonbet | 0.69% | $2499.99 | $17.18 | settled | $+17.20 |
| 38 | 11-08T11:01 | AC Monza v Atalanta BC | 178.3 | betanysports, gtbets, smarkets | 0.53% | $2499.98 | $13.28 | open |  |
| 37 | 11-08T11:01 | Brighton & Hove Albion FC v Brentford FC | 178.3 | matchbook, onexbet | 0.87% | $2499.99 | $21.85 | open |  |
| 36 | 11-08T11:01 | Crystal Palace FC v Liverpool FC | 178.3 | onexbet, unibet_nl | 0.22% | $2499.99 | $5.44 | open |  |
