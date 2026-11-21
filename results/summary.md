# Paper-trading bot: status at 2026-11-21T16:21:52Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 280 / 233 |
| Realised profit | $-90,971.81 ≈ €-78,423.97 |
| … Polymarket/Kalshi only | $48.43 |
| … with bookmakers (all) | $-91,020.24 |
| … with bookmakers licensed in Spain only | $-2,285.19 |
| Open positions (cost) | $117,499.32 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $-60,231.80 ≈ €-51,923.97 |
| Return so far (realised / peak money in use) | -58.323% over 14.7 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 971, executed 36, rounding 90, seen 1192, vanished 72.
Gaps using bookmakers: below_min_size 4, executed 244, no_cash 41, rounding 3, seen 335, vanished 34 (snapshots combined with Polymarket/Kalshi: 1951).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 1,953 (about 3.3 days at the current pace). **Add keys soon: below 3 days only the last 3 snapshots per kick-off are taken.**

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
| betonlineag | $580.00 | $-7,544.31 | $3,494.14 | $4,590.49 | $-7,544.31 |
| betrivers | $580.00 | $4,150.87 | $4,227.93 | $4,227.93 | $-1,141.39 |
| betsson | $580.00 | $2,119.70 | $0.00 | $986.99 | $-406.99 |
| betus | $580.00 | $-3,289.28 | $3,869.28 | $3,869.28 | $-3,289.28 |
| bovada | $580.00 | $-244.12 | $0.00 | $824.12 | $-244.12 |
| boylesports | $580.00 | $1,315.03 | $0.00 | $1,813.51 | $-1,233.51 |
| codere_it | $580.00 | $1,797.50 | $0.00 | $1,295.21 | $-715.21 |
| coolbet | $580.00 | $-1,544.77 | $9,763.13 | $11,130.88 | $-8,022.38 |
| coral | $580.00 | $-1,231.51 | $4,120.88 | $4,120.88 | $-1,699.09 |
| draftkings | $580.00 | $-2,698.54 | $0.00 | $3,278.54 | $-2,698.54 |
| fanduel | $580.00 | $416.03 | $0.00 | $1,659.29 | $-2,247.51 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $-306.09 | $3,535.54 | $6,720.04 | $-7,633.02 |
| ladbrokes_uk | $580.00 | $-7,734.96 | $3,786.05 | $4,528.91 | $-7,734.96 |
| leovegas_se | $580.00 | $-24,122.69 | $11,461.86 | $47,555.97 | $-55,331.30 |
| lowvig | $580.00 | $-5,332.48 | $484.65 | $1,628.95 | $-5,332.48 |
| marathonbet (Spain) | $580.00 | $-11,633.18 | $1,308.14 | $8,525.07 | $-11,633.18 |
| matchbook | $580.00 | $3,486.32 | $6,494.99 | $12,468.15 | $-4,103.15 |
| mybookieag | $580.00 | $-4,546.41 | $0.00 | $4,422.60 | $-7,124.16 |
| onexbet | $580.00 | $-98,615.40 | $26,937.49 | $69,050.38 | $-102,003.41 |
| pinnacle | $580.00 | $-10,287.30 | $7,882.44 | $10,216.96 | $-12,586.95 |
| skybet | $580.00 | $-1,150.75 | $459.14 | $775.64 | $-1,150.75 |
| smarkets | $580.00 | $-2,423.94 | $11,173.16 | $15,891.75 | $-12,057.08 |
| tipico_de | $580.00 | $-3,229.05 | $0.00 | $5,851.05 | $-3,229.05 |
| unibet_nl | $580.00 | $-11,135.76 | $1,175.68 | $4,157.51 | $-11,135.76 |
| unibet_se | $580.00 | $-14,615.37 | $10,411.41 | $24,382.67 | $-28,095.54 |
| williamhill (Spain) | $580.00 | $-1,697.00 | $945.23 | $1,331.77 | $-1,697.00 |
| winamax_de (Spain) | $580.00 | $1,144.17 | $0.00 | $805.80 | $-872.91 |

