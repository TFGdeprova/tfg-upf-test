# Paper-trading bot: status at 2026-11-21T14:42:04Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 267 / 221 |
| Realised profit | $-91,365.08 ≈ €-78,763.00 |
| … Polymarket/Kalshi only | $48.43 |
| … with bookmakers (all) | $-91,413.51 |
| … with bookmakers licensed in Spain only | $-2,285.19 |
| Open positions (cost) | $114,999.32 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $-60,625.08 ≈ €-52,263.00 |
| Return so far (realised / peak money in use) | -58.575% over 14.7 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 970, executed 36, rounding 90, seen 1191, vanished 72.
Gaps using bookmakers: below_min_size 4, executed 231, no_cash 41, rounding 3, seen 319, vanished 31 (snapshots combined with Polymarket/Kalshi: 1882).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 2,157 (about 4.1 days at the current pace).

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $14,960.75 | $0.00 | $4,486.78 | $2,369.73 |
| Kalshi | $5,800.00 | $7,254.92 | $0.00 | $2,216.01 | $2,967.42 |
| betanysports | $580.00 | $-3,094.30 | $2,199.71 | $4,190.72 | $-3,610.72 |
| betfair_ex_eu (Spain) | $580.00 | $66.22 | $386.85 | $386.85 | $66.22 |
| betfair_ex_uk (Spain) | $580.00 | $505.96 | $0.00 | $74.04 | $505.96 |
| betfred_uk | $580.00 | $-768.02 | $0.00 | $1,348.02 | $-768.02 |
| betmgm | $580.00 | $1,716.63 | $3,381.62 | $5,577.36 | $-4,997.36 |
| betonlineag | $580.00 | $-6,806.53 | $3,695.15 | $4,590.49 | $-6,806.53 |
| betrivers | $580.00 | $4,150.87 | $4,227.93 | $4,227.93 | $-1,141.39 |
| betsson | $580.00 | $2,119.70 | $0.00 | $986.99 | $-406.99 |
| betus | $580.00 | $-2,692.04 | $3,272.04 | $3,272.04 | $-2,692.04 |
| bovada | $580.00 | $-244.12 | $0.00 | $824.12 | $-244.12 |
| boylesports | $580.00 | $1,315.03 | $0.00 | $1,813.51 | $-1,233.51 |
| codere_it | $580.00 | $1,797.50 | $0.00 | $1,295.21 | $-715.21 |
| coolbet | $580.00 | $-1,506.34 | $8,562.11 | $8,562.11 | $-8,022.38 |
| coral | $580.00 | $361.09 | $977.58 | $1,948.91 | $-1,194.91 |
| draftkings | $580.00 | $-2,698.54 | $0.00 | $3,278.54 | $-2,698.54 |
| fanduel | $580.00 | $416.03 | $0.00 | $1,659.29 | $-2,247.51 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $1,305.43 | $3,704.51 | $6,720.04 | $-7,633.02 |
| ladbrokes_uk | $580.00 | $-7,734.96 | $3,786.05 | $4,528.91 | $-7,734.96 |
| leovegas_se | $580.00 | $-19,372.84 | $6,712.01 | $47,555.97 | $-55,331.30 |
| lowvig | $580.00 | $-4,847.83 | $0.00 | $1,628.95 | $-4,867.83 |
| marathonbet (Spain) | $580.00 | $-10,325.04 | $0.00 | $8,525.07 | $-10,325.04 |
| matchbook | $580.00 | $-970.46 | $9,335.46 | $9,335.46 | $-3,925.78 |
| mybookieag | $580.00 | $-4,546.41 | $0.00 | $4,422.60 | $-7,124.16 |
| onexbet | $580.00 | $-98,024.66 | $29,968.57 | $69,050.38 | $-98,024.66 |
| pinnacle | $580.00 | $-10,179.85 | $7,809.86 | $7,809.86 | $-10,179.85 |
| skybet | $580.00 | $-1,150.75 | $775.64 | $775.64 | $-1,150.75 |
| smarkets | $580.00 | $-10,771.86 | $14,606.53 | $14,606.53 | $-10,771.86 |
| tipico_de | $580.00 | $-3,229.05 | $0.00 | $5,851.05 | $-3,229.05 |
| unibet_nl | $580.00 | $-10,821.56 | $3,019.88 | $4,157.51 | $-10,821.56 |
| unibet_se | $580.00 | $-11,836.55 | $7,632.59 | $24,382.67 | $-28,095.54 |
| williamhill (Spain) | $580.00 | $-1,697.00 | $945.23 | $1,331.77 | $-1,697.00 |
| winamax_de (Spain) | $580.00 | $1,144.17 | $0.00 | $805.80 | $-872.91 |

Peak money in use across all accounts at the same time: $155,979.62 ≈ €134,465.19.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 178 Polymarket/Kalshi and 352 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 177 | 144 | 107 | 1 | 0 |
| +1 min | 176 | 135 | 99 | 1 | 1 |
| +2 min | 172 | 117 | 80 | 2 | 3 |
| +5 min | 163 | 86 | 62 | 4 | 10 |
| bookmaker confirmation (~1 min) | 615 | 361 | 356 | 13 | 0 |
| next bookmaker snapshot | 491 | 146 | 139 | 15 | 0 |

Depth at detection (capacity = largest size still profitable after walking the order books):

