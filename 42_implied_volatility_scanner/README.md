# Implied Volatility Scanner (Newton-Raphson)

A quantitative tool that reverse-engineers the Black-Scholes pricing model to find the market's Implied Volatility (IV).

## Required Files
* `workflow.json`: The logic pipeline.
* `market_params.json`: **Critical.** Contains the Risk-Free Rate ($r$) and Dividend Yield ($q$) inputs. Without these, the formula fails.

## The Math: Newton-Raphson
There is no simple equation to find Volatility ($\sigma$). We must use an iterative guess-and-check method:

$$\sigma_{n+1} = \sigma_n - \frac{C(\sigma_n) - C_{market}}{\nu(\sigma_n)}$$

* $C(\sigma_n)$: Theoretical Price using current guess.
* $C_{market}$: Actual Market Price.
* $\nu(\sigma_n)$: Vega (Derivative of Price w.r.t Volatility).

## Logic
1.  **Solve for IV:** If the ATM Option is trading at ₹180, the Solver finds that $\sigma = 16\%$.
2.  **Compare to HV:** The stock's Historical Volatility (30-day) is 12%.
3.  **Signal:** IV (16%) > HV (12%). Options are **Expensive**. Strategy: **Sell Volatility** (Short Straddle/Iron Condor).