#  Short Locate Automation

An automated pre-market workflow for Short Sellers. It handles the Locate process (finding shares to borrow) for Hard-To-Borrow (HTB) stocks.

## Workflow Logic
1.  **Trigger:** 8:30 AM (Pre-Market).
2.  **Input:** Reads the strategy's "Hit List" (`short_targets.json`).
3.  **Broker Negotiation:**
    * Queries the Broker API for inventory.
    * Checks the "Cost to Borrow" (Interest Rate).
4.  **Cost Control:**
    * If `Fee > 5%`, the bot REJECTS the short (too expensive).
    * If `Fee < 5%`, the bot APPROVES and stores the `Locate ID`.
5.  **Output:** Updates `available_shorts.json`.
    * *Benefit:* Your trading algorithm reads this file. If a stock isn't in this file, the algo knows it is physically impossible/too expensive to short, preventing failed orders.