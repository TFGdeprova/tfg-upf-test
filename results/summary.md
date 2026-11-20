# Paper-trading bot: status at 2026-11-20T00:24:24Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 180 / 137 |
| Realised profit | $-27,383.98 ≈ €-23,606.88 |
| … Polymarket/Kalshi only | $29.24 |
| … with bookmakers (all) | $-27,413.22 |
| … with bookmakers licensed in Spain only | $214.80 |
| Open positions (cost) | $105,025.17 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $2,196.02 ≈ €1,893.12 |
| Return so far (realised / peak money in use) | -26.074% over 13.1 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 703, executed 29, rounding 84, seen 883, vanished 62.
Gaps using bookmakers: below_min_size 4, executed 151, no_cash 41, rounding 2, seen 231, vanished 24 (snapshots combined with Polymarket/Kalshi: 1540).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 3,205 (about 12.3 days at the current pace).

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $16,531.27 | $25.58 | $4,486.78 | $2,369.73 |
| Kalshi | $5,800.00 | $5,221.37 | $0.00 | $479.57 | $5,176.88 |
| betanysports | $580.00 | $-894.59 | $0.00 | $4,190.72 | $-3,610.72 |
| betfair_ex_eu (Spain) | $580.00 | $453.07 | $0.00 | $126.93 | $453.07 |
| betfair_ex_uk (Spain) | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
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
| leovegas_se | $580.00 | $-42,785.08 | $35,009.75 | $35,009.75 | $-42,785.08 |
| lowvig | $580.00 | $-4,857.78 | $0.00 | $1,628.95 | $-4,857.78 |
| marathonbet (Spain) | $580.00 | $-6,162.83 | $5,056.32 | $5,056.32 | $-6,162.83 |
| matchbook | $580.00 | $8,440.39 | $0.00 | $4,155.10 | $-3,925.78 |
| mybookieag | $580.00 | $-4,546.41 | $0.00 | $4,422.60 | $-7,124.16 |
| onexbet | $580.00 | $-63,713.99 | $45,886.71 | $45,886.71 | $-63,713.99 |
| pinnacle | $580.00 | $-2,307.28 | $0.00 | $3,723.57 | $-6,879.02 |
| skybet | $580.00 | $-375.11 | $0.00 | $567.67 | $-375.11 |
| smarkets | $580.00 | $-6,439.08 | $0.00 | $4,070.28 | $-8,947.57 |
| tipico_de | $580.00 | $-3,229.05 | $5,851.05 | $5,851.05 | $-3,229.05 |
| unibet_nl | $580.00 | $-7,801.68 | $0.00 | $4,157.51 | $-7,801.68 |
| unibet_se | $580.00 | $-16,908.63 | $13,195.76 | $13,195.76 | $-16,908.63 |
| williamhill (Spain) | $580.00 | $-751.77 | $0.00 | $1,331.77 | $-751.77 |
| winamax_de (Spain) | $580.00 | $1,646.54 | $0.00 | $805.80 | $-872.91 |

Peak money in use across all accounts at the same time: $105,025.17 ≈ €90,538.94.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 151 Polymarket/Kalshi and 255 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 150 | 119 | 90 | 1 | 0 |
| +1 min | 149 | 110 | 82 | 1 | 1 |
| +2 min | 146 | 94 | 65 | 2 | 2 |
| +5 min | 140 | 68 | 50 | 3 | 7 |
| bookmaker confirmation (~1 min) | 424 | 236 | 231 | 10 | 0 |
| next bookmaker snapshot | 358 | 90 | 84 | 11 | 0 |

Depth at detection (capacity = largest size still profitable after walking the order books):

