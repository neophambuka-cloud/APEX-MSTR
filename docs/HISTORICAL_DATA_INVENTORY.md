# APEX historical data inventory — researched 2026-11-27

## Data sources found and verification level

| Series | Evidence | Access / constraints |
|---|---|---|
| BTC/USD 2026 monthly | StatMuse monthly 2026 historical table: January open 87508.05; Jan close 78621.12; Oct close 77434.75; November close 60494.71 (Nov partial month, verify observation timestamp). | https://www.statmuse.com/money/ask/bitcoin-price-monthly-in-2026 ; daily series required |
| MSTR NASDAQ daily OHLCV | 2026-01-02 close $157.16; 2026-11-25 close $79.96 in indexed sources. | https://nz.finance.yahoo.com/quote/MSTR/history/ ; https://www.stockquote.io/stocks/MSTR/history ; cross-check adjustments |
| STRC underlying preferred | historical OHLCV & corporate actions. Nov 25 2026 close $98.04 reported by multiple providers. | https://finance.yahoo.com/quote/STRC/history/ ; https://www.strategy.com/strc/learn |
| STRCx issuer | Backed product ISIN CH1500008482; underlying ISIN US5949728530; instrument is a tokenized certificate. | https://assets.backed.fi/products/strategy-pp-variable-xstock |
| STRCx daily token ratio | On-chain multiplier tracker: Nov21 1.10542->1.10577; Nov24 1.10577->1.10623; Nov25 1.10623->1.1069. Independent indexer infers type from multiplier; confirm actual historical daily ratio and account credits. | https://warenciaga.com/token/STRCx ; on-chain and Backed API must be cross-checked |
| VALR borrow-rate history | Public changelog documents /v1/loans/rates/history and /v1/loans/rates/history/average; includeBorrowRates=true added Oct13 2026 to obtain averageBorrowerRate; authenticate/confirm rate coverage before reconstructing. | https://support.valr.com/hc/en-us/articles/360014153500-Changelog-for-VALR-API ; https://docs.valr.com |
| MSTR perp xyz funding | Ironflow tracks hourly xyz:MSTR settlements; 30d average 0.0006%/h in Nov 26 snapshot, extremes +0.0918% (Nov15) and -0.0904% (Nov21); requires full series for rigorous test. | https://ironflow.sh/markets/xyz-mstr/funding-rate ; https://api.ironflow.sh/v1/funding?market=xyz:MSTR-PERP&order=desc&limit=24 |
| VALR perp execution + rules | Official API documented perps pairs/market-summary/orderbook/trade-history/funding-history and margin liquidation transaction codes. | https://support.valr.com/hc/en-us/articles/360014153500-Changelog-for-VALR-API |

## Interpretation
- BTC price decline in 2026 makes short-BTC financing exposure potentially favorable IN RETROSPECT, but cannot prove Apex would have entered, remained collateralized, and sold STRCx token credits at realistic bids.
- 2026-01-02 to 2026-11-25 MSTR close fell from $157.16 to $79.96 (approx -49.12%); a hypothetical short held through that interval would have benefited from direction, but perp trading availability, funding, margin, fills, borrow/locate, leverage and forced liquidation must be independently reconstructed.
- STRCx rebasing is a working numeric phenomenon, not a reason to block research because no cash dividends are distributed. Apply the issuer ratio and actual VENUE wallet credited quantity; do not double count ratio changes and nominal token price.
- Nov 2026 MSTR perp funding is sign-variable and sometimes extreme; do not treat headline 30d average as actual experienced funding for a chosen entry/exit.

## Required reproducible historical ledger
timestamp_utc, source, instrument, product_type, price_open/high/low/close, bid_ask, quote_currency, market_session,
borrow_apr, currency_borrowed, origination_fee, BTCUSD, USDZAR, token_multiplier, STRCx_credited_quantity,
STRCx_bid, perp_mark, perp_index, funding_settlement, open_interest, exchange_trading_fee,
execution_cost, collateral_amount/currency, collateral_weight, margin_threshold, trade_fill,
realized_pnl, data_missing_flag.

For each source tag observed/derived/assumed/unavailable; cache exact source response and retrieval timestamp. Do not invent historical hourly borrow APR or historical VALR token wallet credits that public data does not show.

## First tests
A. 2026 BTC short-financing + STRCx long, compare monthly entry timestamps and full +30/-30 BTC exit sensitivities, with lender-rate history and interest/hour if available.
B. MSTR equity buy/hold vs paper short, Feb/Nov micro-regime, funding-adjusted xyz:MSTR perp strategy only from actual listing date.
C. Token multiplier accrual vs executable STRCx bid and round-trip conversion to ZAR; split valuation from cash-flow, and measure collateral survivability throughout the whole route.

Status: source discovery complete; data extraction/backtest INCOMPLETE. No actual 2026 trading performance claim authorised.
