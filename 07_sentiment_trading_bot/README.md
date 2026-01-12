# 🐂 Sentiment Trading Bot (News Momentum)

An event-driven algorithmic trading module that filters global news feeds for high-impact financial events and uses AI to determine if they are actionable.

## Workflow Logic
1.  **Ingestion:** Polls RSS feeds (Yahoo Finance, Reuters) every minute.
2.  **Pre-Filtering:** Uses a Keyword Whitelist (e.g., "FDA", "Merger") to discard non-market-moving news immediately (saving AI costs).
3.  **AI Analysis:** OpenAI (GPT-4o-Mini) reads the headline/snippet and assigns a `Sentiment Score` (-1.0 to +1.0).
4.  **Decision Engine:**
    * IF `Score > 0.8` (Strongly Bullish) -> **TRIGGER ALERT**
    * IF `Score < 0.8` -> Discard/Ignore
5.  **Output:** Sends a rich-embed message to a Discord Channel for immediate manual execution or review.

## Configuration
1.  **Keywords:** Edit the Code Node to add specific sectors you trade (e.g., "Crypto", "Oil", "EV").
2.  **Discord:**
    * Create a Webhook in your Discord Server (Server Settings > Integrations > Webhooks).
    * Paste the Webhook URL into the n8n Discord Node credentials.
3.  **Threshold:** Adjust the "Is Score > 0.8" node if you want more or fewer alerts.