- Polymarket/Kalshi gaps (178): median capacity $0 (maximum $2,826); still profitable with a $50 stake: 31 of 176; median largest guaranteed profit $0.00.
- Gaps with bookmakers (352): median capacity $20,000 (maximum $20,000); still profitable with a $50 stake: 339 of 352; median largest guaranteed profit $170.80. Bookmakers publish no order-book depth, so only the Polymarket/Kalshi legs limit these sizes and the capacity stops at the search limit of $20,000; the bot's bets with bookmakers are capped at $2,500.

Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 267 | 11-21T14:33 | Sevilla FC v Real Betis Balompié | 176.6 | coolbet, onexbet | 0.94% | $2499.99 | $23.44 | open |  |
| 266 | 11-21T14:33 | Newcastle United FC v Arsenal FC | 176.6 | onexbet, smarkets | 0.64% | $2499.98 | $15.94 | open |  |
| 265 | 11-21T14:33 | AFC Bournemouth v Nottingham Forest FC | 26.9 | onexbet, pinnacle, unibet_se | 0.59% | $2499.98 | $14.80 | open |  |
| 264 | 11-21T14:33 | Coventry City FC v Crystal Palace FC | 26.9 | betanysports, onexbet | 0.70% | $2499.99 | $17.58 | open |  |
| 263 | 11-21T14:33 | Aston Villa FC v Sunderland AFC | 26.9 | onexbet, smarkets | 0.58% | $2499.98 | $14.44 | open |  |
| 262 | 11-21T14:32 | Lincoln City FC v Wrexham AFC | 27.6 | betonlineag, leovegas_se, smarkets | 0.31% | $2499.98 | $7.82 | open |  |
| 261 | 11-21T14:32 | Wolverhampton Wanderers FC v Charlton Athletic FC | 27.7 | gtbets, matchbook, smarkets | 2.36% | $2499.98 | $58.86 | open |  |
| 260 | 11-21T14:27 | SV 07 Elversberg v SC Freiburg | 2.6 | onexbet, unibet_se | 0.91% | $2499.99 | $22.75 | open |  |
| 259 | 11-21T14:27 | Bayer 04 Leverkusen v SC Paderborn 07 | 2.6 | betmgm, betonlineag, matchbook | 0.41% | $2499.98 | $10.17 | open |  |
| 258 | 11-21T14:16 | Borussia Mönchengladbach v BV Borussia 09 Dortmund | 13.3 | smarkets, unibet_se | 1.11% | $2499.98 | $27.62 | open |  |
| 257 | 11-21T14:03 | West Ham United FC v Preston North End FC | 56.9 | betrivers, betus | 0.34% | $2499.99 | $8.57 | open |  |
| 256 | 11-21T14:03 | Lincoln City FC v Wrexham AFC | 56.9 | leovegas_se, pinnacle, smarkets | 1.30% | $2499.98 | $32.37 | open |  |
| 255 | 11-21T14:03 | Wolverhampton Wanderers FC v Charlton Athletic FC | 56.9 | leovegas_se, matchbook, smarkets | 1.92% | $2499.98 | $47.89 | open |  |
| 254 | 11-21T14:02 | Bayer 04 Leverkusen v SC Paderborn 07 | 27.0 | betonlineag, ladbrokes_uk, unibet_se | 0.59% | $2499.98 | $14.56 | open |  |
| 253 | 11-21T14:02 | AFC Bournemouth v Nottingham Forest FC | 57.1 | matchbook, onexbet, unibet_se | 0.81% | $2499.99 | $20.14 | open |  |
| 252 | 11-21T14:02 | Coventry City FC v Crystal Palace FC | 57.2 | coolbet, onexbet, unibet_nl | 1.65% | $2499.99 | $41.36 | open |  |
| 251 | 11-21T14:02 | Aston Villa FC v Sunderland AFC | 57.2 | coolbet, onexbet, pinnacle | 0.79% | $2499.98 | $19.77 | open |  |
| 250 | 11-21T13:58 | SS Lazio v US Lecce | 1.9 | coolbet, onexbet, unibet_se | 0.75% | $2499.98 | $18.60 | open |  |
| 249 | 11-21T13:58 | Como 1907 v Cagliari Calcio | 1.9 | betfair_ex_eu, coolbet, smarkets | 0.74% | $2499.99 | $18.40 | open |  |
| 248 | 11-21T13:47 | SS Lazio v US Lecce | 12.2 | betonlineag, onexbet, unibet_se | 0.96% | $2499.98 | $23.98 | open |  |
| 247 | 11-21T13:47 | Como 1907 v Cagliari Calcio | 12.2 | matchbook, onexbet, smarkets | 1.11% | $2499.99 | $27.84 | open |  |
| 246 | 11-21T13:33 | Eintracht Frankfurt v TSG 1899 Hoffenheim | 56.3 | coolbet, onexbet, smarkets | 0.71% | $2499.98 | $17.76 | open |  |
| 245 | 11-21T13:33 | Borussia Mönchengladbach v BV Borussia 09 Dortmund | 56.3 | betmgm, onexbet, skybet | 1.01% | $2499.99 | $25.28 | open |  |
| 244 | 11-21T13:33 | SS Lazio v US Lecce | 26.7 | onexbet, smarkets, unibet_se | 0.91% | $2499.99 | $22.63 | open |  |
| 243 | 11-21T13:33 | Como 1907 v Cagliari Calcio | 26.7 | betonlineag, matchbook, onexbet | 0.26% | $2499.99 | $6.38 | open |  |
