# Paper-trading bot: status at 2026-11-21T17:25:29Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 293 / 248 |
| Realised profit | $-90,699.62 ≈ €-78,189.32 |
| … Polymarket/Kalshi only | $48.43 |
| … with bookmakers (all) | $-90,748.05 |
| … with bookmakers licensed in Spain only | $-2,285.19 |
| Open positions (cost) | $112,499.37 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $-59,379.61 ≈ €-51,189.32 |
| Return so far (realised / peak money in use) | -58.148% over 14.8 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 971, executed 36, rounding 90, seen 1192, vanished 72.
Gaps using bookmakers: below_min_size 4, executed 257, no_cash 41, rounding 3, seen 351, vanished 35 (snapshots combined with Polymarket/Kalshi: 1994).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 1,733 (about 2.6 days at the current pace). **Add keys soon: below 3 days only the last 3 snapshots per kick-off are taken.**

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $13,743.54 | $1,217.21 | $4,486.78 | $2,369.73 |
| Kalshi | $5,800.00 | $7,254.92 | $0.00 | $2,216.01 | $2,967.42 |
| betanysports | $580.00 | $-585.80 | $1,109.06 | $4,190.72 | $-3,610.72 |
| betfair_ex_eu (Spain) | $580.00 | $66.22 | $0.00 | $386.85 | $66.22 |
| betfair_ex_uk (Spain) | $580.00 | $505.96 | $0.00 | $74.04 | $505.96 |
| betfred_uk | $580.00 | $-768.02 | $0.00 | $1,348.02 | $-768.02 |
| betmgm | $580.00 | $4,769.21 | $1,982.91 | $5,577.36 | $-4,997.36 |
| betonlineag | $580.00 | $-9,325.95 | $3,405.57 | $4,590.49 | $-9,325.95 |
| betrivers | $580.00 | $4,150.87 | $4,227.93 | $4,227.93 | $-1,141.39 |
| betsson | $580.00 | $2,119.70 | $0.00 | $986.99 | $-406.99 |
| betus | $580.00 | $-3,289.28 | $3,869.28 | $3,869.28 | $-3,289.28 |
| bovada | $580.00 | $-244.12 | $0.00 | $824.12 | $-244.12 |
| boylesports | $580.00 | $1,315.03 | $0.00 | $1,813.51 | $-1,233.51 |
| codere_it | $580.00 | $1,797.50 | $0.00 | $1,295.21 | $-715.21 |
| coolbet | $580.00 | $6,010.03 | $5,261.06 | $11,130.88 | $-8,022.38 |
| coral | $580.00 | $-3,247.13 | $6,136.50 | $6,136.50 | $-3,247.13 |
| draftkings | $580.00 | $-2,698.54 | $0.00 | $3,278.54 | $-2,698.54 |
| fanduel | $580.00 | $416.03 | $0.00 | $1,659.29 | $-2,247.51 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $-3,524.42 | $6,753.87 | $6,753.87 | $-7,633.02 |
| ladbrokes_uk | $580.00 | $-2,699.51 | $0.00 | $4,528.91 | $-7,734.96 |
| leovegas_se | $580.00 | $-24,122.69 | $11,461.86 | $47,555.97 | $-55,331.30 |
| lowvig | $580.00 | $-5,332.48 | $484.65 | $1,628.95 | $-5,332.48 |
| marathonbet (Spain) | $580.00 | $-11,633.18 | $1,308.14 | $8,525.07 | $-11,633.18 |
| matchbook | $580.00 | $-1,796.82 | $10,427.94 | $12,468.15 | $-4,103.15 |
| mybookieag | $580.00 | $-4,546.41 | $0.00 | $4,422.60 | $-7,124.16 |
| onexbet | $580.00 | $-95,020.58 | $22,937.71 | $69,050.38 | $-102,003.41 |
| pinnacle | $580.00 | $-11,118.18 | $8,713.32 | $10,216.96 | $-12,586.95 |
| skybet | $580.00 | $-1,150.75 | $0.00 | $775.64 | $-1,150.75 |
| smarkets | $580.00 | $-3,122.87 | $12,344.13 | $15,944.68 | $-12,057.08 |
| tipico_de | $580.00 | $-3,229.05 | $0.00 | $5,851.05 | $-3,229.05 |
| unibet_nl | $580.00 | $-13,566.61 | $3,606.53 | $4,157.51 | $-13,566.61 |
| unibet_se | $580.00 | $-12,272.50 | $5,911.43 | $24,382.67 | $-28,095.54 |
| unibet_uk | $580.00 | $-760.27 | $1,340.27 | $1,340.27 | $-760.27 |
| williamhill (Spain) | $580.00 | $-1,697.00 | $0.00 | $1,331.77 | $-1,697.00 |
| winamax_de (Spain) | $580.00 | $1,144.17 | $0.00 | $805.80 | $-872.91 |

