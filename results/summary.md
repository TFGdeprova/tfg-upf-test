# Paper-trading bot: status at 2026-11-17T01:50:13Z

Started 2026-11-06T22:51:30Z. **Unlimited capital** (test of the opportunities): cash never limits a trade; Polymarket/Kalshi trades take the full size shown at the best prices and trades that use bookmakers (which publish no depth) are capped at $2,500.00. The capital the strategy needed is the peak money in use (table below). Balances start from the earlier reference amounts (Polymarket and Kalshi $5,800.00 each, €500 per bookmaker) and may go below zero. Euro amounts at 1.16 USD/EUR.

| | |
|---|---|
| Trades executed / settled | 104 / 97 |
| Realised profit | $1,762.12 ≈ €1,519.07 |
| … Polymarket/Kalshi only | $26.10 |
| … with bookmakers (all) | $1,736.02 |
| … with bookmakers licensed in Spain only | $0.00 |
| Open positions (cost) | $6,603.75 |
| Money in transit between accounts | $0.00 |
| Equity (cash + open at cost + in transit) | $30,762.13 ≈ €26,519.08 |
| Return so far (realised / peak money in use) | 2.924% over 10.1 days |

Polymarket/Kalshi gaps above the threshold: below_min_size 590, executed 22, rounding 64, seen 730, vanished 49.
Gaps using bookmakers: below_min_size 2, executed 82, no_cash 41, rounding 2, seen 147, vanished 20 (snapshots combined with Polymarket/Kalshi: 1203).

`seen` = first sighting; `executed` = still there at the next check (Polymarket/Kalshi) or in the confirmation
snapshot (bookmakers) and filled; `vanished` = gone by then; `below_min_size` / `rounding` / `no_cash` = too small to
fill, or not enough cash on an account.

The Odds API credits left: 944 (about 4.7 days at the current pace).

## Capital by account

Peak in use = the most money that was tied up in open positions at the same time.

| account | start | cash now | in open positions | peak in use | lowest cash |
|---|---|---|---|---|---|
| Polymarket | $5,800.00 | $3,578.38 | $3,278.13 | $3,278.13 | $2,382.67 |
| Kalshi | $5,800.00 | $5,713.35 | $24.24 | $456.78 | $5,231.94 |
| betanysports | $580.00 | $-2,144.93 | $0.00 | $4,190.72 | $-3,610.72 |
| betfair_ex_eu (Spain) | $580.00 | $453.07 | $0.00 | $126.93 | $453.07 |
| betfair_ex_uk (Spain) | $580.00 | $580.00 | $0.00 | $0.00 | $580.00 |
| betfred_uk | $580.00 | $-768.02 | $0.00 | $1,348.02 | $-768.02 |
| betmgm | $580.00 | $5,098.25 | $0.00 | $5,577.36 | $-4,997.36 |
| betonlineag | $580.00 | $-1,867.05 | $0.00 | $4,590.49 | $-4,391.48 |
| betrivers | $580.00 | $7,162.65 | $0.00 | $2,248.46 | $-1,141.39 |
| betsson | $580.00 | $2,119.70 | $0.00 | $986.99 | $-406.99 |
| bovada | $580.00 | $-244.12 | $0.00 | $824.12 | $-244.12 |
| boylesports | $580.00 | $1,315.03 | $0.00 | $1,813.51 | $-1,233.51 |
| codere_it | $580.00 | $1,797.50 | $0.00 | $1,295.21 | $-715.21 |
| coolbet | $580.00 | $7,055.77 | $0.00 | $7,199.91 | $-8,022.38 |
| coral | $580.00 | $1,338.67 | $0.00 | $1,948.91 | $-1,194.91 |
| draftkings | $580.00 | $-1,407.20 | $1,987.20 | $1,987.20 | $-1,407.20 |
| fanduel | $580.00 | $-1,079.29 | $0.00 | $1,659.29 | $-1,079.29 |
| grosvenor | $580.00 | $580.00 | $0.00 | $292.30 | $287.70 |
| gtbets | $580.00 | $5,009.94 | $0.00 | $6,720.04 | $-7,633.02 |
| leovegas_se | $580.00 | $5,327.11 | $0.00 | $2,971.13 | $-1,181.83 |
| lowvig | $580.00 | $-2,919.78 | $0.00 | $1,628.95 | $-2,919.78 |
| marathonbet (Spain) | $580.00 | $2,060.64 | $0.00 | $2,789.53 | $-1,673.21 |
| matchbook | $580.00 | $5,371.57 | $0.00 | $4,155.10 | $-3,925.78 |
| mybookieag | $580.00 | $-5,651.16 | $1,314.18 | $4,422.60 | $-5,651.16 |
| onexbet | $580.00 | $96.36 | $0.00 | $22,357.23 | $-20,246.55 |
| pinnacle | $580.00 | $-1,761.94 | $0.00 | $3,723.57 | $-6,879.02 |
| skybet | $580.00 | $-375.11 | $0.00 | $567.67 | $-375.11 |
| smarkets | $580.00 | $-6,439.08 | $0.00 | $4,070.28 | $-8,947.57 |
| tipico_de | $580.00 | $2,622.00 | $0.00 | $486.19 | $93.81 |
| unibet_nl | $580.00 | $-7,801.68 | $0.00 | $4,157.51 | $-7,801.68 |
| unibet_se | $580.00 | $-403.85 | $0.00 | $7,330.64 | $-5,486.19 |
| winamax_de (Spain) | $580.00 | $-258.41 | $0.00 | $805.80 | $-258.41 |

Peak money in use across all accounts at the same time: $60,263.56 ≈ €51,951.34.

