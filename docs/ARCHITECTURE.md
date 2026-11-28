# APEX foundation / staged construction

## Mandate
MSTR is the sole trading target. Data sources can include US-listed MSTR, BTC price as a predictive input, MSTR perps on VALR, Strategy capital structure, market hours and news events. No STRC or crypto borrowing/accumulation strategies belong in this project. Execution is separately gated.

```
External sources -> normalised UTC event ledger -> quality gate -> feature builder
-> hypothesis scoring -> independent risk governor -> paper order simulator
-> trade reconciliation -> outcome research -> versioned model proposals
```

## Phases and evidence gates
- F0 inventory: inspect existing code and confirm exact VALR MSTR perps symbol, public API support, market-data rights and legal access.
- F1 observation: timestamped, deduplicated, persisted public data; reconnect/replay tests; stale feed triggers no trade.
- F2 economics: fee tables by instrument and timestamp, hourly funding, spread, slippage, FX, conversion, market-closed pricing and interest accrual. Negative-expectation configurations rejected.
- F3 hypotheses: walk-forward experiments on BTC lead/lag, perp basis/funding and MSTR dislocation; account for US market holidays, time-zone/DST, news gaps, multiple testing.
- F4 shadow execution: simulated IOC partial fills/rejections, stop slippage, exposure checks, kill switch; compare expected vs realised on delayed market replay.
- F5 live readiness only by separate written authorization, code review, capital limits and explicitly permissioned credentials.

## Minimal immutable event fields
event_id, source, source_event_id, timestamp_utc, received_utc, instrument_id, underlying,
product_type, base_currency, quote_currency, bid, ask, mark, index, last, size, funding_rate,
open_interest, session_state, raw_payload_hash, quality_flags.

## Invariants
- Distinguish underlying MSTR listed shares from MSTR perpetual derivatives, and USDC margin from equity exposure; BTC is observational data only.
- Perp price is not necessarily MSTR NASDAQ price; stale underlying prices during closure cannot be treated as arbitrage.
- Position reconciliations require source snapshots and historical fills. Borrowing interest and fees are liabilities.
- No strategy can override execution-risk protections. No automatic self-modification of deployed trading logic.
- Capital-preservation controls: data freshness, max leverage, max adverse gap, max spread, depth/impact, funding exposure, per-position max loss, daily loss, circuit breaker, venue halt and error budget.
- Margin and liquidation policies should be queried or versioned with provenance, not assumed from wallet LTV.
