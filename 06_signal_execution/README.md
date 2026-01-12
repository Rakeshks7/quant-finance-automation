# ⚡ Signal Execution Bridge (TradingView → API)

An automated order routing system that listens for TradingView alerts via Webhook, calculates position size based on risk parameters, and executes the trade via Broker API.

## Workflow Logic
1.  **Trigger:** n8n Webhook URL (configured in TradingView Alert).
2.  **Security:** Payload must contain a matching `secret_token`.
3.  **Risk Management:**
    * Hardcoded Equity: $10,000 (Demo)
    * Risk Per Trade: 1% ($100)
    * Algorithm: `Qty = $Risk / (Entry - StopLoss)`
4.  **Execution:** Sends JSON payload to Alpaca Markets (or Interactive Brokers).
5.  **Journaling:** Automatically logs the trade entry to a Notion Database.

## How to Setup
1.  **In n8n:**
    * Activate the workflow.
    * Copy the **Production Webhook URL**.
2.  **In TradingView:**
    * Create an Alert.
    * Paste the URL into the "Webhook URL" field.
    * Paste the content of `tv_payload_template.json` into the Message box.
    * **IMPORTANT:** Update the `secret_token` in the JSON to match the one in the n8n Code Node.