Transfers between accounts: 4 ($1,399.69 moved, $0.00 in fees; 0 still in transit). Delays used: Polymarket out instantly, in 15 min; Kalshi crypto 30 min each way; bookmakers in instantly, out 24 h; dollars↔euros 2 h and 0.5% (see `bot/accounts.py`).

## Gaps followed: the same portfolio re-checked later, and order-book depth

Gaps above 0.1% followed: 115 Polymarket/Kalshi and 169 with bookmakers. A re-check prices the same shares and stakes at the later prices (ex-ante test); `censored` = the game started or the run ended before the re-check.

| re-check | measured | still profitable | above 0.2% | a leg no longer offered | censored |
|---|---|---|---|---|---|
| +30 s | 115 | 89 | 69 | 0 | 0 |
| +1 min | 114 | 83 | 63 | 0 | 1 |
| +2 min | 114 | 69 | 50 | 0 | 1 |
| +5 min | 109 | 54 | 41 | 0 | 6 |
| bookmaker confirmation (~1 min) | 291 | 119 | 114 | 5 | 0 |
| next bookmaker snapshot | 271 | 26 | 20 | 8 | 0 |

Depth at detection (capacity = largest size still profitable after walking the order books):

- Polymarket/Kalshi gaps (115): median capacity $0 (maximum $2,826); still profitable with a $50 stake: 22 of 114; median largest guaranteed profit $0.00.
- Gaps with bookmakers (169): median capacity $20,000 (maximum $20,000); still profitable with a $50 stake: 161 of 169; median largest guaranteed profit $118.79. Bookmakers publish no order-book depth, so only the Polymarket/Kalshi legs limit these sizes and the capacity stops at the search limit of $20,000; the bot's bets with bookmakers are capped at $2,500.

Details: `results/rechecks.csv`, `results/depth.csv`.

## Last trades

| # | time (UTC) | game | min to KO | with bookmakers | gap | cost | guaranteed profit | status | P&L |
|---|---|---|---|---|---|---|---|---|---|
| 104 | 11-17T01:46 | PHX at DEN | 13.4 | draftkings | 0.21% | $2499.99 | $5.21 | open |  |
| 103 | 11-17T01:31 | PHX at DEN | 28.4 | draftkings | 0.21% | $1347.16 | $2.80 | open |  |
| 102 | 11-16T23:56 | ORL at BOS | 3.2 | mybookieag | 0.40% | $2500.00 | $10.09 | open |  |
| 101 | 11-16T23:19 | ORL at BOS | 40.2 | no | 1.05% | $214.01 | $1.99 | open |  |
| 100 | 11-16T23:14 | ORL at BOS | 45.3 | no | 1.05% | $15.84 | $0.16 | open |  |
| 99 | 11-16T23:13 | ORL at BOS | 46.8 | no | 1.05% | $19.80 | $0.20 | open |  |
| 98 | 11-16T22:26 | MEM at WAS | 93.8 | no | 0.85% | $6.95 | $0.04 | open |  |
| 97 | 11-16T01:16 | PIT at CIN | 3.2 | betrivers, bovada | 0.54% | $2499.98 | $12.86 | settled | $+13.60 |
| 96 | 11-15T23:02 | VAN at VGK | 177.9 | betmgm | 0.40% | $117.84 | $0.47 | settled | $+0.47 |
| 95 | 11-15T21:17 | DAL at BOS | 102.4 | no | 1.06% | $380.95 | $4.04 | settled | $+4.05 |
| 94 | 11-15T21:12 | SAS at UTA | 47.4 | no | 0.85% | $1936.85 | $16.15 | settled | $+16.48 |
| 93 | 11-15T18:33 | SF at DAL | 171.4 | no | 1.78% | $4.91 | $0.09 | settled | $+0.09 |
| 92 | 11-15T18:07 | SEA at LV | 178.0 | mybookieag | 0.25% | $2499.99 | $6.27 | settled | $+6.28 |
| 91 | 11-15T17:51 | MIA at IND | 8.8 | no | 0.58% | $26.96 | $0.04 | settled | $+0.18 |
| 90 | 11-15T17:17 | MIN at GB | 42.8 | no | 0.84% | $36.90 | $0.10 | settled | $+1.10 |
| 89 | 11-15T16:50 | CAR at NO | 69.8 | no | 0.37% | $31.90 | $0.10 | settled | $+0.10 |
| 88 | 11-14T23:56 | DET at TB | 3.2 | betrivers, lowvig | 0.34% | $2499.99 | $8.59 | settled | $+8.61 |
| 87 | 11-12T02:26 | UTA at VGK | 3.5 | betrivers, lowvig | 1.36% | $2499.99 | $33.98 | settled | $+33.98 |
| 86 | 11-12T02:16 | UTA at VGK | 13.5 | betrivers, fanduel | 0.89% | $2499.99 | $22.11 | settled | $+22.11 |
| 85 | 11-11T01:01 | MIA at UTA | 58.4 | mybookieag | 4.63% | $83.14 | $3.84 | settled | $+3.86 |
| 84 | 11-11T00:00 | MIL at NYK | 29.9 | no | 0.70% | $4.97 | $0.03 | settled | $+0.03 |
| 83 | 11-10T23:59 | MIL at NYK | 30.9 | no | 0.70% | $4.97 | $0.03 | settled | $+0.03 |
| 82 | 11-10T22:00 | MIL at NYK | 149.4 | no | 0.23% | $43.93 | $0.07 | settled | $+0.07 |
| 81 | 11-10T01:13 | BUF at MIN | 1.4 | no | 0.30% | $19.94 | $0.06 | settled | $+0.06 |
| 80 | 11-10T00:42 | BUF at MIN | 32.3 | no | 1.69% | $10.45 | $0.17 | settled | $+0.18 |
