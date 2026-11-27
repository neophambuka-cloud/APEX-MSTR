# STRC carry research — NOT an executable trade plan

## Primary constraint
STRC's 12% rate is a variable annualized dividend rate on $100 stated value, not a guaranteed yield on market cost. It may change; a holder must be entitled to actual cash distributions. VALR xStocks token holders do NOT have guaranteed dividend rights or even guaranteed issuer rebase benefits. Verify whether STRC is actually available on VALR, as what exact product, and document issuer corporate-action policy before using a yield assumption.

## Observed indications (screenshots 2026-11-27)
Estimated variable VALR borrow rates: BTC 1.37%; ETH 0.62%; USDT 11.14%; USDC 12.71%. These are not fixed funding quotes, and exclude the VALR 0.5% upfront borrowing fee and execution costs.

## Core model — borrowed asset B, share cashflows USD
Let N_B = quantity borrowed; P_BUSD(t) = USD price of borrowed asset; r_B(t) = variable interest; F_B = origination fees in B; D_USD(t) = cash distributions actually received on owned eligible STRC shares after withholding/tax; P_STRC(t) = share price; C(t) = all conversion, brokerage, custody, hedge and financing costs.

Final USD profit = market value of STRC + cumulative dividends + residual cash
                   - value of B liability (principal + accrued interest + fees)
                   - all other costs - initial invested capital (properly financed).

If borrow BTC/ETH and immediately sell to USD for STRC, the liability is short BTC/ETH. BTC/ETH appreciation can swamp the 12% distribution. A hedge is not free: its basis/funding/counterparty collateral and liquidation risk must be modelled. If borrow USDT/USDC directly, screenshot rates are near or above STRC headline dividend before fees.

## Minimum gating checks
1. Obtain exact STRC instrument on VALR and whether it is an actual share, xStock, derivative or not listed.
2. Verify transferable asset/withdrawal path to brokerage where STRC cash distributions legally accrue.
3. Collect actual borrowing APR history, borrowing currency, hourly auction regime, origination fees, minimums, fees on repayment, compulsory liquidation triggers and collateral weights.
4. Model 24+ month downside: BTC +100% vs USD while STRC price -20%; dividend rate reduced; funding APR spikes; collateral haircut changes; FX and exchange interruptions.
5. Calculate after-tax USD and ZAR returns, maximum cash deficit and survival without selling permanent BTC.
6. Compare alternatives: unsecured asset-level debt, direct USD finance, unlevered STRC, reserve-funded deployment, and fixed-rate borrowing.
Decision threshold: no deployment unless verified after-cost risk-adjusted benefit is positive AND stress-case solvency survives; otherwise do nothing.

Sources:
https://www.strategy.com/strc/learn
https://support.valr.com/hc/en-us/articles/21439426222492-What-are-xStocks
https://support.valr.com/hc/en-us/articles/21462249717276-VALR-Tokenised-Stocks-Terms-of-Service
https://support.valr.com/hc/en-us/articles/360015777451-What-are-VALR-s-charges
