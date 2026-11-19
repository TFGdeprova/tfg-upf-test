# Paper-trading bot: status at 2026-11-19T21:48:40Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 144 / 135 |
| Realised profit | $-27,384.08 ≈ €-23,606.97 |
| … Polymarket/Kalshi only | $29.14 |
| … with bookmakers (all) | $-27,413.22 |
| … with bookmakers licensed in Spain only | $214.80 |
| Open positions (cost) | $17,523.82 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $2,195.92 ≈ €1,893.03 |
| Return so far (realised / peak money in use) | -45.441% over 13.0 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 700, executed 28, rounding 83, seen 876, vanished 60.
Gaps using bookmakers: below_min_size 2, executed 116, no_cash 41, rounding 2, seen 185, vanished 24 (snapshots combined with Polymarket/Kalshi: 1444).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 3,349 (about 18.2 days at the current pace).

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $16,532.86 | $21.38 | $4,486.78 | $2,369.73 |
| Kalshi | $5,800.00 | $5,221.37 | $2.51 | $479.57 | $5,176.88 |
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
| leovegas_se | $580.00 | $-16,383.35 | $8,608.02 | $13,102.44 | $-16,383.35 |
| lowvig | $580.00 | $-4,857.78 | $0.00 | $1,628.95 | $-4,857.78 |
| marathonbet (Spain) | $580.00 | $-1,106.51 | $0.00 | $3,167.15 | $-1,673.21 |
| matchbook | $580.00 | $8,440.39 | $0.00 | $4,155.10 | $-3,925.78 |
| mybookieag | $580.00 | $-4,546.41 | $0.00 | $4,422.60 | $-7,124.16 |
| onexbet | $580.00 | $-24,192.36 | $6,365.08 | $22,357.23 | $-24,192.36 |
| pinnacle | $580.00 | $-2,307.28 | $0.00 | $3,723.57 | $-6,879.02 |
| skybet | $580.00 | $-375.11 | $0.00 | $567.67 | $-375.11 |
| smarkets | $580.00 | $-6,439.08 | $0.00 | $4,070.28 | $-8,947.57 |
| tipico_de | $580.00 | $2,622.00 | $0.00 | $486.19 | $93.81 |
| unibet_nl | $580.00 | $-7,801.68 | $0.00 | $4,157.51 | $-7,801.68 |
| unibet_se | $580.00 | $-6,239.70 | $2,526.83 | $7,330.64 | $-6,239.70 |
| williamhill (Spain) | $580.00 | $-751.77 | $0.00 | $1,331.77 | $-751.77 |
| winamax_de (Spain) | $580.00 | $1,646.54 | $0.00 | $805.80 | $-872.91 |

Peak money in use across all accounts at the same time: $60,263.56 ≈ €51,951.34.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 147 Polymarket/Kalshi and 209 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 146 | 116 | 87 | 1 | 0 |
| +1 min | 145 | 108 | 80 | 1 | 1 |
| +2 min | 143 | 92 | 63 | 2 | 2 |
| +5 min | 137 | 67 | 49 | 3 | 7 |
| bookmaker confirmation (~1 min) | 359 | 171 | 166 | 10 | 0 |
| next bookmaker snapshot | 314 | 48 | 42 | 11 | 0 |

Depth at detection (capacity = largest size still profitable after walking the order books):

