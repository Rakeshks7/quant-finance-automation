# Basket Arbitrage (ETF vs Constituents)

A core HFT strategy that exploits pricing inefficiencies between an ETF and its underlying assets.

## The Logic

An ETF (like Nifty Bees) is not a stock; it is a receipt for a basket of 50 stocks.

* **NAV (Fair Value):** The live value of those 50 stocks combined.
* **Market Price:** What traders are currently paying for the ETF.

## The Trade

1. **Scenario:** Panic selling drives Nifty Bees price down to ₹248, but the stocks (HDFC, Reliance, etc.) are stable with a NAV of ₹250.
2. **The Arb:**

   * **Buy ETF** @ ₹248.
   * **Sell Stocks** @ ₹250 (Short the basket).
   * **Profit:** ₹2 Risk-Free (minus fees).
3. **Settlement:** You give the ETF units to the issuer and get the stocks back to cover your short position (Redemption).

