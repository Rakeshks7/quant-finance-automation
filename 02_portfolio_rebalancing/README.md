# ⚖️ Portfolio Rebalancing Engine

Automatically calculates the difference between your **Current Portfolio** (Broker) and **Target Allocations** (Strategy) and generates a trade list.

## Workflow Logic
1.  **Inputs:** * `Target Weights`: Fetched from Google Sheets.
    * `Current Holdings`: Fetched from Broker API (Mocked in workflow for demo).
2.  **Processing (Python):** * Calculates Total Portfolio Value (Holdings + Cash).
    * Derives Target Value per asset.
    * Computes `Delta` (Target - Current).
3.  **Output:** * Sends a formatted "Trade Approval" alert to Slack/Email if rebalancing is needed.

## Configuration
1.  **Google Sheet:** Create a sheet with columns `Ticker` and `Target_Weight` (e.g., 0.4 for 40%).
2.  **Broker Connection:** Replace the "Mock Holdings" node with a real HTTP Request to your broker (Interactive Brokers, Alpaca, etc.).
3.  **Thresholds:** The Python script currently has a `$100` buffer to prevent micro-trading. Adjust this in the Code Node.