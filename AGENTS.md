# APEX-MSTR — instructions for Codex

Objective: Build an MSTR-specialist market intelligence and selective execution system. Apex observes more than it trades; no trade is preferable to a weak trade.

## Standing engineering constraints
- Work bottom-up. Preserve existing architecture and report conflicts before changing it.
- Read-only by default. All real trading, margin borrowing, key provisioning, withdrawals and leverage are explicitly OUT OF SCOPE until separately authorised.
- Never store API keys/secrets in git, logs, issues or example files.
- Do not invent or hardcode exchange instrument IDs, fees, liquidation thresholds, dividend entitlements, trading hours or API response shapes. Discover, verify and record sources.
- For STRC token carry, model the practical route: tokens held -> issuer/venue token credits or rebases (if actually observed) -> sell credited tokens -> convert to ZAR -> repay financing -> measure net proceeds. Cash dividends are NOT a prerequisite for research. Verify token credits and market execution via records without turning legal terminology into an implementation bottleneck. Distinguish product types only where it changes the actual numbers.
- Use UTC timestamps and record data source, timestamp, market session, unit, quote currency and staleness for every observation.
- Models must fail closed on missing data, stale data, inconsistent positions, unknown fee schedule or unavailable market.
- Risk controls exist outside signal models; signal models cannot disable their own risk checks.
- Prefer typed, testable Python components, fixtures, deterministic replay and offline validation over an overbuilt distributed system.
- Hypotheses require pre-registered tests, walk-forward out-of-sample evaluation, trading-friction modelling and disconfirming conditions.
- Borrowing and STRC carry research belongs in a separate research module and may NOT control Apex live execution.
- Never modify real accounts or trade from tests; network mocks are mandatory in CI.

## Immediate implementation order
1. Inspect current project files; preserve prior code.
2. Implement market event schema, time synchronisation, durable event log and data quality checks.
3. Implement read-only VALR instrument discovery, MSTR perps funding/mark/depth and BTC markets adapters; verify API paths against live published documentation before use.
4. Implement isolated risk governor and frozen config (no live orders).
5. Build replay/backtest with maker/taker fees, slippage, funding, FX, gaps and partial fill assumptions.
6. Implement three research hypotheses described in docs/HYPOTHESES.md and produce reproducible rejection/acceptance reports.
7. Only after evidence gates pass, propose a separately reviewed paper execution harness; no live trading by default.

## Pull request acceptance
Every PR must state what is verified, assumed, unverified and intentionally excluded; include tests and a rollback path. Never assert profitability from an untested spread.
