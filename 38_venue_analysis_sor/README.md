# Venue Analysis (Smart Order Routing)

A High-Frequency Trading (HFT) utility that dynamically routes orders to the exchange with the best liquidity or price at that exact microsecond.

## Workflow Logic

1. **Input:** Buy 500 shares of Reliance.
2. **Market Scan:**

   * **NSE:** Best Ask ₹2400.05 | Qty Available: 200.
   * **BSE:** Best Ask ₹2400.05 | Qty Available: 1000.
3. **Comparator (Python):**

   * Prices are equal.
   * NSE cannot fill the full order (200 < 500).
   * BSE can fill the full order (1000 > 500).
4. **Decision:** Route to **BSE**.
5. **Result:** The order is filled instantly in one go, avoiding partial fills and multiple transaction fees.

## Why this is Pro

Retail traders usually just default to the primary exchange (NSE). Institutional algos scan *every* liquidity pool to minimize Impact Cost.

