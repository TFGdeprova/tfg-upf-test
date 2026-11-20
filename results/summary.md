# Paper-trading bot: status at 2026-11-20T02:24:58Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 199 / 137 |
| Realised profit | $-27,383.98 ≈ €-23,606.88 |
| … Polymarket/Kalshi only | $29.24 |
| … with bookmakers (all) | $-27,413.22 |
| … with bookmakers licensed in Spain only | $214.80 |
| Open positions (cost) | $143,479.67 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $2,196.02 ≈ €1,893.12 |
| Return so far (realised / peak money in use) | -19.086% over 13.1 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 713, executed 30, rounding 86, seen 898, vanished 63.
Gaps using bookmakers: below_min_size 4, executed 169, no_cash 41, rounding 3, seen 250, vanished 24 (snapshots combined with Polymarket/Kalshi: 1589).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 3,013 (about 8.8 days at the current pace).

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $16,186.94 | $369.91 | $4,486.78 | $2,369.73 |
| Kalshi | $5,800.00 | $5,046.43 | $174.94 | $479.57 | $5,046.43 |
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
| leovegas_se | $580.00 | $-55,331.30 | $47,555.97 | $47,555.97 | $-55,331.30 |
| lowvig | $580.00 | $-4,867.83 | $10.05 | $1,628.95 | $-4,867.83 |
| marathonbet (Spain) | $580.00 | $-8,874.01 | $7,767.50 | $7,767.50 | $-8,874.01 |
| matchbook | $580.00 | $8,440.39 | $0.00 | $4,155.10 | $-3,925.78 |
| mybookieag | $580.00 | $-4,546.41 | $0.00 | $4,422.60 | $-7,124.16 |
| onexbet | $580.00 | $-81,044.35 | $63,217.07 | $63,217.07 | $-81,044.35 |
| pinnacle | $580.00 | $-2,366.86 | $59.58 | $3,723.57 | $-6,879.02 |
| skybet | $580.00 | $-375.11 | $0.00 | $567.67 | $-375.11 |
| smarkets | $580.00 | $-6,439.08 | $0.00 | $4,070.28 | $-8,947.57 |
| tipico_de | $580.00 | $-3,229.05 | $5,851.05 | $5,851.05 | $-3,229.05 |
| unibet_nl | $580.00 | $-7,801.68 | $0.00 | $4,157.51 | $-7,801.68 |
| unibet_se | $580.00 | $-22,186.47 | $18,473.60 | $18,473.60 | $-22,186.47 |
| williamhill (Spain) | $580.00 | $-751.77 | $0.00 | $1,331.77 | $-751.77 |
| winamax_de (Spain) | $580.00 | $1,646.54 | $0.00 | $805.80 | $-872.91 |

Peak money in use across all accounts at the same time: $143,479.67 ≈ €123,689.37.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 155 Polymarket/Kalshi and 274 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 154 | 122 | 93 | 1 | 0 |
| +1 min | 153 | 113 | 85 | 1 | 1 |
| +2 min | 150 | 96 | 67 | 2 | 3 |
| +5 min | 144 | 69 | 51 | 3 | 8 |
| bookmaker confirmation (~1 min) | 475 | 286 | 281 | 11 | 0 |
| next bookmaker snapshot | 391 | 122 | 116 | 13 | 0 |

Depth at detection (capacity = largest size still profitable after walking the order books):

