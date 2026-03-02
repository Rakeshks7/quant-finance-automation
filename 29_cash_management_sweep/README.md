#  Cash Management & Sweep

An automated Treasury operation that eliminates Cash Drag. It ensures that any significant idle capital (> ₹1L) is automatically invested in safe, interest-bearing instruments (like Liquid Bees) overnight.

## Workflow Logic
1.  **Trigger:** Runs daily at 3:15 PM (Pre-Market Close).
2.  **Input:** Fetches available "Free Margin" from the broker.
3.  **Calculation:**
    * `Investable = Free Margin - Cash Buffer (e.g., ₹50k)`.
    * If `Investable` > `Threshold (e.g., ₹1L)`, proceed.
4.  **Action:** Places a Market Order to buy the calculated quantity of `LIQUIDBEES` or `Overnight Mutual Fund`.

## Why this is valuable
Idle cash earns 0%. Liquid Bees earn ~6-7% annualized. Over a year, on a ₹10L account, simply running this script can add ₹60,000-70,000 in "Free" profit with near-zero risk.