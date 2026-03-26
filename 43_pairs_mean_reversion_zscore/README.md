# Pairs Mean Reversion (Z-Score)

A Statistical Arbitrage strategy that relies on the Mean Reverting nature of cointegrated pairs.

## The Math

We don't trade the raw price difference because ₹50 spread means nothing without context. Instead, we use the **Z-Score**:

$$Z = \\frac{\\text{Current Spread} - \\text{Rolling Mean}}{\\text{Rolling Std Dev}}$$

* **Mean ($\\mu$):** The "Normal" relationship.
* **Std Dev ($\\sigma$):** The volatility of that relationship.

## Logic

1. **Z > 2.0:** The spread is 2 Standard Deviations wider than normal (95% statistical anomaly).

   * **Action:** Short the Spread (Bet it will shrink).
2. **Z < -2.0:** The spread is 2 Standard Deviations tighter than normal.

   * **Action:** Long the Spread (Bet it will widen).
3. **Z = 0:** The spread has returned to normal.

   * **Action:** Close positions and take profit.

