# 🧤 Fat Finger Protection (Pre-Trade Validation)

A middleware validation layer that sits between your Trading Strategy and the Broker Execution. It acts as a digital "Risk Manager," preventing erroneous code or typos from bankrupting the fund.

## Workflow Logic
1.  **Trigger:** An order request arrives via Webhook (from a strategy script).
2.  **Context Retrieval:**
    * Fetches current **Account Equity (NAV)**.
    * Loads **Risk Limits** from `risk_limits.json`.
3.  **Validation Engine:** Checks the order against critical rules:
    * **Value Limit:** Order Value cannot exceed 5% of NAV.
    * **Quantity Limit:** No single order > 1000 shares.
    * **Blacklist:** Ticker cannot be in the restricted list (e.g., highly volatile meme stocks).
4.  **Action:**
    * **Safe:** Passes the order to the Broker API.
    * **Unsafe:** Drops the order and sends a critical Slack alert.

## Why this is critical
Algorithmic trading bugs can send thousands of orders in seconds. This "Circuit Breaker" ensures that no single logic error can cause catastrophic capital loss.