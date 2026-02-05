#  Cointegration Scanner (Pairs Trading)

A statistical arbitrage maintenance tool. It performs a weekly health check on correlated asset pairs to ensure the mathematical relationship (mean reversion) still holds valid.

## Workflow Logic
1.  **Trigger:** Weekly Schedule.
2.  **Input:** Reads the `active_pairs.json` config file.
3.  **Math Engine (Python):**
    * Simulates fetching 90-day historical prices.
    * Runs the **Augmented Dickey-Fuller (ADF)** test on the price spread.
4.  **Decision:**
    * **P-Value > 0.05:** The pair is "Walking Away" (Non-Stationary).
    * **Action:** Triggers a Slack Alert to remove the pair from the trading universe to prevent losses.

## Why this is critical
Trading a pair that has lost its correlation is the fastest way to blow up a market-neutral fund. This bot automates the "Exit" decision.