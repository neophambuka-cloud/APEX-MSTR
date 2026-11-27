# APEX — execution plan and gates (2026-11-27)

Mandate: direction-agnostic MSTR specialist ONLY. BTC is an explanatory market-data input, not an independently traded mandate. STRC token accrual and financing arbitrage are completely outside Apex. No market direction is privileged.

## Gated sequence
G0 Repository integrity: inventory pre-existing files; tests, README/commands, secrets scan, reproducible environment. PASS only if isolated read-only tests work and existing behaviour is preserved.
G1 Observation: verified VALR MSTR perp instrument and data availability; MSTR equity and BTC/USD as a predictive reference; timestamped append-only record, time sync, dedup, gap handling, session flag. No STRC or lending feeds. PASS only on replay and disconnected-feed tests, quality metrics and explicit data coverage report.
G2 Accounting: reconcile MSTR perpetual/equity instrument exposure, executed trades, entry/exit fees, funding, margin, liquidation state, FX and net P&L. Use precise decimal quantities. PASS on deterministic fixtures for MSTR long, short, flat, adverse moves, partial fills and liquidation, with independently checked balances. No borrowing product implementation.
G3 Historical tests: pre-register H1 BTC->MSTR lead-lag, H2 MSTR perpetual funding/basis, H3 MSTR perp/equity dislocations. Use true instrument listing dates and only data available at each hypothetical decision time. PASS if out-of-sample, fee-inclusive and liquidation-aware studies produce trustworthy acceptance/rejection reports; profitability is not presumed.
G4 Judge: rank qualified opportunities by estimated net expectancy, liquidity, downside, uncertainty, survival; no-trade option. PASS if risk governor cannot be bypassed and decisions are reproducible.
G5 Paper hunt: live-read-only observations + paper order state machine with IOC/partial fills/errors, realistic latency; forward evidence. PASS against pre-agreed prospective metrics, not cherry-picked backtests.
G6 Limited live: a fresh explicit approval, minimal permissions, capital ceiling, kill switch and audited exchange reconciliation. No automatic activation.

## Immediate Codex work order
1. Inventory the repository and run existing tests; show baseline findings.
2. Complete G0; implement G1 public read-only connector + event ledger with fixtures, timeout/retry, stale-feed stop.
3. Verify actual VALR MSTR perpetual availability and mechanics. Do not investigate STRC as part of Apex.
4. Open PR with tested code, concise proof of success and one next task.
No real API keys, borrowing, deposits, or trading.

## User inputs — only when needed
NOW: none to begin read-only public work. To run Codex, select repository neophambuka-cloud/APEX-MSTR and branch codex/apex-foundation-2026-11.
LATER, when public data are insufficient: redacted VALR MSTR perpetual fills, funding and position exports, not unrelated BTC loans or STRC balances.
LATER, at live activation: explicit maximum risk budget, permitted instruments, deployment approval and least-privilege credentials via secrets manager, never chat/GitHub.

## External review requirement
Blue team proves intended behaviour using reproducible acceptance tests. Independent red team attempts to break assumptions, state transitions and risk protections. Claude reviews the same evidence as an external critic; record the actual report before declaring that review complete. A critical unresolved finding blocks promotion, not unrelated research. See docs/REVIEW_PROTOCOL.md.

## Definition of done for every gate
Evidence/artifact, executed tests, failure behaviour, known uncertainties, decision PASS/FAIL, and precisely one recommended next operation. If FAIL, repair only failed prerequisite. No new scope by default.
