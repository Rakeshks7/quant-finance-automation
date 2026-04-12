# Trend Following (CTA Style)

A classic systematic strategy used by Commodity Trading Advisors (CTAs) to capture long-term market moves.

## The Logic

This strategy is based on **Absolute Momentum**.

* **Rule:** If Price > 200-Day EMA, the trend is UP. We Buy.
* **Rule:** If Price < 200-Day EMA, the trend is DOWN. We Sell (Short).
* **Philosophy:** Cut losses short, let winners run. We do not predict tops or bottoms; we simply ride the middle 60% of the move.

## Workflow

1. **Input:** Weekly Closing Prices for Nifty, Gold, Oil, etc.
2. **Calculation:** Compute the Exponential Moving Average (EMA) for the last 200 days.
3. **Output:** A binary signal (LONG/SHORT) that updates the central trading database.

