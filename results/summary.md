# Paper-trading bot: status at 2026-11-19T00:09:29Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 128 / 113 |
| Realised profit | $2,060.82 ≈ €1,776.57 |
| … Polymarket/Kalshi only | $28.75 |
| … with bookmakers (all) | $2,032.06 |
| … with bookmakers licensed in Spain only | $0.00 |
| Open positions (cost) | $30,091.58 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $31,640.82 ≈ €27,276.57 |
| Return so far (realised / peak money in use) | 3.420% over 12.1 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 642, executed 25, rounding 74, seen 802, vanished 55.
Gaps using bookmakers: below_min_size 2, executed 103, no_cash 41, rounding 2, seen 168, vanished 20 (snapshots combined with Polymarket/Kalshi: 1388).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 3,529 (about 19.9 days at the current pace).

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $10,552.78 | $2,060.81 | $4,486.78 | $2,369.73 |
| Kalshi | $5,800.00 | $5,192.77 | $41.01 | $479.57 | $5,192.77 |
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
| fanduel | $580.00 | $-2,247.51 | $1,168.22 | $1,659.29 | $-2,247.51 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $5,009.94 | $0.00 | $6,720.04 | $-7,633.02 |
| leovegas_se | $580.00 | $-2,775.34 | $8,102.45 | $8,102.45 | $-2,775.34 |
| lowvig | $580.00 | $-3,946.77 | $0.00 | $1,628.95 | $-3,946.77 |
| marathonbet (Spain) | $580.00 | $624.25 | $1,436.39 | $2,789.53 | $-1,673.21 |
| matchbook | $580.00 | $5,916.30 | $960.90 | $4,155.10 | $-3,925.78 |
| mybookieag | $580.00 | $-4,546.41 | $0.00 | $4,422.60 | $-7,124.16 |
| onexbet | $580.00 | $-16,441.92 | $11,919.75 | $22,357.23 | $-20,246.55 |
| pinnacle | $580.00 | $-2,307.28 | $0.00 | $3,723.57 | $-6,879.02 |
| skybet | $580.00 | $-375.11 | $0.00 | $567.67 | $-375.11 |
| smarkets | $580.00 | $-6,439.08 | $0.00 | $4,070.28 | $-8,947.57 |
| tipico_de | $580.00 | $2,622.00 | $0.00 | $486.19 | $93.81 |
| unibet_nl | $580.00 | $-7,801.68 | $0.00 | $4,157.51 | $-7,801.68 |
| unibet_se | $580.00 | $-2,166.46 | $3,070.28 | $7,330.64 | $-5,486.19 |
| williamhill (Spain) | $580.00 | $-751.77 | $1,331.77 | $1,331.77 | $-751.77 |
| winamax_de (Spain) | $580.00 | $1,646.54 | $0.00 | $805.80 | $-872.91 |

Peak money in use across all accounts at the same time: $60,263.56 ≈ €51,951.34.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 136 Polymarket/Kalshi and 192 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 136 | 108 | 80 | 0 | 0 |
| +1 min | 135 | 102 | 74 | 0 | 1 |
| +2 min | 134 | 87 | 59 | 1 | 1 |
| +5 min | 128 | 64 | 46 | 2 | 6 |
| bookmaker confirmation (~1 min) | 326 | 145 | 140 | 9 | 0 |
| next bookmaker snapshot | 295 | 34 | 28 | 11 | 0 |

Depth at detection (capacity = largest size still profitable after walking the order books):

