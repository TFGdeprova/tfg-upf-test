# Paper-trading bot: status at 2026-11-21T14:01:18Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 250 / 221 |
| Realised profit | $-91,365.08 ≈ €-78,763.00 |
| … Polymarket/Kalshi only | $48.43 |
| … with bookmakers (all) | $-91,413.51 |
| … with bookmakers licensed in Spain only | $-2,285.19 |
| Open positions (cost) | $72,499.60 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $-60,625.08 ≈ €-52,263.00 |
| Return so far (realised / peak money in use) | -58.575% over 14.6 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 934, executed 36, rounding 90, seen 1152, vanished 69.
Gaps using bookmakers: below_min_size 4, executed 214, no_cash 41, rounding 3, seen 309, vanished 30 (snapshots combined with Polymarket/Kalshi: 1832).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 2,259 (about 4.6 days at the current pace).

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $14,960.75 | $0.00 | $4,486.78 | $2,369.73 |
| Kalshi | $5,800.00 | $7,254.92 | $0.00 | $2,216.01 | $2,967.42 |
| betanysports | $580.00 | $-1,985.24 | $1,090.65 | $4,190.72 | $-3,610.72 |
| betfair_ex_eu (Spain) | $580.00 | $66.22 | $386.85 | $386.85 | $66.22 |
| betfair_ex_uk (Spain) | $580.00 | $505.96 | $0.00 | $74.04 | $505.96 |
| betfred_uk | $580.00 | $-768.02 | $0.00 | $1,348.02 | $-768.02 |
| betmgm | $580.00 | $3,604.00 | $1,494.25 | $5,577.36 | $-4,997.36 |
| betonlineag | $580.00 | $-5,181.44 | $2,070.06 | $4,590.49 | $-5,181.44 |
| betrivers | $580.00 | $5,560.18 | $2,818.62 | $2,818.62 | $-1,141.39 |
| betsson | $580.00 | $2,119.70 | $0.00 | $986.99 | $-406.99 |
| betus | $580.00 | $-1,601.36 | $2,181.36 | $2,181.36 | $-1,601.36 |
| bovada | $580.00 | $-244.12 | $0.00 | $824.12 | $-244.12 |
| boylesports | $580.00 | $1,315.03 | $0.00 | $1,813.51 | $-1,233.51 |
| codere_it | $580.00 | $1,797.50 | $0.00 | $1,295.21 | $-715.21 |
| coolbet | $580.00 | $1,185.95 | $5,869.82 | $7,199.91 | $-8,022.38 |
| coral | $580.00 | $361.09 | $977.58 | $1,948.91 | $-1,194.91 |
| draftkings | $580.00 | $-2,698.54 | $0.00 | $3,278.54 | $-2,698.54 |
| fanduel | $580.00 | $416.03 | $0.00 | $1,659.29 | $-2,247.51 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $3,229.45 | $1,780.49 | $6,720.04 | $-7,633.02 |
| ladbrokes_uk | $580.00 | $-5,844.26 | $1,895.35 | $4,528.91 | $-5,844.26 |
| leovegas_se | $580.00 | $-15,991.94 | $3,331.11 | $47,555.97 | $-55,331.30 |
| lowvig | $580.00 | $-4,847.83 | $0.00 | $1,628.95 | $-4,867.83 |
| marathonbet (Spain) | $580.00 | $-10,325.04 | $0.00 | $8,525.07 | $-10,325.04 |
| matchbook | $580.00 | $1,285.12 | $7,079.88 | $7,079.88 | $-3,925.78 |
| mybookieag | $580.00 | $-4,546.41 | $0.00 | $4,422.60 | $-7,124.16 |
| onexbet | $580.00 | $-87,160.81 | $19,104.72 | $69,050.38 | $-87,160.81 |
| pinnacle | $580.00 | $-6,767.62 | $4,397.63 | $4,397.63 | $-6,879.02 |
| skybet | $580.00 | $-1,150.75 | $775.64 | $775.64 | $-1,150.75 |
| smarkets | $580.00 | $-6,253.43 | $10,088.10 | $10,088.10 | $-8,947.57 |
| tipico_de | $580.00 | $-3,229.05 | $0.00 | $5,851.05 | $-3,229.05 |
| unibet_nl | $580.00 | $-9,960.08 | $2,158.40 | $4,157.51 | $-9,960.08 |
| unibet_se | $580.00 | $-8,257.82 | $4,053.86 | $24,382.67 | $-28,095.54 |
| williamhill (Spain) | $580.00 | $-1,697.00 | $945.23 | $1,331.77 | $-1,697.00 |
| winamax_de (Spain) | $580.00 | $1,144.17 | $0.00 | $805.80 | $-872.91 |

