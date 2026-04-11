# Volatility Targeting (Vol Control)

A sophisticated risk management technique that sizes positions based on market turbulence.

## The Logic

* **High Volatility = Lower Size:** If the market is moving 2% a day, you hold less.
* **Low Volatility = Higher Size:** If the market is moving 0.5% a day, you hold more (leveraged) to make returns meaningful.

## The Formula

$$Leverage\_{Target} = \\frac{Vol\_{Target}}{Vol\_{Realized}}$$

* **Scenario:** Target is 12%. Current Market Vol is 24% (Crash Mode).
* **Result:** $12/24 = 0.5x$.
* **Action:** The algorithm forces you to sell 50% of your holdings to cash. This prevents Blowups during market crashes.

