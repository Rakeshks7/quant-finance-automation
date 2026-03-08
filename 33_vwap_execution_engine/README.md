# VWAP Engine (Execution Algo)

A smart execution algorithm that slices large orders based on the market's historical **Volume Profile**. Unlike TWAP (which slices evenly), VWAP slices *proportionally*.

## Workflow Logic

1. **Input:** "Buy 10,000 shares of ITC".
2. **Context:** Fetches the historical volume curve for ITC.

   * *Insight:* Markets typically form a "U-Curve" (High volume at Open/Close, Low volume at Lunch).

3. **Slicing (Math):**

   * **9:15-9:30 (15% Vol):** Buy 1,500 shares.
   * **12:00-12:30 (5% Vol):** Buy 500 shares.

4. **Execution:** Submits the child orders at the start of each time bucket.

## Why this is Pro

If you execute a large order during lunch (low liquidity), you will move the price significantly (Slippage). VWAP avoids this by executing heavily only when liquidity is high.