Peak money in use across all accounts at the same time: $155,979.62 ≈ €134,465.19.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 175 Polymarket/Kalshi and 338 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 174 | 141 | 105 | 1 | 0 |
| +1 min | 173 | 132 | 97 | 1 | 1 |
| +2 min | 170 | 115 | 79 | 2 | 3 |
| +5 min | 162 | 85 | 61 | 4 | 9 |
| bookmaker confirmation (~1 min) | 590 | 346 | 341 | 12 | 0 |
| next bookmaker snapshot | 478 | 145 | 139 | 14 | 0 |

Depth at detection (capacity = largest size still profitable after walking the order books):

- Polymarket/Kalshi gaps (175): median capacity $0 (maximum $2,826); still profitable with a $50 stake: 31 of 173; median largest guaranteed profit $0.00.
- Gaps with bookmakers (338): median capacity $20,000 (maximum $20,000); still profitable with a $50 stake: 325 of 338; median largest guaranteed profit $178.82. Bookmakers publish no order-book depth, so only the Polymarket/Kalshi legs limit these sizes and the capacity stops at the search limit of $20,000; the bot's bets with bookmakers are capped at $2,500.

Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 250 | 11-21T13:58 | SS Lazio v US Lecce | 1.9 | coolbet, onexbet, unibet_se | 0.75% | $2499.98 | $18.60 | open |  |
| 249 | 11-21T13:58 | Como 1907 v Cagliari Calcio | 1.9 | betfair_ex_eu, coolbet, smarkets | 0.74% | $2499.99 | $18.40 | open |  |
| 248 | 11-21T13:47 | SS Lazio v US Lecce | 12.2 | betonlineag, onexbet, unibet_se | 0.96% | $2499.98 | $23.98 | open |  |
| 247 | 11-21T13:47 | Como 1907 v Cagliari Calcio | 12.2 | matchbook, onexbet, smarkets | 1.11% | $2499.99 | $27.84 | open |  |
| 246 | 11-21T13:33 | Eintracht Frankfurt v TSG 1899 Hoffenheim | 56.3 | coolbet, onexbet, smarkets | 0.71% | $2499.98 | $17.76 | open |  |
| 245 | 11-21T13:33 | Borussia Mönchengladbach v BV Borussia 09 Dortmund | 56.3 | betmgm, onexbet, skybet | 1.01% | $2499.99 | $25.28 | open |  |
| 244 | 11-21T13:33 | SS Lazio v US Lecce | 26.7 | onexbet, smarkets, unibet_se | 0.91% | $2499.99 | $22.63 | open |  |
| 243 | 11-21T13:33 | Como 1907 v Cagliari Calcio | 26.7 | betonlineag, matchbook, onexbet | 0.26% | $2499.99 | $6.38 | open |  |
| 242 | 11-21T13:03 | West Ham United FC v Preston North End FC | 116.9 | betrivers, betus | 0.34% | $2499.99 | $8.57 | open |  |
| 241 | 11-21T13:03 | Lincoln City FC v Wrexham AFC | 116.9 | leovegas_se, smarkets | 0.56% | $2499.99 | $13.87 | open |  |
| 240 | 11-21T13:03 | Coventry City FC v Crystal Palace FC | 117.0 | onexbet, pinnacle, unibet_se | 1.20% | $2499.99 | $29.91 | open |  |
| 239 | 11-21T13:02 | Como 1907 v Cagliari Calcio | 57.2 | betanysports, unibet_se, williamhill | 0.34% | $2499.98 | $8.50 | open |  |
| 238 | 11-21T12:48 | Deportivo Alavés v RC Deportivo A Coruña | 11.5 | pinnacle, smarkets, unibet_nl | 1.17% | $2499.99 | $29.33 | open |  |
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
