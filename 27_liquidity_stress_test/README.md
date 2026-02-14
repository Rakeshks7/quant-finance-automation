#  Liquidity Stress Test

A pre-trade risk filter that prevents the algorithm from entering positions that are too large for the market to handle.

## The Logic: Participation Rate
* **Formula:** `Order Size / 30-Day Avg Daily Volume (ADV)`
* **Rule:** If Rate > 10%, REJECT.
* **Why?** If you try to sell 20% of a stock's daily volume, you will crash the price by 5-10% (Slippage), destroying your alpha.

## Workflow
1.  **Input:** Trade Intent (Ticker + Qty).
2.  **Data:** Fetches ADV (e.g., 200,000 shares).
3.  **Calculation:**
    * Input: 50,000 shares.
    * Ratio: 25%.
    * Result: **Unsafe**.
4.  **Action:** The bot rejects the order and returns a `suggested_qty` (e.g., 20,000) that fits within the safety limits.