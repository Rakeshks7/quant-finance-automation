# &nbsp;Portfolio VaR (Value at Risk) Calculator

A quantitative risk engine that computes the daily Value at Risk (VaR) using the Variance-Covariance method. It provides a single metric to summarize the total downside exposure of the fund.

## Workflow Logic

1. **Trigger:** Runs daily at Market Close.
2. **Input:** Fetches current Portfolio Weights and the Correlation Matrix of the assets.

   * *Note:* Correlation is key. If assets are perfectly correlated, risk is additive. If uncorrelated, risk is diversified.

3. **Math Engine (Python):**

   * Computes **Portfolio Variance** ($\\sigma\_p^2$) using matrix algebra.
   * $\\text{VaR} = \\text{Portfolio Value} \\times 1.65 \\times \\sigma\_p$ (for 95% confidence).

4. **Output:**

   * "We are 95% confident we won't lose more than ₹20,000 tomorrow."
   * Alerts the Risk Manager if VaR exceeds 2% of equity.

## Why this is critical

Regulators and Investors demand this metric. It proves you understand that risk isn't just about what stocks you own, but how they interact with each other.

