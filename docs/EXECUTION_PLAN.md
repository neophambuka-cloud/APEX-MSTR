# APEX — execution plan and gates (2026-11-27)

Mandate: direction-agnostic MSTR/BTC specialist. Investigate STRC token-carry and financing as additional independent research strategies. No market direction is privileged.

## Gated sequence
G0 Repository integrity: inventory pre-existing files; tests, README/commands, secrets scan, reproducible environment. PASS only if isolated read-only tests work and existing behaviour is preserved.
G1 Observation: verified VALR instrument IDs/data availability; BTC/USD, MSTR equity, MSTR perp, STRC token/accrual/borrowing rates; timestamped append-only record, time sync, dedup, gap handling, session flag. PASS only on replay and disconnected-feed tests, quality metrics and explicit data coverage report.
G2 Accounting: reconcile spot/perp/loan movements, STRC token units, fees, conversions, interest, funding, collateral, LTV vs margin, P&L in USD/ZAR; use precise decimal quantities. PASS on deterministic fixtures incl. 101-satoshi loan, opposing price moves, and liquidation cases, with independently checked balances.
G3 Historical tests: pre-register H1 BTC->MSTR lead-lag, H2 perp funding/basis, H3 dislocations, H4 STRCx token accrual + borrowed BTC/ETH/stablecoin financing. Use true instrument listing dates and only data that existed at each hypothetical decision time. PASS if out-of-sample, fee-inclusive and liquidation-aware studies produce trustworthy acceptance/rejection reports; profitability is not presumed.
G4 Judge: rank qualified opportunities by estimated net expectancy, liquidity, downside, uncertainty, survival; no-trade option. PASS if risk governor cannot be bypassed and decisions are reproducible.
G5 Paper hunt: live-read-only observations + paper order state machine with IOC/partial fills/errors, realistic latency; forward evidence. PASS against pre-agreed prospective metrics, not cherry-picked backtests.
G6 Limited live: a fresh explicit approval, minimal permissions, capital ceiling, kill switch and audited exchange reconciliation. No automatic activation.

## Immediate Codex work order
1. Inventory the repository and run existing tests; show baseline findings.
2. Complete G0; implement G1 public read-only connector + event ledger with fixtures, timeout/retry, stale-feed stop.
3. Verify actual VALR MSTR perp and STRC availability and mechanics; unknown access does not stop work on BTC/MSTR public data.
4. Open PR with tested code, concise proof of success and one next task.
No real API keys, borrowing, deposits, or trading.

## User inputs — only when needed
NOW: none to begin read-only public work. To run Codex, select repository neophambuka-cloud/APEX-MSTR and branch codex/apex-foundation-2026-11.
LATER, when verified public records insufficient: export of VALR loan interest/transactions, STRC credited token balances, actual trading fills; redacted, no keys or passwords.
LATER, at live activation: explicit maximum risk budget, permitted instruments, deployment approval and least-privilege credentials via secrets manager, never chat/GitHub.

## Definition of done for every gate
Evidence/artifact, executed tests, failure behaviour, known uncertainties, decision PASS/FAIL, and precisely one recommended next operation. If FAIL, repair only failed prerequisite. No new scope by default.
