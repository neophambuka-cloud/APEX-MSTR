# MSTR three-hypothesis research plan

All hypotheses are unproven. Do not optimise on the final test period. Compare against a no-trade baseline and friction-aware buy-and-hold/naive benchmark where appropriate.

## H1 BTC leads MSTR
- Collect synchronized BTC USD and NASDAQ MSTR midpoint/trade data at 1m/5m intervals, with MSTR US session labels.
- Define pre-specified BTC shocks, MSTR residual return vs fitted market/Bitcoin beta, future horizons 1/5/15/60 minutes.
- Measure lag correlations, conditional directional accuracy, net tradable P&L, regime and session stability. Use embargoed walk-forward splits, transaction costs and realistic latency.
- Reject if effect vanishes out of sample, in closing auctions, under fees, or after controlling market beta.

## H2 MSTR perp positioning extremes
- Collect VALR MSTR perp mark, index, bid/ask, funding, OI, provider state, and actual MSTR price with trading-session flag.
- Measure basis and funding percentile only against comparable active-session observations.
- Test mean reversion and trend continuation separately; no inference during stale equity sessions without explicit market-halt model.
- Reject if predictive power disappears after funding, spread, adverse selection, liquidation risk and venue/provider costs.

## H3 cross-market dislocation
- Align BTC/MSTR equity/MSTR perp reference prices; model fair-value range rather than naive equality.
- Record event windows: equity open, close, weekend, earnings, Strategy issuance/repurchases, BTC shocks.
- Simulate executable IOC fills and slippage using observed depth; avoid look-ahead and stale equity references.
- Reject if divergence cannot be monetized with permitted instruments or is dominated by risk/financing.

## Reporting contract
For each experiment record: thesis, dataset coverage, missingness, selection rules, train/validation/test dates,
model version, parameters frozen before test, gross and net P&L, volatility, max drawdown,
expected shortfall, fees, funding, turnover, turnover-adjusted edge, exposure, uncertainty,
regime breakdown, leakage audit, and explicit disconfirmation.
Never claim an edge from one visually compelling chart.