- Polymarket/Kalshi gaps (147): median capacity $0 (maximum $2,826); still profitable with a $50 stake: 27 of 145; median largest guaranteed profit $0.00.
- Gaps with bookmakers (209): median capacity $20,000 (maximum $20,000); still profitable with a $50 stake: 201 of 209; median largest guaranteed profit $136.12. Bookmakers publish no order-book depth, so only the Polymarket/Kalshi legs limit these sizes and the capacity stops at the search limit of $20,000; the bot's bets with bookmakers are capped at $2,500.

Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 144 | 11-19T21:31 | EDM at TB | 178.4 | leovegas_se, onexbet | 48.51% | $2499.99 | $1212.68 | open |  |
| 143 | 11-19T21:01 | NYI at WPG | 178.4 | onexbet, unibet_se | 56.64% | $2499.99 | $1416.04 | open |  |
| 142 | 11-19T21:01 | MTL at CAR | 178.4 | leovegas_se, onexbet | 20.93% | $2499.99 | $523.30 | open |  |
| 141 | 11-19T21:01 | PHI at OTT | 178.4 | leovegas_se, onexbet | 42.45% | $2499.99 | $1061.18 | open |  |
| 140 | 11-19T21:01 | STL at PIT | 178.4 | onexbet, unibet_se | 61.13% | $2499.99 | $1528.14 | open |  |
| 139 | 11-19T21:01 | LA at TOR | 178.4 | leovegas_se, onexbet | 58.13% | $2499.99 | $1453.31 | open |  |
| 138 | 11-19T21:01 | BUF at WSH | 178.4 | leovegas_se, onexbet | 49.10% | $2499.99 | $1227.48 | open |  |
| 137 | 11-19T15:21 | FK Austria Wien v FC Bayern München | 143.0 | no | 0.34% | $11.97 | $0.03 | open |  |
| 136 | 11-19T15:06 | FK Austria Wien v FC Bayern München | 158.0 | no | 0.57% | $11.92 | $0.06 | open |  |
| 135 | 11-19T00:57 | GSW at DAL | 2.7 | no | 0.26% | $16.96 | $0.04 | settled | $+0.04 |
| 134 | 11-19T00:56 | DET at NOP | 3.2 | onexbet | 1.14% | $704.35 | $8.05 | settled | $+8.05 |
| 133 | 11-19T00:31 | DET at NOP | 28.3 | lowvig | 3.86% | $2499.99 | $96.38 | settled | $+96.39 |
| 132 | 11-19T00:26 | BOS at DET | 3.2 | leovegas_se | 59.38% | $2500.00 | $1484.38 | settled | $-2500.00 |
| 131 | 11-19T00:26 | MTL at NJ | 3.2 | marathonbet, unibet_se | 38.46% | $2499.99 | $961.53 | settled | $-2499.99 |
| 130 | 11-19T00:16 | BOS at DET | 13.2 | leovegas_se | 59.38% | $2499.99 | $1484.36 | settled | $-2499.99 |
| 129 | 11-19T00:16 | MTL at NJ | 13.2 | onexbet, unibet_se | 39.89% | $2499.99 | $997.31 | settled | $-2499.99 |
| 128 | 11-19T00:02 | BOS at DET | 27.9 | leovegas_se, onexbet | 60.73% | $2499.99 | $1518.33 | settled | $-2499.99 |
| 127 | 11-19T00:02 | MTL at NJ | 27.9 | onexbet, unibet_se | 39.89% | $2499.99 | $997.31 | settled | $-2499.99 |
| 126 | 11-18T23:57 | PHI at ORL | 2.9 | onexbet | 1.91% | $2499.99 | $47.70 | settled | $+47.71 |
| 125 | 11-18T23:51 | PHI at ORL | 8.4 | no | 0.52% | $19.92 | $0.10 | settled | $+0.13 |
| 124 | 11-18T23:47 | PHI at ORL | 13.0 | matchbook, onexbet | 0.96% | $2499.99 | $24.10 | settled | $+24.10 |
| 123 | 11-18T23:31 | BOS at DET | 58.1 | leovegas_se, onexbet | 58.81% | $2499.99 | $1470.21 | settled | $-2499.99 |
| 122 | 11-18T23:31 | MTL at NJ | 58.1 | onexbet, unibet_se | 39.89% | $2499.99 | $997.31 | settled | $-2499.99 |
| 121 | 11-18T23:31 | PHI at ORL | 28.1 | marathonbet | 8.59% | $2499.99 | $214.79 | settled | $+214.80 |
| 120 | 11-18T23:27 | PHI at ORL | 32.2 | no | 0.68% | $11.93 | $0.07 | settled | $+0.07 |
