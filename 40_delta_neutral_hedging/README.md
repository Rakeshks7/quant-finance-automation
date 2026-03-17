# Delta Neutral Hedging

The ultimate risk management workflow for Options Market Makers. It ensures the portfolio remains Directionally Agnostic by balancing positive and negative Deltas.

## Workflow Logic

1. **Trigger:** Recurring Schedule (Every 5 mins) or Price Spike.
2. **Input:** Fetches the entire Option Book.
3. **The Greek Math (Python):**

   * **Call Option ($\\Delta +0.60$):** You own 500. Impact: $+300$ Delta.
   * **Put Option ($\\Delta -0.40$):** You own 300. Impact: $-120$ Delta.
   * **Net Delta:** $+180$ (You are accidentally Bullish).
4. **Action:**

   * To reach Zero, you need $-180$ Delta.
   * The bot **Sells 180 Qty** of Futures (since Future $\\Delta = 1$).
5. **Result:** Net Delta becomes $0$. You are now immune to small price moves and profit purely from Theta (Time Decay).

## Why this is Pro

This is how firms like Citadel and Jane Street operate. They don't gamble on direction; they hedge the direction instantly and keep the spread/fee.

