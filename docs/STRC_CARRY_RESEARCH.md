# STRC token carry research — small, testable economics experiment

## Working route (no cash dividend required)
Borrow asset B -> sell/convert to STRC token -> accrue new tokens or receive rebase (verify actual credited quantity on VALR) -> sell new tokens when liquid -> convert proceeds to ZAR -> service loan -> track net gain/loss.

What matters is units accrued × achievable sell price, not whether distribution is legally called a dividend. Measure credited token quantities and executable ZAR conversion; do not make product terminology a bottleneck. Account history is the evidence gate for the exact STRC token accrual mechanism.

## Screenshot financing inputs (27 November 2026)
Estimated variable VALR borrowing rates: BTC 1.37%; ETH 0.62%; USDT 11.14%; USDC 12.71%. Annualized estimates, not locked borrowing terms. VALR origination fee observed in published schedule as 0.5%; verify actual rounding and fee impacts at tiny size.

## Full symmetric BTC-debt scenario
Borrow 1 BTC notionally worth $10,000; convert all proceeds to STRC, assume $1,200 realized value of additional credited tokens after 1 year, STRC original market value unchanged, 1.37% simple annual BTC interest, 0.5% BTC origination fee, no other costs. Debt at end: 1.0187 BTC.
```
Profit USD = 11,200 - 10,187 * (BTC_end_USD / BTC_start_USD)
BTC -50%: +6,106.50
BTC -30%: +4,069.10
BTC   0%: +1,013.00
BTC +30%: -2,043.10
BTC +50%: -4,080.50
Break-even BTC price appreciation: approximately 9.94%.
```
For this short-BTC liability structure, BTC falling can amplify profits while BTC rising can wipe out the yield spread. This is directional speculation plus a carry stream, not risk-free arbitrage.

## Compact executable test plan
1. Identify actual VALR STRC token symbol and record a pair of balances across a credited-token event, adjusted for trades; never assume credits exist until observed.
2. Calculate STRC yield as **credited tokens × executable bid price** rather than dividend label or advertised headline rate.
3. Build deterministic round-trip examples: borrow BTC/ETH/USDT, convert to token, accrue, sell tokens, convert proceeds to debt unit and ZAR, repay loan; every leg has spread, fee, latency and slippage.
4. Stress BTC/ETH both down and up by 10/30/50/100%, STRC price +/-20%, accrual curtailed, credit cost jumps, haircut and liquidation changes. Include BTC/ZAR and USD/ZAR exposures separately.
5. Compute net P&L and path-dependent liquidation risk under actual collateral composition. Separately compare with unlevered STRC token accumulation.
6. Never enable real borrowing, liquidation experiments or live execution through this research code. Unknown parameters become sensitivity intervals or documented validation tasks; they do not block MSTR market observation work.

Useful documentation:
https://www.strategy.com/strc/learn
https://support.valr.com/hc/en-us/articles/21439426222492-What-are-xStocks
https://support.valr.com/hc/en-us/articles/21462249717276-VALR-Tokenised-Stocks-Terms-of-Service
https://support.valr.com/hc/en-us/articles/360015777451-What-are-VALR-s-charges
