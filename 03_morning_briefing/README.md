# ☕ AI Morning Briefing Agent

An autonomous agent that wakes up at 8:00 AM, scans global markets and news, and generates a risk assessment briefing sent to Telegram.

## Architecture
* **Data Sources:** * NewsAPI (Headlines)
    * AlphaVantage/Yahoo Finance (Indices & Futures)
* **Intelligence:** OpenAI (GPT-4o)
* **Delivery:** Telegram Bot

## Setup Guide
1. **API Keys Required:**
    * `OPENAI_API_KEY`: For the analysis.
    * `TELEGRAM_BOT_TOKEN` & `CHAT_ID`: For delivery.
    * (Optional) `NEWS_API_KEY`: If replacing the mock data.
2. **Customizing the Agent:**
    * Edit the **OpenAI Analyst** node prompt to change the persona (e.g., change "Conservative Analyst" to "Aggressive Day Trader").
3. **Usage:**
    * Import `workflow.json` into n8n.
    * Fill in the Credentials in the OpenAI and Telegram nodes.
    * Activate the workflow.