Peak money in use across all accounts at the same time: $155,979.62 ≈ €134,465.19.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 180 Polymarket/Kalshi and 372 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 179 | 146 | 107 | 1 | 0 |
| +1 min | 178 | 137 | 99 | 1 | 1 |
| +2 min | 175 | 120 | 81 | 2 | 3 |
| +5 min | 166 | 87 | 62 | 4 | 10 |
| bookmaker confirmation (~1 min) | 654 | 372 | 366 | 14 | 0 |
| next bookmaker snapshot | 534 | 150 | 142 | 17 | 0 |

Depth at detection (capacity = largest size still profitable after walking the order books):

- Polymarket/Kalshi gaps (180): median capacity $0 (maximum $2,826); still profitable with a $50 stake: 31 of 178; median largest guaranteed profit $0.00.
- Gaps with bookmakers (372): median capacity $20,000 (maximum $20,000); still profitable with a $50 stake: 359 of 372; median largest guaranteed profit $162.33. Bookmakers publish no order-book depth, so only the Polymarket/Kalshi legs limit these sizes and the capacity stops at the search limit of $20,000; the bot's bets with bookmakers are capped at $2,500.

Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 280 | 11-21T15:47 | Feyenoord Rotterdam v SBV Excelsior | 117.9 | coral, pinnacle, unibet_nl | 0.56% | $2499.98 | $13.94 | open |  |
| 279 | 11-21T15:17 | OGC Nice v Paris Saint-Germain FC | 58.0 | onexbet, smarkets, unibet_se | 0.22% | $2499.99 | $5.52 | open |  |
| 278 | 11-21T15:01 | Rayo Vallecano de Madrid v Valencia CF | 13.0 | betus, onexbet, unibet_se | 0.34% | $2499.99 | $8.42 | open |  |
| 277 | 11-21T14:57 | West Ham United FC v Preston North End FC | 2.4 | betonlineag, coolbet, smarkets | 0.85% | $2499.99 | $21.22 | open |  |
| 276 | 11-21T14:57 | Bolton Wanderers FC v Portsmouth FC | 2.4 | leovegas_se, matchbook, pinnacle | 0.24% | $2499.98 | $6.08 | open |  |
| 275 | 11-21T14:57 | Wolverhampton Wanderers FC v Charlton Athletic FC | 2.4 | leovegas_se, matchbook | 1.00% | $2499.99 | $25.06 | open |  |
| 274 | 11-21T14:57 | Tottenham Hotspur FC v Ipswich Town FC | 2.5 | gtbets, matchbook, smarkets | 0.56% | $2499.99 | $13.98 | open |  |
| 273 | 11-21T14:57 | Aston Villa FC v Sunderland AFC | 2.5 | lowvig, marathonbet, pinnacle | 0.42% | $2499.99 | $10.50 | open |  |
| 272 | 11-21T14:47 | Feyenoord Rotterdam v SBV Excelsior | 177.2 | coral, pinnacle, unibet_nl | 0.54% | $2499.98 | $13.30 | open |  |
| 271 | 11-21T14:47 | Wolverhampton Wanderers FC v Charlton Athletic FC | 12.8 | betonlineag, leovegas_se, smarkets | 0.26% | $2499.98 | $6.52 | open |  |
| 270 | 11-21T14:47 | Rayo Vallecano de Madrid v Valencia CF | 27.9 | onexbet, unibet_se | 1.08% | $2499.99 | $27.02 | open |  |
| 269 | 11-21T14:47 | AFC Bournemouth v Nottingham Forest FC | 12.9 | coolbet, marathonbet, matchbook | 0.70% | $2499.99 | $17.45 | open |  |
| 268 | 11-21T14:47 | Aston Villa FC v Sunderland AFC | 12.9 | onexbet, smarkets | 0.98% | $2499.99 | $24.52 | open |  |
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
