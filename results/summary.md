# Paper-trading bot: status at 2026-11-21T12:41:59Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 237 / 221 |
| Realised profit | $-91,365.08 ≈ €-78,763.00 |
| … Polymarket/Kalshi only | $48.43 |
| … with bookmakers (all) | $-91,413.51 |
| … with bookmakers licensed in Spain only | $-2,285.19 |
| Open positions (cost) | $39,999.77 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $-60,625.08 ≈ €-52,263.00 |
| Return so far (realised / peak money in use) | -58.575% over 14.6 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 871, executed 36, rounding 90, seen 1085, vanished 68.
Gaps using bookmakers: below_min_size 4, executed 201, no_cash 41, rounding 3, seen 288, vanished 30 (snapshots combined with Polymarket/Kalshi: 1762).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 2,403 (about 5.3 days at the current pace).

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $14,960.75 | $0.00 | $4,486.78 | $2,369.73 |
| Kalshi | $5,800.00 | $7,254.92 | $0.00 | $2,216.01 | $2,967.42 |
| betanysports | $580.00 | $-894.59 | $0.00 | $4,190.72 | $-3,610.72 |
| betfair_ex_eu (Spain) | $580.00 | $453.07 | $0.00 | $126.93 | $453.07 |
| betfair_ex_uk (Spain) | $580.00 | $505.96 | $0.00 | $74.04 | $505.96 |
| betfred_uk | $580.00 | $-768.02 | $0.00 | $1,348.02 | $-768.02 |
| betmgm | $580.00 | $5,098.25 | $0.00 | $5,577.36 | $-4,997.36 |
| betonlineag | $580.00 | $-4,402.73 | $1,291.35 | $4,590.49 | $-4,402.73 |
| betrivers | $580.00 | $6,969.49 | $1,409.31 | $2,248.46 | $-1,141.39 |
| betsson | $580.00 | $2,119.70 | $0.00 | $986.99 | $-406.99 |
| betus | $580.00 | $-510.68 | $1,090.68 | $1,090.68 | $-510.68 |
| bovada | $580.00 | $-244.12 | $0.00 | $824.12 | $-244.12 |
| boylesports | $580.00 | $1,315.03 | $0.00 | $1,813.51 | $-1,233.51 |
| codere_it | $580.00 | $1,797.50 | $0.00 | $1,295.21 | $-715.21 |
| coolbet | $580.00 | $5,688.02 | $1,367.75 | $7,199.91 | $-8,022.38 |
| coral | $580.00 | $361.09 | $977.58 | $1,948.91 | $-1,194.91 |
| draftkings | $580.00 | $-2,698.54 | $0.00 | $3,278.54 | $-2,698.54 |
| fanduel | $580.00 | $416.03 | $0.00 | $1,659.29 | $-2,247.51 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $3,229.45 | $1,780.49 | $6,720.04 | $-7,633.02 |
| ladbrokes_uk | $580.00 | $-5,844.26 | $1,895.35 | $4,528.91 | $-5,844.26 |
| leovegas_se | $580.00 | $-14,327.40 | $1,666.57 | $47,555.97 | $-55,331.30 |
| lowvig | $580.00 | $-4,847.83 | $0.00 | $1,628.95 | $-4,867.83 |
| marathonbet (Spain) | $580.00 | $-10,325.04 | $0.00 | $8,525.07 | $-10,325.04 |
| matchbook | $580.00 | $1,731.02 | $6,633.98 | $6,633.98 | $-3,925.78 |
| mybookieag | $580.00 | $-4,546.41 | $0.00 | $4,422.60 | $-7,124.16 |
| onexbet | $580.00 | $-78,045.12 | $9,989.03 | $69,050.38 | $-86,877.66 |
| pinnacle | $580.00 | $-5,154.48 | $2,784.49 | $3,723.57 | $-6,879.02 |
| skybet | $580.00 | $-691.61 | $316.50 | $567.67 | $-691.61 |
| smarkets | $580.00 | $-2,387.16 | $6,221.83 | $6,221.83 | $-8,947.57 |
| tipico_de | $580.00 | $-3,229.05 | $0.00 | $5,851.05 | $-3,229.05 |
| unibet_nl | $580.00 | $-9,257.49 | $1,455.81 | $4,157.51 | $-9,257.49 |
| unibet_se | $580.00 | $-5,323.01 | $1,119.05 | $24,382.67 | $-28,095.54 |
| williamhill (Spain) | $580.00 | $-751.77 | $0.00 | $1,331.77 | $-751.77 |
| winamax_de (Spain) | $580.00 | $1,144.17 | $0.00 | $805.80 | $-872.91 |

Peak money in use across all accounts at the same time: $155,979.62 ≈ €134,465.19.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 169 Polymarket/Kalshi and 314 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 168 | 135 | 102 | 1 | 0 |
| +1 min | 167 | 126 | 94 | 1 | 1 |
| +2 min | 164 | 109 | 76 | 2 | 3 |
| +5 min | 156 | 79 | 58 | 4 | 9 |
| bookmaker confirmation (~1 min) | 566 | 334 | 329 | 12 | 0 |
| next bookmaker snapshot | 460 | 143 | 137 | 14 | 0 |

Depth at detection (capacity = largest size still profitable after walking the order books):

