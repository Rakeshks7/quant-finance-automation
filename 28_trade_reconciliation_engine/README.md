# Trade Reconciliation Engine (Recs)

A critical Middle Office automation that performs "T+0 Reconciliation." It compares the fund's internal trade ledger against the official contract note received from the broker to ensure accurate accounting.

## Workflow Logic

1. **Trigger:** Listens for the "Daily Contract Note" email from the Prime Broker.
2. **Extraction:** Downloads the CSV attachment and parses the execution data (External Truth).
3. **Comparison (Python):** Matches trades against the internal SQL database (Internal Truth) using Ticker, Side, and Date.
4. **Logic Checks:**

   * **Quantity Break:** Did we record 50 shares but the broker executed 40?
   * **Price Break:** Is the price difference greater than 0.01 (rounding error)?
   * **Missing Trade:** Did a trade happen that we didn't record?

5. **Output:** Sends a "Break Sheet" to the Operations team for manual investigation.

## Why this is critical

If your internal ledger is wrong, your Risk Management (Process 23) and Tax Calculations (Process 13) will also be wrong. This is the "Source of Truth" validator.

