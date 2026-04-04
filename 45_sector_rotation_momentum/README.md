# Sector Rotation (Dual Momentum)

A systematic trend-following strategy that moves capital into the strongest performing sectors of the economy.

## The Logic: Dual Momentum

We don't just ask "Is Auto up?" (Absolute Momentum). We ask "Is Auto up *more than* IT?" (Relative Momentum).

## Calculation

1. **Long-Term Trend (120 Days):** Determines the major direction. Weighted 70%.
2. **Short-Term Trend (20 Days):** Determines the immediate velocity. Weighted 30%.
3. **Ranking:**

   * **Pharma:** +25 Score
   * **Auto:** +15 Score
   * **IT:** -5 Score
   * **Metal:** -12 Score
4. **Action:** The algorithm outputs a signal to **Overweight Pharma \& Auto** and **Underweight IT \& Metal**.

