# 🛡️ Volatility Guard (Circuit Breaker)

An automated risk management system that enforces "Regime Switching." It constantly monitors market volatility (CBOE VIX) and physically stops the trading server if conditions become too dangerous for the current strategy.

## Workflow Logic
1.  **Trigger:** Schedule runs every 15 minutes.
2.  **Data:** Fetches real-time VIX (Volatility Index) data from Yahoo Finance.
3.  **Logic:**
    * **Safe Zone (VIX < 30):** Logs "Normal" status to Slack.
    * **Danger Zone (VIX > 30):** Triggers the Kill Switch.
4.  **Action (SSH):** Connects to the remote trading server (AWS EC2 / DigitalOcean) via SSH and executes:
    `sudo systemctl stop algo-trading.service`
5.  **Alert:** Sends an immediate SMS via Twilio to the Risk Manager.

## Configuration
1.  **SSH Credentials:**
    * You must upload your `.pem` private key or SSH password to n8n's Credential Manager.
    * Ensure the n8n user has `sudo` permissions on the server (or use a specific user that can stop services).
2.  **Threshold:** Default is set to `30.0`. Adjust in the Code Node based on your strategy's sensitivity to volatility.