Peak money in use across all accounts at the same time: $155,979.62 ≈ €134,465.19.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 180 Polymarket/Kalshi and 389 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 179 | 146 | 107 | 1 | 0 |
| +1 min | 178 | 137 | 99 | 1 | 1 |
| +2 min | 175 | 120 | 81 | 2 | 3 |
| +5 min | 166 | 87 | 62 | 4 | 10 |
| bookmaker confirmation (~1 min) | 674 | 384 | 378 | 14 | 0 |
| next bookmaker snapshot | 546 | 152 | 144 | 17 | 0 |

Depth at detection (capacity = largest size still profitable after walking the order books):

- Polymarket/Kalshi gaps (180): median capacity $0 (maximum $2,826); still profitable with a $50 stake: 31 of 178; median largest guaranteed profit $0.00.
- Gaps with bookmakers (389): median capacity $20,000 (maximum $20,000); still profitable with a $50 stake: 376 of 389; median largest guaranteed profit $161.60. Bookmakers publish no order-book depth, so only the Polymarket/Kalshi legs limit these sizes and the capacity stops at the search limit of $20,000; the bot's bets with bookmakers are capped at $2,500.

Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 293 | 11-21T17:17 | Feyenoord Rotterdam v SBV Excelsior | 27.8 | matchbook, onexbet | 2.85% | $2499.99 | $71.33 | open |  |
| 292 | 11-21T17:17 | FC Schalke 04 v VfB Stuttgart | 12.8 | matchbook, onexbet, unibet_uk | 0.76% | $2499.99 | $19.03 | open |  |
| 291 | 11-21T17:17 | Sevilla FC v Real Betis Balompié | 12.8 | matchbook, onexbet | 0.26% | $2499.98 | $6.40 | open |  |
| 290 | 11-21T17:17 | Newcastle United FC v Arsenal FC | 12.8 | betonlineag, gtbets | 2.02% | $2499.98 | $50.35 | open |  |
| 289 | 11-21T17:02 | FC Groningen v SC Heerenveen | 177.7 | matchbook, smarkets, unibet_nl | 0.30% | $2499.99 | $7.37 | open |  |
| 288 | 11-21T17:02 | FC Schalke 04 v VfB Stuttgart | 27.7 | onexbet, smarkets, unibet_uk | 0.28% | $2499.99 | $7.00 | open |  |
| 287 | 11-21T17:02 | Real Madrid CF v RC Celta de Vigo | 177.7 | onexbet, smarkets | 1.93% | $2499.98 | $48.22 | open |  |
| 286 | 11-21T16:57 | Parma Calcio 1913 v AS Roma | 2.8 | coral, smarkets | 0.78% | $2499.98 | $19.48 | open |  |
| 285 | 11-21T16:47 | FC Utrecht v SC Cambuur-Leeuwarden | 57.8 | smarkets, unibet_nl | 0.92% | $2499.98 | $22.94 | open |  |
| 284 | 11-21T16:47 | Feyenoord Rotterdam v SBV Excelsior | 57.8 | onexbet, smarkets, unibet_nl | 0.24% | $2499.99 | $5.93 | open |  |
| 283 | 11-21T16:31 | Sevilla FC v Real Betis Balompié | 58.3 | matchbook, pinnacle, unibet_nl | 1.04% | $2499.99 | $25.86 | open |  |
| 282 | 11-21T16:31 | Newcastle United FC v Arsenal FC | 58.3 | betonlineag, gtbets | 1.38% | $2499.99 | $34.56 | open |  |
| 281 | 11-21T16:31 | Parma Calcio 1913 v AS Roma | 28.3 | betmgm, smarkets, unibet_se | 0.73% | $2499.99 | $18.19 | open |  |
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