- Polymarket/Kalshi gaps (151): median capacity $0 (maximum $2,826); still profitable with a $50 stake: 27 of 149; median largest guaranteed profit $0.00.
- Gaps with bookmakers (255): median capacity $20,000 (maximum $20,000); still profitable with a $50 stake: 245 of 255; median largest guaranteed profit $176.99. Bookmakers publish no order-book depth, so only the Polymarket/Kalshi legs limit these sizes and the capacity stops at the search limit of $20,000; the bot's bets with bookmakers are capped at $2,500.

Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 180 | 11-20T00:16 | EDM at TB | 13.1 | leovegas_se, onexbet | 47.87% | $2499.99 | $1196.71 | open |  |
| 179 | 11-20T00:02 | DAL at VGK | 177.9 | onexbet, unibet_se | 51.91% | $2499.99 | $1297.86 | open |  |
| 178 | 11-20T00:02 | ANA at COL | 117.9 | leovegas_se, onexbet | 52.66% | $2499.99 | $1316.50 | open |  |
| 177 | 11-20T00:02 | MIN at CGY | 57.9 | leovegas_se, onexbet | 130.02% | $2499.99 | $3250.51 | open |  |
| 176 | 11-20T00:02 | CBJ at CHI | 57.9 | onexbet, unibet_se | 88.89% | $2499.99 | $2222.12 | open |  |
| 175 | 11-20T00:02 | EDM at TB | 27.9 | leovegas_se, onexbet | 47.87% | $2499.99 | $1196.71 | open |  |
| 174 | 11-19T23:57 | NYI at WPG | 2.9 | marathonbet, unibet_se | 55.91% | $2499.99 | $1397.80 | open |  |
| 173 | 11-19T23:57 | MTL at CAR | 2.9 | leovegas_se, tipico_de | 20.92% | $2499.99 | $523.03 | open |  |
| 172 | 11-19T23:57 | PHI at OTT | 2.9 | marathonbet, onexbet | 41.75% | $2499.99 | $1043.63 | open |  |
| 171 | 11-19T23:57 | STL at PIT | 2.9 | marathonbet | 58.60% | $2499.99 | $1465.11 | open |  |
| 170 | 11-19T23:57 | LA at TOR | 2.9 | leovegas_se, marathonbet | 53.83% | $2499.99 | $1345.83 | open |  |
| 169 | 11-19T23:57 | BUF at WSH | 2.9 | leovegas_se, onexbet | 45.44% | $2499.99 | $1135.88 | open |  |
| 168 | 11-19T23:47 | Orlando City SC v FC Cincinnati | 42.0 | no | 0.26% | $25.58 | $0.07 | open |  |
| 167 | 11-19T23:46 | NYI at WPG | 13.1 | onexbet, unibet_se | 56.64% | $2499.99 | $1416.04 | open |  |
| 166 | 11-19T23:46 | MTL at CAR | 13.1 | leovegas_se, tipico_de | 20.92% | $2499.99 | $523.03 | open |  |
| 165 | 11-19T23:46 | PHI at OTT | 13.1 | onexbet | 40.94% | $2500.00 | $1023.44 | open |  |
| 164 | 11-19T23:46 | STL at PIT | 13.1 | onexbet | 61.02% | $2499.99 | $1525.47 | open |  |
| 163 | 11-19T23:46 | LA at TOR | 13.1 | leovegas_se, onexbet | 55.19% | $2499.99 | $1379.67 | open |  |
| 162 | 11-19T23:46 | BUF at WSH | 13.1 | onexbet | 45.22% | $2499.99 | $1130.44 | open |  |
| 161 | 11-19T23:42 | VAN at SEA | 177.8 | onexbet | 38.55% | $2499.99 | $963.80 | open |  |
| 160 | 11-19T23:32 | NYI at WPG | 28.0 | onexbet, unibet_se | 56.64% | $2499.99 | $1416.04 | open |  |
| 159 | 11-19T23:32 | MTL at CAR | 28.0 | leovegas_se, tipico_de | 20.92% | $2499.99 | $523.03 | open |  |
| 158 | 11-19T23:31 | PHI at OTT | 28.1 | leovegas_se, onexbet | 40.56% | $2499.99 | $1013.99 | open |  |
| 157 | 11-19T23:31 | STL at PIT | 28.1 | onexbet, unibet_se | 61.54% | $2499.99 | $1538.44 | open |  |
| 156 | 11-19T23:31 | EDM at TB | 58.1 | leovegas_se, onexbet | 49.22% | $2499.99 | $1230.44 | open |  |
