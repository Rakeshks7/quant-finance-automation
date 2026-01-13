# 🧬 CI/CD Strategy Pipeline

An automated DevOps pipeline for Quantitative Strategies. It ensures that no code is ever deployed without passing a historical simulation (Backtest).

## Workflow Logic
1.  **Trigger:** Listens for a `git push` event on the strategy repository (GitHub).
2.  **Execution Environment:** Connects to a dedicated Backtesting Server via SSH.
3.  **Action:**
    * Pulls the new code (`git pull`).
    * Runs the backtesting engine (`python3 backtest.py`).
    * Captures the console output (JSON metrics).
4.  **Reporting:** Parses the `Sharpe Ratio` and `Max Drawdown` and emails a pass/fail report to the Quants.

## Setup Guide
1.  **GitHub:** Connect the n8n GitHub Trigger to your repository and select the `push` event.
2.  **Server:** Ensure your remote server has Python installed and the repo cloned at `/opt/trading-bot` (or your preferred path).
3.  **Script:** The Python script must output the final metrics as a JSON string to `stdout` for n8n to parse it successfully.