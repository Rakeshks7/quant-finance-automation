# 🧾 Real-Time Tax Impact Monitor

An automated accounting bot that calculates Tax Liability (STCG vs LTCG) immediately upon closing a trade. This allows for real-time provisioning of funds rather than year-end shock.

## Workflow Logic
1.  **Trigger:** Broker Webhook (simulated) sends trade details immediately after a sell order is filled.
2.  **Cost Basis Retrieval:** The bot looks up the database for the corresponding "Buy" record (using FIFO logic).
3.  **Tax Engine (Python):**
    * Computes `Holding Period` (Sell Date - Buy Date).
    * Applies conditional logic:
        * **< 365 Days:** Short Term Capital Gain (STCG) @ 20%.
        * **> 365 Days:** Long Term Capital Gain (LTCG) @ 12.5%.
4.  **Output:** Updates a `tax_provision_ledger` SQL table and sends a Slack alert to the CFO/Trader.

## Logic Implementation
The tax rates are hardcoded in the Python Node but can be easily swapped for a `tax_config.json` file lookup to handle different asset classes (e.g., Debt/Gold vs Equity).