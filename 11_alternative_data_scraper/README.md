# 🏎️ Alternative Data Scraper

A web scraping pipeline that turns unstructured web data into structured financial metrics. It uses Generative AI to parse text that traditional RegEx cannot handle.

## Use Case Example: F1 & Stock Prices
* **Hypothesis:** If Ferrari (RACE) wins a Grand Prix, their merchandise sales and brand sentiment spike, potentially leading to a short-term stock price increase on Monday.
* **Process:**
    1.  Scrape race results on Sunday evening.
    2.  Extract the winning constructor.
    3.  Store in DB.
    4.  (Future) Correlate with Monday's opening price action.

## Workflow Logic
1.  **Fetch:** HTTP Request gets the full HTML of a results page.
2.  **Extract:** (Simulated) Grabs the relevant text block.
3.  **Structure (AI):** GPT-4o takes the text "Leclerc won for Ferrari" and turns it into `{"winner": "Ferrari"}`.
4.  **Store:** Saves to PostgreSQL for quantitative analysis.