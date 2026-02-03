#  Dynamic Universe Selection

A quantitative filtering pipeline that runs monthly to define the "Tradable Universe" for all downstream strategies. It ensures that algorithms only interact with liquid, high-quality assets.

## Workflow Logic
1.  **Trigger:** Scheduled for the 1st of every month.
2.  **Input:** Fetches the entire market (simulated 5000+ tickers) via API.
3.  **Filtering (Python):** Applies liquidity and size constraints to remove "junk" stocks.
    * **Rule 1:** Market Cap > $2 Billion.
    * **Rule 2:** Avg Daily Volume (30d) > 1 Million.
    * **Rule 3:** Price > $5 (Avoid Penny Stocks).
4.  **Persistence:**
    * Truncates the SQL table `active_universe`.
    * Inserts the new list of approved tickers.

## Why this is critical
Running complex backtests on illiquid stocks leads to "Slippage" errors. By filtering the universe first, we ensure that our backtest results match reality.