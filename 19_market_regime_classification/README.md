#  Market Regime Classification

An automated "Traffic Controller" for the trading system. It determines the current state of the market (e.g., Bullish & Calm vs. Bearish & Volatile) and enables/disables specific strategies accordingly.

## Workflow Logic
1.  **Trigger:** Runs daily at 8:30 AM (Pre-Market).
2.  **Input:** Fetches Index Prices (NIFTY/SPX) and Volatility Index (VIX).
3.  **Classification (Python):**
    * **Trend Filter:** Compares Current Price vs. 200-Day SMA.
    * **Volatility Filter:** Checks VIX levels (<15 Low, >25 High).
4.  **Output:** Updates the `current_regime.json` file.
    * *Example Output:* `"BULL_LOW_VOL"`
5.  **Downstream Effect:** Other bots read this file. If the regime is `BEAR_HIGH_VOL`, the "Long Only" bots automatically go into sleep mode.

## Why this is critical
"A rising tide lifts all boats, but a storm sinks the small ones." Running a Bull strategy in a Bear market is the #1 reason for algo bankruptcy. This workflow prevents that.