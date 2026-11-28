# APEX-MSTR — instructions for Codex

Objective: Build a direction-agnostic MSTR-specialist predator: seek positive net expected returns in rising, falling, and sideways BTC/MSTR markets using the most appropriate validated exposure, or abstain. Apex observes more than it trades; no trade is preferable to a weak trade.

## Apex mandate is independent
- Do NOT impose Endurance's permanent-Bitcoin ownership thesis, long-only preferences, or investment doctrines on Apex signal selection. Apex is a standalone, tactical trading research system.
- Evaluate long, short and flat MSTR exposure symmetrically. MSTR perpetual funding is an execution cost or benefit; STRC token accumulation and crypto borrowing arbitrage are outside Apex's mandate.
- A scenario payoff table is NOT evidence of historical profitability or a predictive edge. Use time-specific MSTR/market data, fees and funding before claiming actual profits.
- "Profit whichever way markets move" is a research objective, not a guarantee. Avoid reversal chasing, overtrading, and an assumption that Apex can foresee regime changes.
- Maintain independent hard risk controls, fees, liquidation and venue safeguards; profit seeking cannot override insolvency prevention.

## Standing engineering constraints
- Work bottom-up. Preserve existing architecture and report conflicts before changing it.
- Read-only by default. All real trading, margin borrowing, key provisioning, withdrawals and leverage are explicitly OUT OF SCOPE until separately authorised.
- Never store API keys/secrets in git, logs, issues or example files.
- Do not invent or hardcode exchange instrument IDs, fees, liquidation thresholds, dividend entitlements, trading hours or API response shapes. Discover, verify and record sources.
- HARD SCOPE WALL: STRC, STRCx, lending arbitrage, token accumulation and borrowed-BTC carry are separate research only. Do not add their data collection, signals, balances, accounting, dependencies, test fixtures or execution logic to Apex. Existing docs/STRC_CARRY_RESEARCH.md is archival context, not an Apex work item.
- Use UTC timestamps and record data source, timestamp, market session, unit, quote currency and staleness for every observation.
- Models must fail closed on missing data, stale data, inconsistent positions, unknown fee schedule or unavailable market.
- Risk controls exist outside signal models; signal models cannot disable their own risk checks.
- Prefer typed, testable Python components, fixtures, deterministic replay and offline validation over an overbuilt distributed system.
- Hypotheses require pre-registered tests, walk-forward out-of-sample evaluation, trading-friction modelling and disconfirming conditions.
- Keep outside financing research in a separate future repository or independent research project, with no Apex dependency.
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

## Mandatory quality gates
- Follow docs/EXECUTION_PLAN.md in gate order. Complete each gate with evidence, tests, PASS/FAIL and exactly one next step.
- Follow docs/REASONING_QA.md and docs/REVIEW_PROTOCOL.md before any report, chart, strategy assessment, or PR. Require blue-team functional tests, independent red-team adversarial tests and a separately recorded Claude review prior to promotion. Never claim Claude reviewed until its actual report is attached.

## Evidence-first safety invariant (mandatory)
- Apex's design cannot rely on plausible explanations or unverified exchange behavior. Every execution-critical claim requires a traceable primary source, independently reproducible observation or account/exchange event log, timestamp and a named test.
- Documentation establishes intended behavior; test vectors, recorded API responses, reconciliation and operational drills establish observed behavior. If not independently observed, mark UNVERIFIED and prohibit that capability from live deployment.
- Before any live MSTR order workflow, demonstrate idempotent order placement, rejected/time-out order reconciliation, partial fills, funding and fee posting, margin and liquidation monitoring, venue failures, reconnection, and emergency safe-state procedures.
- Confirm shutdown behavior for existing positions separately from the no-new-trades gate. Never assume loss of connectivity safely closes exposure.
- Red team, blue team and an actual independent Claude review require evidence artifacts. Reviewer agreement does not override a failed test or unknown critical exchange behavior.

## Avoid analysis paralysis — minimum viable live discovery
- Do not insist on perfect models, exhaustive history or completed advanced strategy architecture before an explicitly authorised, minuscule, supervised *mechanical* MSTR execution test. Follow G2.5 in docs/EXECUTION_PLAN.md.
- Distinguish mechanical exchange verification from proving a trading edge. Early live results are observations; don't promote them to evidence of sustainable profitability.
- Non-negotiable prerequisites are instrument/API availability, maximum possible loss boundary, tested reconciliation and exit/contingency behaviour, explicit user budget and approval, and critical-control red/blue/Claude review. No approval is implied by this instruction.
- Defer optimisations, dashboards, extensive indicators and non-critical features. Build the smallest working system and improve from real, reconciled observations.
