#  Corporate Action Adjustment

A Data Hygiene workflow that prevents False Signals in backtesting. It monitors the market for Stock Splits and Dividends and automatically patches the historical price database.

## Workflow Logic
1.  **Trigger:** Daily at 6:00 AM.
2.  **Input:** Fetches Corporate Action Calendar (Splits/Dividends) effective today.
3.  **Calculation (Python):**
    * **Splits:** If Stock A splits 1:10 (Price goes from 1000 to 100), we multiply all historical `Close`, `Open`, `High`, `Low` by `0.1`.
    * **Dividends:** If Stock B pays a ₹5 dividend, we subtract ₹5 from all historical prices (Backward Adjustment) to maintain the Total Return continuity.
4.  **Action:** Runs `UPDATE` SQL queries on the Postgres database.

## Why this is critical
Without this, a 1:10 split looks like a 90% price crash. Any Stop Loss algorithm running on unadjusted data would instantly panic sell, causing a disaster.