- Polymarket/Kalshi gaps (169): median capacity $0 (maximum $2,826); still profitable with a $50 stake: 31 of 167; median largest guaranteed profit $0.00.
- Gaps with bookmakers (314): median capacity $20,000 (maximum $20,000); still profitable with a $50 stake: 301 of 314; median largest guaranteed profit $184.01. Bookmakers publish no order-book depth, so only the Polymarket/Kalshi legs limit these sizes and the capacity stops at the search limit of $20,000; the bot's bets with bookmakers are capped at $2,500.

Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 237 | 11-21T12:34 | SV 07 Elversberg v SC Freiburg | 115.5 | matchbook, onexbet, smarkets | 0.26% | $2499.98 | $6.50 | open |  |
| 236 | 11-21T12:32 | Deportivo Alavés v RC Deportivo A Coruña | 27.6 | matchbook, smarkets, unibet_nl | 1.56% | $2499.99 | $39.02 | open |  |
| 235 | 11-21T12:27 | Millwall FC v Queens Park Rangers FC | 2.5 | betonlineag, onexbet, smarkets | 0.26% | $2499.98 | $6.59 | open |  |
| 234 | 11-21T12:27 | Manchester City FC v Fulham FC | 2.5 | coral, gtbets, smarkets | 1.13% | $2499.99 | $28.28 | open |  |
| 233 | 11-21T12:04 | West Ham United FC v Preston North End FC | 175.9 | betrivers, betus | 0.34% | $2499.99 | $8.57 | open |  |
| 232 | 11-21T12:04 | Lincoln City FC v Wrexham AFC | 175.9 | leovegas_se, pinnacle | 0.68% | $2499.99 | $16.93 | open |  |
| 231 | 11-21T12:02 | Coventry City FC v Crystal Palace FC | 177.2 | onexbet, smarkets, unibet_se | 0.57% | $2499.98 | $14.23 | open |  |
| 230 | 11-21T12:02 | Deportivo Alavés v RC Deportivo A Coruña | 57.7 | matchbook, onexbet, unibet_nl | 2.07% | $2499.98 | $51.82 | open |  |
| 229 | 11-21T12:02 | Manchester City FC v Fulham FC | 28.0 | matchbook, onexbet, smarkets | 0.98% | $2499.98 | $24.41 | open |  |
| 228 | 11-21T11:32 | Bayer 04 Leverkusen v SC Paderborn 07 | 177.4 | betonlineag, ladbrokes_uk, unibet_se | 0.83% | $2499.99 | $20.81 | open |  |
| 227 | 11-21T11:31 | Norwich City FC v Cardiff City FC | 58.3 | coral, pinnacle, smarkets | 3.27% | $2499.99 | $81.82 | open |  |
| 226 | 11-21T11:31 | Southampton FC v Derby County FC | 58.3 | matchbook, pinnacle, skybet | 1.28% | $2499.98 | $32.02 | open |  |
| 225 | 11-21T11:31 | Manchester City FC v Fulham FC | 58.3 | coolbet, matchbook | 1.21% | $2499.99 | $30.34 | open |  |
| 224 | 11-21T11:02 | Deportivo Alavés v RC Deportivo A Coruña | 117.6 | matchbook, onexbet | 2.09% | $2499.99 | $52.25 | open |  |
| 223 | 11-21T10:31 | Manchester City FC v Fulham FC | 118.0 | onexbet, smarkets | 0.48% | $2499.99 | $11.96 | open |  |
| 222 | 11-21T09:31 | Manchester City FC v Fulham FC | 178.3 | matchbook, onexbet, smarkets | 0.21% | $2499.98 | $5.19 | open |  |
| 221 | 11-21T03:03 | Club Tijuana v Atlante FC | 6.4 | no | 0.29% | $160.59 | $0.41 | settled | $+0.46 |
| 220 | 11-21T03:02 | Club Tijuana v Atlante FC | 7.4 | no | 0.29% | $764.79 | $2.21 | settled | $+2.21 |
| 219 | 11-21T00:26 | TOR at DET | 3.2 | betrivers | 0.95% | $2499.99 | $23.83 | settled | $+23.83 |
| 218 | 11-20T19:46 | Athletic Club v RCD Espanyol de Barcelona | 13.1 | onexbet, smarkets, winamax_de | 0.47% | $2499.99 | $11.86 | settled | $+11.87 |
| 217 | 11-20T19:41 | ES Troyes AC v Le Havre AC | 3.1 | marathonbet, pinnacle, unibet_se | 0.97% | $2499.98 | $24.20 | settled | $+24.22 |
| 216 | 11-20T19:31 | ES Troyes AC v Le Havre AC | 13.1 | onexbet, pinnacle, unibet_se | 1.59% | $2499.99 | $39.73 | settled | $+39.73 |
| 215 | 11-20T19:26 | FC Bayern München v 1. FC Köln | 3.1 | betfair_ex_uk, ladbrokes_uk, smarkets | 1.45% | $2499.98 | $35.89 | settled | $+36.04 |
| 214 | 11-20T19:16 | ES Troyes AC v Le Havre AC | 28.1 | onexbet, smarkets, unibet_se | 1.83% | $2499.99 | $45.72 | settled | $+45.72 |
| 213 | 11-20T19:16 | FC Bayern München v 1. FC Köln | 13.1 | onexbet | 1.15% | $2499.92 | $28.08 | settled | $+28.08 |
