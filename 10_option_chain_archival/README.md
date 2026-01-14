# 📉 Option Chain Archival System

A data engineering pipeline that captures the entire NIFTY Option Chain every 3 minutes, effectively building a proprietary historical database for backtesting options strategies.

## Workflow Logic
1.  **Trigger:** Cron Schedule `*/3 9-15 * * 1-5`. This runs every 3 minutes only on weekdays between 9 AM and 3 PM.
2.  **Source:** Fetches JSON data from the NSE website (or Broker API like Kite/Upstox).
3.  **Transformation (Python):**
    * The raw API response returns a nested JSON object (Strike -> CE/PE).
    * The Python Code Node "flattens" this structure.
    * Converts 1 API call into ~200 database rows (one for every strike price/option type).
4.  **Storage:** Inserts the clean rows into PostgreSQL (or Google BigQuery).

## Why this is valuable
* **Cost Savings:** Purchasing 1-minute historical option data costs thousands of dollars per year. This bot builds it for free.
* **Backtesting:** You can query this database later to ask: *"What happened to the 21000 CE premiums when NIFTY fell 100 points on Jan 28th?"*

## Technical Note
Fetching data directly from `nseindia.com` is difficult due to cookie protection. It is recommended to replace the HTTP Request node with a Broker API (Zerodha/AngelOne) for production stability.