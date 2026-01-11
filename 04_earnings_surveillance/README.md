# 📈 Earnings Surveillance System

An event-driven workflow that monitors corporate earnings releases. It not only tracks the numbers (EPS Surprise) but uses Generative AI to read the management's "Forward Guidance" and gauge sentiment.

## Workflow Logic
1. **Source:** Fetches a daily earnings calendar (Mocked, can use Yahoo Finance API).
2. **Filter:** Matches reporting companies against a user-defined `watchlist.json`.
3. **Quantitative Analysis:** Calculates `EPS Surprise %` (Actual vs Consensus).
4. **Qualitative Analysis:** Uses GPT-4 to parse the text of the "Guidance" section (Forward-looking statements).
5. **Alert:** Sends a rich-text Slack notification with color coding (Green for Beat, Red for Miss).

## Use Case
* **For Traders:** Immediate reaction to "Guidance" tone (which often moves stock more than the EPS number).
* **For Analysts:** Automates the initial screening of hundreds of earnings reports.