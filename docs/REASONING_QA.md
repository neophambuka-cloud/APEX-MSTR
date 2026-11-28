# APEX — reasoning and evidence QA protocol

This protocol is mandatory for analysis reports, simulations, Codex PRs and strategy proposals.

## Five checks before presenting a result
1. SCOPE: Is this about Apex trading or Endurance asset ownership? Do not import long-term BTC ownership thesis into Apex unless asked.
2. PAYOFF SYMMETRY: For any directional trade show both favourable AND unfavourable price changes plus unchanged baseline; direction-neutral or "sideways" also. Show at least +/-10%, +/-30%, +/-50% where sensible. Identify nonlinear liquidation and margin events, not just endpoint P&L.
3. REALISED EXECUTION: Distinguish MSTR reference prices, perpetual marks, actual fills, funding paid/received, trading fees, collateral changes and net executable P&L. No STRC token-accrual logic in Apex.
4. EVIDENCE: Label every material figure VERIFIED (source and timestamp), DERIVED (formula and inputs), ASSUMED (scenario) or UNKNOWN (one validation task). Hypothetical positive P&L is not a historical actual kill.
5. ARITHMETIC: Compute displayed scenario tables and charts from ONE calculation function, test spot cases and assert table/chart values agree. Include borrowing origination fee, compounding convention, price changes, funding and FX, and account for drawdown and liquidation *along the path*, not only final price.

## Practical proportionality
A qualification is a BLOCKER only if it prevents a specific next operation or causes unbounded risk. Otherwise, make it a measured input and continue unrelated work. Prioritise decision-changing facts, not long legal caveats or speculative architecture. Do not turn Apex into multiple bots.

## Example unit test for historical scenario consistency
For an unleveraged $1,000 notional MSTR perpetual long with fees/funding set to zero: +10% underlying move = +$100, 0% = $0, -10% = -$100. For the symmetric short: +10% = -$100, 0% = $0, -10% = +$100. Assert calculated tables/figures reconcile. With leverage, test path-dependent liquidation independently; these are theoretical endpoint P&L, not executable results.

## Independent red-team review
Before accepting a new strategy, an independent adversarial test must try to defeat it via timestamp leakage, stale MSTR market price, incorrectly signed funding, incorrect funding accrual, fee double counting, unfilled IOC orders, manipulated market depth, BTC repricing, collateral haircuts, a market gap, API outage, and unexpected funding-rate changes.
A hypothesis passes only when it survives pre-defined evidence gates. No change of gate after looking at test output without marking that result exploratory.

## Evidence hierarchy for critical Apex claims
1. Verified recorded exchange/account behavior (timestamped raw event + independently reconciled result).
2. Published exchange specification corroborated by independent test or account record.
3. Official published documentation alone: SPECIFIED, NOT YET OPERATIONALLY VERIFIED.
4. Third-party observation: corroboration candidate, NOT execution proof.
5. Model inference or scenario: HYPOTHESIS, never executable fact.

For each critical claim, log: claim ID; instrument and account mode; exact source URL/API and observation timestamp; raw payload hash or immutable test fixture; independently checked interpretation; test name and PASS/FAIL; known exceptions; unresolved uncertainty; operational consequence. Missing critical evidence blocks that *capability*, not unrelated read-only development.

## Catastrophic latent-failure tests
- Exactly-once intended economic effect despite API request retries, lost acknowledgments, duplicated WebSocket updates and out-of-order fills.
- Risk governor receives delayed or inconsistent mark/index prices; does not open orders; existing positions are reconciled and handled per verified contingency protocol.
- Surprise account-side liquidation, position change, fees/funding and cancelled orders force a new account reconciliation before any new exposure.
- Stop-loss and market close are never presumed guaranteed fills. Test partial fills, gaps, provider halts and adverse liquidity.
- Every trade must reconcile intent, accepted exchange order, fills, fees, funding, open risk, and end balance. Unknown position state means no increase in exposure.
