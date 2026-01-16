# 🎛️ Strategy Parameter Optimization (WFA)

Automates the **Walk-Forward Analysis** process. Instead of using static indicators (which stop working as markets change), this workflow re-optimizes the strategy every weekend to find the best parameters for the *current* market regime.

## Workflow Logic
1.  **Trigger:** Runs every Sunday evening.
2.  **Computation:** Connects to a powerful remote server (via SSH) to run a computationally expensive Python script (`optimize.py`).
3.  **Process:** The script performs a "Grid Search" or "Bayesian Optimization" on historical data from the last 30 days.
4.  **Output:** Returns the new "Best" parameters (e.g., changing Moving Average from 50 to 42).
5.  **Action:** Emails the Trader the new configuration to apply for the coming week.

## Why this matters
Static strategies decay. Dynamic strategies that adapt to volatility (like this one) survive longer. This pipeline ensures the bot is never "stale."