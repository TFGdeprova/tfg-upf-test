# Paper-trading bot: status at 2026-11-08T11:33:15Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 40 / 31 |
| Realised profit | $614.61 ≈ €529.84 |
| … Polymarket/Kalshi only | $0.00 |
| … with bookmakers (all) | $614.61 |
| … with bookmakers licensed in Spain only | $0.00 |
| Open positions (cost) | $22,499.88 |
| Money in transit between accounts | $1,399.69 |
| Equity (cash + open at cost + in transit) | $26,714.62 ≈ €23,029.84 |
| Return so far (realised / peak money in use) | 1.316% over 1.5 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 1, seen 2, vanished 1.
Gaps using bookmakers: executed 40, no_cash 41, rounding 1, seen 95, vanished 13 (snapshots combined with Polymarket/Kalshi: 503).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 1,311 (about 3.0 days at the current pace). **Add keys soon: below 3 days only the last 3 snapshots per kick-off are taken.**

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $5,659.20 | $0.00 | $140.80 | $5,659.20 |
| Kalshi | $5,800.00 | $5,632.90 | $0.00 | $167.10 | $5,632.90 |
| betanysports | $580.00 | $-2,998.09 | $3,578.09 | $3,578.09 | $-2,998.09 |
| betfair_ex_eu (Spain) | $580.00 | $453.07 | $0.00 | $126.93 | $453.07 |
| betfair_ex_uk (Spain) | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| betfred_uk | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| betmgm | $580.00 | $5,041.89 | $0.00 | $5,577.36 | $-4,997.36 |
| betonlineag | $580.00 | $-3,520.56 | $3,432.94 | $3,432.94 | $-3,520.56 |
| betrivers | $580.00 | $1,389.05 | $0.00 | $1,721.39 | $-1,141.39 |
| betsson | $580.00 | $-406.99 | $986.99 | $986.99 | $-406.99 |
| coolbet | $580.00 | $-89.73 | $0.00 | $669.73 | $-89.73 |
| coral | $580.00 | $1,338.67 | $0.00 | $1,948.91 | $-1,194.91 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $-2,121.28 | $1,208.30 | $1,492.98 | $-2,121.28 |
| leovegas_se | $580.00 | $1,789.30 | $0.00 | $1,403.00 | $-722.07 |
| lowvig | $580.00 | $-198.60 | $0.00 | $778.60 | $-198.60 |
| marathonbet (Spain) | $580.00 | $1,064.24 | $52.08 | $1,986.36 | $-1,406.36 |
| matchbook | $580.00 | $3,022.41 | $609.73 | $2,789.92 | $-3,925.78 |
| mybookieag | $580.00 | $-3,842.60 | $0.00 | $4,422.60 | $-3,842.60 |
| onexbet | $580.00 | $-2,998.30 | $8,373.74 | $22,357.23 | $-20,246.55 |
| pinnacle | $580.00 | $-1,226.60 | $0.00 | $1,226.60 | $-1,226.60 |
| skybet | $580.00 | $192.56 | $0.00 | $387.44 | $192.56 |
| smarkets | $580.00 | $-4,229.38 | $2,047.80 | $2,761.58 | $-4,229.38 |
| tipico_de | $580.00 | $2,622.00 | $0.00 | $486.19 | $93.81 |
| unibet_nl | $580.00 | $-5,806.48 | $1,558.00 | $4,157.51 | $-5,806.48 |
| unibet_se | $580.00 | $566.78 | $652.21 | $1,879.37 | $-1,299.37 |
| winamax_de (Spain) | $580.00 | $-258.41 | $0.00 | $805.80 | $-258.41 |

Peak money in use across all accounts at the same time: $46,687.66 ≈ €40,247.99.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 4 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 8 Polymarket/Kalshi and 110 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 8 | 5 | 0 | 0 | 0 |
| +1 min | 7 | 4 | 0 | 0 | 1 |
| +2 min | 7 | 5 | 0 | 0 | 1 |
| +5 min | 7 | 3 | 0 | 0 | 1 |
| bookmaker confirmation (~1 min) | 206 | 82 | 79 | 2 | 0 |
| next bookmaker snapshot | 203 | 17 | 14 | 0 | 0 |

