#  Smart Order Slicing (TWAP Execution)

An institutional-grade execution algorithm designed to minimize "Market Impact" and slippage. It takes a large Parent Order and slices it into smaller Child Orders distributed evenly over time.

## Workflow Logic
1.  **Trigger:** Webhook receives a Parent Order (e.g., "Buy 1000 AAPL over 60 minutes").
2.  **Calculation:** The Code Node calculates the optimal slice size and delay interval.
    * *Example:* 1000 shares / 10 slices = 100 shares per slice every 6 minutes.
3.  **Loop Execution:** n8n's `SplitInBatches` node iterates through the list.
4.  **Timing:** The `Wait` node pauses execution between slices to ensure the time-weighting is respected.
5.  **Output:** Submits 10 separate limit orders to the Broker API.

## Why this is valuable
If you try to buy 10,000 shares of a small-cap stock instantly, you will push the price up by 2-3% (Slippage). TWAP prevents this by "hiding" your volume.