# 🚑 Infrastructure Watchdog (System Health)

A critical reliability workflow that monitors the pulse of the trading infrastructure. It ensures that the algorithms are not trading blindly due to stale data or disconnected databases.

## Architecture
* **Trigger:** Cron Job (Every 5 Minutes).
* **Checks:**
    1.  **API Latency:** Pings the Market Data Provider. If response > 2000ms, flags as degraded.
    2.  **Database Integrity:** Runs a lightweight `SELECT 1` query to ensure the SQL engine is responsive.
* **Logic:** Aggregates errors from parallel execution threads.
* **Escalation:**
    * **Level 1 (Warning):** Slack Log (if services are slow but working).
    * **Level 2 (Critical):** Twilio Voice Call/SMS (if Database or API is completely unreachable).

## Configuration
1.  **Twilio Setup:**
    * Add your `Account SID` and `Auth Token` in n8n Credentials.
    * Set the `From` number to your Twilio purchased number.
    * Set the `To` number to the Head Trader's mobile.
2.  **Thresholds:**
    * Adjust latency tolerance in the "Analyze Health Status" Code Node (Default: 1000ms).

## Why this matters
In high-frequency or algorithmic trading, a "stuck" connection can result in significant financial loss if the system thinks it has no positions open when it actually does. This watchdog is the "Kill Switch" activator.