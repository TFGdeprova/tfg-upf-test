# Paper-trading bot: status at 2026-11-21T05:22:27Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 221 / 219 |
| Realised profit | $-91,367.76 ≈ €-78,765.31 |
| … Polymarket/Kalshi only | $45.76 |
| … with bookmakers (all) | $-91,413.51 |
| … with bookmakers licensed in Spain only | $-2,285.19 |
| Open positions (cost) | $925.37 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $-61,207.75 ≈ €-52,765.31 |
| Return so far (realised / peak money in use) | -58.577% over 14.3 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 760, executed 36, rounding 86, seen 954, vanished 65.
Gaps using bookmakers: below_min_size 4, executed 185, no_cash 41, rounding 3, seen 268, vanished 26 (snapshots combined with Polymarket/Kalshi: 1684).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 2,613 (about 6.3 days at the current pace).

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $14,032.70 | $875.87 | $4,486.78 | $2,369.73 |
| Kalshi | $5,800.00 | $7,254.92 | $49.50 | $2,216.01 | $2,967.42 |
| betanysports | $580.00 | $-894.59 | $0.00 | $4,190.72 | $-3,610.72 |
| betfair_ex_eu (Spain) | $580.00 | $453.07 | $0.00 | $126.93 | $453.07 |
| betfair_ex_uk (Spain) | $580.00 | $505.96 | $0.00 | $74.04 | $505.96 |
| betfred_uk | $580.00 | $-768.02 | $0.00 | $1,348.02 | $-768.02 |
| betmgm | $580.00 | $5,098.25 | $0.00 | $5,577.36 | $-4,997.36 |
| betonlineag | $580.00 | $-3,111.38 | $0.00 | $4,590.49 | $-4,391.48 |
| betrivers | $580.00 | $8,378.80 | $0.00 | $2,248.46 | $-1,141.39 |
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
| ladbrokes_uk | $580.00 | $-3,948.91 | $0.00 | $4,528.91 | $-3,948.91 |
| leovegas_se | $580.00 | $-12,660.83 | $0.00 | $47,555.97 | $-55,331.30 |
| lowvig | $580.00 | $-4,847.83 | $0.00 | $1,628.95 | $-4,867.83 |
| marathonbet (Spain) | $580.00 | $-10,325.04 | $0.00 | $8,525.07 | $-10,325.04 |
| matchbook | $580.00 | $8,365.00 | $0.00 | $4,155.10 | $-3,925.78 |
| mybookieag | $580.00 | $-4,546.41 | $0.00 | $4,422.60 | $-7,124.16 |
| onexbet | $580.00 | $-68,056.09 | $0.00 | $69,050.38 | $-86,877.66 |
| pinnacle | $580.00 | $-2,369.99 | $0.00 | $3,723.57 | $-6,879.02 |
| skybet | $580.00 | $-375.11 | $0.00 | $567.67 | $-375.11 |
| smarkets | $580.00 | $3,834.67 | $0.00 | $4,070.28 | $-8,947.57 |
| tipico_de | $580.00 | $-3,229.05 | $0.00 | $5,851.05 | $-3,229.05 |
| unibet_nl | $580.00 | $-7,801.68 | $0.00 | $4,157.51 | $-7,801.68 |
| unibet_se | $580.00 | $-4,203.96 | $0.00 | $24,382.67 | $-28,095.54 |
| williamhill (Spain) | $580.00 | $-751.77 | $0.00 | $1,331.77 | $-751.77 |
| winamax_de (Spain) | $580.00 | $1,144.17 | $0.00 | $805.80 | $-872.91 |

Peak money in use across all accounts at the same time: $155,979.62 ≈ €134,465.19.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 162 Polymarket/Kalshi and 293 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 161 | 128 | 98 | 1 | 0 |
| +1 min | 160 | 119 | 90 | 1 | 1 |
| +2 min | 157 | 102 | 72 | 2 | 3 |
| +5 min | 149 | 73 | 55 | 4 | 9 |
| bookmaker confirmation (~1 min) | 530 | 322 | 317 | 11 | 0 |
| next bookmaker snapshot | 434 | 143 | 137 | 13 | 0 |

Depth at detection (capacity = largest size still profitable after walking the order books):

