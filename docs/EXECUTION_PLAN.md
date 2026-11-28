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


## Early micro-funded hunt — operational discovery, not a claim of proven edge
A bounded live discovery stage G2.5 may follow G0-G2, *before* extensive historical model optimization and full G3-G5, if the exchange supports an eligible MSTR instrument with a position size below an explicitly authorised total-loss budget. This stage must not be described as production autonomy or validated profitable strategy.

Minimum non-negotiable gates:
1. Verify MSTR instrument, API access/order path, minimum order size, fees, funding if applicable, margin and liquidation/close rules, and venue trading availability with source evidence and small-scale read-only tests.
2. Demonstrate order intent -> acknowledgment -> fills/partial fills -> fees -> position/balance reconciliation, with safe handling of ambiguous responses, duplicate events and cancelled requests; test a safe manual exit procedure and loss-of-connectivity response.
3. User gives explicit bounded budget for **total possible loss including fees and any liabilities**, instrument, account isolation and specific live-test approval. Ensure no other assets are exposed. No withdrawals permission.
4. First live test is manually supervised, one position at a time, minimum supported notional and the smallest permitted effective leverage, with no auto-resizing, averaging down, martingale, recurring order loop or autonomous self-modification.
5. Observe, reconcile and record actual execution, costs, positions and exit. If exit/position state is ambiguous, halt new orders and perform verified account reconciliation. A kill switch blocks new submissions; it does not assume existing risk disappears.
6. Red, blue and Claude review should target only the micro-hunt critical controls before this stage, not demand completion of all future architecture. No critical unresolved defect may be accepted into a funded test. Document what is deliberately untested and keep exposure bounded accordingly.

After a successful **mechanical** micro-hunt, return to G3-G5 for evidence of strategy edge before any sustained or autonomous scale-up. A successful entry/exit confirms connectivity and process, NOT profitability or general safety. If feasible minimum position risks more than the user's cap, no funded trade.
