# APEX — reasoning and evidence QA protocol

This protocol is mandatory for analysis reports, simulations, Codex PRs and strategy proposals.

## Five checks before presenting a result
1. SCOPE: Is this about Apex trading or Endurance asset ownership? Do not import long-term BTC ownership thesis into Apex unless asked.
2. PAYOFF SYMMETRY: For any directional trade show both favourable AND unfavourable price changes plus unchanged baseline; direction-neutral or "sideways" also. Show at least +/-10%, +/-30%, +/-50% where sensible. Identify nonlinear liquidation and margin events, not just endpoint P&L.
3. CASH REALISATION: Distinguish yield headline, accrued STRC token units, actual credited quantities, executable bid, ZAR conversion and repayable borrowing currency. Dividends-in-cash are not needed if tokens can be sold; don't confuse nominal accrual with realised profit.
4. EVIDENCE: Label every material figure VERIFIED (source and timestamp), DERIVED (formula and inputs), ASSUMED (scenario) or UNKNOWN (one validation task). Hypothetical positive P&L is not a historical actual kill.
5. ARITHMETIC: Compute displayed scenario tables and charts from ONE calculation function, test spot cases and assert table/chart values agree. Include borrowing origination fee, compounding convention, price changes, funding and FX, and account for drawdown and liquidation *along the path*, not only final price.

## Practical proportionality
A qualification is a BLOCKER only if it prevents a specific next operation or causes unbounded risk. Otherwise, make it a measured input and continue unrelated work. Prioritise decision-changing facts, not long legal caveats or speculative architecture. Do not turn Apex into multiple bots.

## Example unit test for historical scenario consistency
Borrow 1 BTC at $10,000, earn $1,200 realised STRC token accrual, 1.37% APR simple 1y, 0.5% upfront fee, end debt 1.0187 BTC:
P&L($) = 11200 - 10187 * (1 + BTC_return)
-50% +6106.50; -30% +4069.10; flat +1013.00; +30% -2043.10; +50% -4080.50.
If a generated chart/table differs from these exact values, FAIL the report.
These are illustrative ENDPOINT values, not proof of achievable results, executable returns, or absence of midperiod liquidation.

## Independent red-team review
Before accepting a new strategy, an independent adversarial test must try to defeat it via timestamp leakage, stale MSTR market price, incorrectly signed funding, unseen accrued interest, fee double counting, unfilled IOC orders, illiquid STRCx credits, BTC repricing, collateral haircuts, a market gap, API outage and adverse financing-rate change.
A hypothesis passes only when it survives pre-defined evidence gates. No change of gate after looking at test output without marking that result exploratory.
