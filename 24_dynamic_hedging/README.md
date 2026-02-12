#  Dynamic Portfolio Hedging (Beta Neutralizer)

An algorithmic risk management overlay that automatically keeps the portfolio's market exposure (Beta) within a target range. It uses Index Futures to offset the directional risk of your stock holdings.

## Workflow Logic
1.  **Trigger:** Hourly (during Market Hours).
2.  **Calculation:**
    * Computes the rolling 60-day Beta of the portfolio vs NIFTY.
    * Checks if the `Current Beta` deviates from `Target Beta` by more than 0.1.
3.  **Sizing:**
    * `Hedge $ = Portfolio Value * (Beta_Current - Beta_Target)`
    * Converts this dollar amount into "Lots" of NIFTY Futures.
4.  **Action:**
    * If Beta is too high (Too bullish), it **Shorts** NIFTY Futures.
    * If Beta is too low (Too bearish/hedged), it **Buys** NIFTY Futures (or covers shorts).

## Use Case
Perfect for "Market Neutral" strategies (Pairs Trading, Stat Arb) where you want to profit from the spread between stocks, not the direction of the overall market.