- Polymarket/Kalshi gaps (136): median capacity $0 (maximum $2,826); still profitable with a $50 stake: 27 of 135; median largest guaranteed profit $0.00.
- Gaps with bookmakers (192): median capacity $20,000 (maximum $20,000); still profitable with a $50 stake: 184 of 192; median largest guaranteed profit $129.03. Bookmakers publish no order-book depth, so only the Polymarket/Kalshi legs limit these sizes and the capacity stops at the search limit of $20,000; the bot's bets with bookmakers are capped at $2,500.

Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 128 | 11-19T00:02 | BOS at DET | 27.9 | leovegas_se, onexbet | 60.73% | $2499.99 | $1518.33 | open |  |
| 127 | 11-19T00:02 | MTL at NJ | 27.9 | onexbet, unibet_se | 39.89% | $2499.99 | $997.31 | open |  |
| 126 | 11-18T23:57 | PHI at ORL | 2.9 | onexbet | 1.91% | $2499.99 | $47.70 | open |  |
| 125 | 11-18T23:51 | PHI at ORL | 8.4 | no | 0.52% | $19.92 | $0.10 | open |  |
| 124 | 11-18T23:47 | PHI at ORL | 13.0 | matchbook, onexbet | 0.96% | $2499.99 | $24.10 | open |  |
| 123 | 11-18T23:31 | BOS at DET | 58.1 | leovegas_se, onexbet | 58.81% | $2499.99 | $1470.21 | open |  |
| 122 | 11-18T23:31 | MTL at NJ | 58.1 | onexbet, unibet_se | 39.89% | $2499.99 | $997.31 | open |  |
| 121 | 11-18T23:31 | PHI at ORL | 28.1 | marathonbet | 8.59% | $2499.99 | $214.79 | open |  |
| 120 | 11-18T23:27 | PHI at ORL | 32.2 | no | 0.68% | $11.93 | $0.07 | open |  |
| 119 | 11-18T23:21 | MIL at MIA | 38.2 | no | 0.26% | $59.84 | $0.14 | open |  |
| 118 | 11-18T23:02 | PHI at ORL | 58.0 | fanduel, williamhill | 6.54% | $2499.99 | $163.55 | open |  |
| 117 | 11-18T22:31 | BOS at DET | 118.1 | leovegas_se | 60.76% | $2499.99 | $1519.01 | open |  |
| 116 | 11-18T22:31 | MTL at NJ | 118.1 | onexbet, unibet_se | 42.74% | $2499.99 | $1068.48 | open |  |
| 115 | 11-18T21:31 | BOS at DET | 178.2 | leovegas_se | 60.76% | $2499.99 | $1519.01 | open |  |
| 114 | 11-18T21:31 | MTL at NJ | 178.2 | onexbet, unibet_se | 42.26% | $2499.99 | $1056.36 | open |  |
| 113 | 11-18T00:31 | POR at MIN | 28.2 | lowvig, mybookieag | 3.11% | $2499.99 | $77.75 | settled | $+77.76 |
| 112 | 11-17T19:41 | Denmark v Norway | 3.3 | onexbet | 0.36% | $2499.99 | $8.96 | settled | $+8.97 |
| 111 | 11-17T19:31 | Poland v Sweden | 13.3 | onexbet | 0.67% | $2499.99 | $16.84 | settled | $+16.84 |
| 110 | 11-17T19:31 | Israel v Austria | 13.3 | onexbet, pinnacle, winamax_de | 0.78% | $2499.98 | $19.47 | settled | $+19.47 |
| 109 | 11-17T19:31 | Denmark v Norway | 13.3 | betanysports, onexbet | 1.05% | $2499.68 | $25.66 | settled | $+26.52 |
| 108 | 11-17T19:16 | Denmark v Norway | 28.3 | matchbook, onexbet | 1.75% | $2499.99 | $43.72 | settled | $+43.72 |
| 107 | 11-17T18:46 | Poland v Sweden | 58.2 | onexbet | 0.64% | $2500.00 | $16.07 | settled | $+16.08 |
| 106 | 11-17T18:46 | Hungary v Northern Ireland | 58.2 | betonlineag, unibet_se | 2.53% | $2499.98 | $63.32 | settled | $+63.34 |
| 105 | 11-17T01:56 | PHX at DEN | 3.4 | draftkings | 0.21% | $2499.99 | $5.21 | settled | $+5.22 |
| 104 | 11-17T01:46 | PHX at DEN | 13.4 | draftkings | 0.21% | $2499.99 | $5.21 | settled | $+5.22 |