Depth at detection (118 gaps with full order books): median capacity (largest size still profitable after walking the order books) $20,000; median largest guaranteed profit $109.41. Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 40 | 11-08T11:26 | SSC Napoli v SS Lazio | 3.1 | betanysports, betonlineag, marathonbet | 0.69% | $2499.99 | $17.18 | open |  |
| 39 | 11-08T11:16 | SSC Napoli v SS Lazio | 13.1 | betanysports, betonlineag, marathonbet | 0.69% | $2499.99 | $17.18 | open |  |
| 38 | 11-08T11:01 | AC Monza v Atalanta BC | 178.3 | betanysports, gtbets, smarkets | 0.53% | $2499.98 | $13.28 | open |  |
| 37 | 11-08T11:01 | Brighton & Hove Albion FC v Brentford FC | 178.3 | matchbook, onexbet | 0.87% | $2499.99 | $21.85 | open |  |
| 36 | 11-08T11:01 | Crystal Palace FC v Liverpool FC | 178.3 | onexbet, unibet_nl | 0.22% | $2499.99 | $5.44 | open |  |
| 35 | 11-08T11:01 | Elche CF v Real Betis Balompié | 118.3 | betsson, onexbet | 1.07% | $2499.99 | $26.70 | open |  |
| 34 | 11-08T11:01 | SSC Napoli v SS Lazio | 28.3 | betanysports, onexbet, smarkets | 0.53% | $2499.98 | $13.26 | open |  |
| 33 | 11-08T10:31 | SSC Napoli v SS Lazio | 58.5 | betonlineag, onexbet, unibet_se | 0.44% | $2499.98 | $11.01 | open |  |
| 32 | 11-08T10:01 | Elche CF v Real Betis Balompié | 178.4 | onexbet, smarkets, unibet_nl | 0.73% | $2499.99 | $18.22 | open |  |
| 31 | 11-08T02:57 | VAN at EDM | 3.0 | betmgm, mybookieag | 0.39% | $2499.99 | $9.82 | settled | $+9.82 |
| 30 | 11-08T02:47 | VAN at EDM | 13.0 | betmgm, mybookieag | 0.39% | $2499.99 | $9.82 | settled | $+9.82 |
| 29 | 11-08T02:31 | VAN at EDM | 28.4 | betmgm, mybookieag | 0.39% | $2499.99 | $9.82 | settled | $+9.82 |
| 28 | 11-08T01:01 | VAN at EDM | 118.3 | betmgm, mybookieag | 0.39% | $2499.99 | $9.82 | settled | $+9.82 |
| 27 | 11-08T00:26 | BKN at ATL | 3.3 | betrivers, lowvig | 1.22% | $2499.99 | $30.45 | settled | $+30.45 |
| 26 | 11-07T19:56 | Valencia CF v Real Madrid CF | 3.0 | marathonbet, matchbook, unibet_nl | 0.91% | $2499.98 | $22.57 | settled | $+22.70 |
| 25 | 11-07T19:52 | Paris Saint-Germain FC v ES Troyes AC | 13.0 | onexbet, smarkets | 0.55% | $2499.99 | $13.82 | settled | $+13.86 |
| 24 | 11-07T19:46 | Valencia CF v Real Madrid CF | 13.0 | onexbet, smarkets, unibet_nl | 1.91% | $2499.99 | $47.71 | settled | $+47.76 |
| 23 | 11-07T19:42 | AS Roma v US Sassuolo Calcio | 3.0 | skybet, smarkets, unibet_se | 0.73% | $2499.99 | $18.35 | settled | $+18.37 |
| 22 | 11-07T19:37 | Paris Saint-Germain FC v ES Troyes AC | 28.0 | onexbet, smarkets | 1.36% | $2499.99 | $34.01 | settled | $+34.08 |
| 21 | 11-07T19:32 | SBV Excelsior v Go Ahead Eagles | 27.9 | betonlineag, matchbook, unibet_nl | 0.68% | $2499.99 | $16.94 | settled | $+16.95 |
| 20 | 11-07T19:32 | Valencia CF v Real Madrid CF | 28.0 | onexbet, unibet_nl | 1.48% | $2499.98 | $36.84 | settled | $+36.92 |
| 19 | 11-07T19:07 | Paris Saint-Germain FC v ES Troyes AC | 58.0 | onexbet | 2.20% | $288.22 | $6.35 | settled | $+6.35 |
| 18 | 11-07T19:01 | SBV Excelsior v Go Ahead Eagles | 58.0 | coolbet, matchbook, unibet_nl | 0.46% | $2499.99 | $11.50 | settled | $+11.52 |
| 17 | 11-07T19:01 | Valencia CF v Real Madrid CF | 58.0 | coral, smarkets, unibet_nl | 1.34% | $2499.99 | $33.51 | settled | $+33.59 |
| 16 | 11-07T18:46 | AS Roma v US Sassuolo Calcio | 58.0 | onexbet, smarkets, winamax_de | 0.83% | $2499.98 | $20.72 | settled | $+20.78 |
