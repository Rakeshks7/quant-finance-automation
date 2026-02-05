#  Post-Trade TCA (Transaction Cost Analysis)

A forensic audit system that benchmarks every executed trade against the market conditions at the exact moment of execution.

## Workflow Logic
1.  **Trigger:** Broker Webhook (Fill Event).
2.  **Context:** Fetches the NBBO (National Best Bid/Offer) for that timestamp.
3.  **Calculation (Python):**
    * Computes the **Market Midpoint** (Fair Value).
    * Calculates **Slippage** in Basis Points (bps).
    * `Slippage = (Execution Price - Midpoint) / Midpoint * 10000`
4.  **Output:** Logs the performance to SQL.
    * *Insight:* If your slippage is consistently >5 bps, your strategy is too aggressive or your broker is routing your orders poorly.

## Why this is critical
In High-Frequency Trading (HFT), "Alpha" is often eaten away by transaction costs. This bot makes those hidden costs visible.