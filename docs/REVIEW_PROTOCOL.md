# APEX — blue team, red team and Claude review gate

## Strict scope
Apex trades only MSTR exposure through validated MSTR instruments (e.g., MSTR perps). BTC price is a market signal, not a separate trading strategy. STRC token accumulation, lending arbitrage and standalone crypto strategies are excluded from Apex engineering, tests and deployment. Separate investigations may be maintained in an independent research project and must never gate Apex progress.

## Cycle for every engineering gate / material strategy change
1. BLUE TEAM (Codex implementer): Specify required behavior, configuration, test fixtures, deterministic unit/integration tests, data provenance, P&L reconciliation and rollback. Run tests and produce a signed or commit-linked evidence report. Explicitly tag VERIFIED / DERIVED / ASSUMED / UNKNOWN. Do not claim "passed" without test output.
2. RED TEAM (independent adversarial pass): Challenge data leakage, session mismatch, stale prices, fabricated fills, wrong funding signs, leverage and margin checks, race conditions, WebSocket disconnect, duplicate events, rate limits, missing fee data, spot/perp mismatch, invalid credentials, liquidation, disconnect under exposure and bypass of kill-switch. Produce reproduction steps, severity, evidence and regression tests for all critical/high issues.
3. CLAUDE (external independent critic): Provide a sanitized package of requirements, changed-file diff, architecture, fixture data, unit/integration results, blue-team report and red-team findings. Ask Claude to look for contradictory assumptions, hidden scope expansion, inaccurate API use, financial calculation mistakes, leakage, weak acceptance tests and unexamined failure modes. Capture Claude's actual output in an attached review report; do not mark review complete simply because a prompt was prepared. Never provide credentials, account secrets or private identifying information.
4. RECONCILIATION (Codex implementer): Triage each finding as FIX / ACCEPT WITH EVIDENCE / REJECT WITH REASONS. Add test regressions for material corrections. Re-run the full test suite and issue final disposition.
5. GATE DECISION (owner): Critical/high unmitigated findings block promotion. Low-impact or unrelated findings become backlog items, never fabricated blockers. A gate can move forward only with test proof + red team result + actual Claude report + resolved critical items. Final live trading always requires separate user authorization.

## Review report template
- Gate / commit / scope:
- Blue-team tests run, command, exit status and artifacts:
- Red-team attack cases, outcomes, severity, reproductions:
- Claude review date / actual report attachment:
- Findings resolution with code/test references:
- Calculations checked and exact source inputs:
- Outstanding uncertainties / why safe to proceed or why blocked:
- Verdict PASS / FAIL / NOT REVIEWED:
- Single next operation:

## Claude handoff prompt
Review this Apex-MSTR pull request as a technically and financially adversarial independent reviewer. The mandate is a direction-agnostic MSTR specialist ONLY; BTC is a reference signal, not a traded strategy. STRC and borrowing arbitrage are OUT OF SCOPE. Read the attached diff and specs, reproduce or challenge the tests and financial assumptions, find critical failures or overengineering, then rank findings by severity with exact file/line, evidence, minimal correction and a disconfirming test. Do not invent API facts, execution success or historical returns. Separate VERIFIED, ASSUMED and UNKNOWN. Conclude PASS/FAIL/NEEDS EVIDENCE. Treat a claim of another review as unverified until its report is supplied.