- Polymarket/Kalshi gaps (155): median capacity $0 (maximum $2,826); still profitable with a $50 stake: 28 of 153; median largest guaranteed profit $0.00.
- Gaps with bookmakers (274): median capacity $20,000 (maximum $20,000); still profitable with a $50 stake: 262 of 274; median largest guaranteed profit $184.81. Bookmakers publish no order-book depth, so only the Polymarket/Kalshi legs limit these sizes and the capacity stops at the search limit of $20,000; the bot's bets with bookmakers are capped at $2,500.

Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 199 | 11-20T02:11 | VAN at SEA | 28.4 | onexbet | 39.05% | $2499.99 | $976.16 | open |  |
| 198 | 11-20T01:56 | ANA at COL | 3.4 | marathonbet, onexbet | 53.78% | $2499.99 | $1344.41 | open |  |
| 197 | 11-20T01:46 | ANA at COL | 13.4 | onexbet | 50.47% | $2499.99 | $1261.74 | open |  |
| 196 | 11-20T01:41 | VAN at SEA | 58.4 | onexbet | 39.05% | $2499.99 | $976.16 | open |  |
| 195 | 11-20T01:31 | ANA at COL | 28.4 | leovegas_se, onexbet | 49.55% | $2499.99 | $1238.71 | open |  |
| 194 | 11-20T01:09 | IND at HOU | 5.4 | no | 0.30% | $136.77 | $0.23 | open |  |
| 193 | 11-20T01:01 | DAL at VGK | 118.1 | onexbet, unibet_se | 51.91% | $2499.99 | $1297.86 | open |  |
| 192 | 11-20T01:01 | ANA at COL | 58.1 | leovegas_se, onexbet | 52.66% | $2499.99 | $1316.50 | open |  |
| 191 | 11-20T00:57 | MIN at CGY | 3.0 | leovegas_se | 131.18% | $2499.99 | $3279.55 | open |  |
| 190 | 11-20T00:57 | CBJ at CHI | 3.0 | marathonbet, unibet_se | 88.71% | $2499.99 | $2217.72 | open |  |
| 189 | 11-20T00:57 | POR at MIL | 3.0 | onexbet | 1.14% | $687.07 | $7.85 | open |  |
| 188 | 11-20T00:46 | MIN at CGY | 13.1 | leovegas_se | 131.18% | $2499.99 | $3279.55 | open |  |
| 187 | 11-20T00:46 | CBJ at CHI | 13.1 | onexbet, unibet_se | 89.93% | $2499.99 | $2248.23 | open |  |
| 186 | 11-20T00:46 | GSW at MEM | 13.1 | lowvig | 1.09% | $19.80 | $0.20 | open |  |
| 185 | 11-20T00:41 | VAN at SEA | 118.2 | onexbet | 39.05% | $2499.99 | $976.16 | open |  |
| 184 | 11-20T00:32 | MIN at CGY | 27.8 | leovegas_se | 129.73% | $2499.99 | $3243.21 | open |  |
| 183 | 11-20T00:32 | CBJ at CHI | 27.8 | onexbet, unibet_se | 89.93% | $2499.99 | $2248.23 | open |  |
| 182 | 11-20T00:32 | POR at MIL | 27.8 | pinnacle | 3.60% | $111.01 | $3.98 | open |  |
| 181 | 11-20T00:27 | EDM at TB | 2.8 | leovegas_se, marathonbet | 47.22% | $2499.99 | $1180.43 | open |  |
| 180 | 11-20T00:16 | EDM at TB | 13.1 | leovegas_se, onexbet | 47.87% | $2499.99 | $1196.71 | open |  |
| 179 | 11-20T00:02 | DAL at VGK | 177.9 | onexbet, unibet_se | 51.91% | $2499.99 | $1297.86 | open |  |
| 178 | 11-20T00:02 | ANA at COL | 117.9 | leovegas_se, onexbet | 52.66% | $2499.99 | $1316.50 | open |  |
| 177 | 11-20T00:02 | MIN at CGY | 57.9 | leovegas_se, onexbet | 130.02% | $2499.99 | $3250.51 | open |  |
| 176 | 11-20T00:02 | CBJ at CHI | 57.9 | onexbet, unibet_se | 88.89% | $2499.99 | $2222.12 | open |  |
| 175 | 11-20T00:02 | EDM at TB | 27.9 | leovegas_se, onexbet | 47.87% | $2499.99 | $1196.71 | open |  |
