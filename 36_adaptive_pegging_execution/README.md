# Adaptive Pegging (Limit Chaser)

A smart execution algorithm that attempts to capture the Spread by placing passive Limit orders at the Best Bid. If the market moves away, it automatically cancels and Chases the price up to a defined limit.

## Workflow Logic

1. **Goal:** Buy TCS.

   * *Current Market:* Bid 3490 / Ask 3495.
   * *Spread:* ₹5.

2. **Step 1:** Place Limit Order at **3490** (Best Bid).

   * *Benefit:* If filled, we save ₹5/share compared to a Market Order.

3. **Step 2:** Wait 30 seconds.
4. **Step 3:** Re-check Market.

   * *Scenario:* Market moves up. New Bid is **3495**.
   * *Risk:* Our order at 3490 will never fill.

5. **Action:**

   * **Cancel** Order @ 3490.
   * **Replace** with Order @ 3495 (Peg to new Bid).
   * **Loop:** Repeat until filled or price > Hard Limit (3500).

## Why this is Pro

This mimics how human traders work the order book—trying to be patient (Passive) but reacting quickly (Aggressive) if the train is leaving the station.