- Polymarket/Kalshi gaps (162): median capacity $0 (maximum $2,826); still profitable with a $50 stake: 31 of 160; median largest guaranteed profit $0.00.
- Gaps with bookmakers (293): median capacity $20,000 (maximum $20,000); still profitable with a $50 stake: 280 of 293; median largest guaranteed profit $187.91. Bookmakers publish no order-book depth, so only the Polymarket/Kalshi legs limit these sizes and the capacity stops at the search limit of $20,000; the bot's bets with bookmakers are capped at $2,500.

Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 221 | 11-21T03:03 | Club Tijuana v Atlante FC | 6.4 | no | 0.29% | $160.59 | $0.41 | open |  |
| 220 | 11-21T03:02 | Club Tijuana v Atlante FC | 7.4 | no | 0.29% | $764.79 | $2.21 | open |  |
| 219 | 11-21T00:26 | TOR at DET | 3.2 | betrivers | 0.95% | $2499.99 | $23.83 | settled | $+23.83 |
| 218 | 11-20T19:46 | Athletic Club v RCD Espanyol de Barcelona | 13.1 | onexbet, smarkets, winamax_de | 0.47% | $2499.99 | $11.86 | settled | $+11.87 |
| 217 | 11-20T19:41 | ES Troyes AC v Le Havre AC | 3.1 | marathonbet, pinnacle, unibet_se | 0.97% | $2499.98 | $24.20 | settled | $+24.22 |
| 216 | 11-20T19:31 | ES Troyes AC v Le Havre AC | 13.1 | onexbet, pinnacle, unibet_se | 1.59% | $2499.99 | $39.73 | settled | $+39.73 |
| 215 | 11-20T19:26 | FC Bayern München v 1. FC Köln | 3.1 | betfair_ex_uk, ladbrokes_uk, smarkets | 1.45% | $2499.98 | $35.89 | settled | $+36.04 |
| 214 | 11-20T19:16 | ES Troyes AC v Le Havre AC | 28.1 | onexbet, smarkets, unibet_se | 1.83% | $2499.99 | $45.72 | settled | $+45.72 |
| 213 | 11-20T19:16 | FC Bayern München v 1. FC Köln | 13.1 | onexbet | 1.15% | $2499.92 | $28.08 | settled | $+28.08 |
| 212 | 11-20T19:01 | Athletic Club v RCD Espanyol de Barcelona | 58.1 | onexbet, smarkets | 1.07% | $2499.98 | $26.70 | settled | $+26.70 |
| 211 | 11-20T19:01 | FC Bayern München v 1. FC Köln | 28.1 | onexbet, smarkets | 1.43% | $2499.99 | $35.72 | settled | $+35.72 |
| 210 | 11-20T18:37 | FC Bayern München v 1. FC Köln | 52.5 | no | 0.55% | $2522.18 | $13.86 | settled | $+13.87 |
| 209 | 11-20T18:35 | FC Bayern München v 1. FC Köln | 54.5 | no | 0.45% | $185.57 | $0.78 | settled | $+0.78 |
| 208 | 11-20T18:33 | FC Bayern München v 1. FC Köln | 56.5 | no | 0.46% | $327.49 | $1.49 | settled | $+1.49 |
| 207 | 11-20T18:31 | FC Bayern München v 1. FC Köln | 58.1 | ladbrokes_uk, matchbook, smarkets | 0.54% | $2499.99 | $13.51 | settled | $+13.58 |
| 206 | 11-20T17:01 | Athletic Club v RCD Espanyol de Barcelona | 178.3 | onexbet, pinnacle | 0.38% | $2499.81 | $9.18 | settled | $+9.67 |
| 205 | 11-20T12:40 | Al Sadd SC v Lusail SC | 19.8 | no | 0.26% | $27.38 | $0.07 | settled | $+0.07 |
| 204 | 11-20T02:56 | DAL at VGK | 3.4 | unibet_se | 51.91% | $2499.99 | $1297.86 | settled | $-2499.99 |
| 203 | 11-20T02:46 | DAL at VGK | 13.4 | unibet_se | 51.91% | $2499.99 | $1297.86 | settled | $-2499.99 |
| 202 | 11-20T02:36 | VAN at SEA | 3.4 | marathonbet, onexbet | 39.39% | $2499.99 | $984.83 | settled | $+984.85 |
| 201 | 11-20T02:31 | DAL at VGK | 28.4 | onexbet, unibet_se | 52.73% | $2499.99 | $1318.17 | settled | $-2499.99 |
| 200 | 11-20T02:26 | VAN at SEA | 13.4 | onexbet | 39.05% | $2499.99 | $976.16 | settled | $+976.16 |
| 199 | 11-20T02:11 | VAN at SEA | 28.4 | onexbet | 39.05% | $2499.99 | $976.16 | settled | $+976.16 |
| 198 | 11-20T01:56 | ANA at COL | 3.4 | marathonbet, onexbet | 53.78% | $2499.99 | $1344.41 | settled | $+1344.43 |
| 197 | 11-20T01:46 | ANA at COL | 13.4 | onexbet | 50.47% | $2499.99 | $1261.74 | settled | $+1261.76 |
