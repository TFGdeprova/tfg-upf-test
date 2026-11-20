# Paper-trading bot: status at 2026-11-20T21:46:38Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 218 / 205 |
| Realised profit | $-91,679.08 ≈ €-79,033.69 |
| … Polymarket/Kalshi only | $29.61 |
| … with bookmakers (all) | $-91,708.69 |
| … with bookmakers licensed in Spain only | $-2,285.19 |
| Open positions (cost) | $28,034.86 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $-61,519.07 ≈ €-53,033.68 |
| Return so far (realised / peak money in use) | -58.776% over 14.0 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 751, executed 34, rounding 86, seen 942, vanished 65.
Gaps using bookmakers: below_min_size 4, executed 184, no_cash 41, rounding 3, seen 266, vanished 25 (snapshots combined with Polymarket/Kalshi: 1632).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 2,753 (about 8.2 days at the current pace).

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $14,858.50 | $1,354.16 | $4,486.78 | $2,369.73 |
| Kalshi | $5,800.00 | $2,967.42 | $2,216.01 | $2,216.01 | $2,967.42 |
| betanysports | $580.00 | $-894.59 | $0.00 | $4,190.72 | $-3,610.72 |
| betfair_ex_eu (Spain) | $580.00 | $453.07 | $0.00 | $126.93 | $453.07 |
| betfair_ex_uk (Spain) | $580.00 | $505.96 | $74.04 | $74.04 | $505.96 |
| betfred_uk | $580.00 | $-768.02 | $0.00 | $1,348.02 | $-768.02 |
| betmgm | $580.00 | $5,098.25 | $0.00 | $5,577.36 | $-4,997.36 |
| betonlineag | $580.00 | $-3,111.38 | $0.00 | $4,590.49 | $-4,391.48 |
| betrivers | $580.00 | $7,162.65 | $0.00 | $2,248.46 | $-1,141.39 |
| betsson | $580.00 | $2,119.70 | $0.00 | $986.99 | $-406.99 |
| bovada | $580.00 | $-244.12 | $0.00 | $824.12 | $-244.12 |
| boylesports | $580.00 | $1,315.03 | $0.00 | $1,813.51 | $-1,233.51 |
| codere_it | $580.00 | $1,797.50 | $0.00 | $1,295.21 | $-715.21 |
| coolbet | $580.00 | $7,055.77 | $0.00 | $7,199.91 | $-8,022.38 |
| coral | $580.00 | $1,338.67 | $0.00 | $1,948.91 | $-1,194.91 |
| draftkings | $580.00 | $-2,698.54 | $0.00 | $3,278.54 | $-2,698.54 |
| fanduel | $580.00 | $416.03 | $0.00 | $1,659.29 | $-2,247.51 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $5,009.94 | $0.00 | $6,720.04 | $-7,633.02 |
| ladbrokes_uk | $580.00 | $-3,948.91 | $4,528.91 | $4,528.91 | $-3,948.91 |
| leovegas_se | $580.00 | $-12,660.83 | $0.00 | $47,555.97 | $-55,331.30 |
| lowvig | $580.00 | $-4,847.83 | $0.00 | $1,628.95 | $-4,867.83 |
| marathonbet (Spain) | $580.00 | $-10,325.04 | $693.46 | $8,525.07 | $-10,325.04 |
| matchbook | $580.00 | $8,365.00 | $75.39 | $4,155.10 | $-3,925.78 |
| mybookieag | $580.00 | $-4,546.41 | $0.00 | $4,422.60 | $-7,124.16 |
| onexbet | $580.00 | $-68,056.09 | $10,332.76 | $69,050.38 | $-86,877.66 |
| pinnacle | $580.00 | $-4,879.47 | $2,627.60 | $3,723.57 | $-6,879.02 |
| skybet | $580.00 | $-375.11 | $0.00 | $567.67 | $-375.11 |
| smarkets | $580.00 | $-8,789.17 | $2,350.09 | $4,070.28 | $-8,947.57 |
| tipico_de | $580.00 | $-3,229.05 | $0.00 | $5,851.05 | $-3,229.05 |
| unibet_nl | $580.00 | $-7,801.68 | $0.00 | $4,157.51 | $-7,801.68 |
| unibet_se | $580.00 | $-11,813.59 | $3,280.07 | $24,382.67 | $-28,095.54 |
| williamhill (Spain) | $580.00 | $-751.77 | $0.00 | $1,331.77 | $-751.77 |
| winamax_de (Spain) | $580.00 | $1,144.17 | $502.37 | $805.80 | $-872.91 |

Peak money in use across all accounts at the same time: $155,979.62 ≈ €134,465.19.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 160 Polymarket/Kalshi and 291 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 159 | 126 | 96 | 1 | 0 |
| +1 min | 158 | 117 | 88 | 1 | 1 |
| +2 min | 155 | 100 | 70 | 2 | 3 |
| +5 min | 147 | 71 | 53 | 4 | 9 |
| bookmaker confirmation (~1 min) | 528 | 321 | 316 | 11 | 0 |
| next bookmaker snapshot | 433 | 143 | 137 | 13 | 0 |

