#  Ticker Symbol Mapper

A Reference Data Management system that tracks symbol changes (Renames, Mergers, Delistings) to ensure historical data continuity.

## Workflow Logic
1.  **Trigger:** Weekly.
2.  **Input:**
    * **Source A:** Official Exchange Master List (contains `Ticker` and `ISIN`).
    * **Source B:** Internal Database.
3.  **Matching Logic (Python):**
    * The **ISIN** (International Securities Identification Number) is a unique ID that stays constant even if the Ticker changes.
    * We match records by ISIN.
    * `If ISIN Match AND Ticker Mismatch`: It's a Rename (e.g., FB -> META).
4.  **Action:** Updates the `symbol_map` table so that a request for "FB" in 2021 correctly redirects to the "META" data file.

## Use Case
Crucial for backtesting. If your strategy tries to buy "META" in 2015, it will fail because the stock didn't exist under that name. This mapper translates the request to "FB".