Depth at detection (capacity = largest size still profitable after walking the order books):

- Polymarket/Kalshi gaps (160): median capacity $0 (maximum $2,826); still profitable with a $50 stake: 30 of 158; median largest guaranteed profit $0.00.
- Gaps with bookmakers (291): median capacity $20,000 (maximum $20,000); still profitable with a $50 stake: 279 of 291; median largest guaranteed profit $190.34. Bookmakers publish no order-book depth, so only the Polymarket/Kalshi legs limit these sizes and the capacity stops at the search limit of $20,000; the bot's bets with bookmakers are capped at $2,500.

Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 218 | 11-20T19:46 | Athletic Club v RCD Espanyol de Barcelona | 13.1 | onexbet, smarkets, winamax_de | 0.47% | $2499.99 | $11.86 | open |  |
| 217 | 11-20T19:41 | ES Troyes AC v Le Havre AC | 3.1 | marathonbet, pinnacle, unibet_se | 0.97% | $2499.98 | $24.20 | open |  |
| 216 | 11-20T19:31 | ES Troyes AC v Le Havre AC | 13.1 | onexbet, pinnacle, unibet_se | 1.59% | $2499.99 | $39.73 | open |  |
| 215 | 11-20T19:26 | FC Bayern München v 1. FC Köln | 3.1 | betfair_ex_uk, ladbrokes_uk, smarkets | 1.45% | $2499.98 | $35.89 | open |  |
| 214 | 11-20T19:16 | ES Troyes AC v Le Havre AC | 28.1 | onexbet, smarkets, unibet_se | 1.83% | $2499.99 | $45.72 | open |  |
| 213 | 11-20T19:16 | FC Bayern München v 1. FC Köln | 13.1 | onexbet | 1.15% | $2499.92 | $28.08 | open |  |
| 212 | 11-20T19:01 | Athletic Club v RCD Espanyol de Barcelona | 58.1 | onexbet, smarkets | 1.07% | $2499.98 | $26.70 | open |  |
| 211 | 11-20T19:01 | FC Bayern München v 1. FC Köln | 28.1 | onexbet, smarkets | 1.43% | $2499.99 | $35.72 | open |  |
| 210 | 11-20T18:37 | FC Bayern München v 1. FC Köln | 52.5 | no | 0.55% | $2522.18 | $13.86 | open |  |
| 209 | 11-20T18:35 | FC Bayern München v 1. FC Köln | 54.5 | no | 0.45% | $185.57 | $0.78 | open |  |
| 208 | 11-20T18:33 | FC Bayern München v 1. FC Köln | 56.5 | no | 0.46% | $327.49 | $1.49 | open |  |
| 207 | 11-20T18:31 | FC Bayern München v 1. FC Köln | 58.1 | ladbrokes_uk, matchbook, smarkets | 0.54% | $2499.99 | $13.51 | open |  |
| 206 | 11-20T17:01 | Athletic Club v RCD Espanyol de Barcelona | 178.3 | onexbet, pinnacle | 0.38% | $2499.81 | $9.18 | open |  |
| 205 | 11-20T12:40 | Al Sadd SC v Lusail SC | 19.8 | no | 0.26% | $27.38 | $0.07 | settled | $+0.07 |
| 204 | 11-20T02:56 | DAL at VGK | 3.4 | unibet_se | 51.91% | $2499.99 | $1297.86 | settled | $-2499.99 |
| 203 | 11-20T02:46 | DAL at VGK | 13.4 | unibet_se | 51.91% | $2499.99 | $1297.86 | settled | $-2499.99 |
| 202 | 11-20T02:36 | VAN at SEA | 3.4 | marathonbet, onexbet | 39.39% | $2499.99 | $984.83 | settled | $+984.85 |
| 201 | 11-20T02:31 | DAL at VGK | 28.4 | onexbet, unibet_se | 52.73% | $2499.99 | $1318.17 | settled | $-2499.99 |
| 200 | 11-20T02:26 | VAN at SEA | 13.4 | onexbet | 39.05% | $2499.99 | $976.16 | settled | $+976.16 |
| 199 | 11-20T02:11 | VAN at SEA | 28.4 | onexbet | 39.05% | $2499.99 | $976.16 | settled | $+976.16 |
| 198 | 11-20T01:56 | ANA at COL | 3.4 | marathonbet, onexbet | 53.78% | $2499.99 | $1344.41 | settled | $+1344.43 |
| 197 | 11-20T01:46 | ANA at COL | 13.4 | onexbet | 50.47% | $2499.99 | $1261.74 | settled | $+1261.76 |
| 196 | 11-20T01:41 | VAN at SEA | 58.4 | onexbet | 39.05% | $2499.99 | $976.16 | settled | $+976.16 |
| 195 | 11-20T01:31 | ANA at COL | 28.4 | leovegas_se, onexbet | 49.55% | $2499.99 | $1238.71 | settled | $+1238.71 |
| 194 | 11-20T01:09 | IND at HOU | 5.4 | no | 0.30% | $136.77 | $0.23 | settled | $+0.23 |
