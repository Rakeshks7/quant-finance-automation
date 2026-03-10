# Iceberg Order Management

A stealth execution algorithm designed to hide large order sizes from the market. It slices a Parent Order into many tiny Child Orders that refill only after the previous one is executed.

## Workflow Logic

1. **Input:** Buy 5,000 shares of Reliance @ Limit ₹2400.
2. **Configuration:** Visible Tip = 100 shares.
3. **The Loop:**

   * **Step A:** Place Limit Order for 100 shares.
   * **Step B:** Market participants see only 100 shares (looks like a retail trader).
   * **Step C:** Wait for a Fill event.
   * **Step D:** Immediately place the *next* 100 shares.

4. **Result:** You buy 5,000 shares without ever showing more than 100 on the Order Book, preventing HFTs from penny jumping you.

## Why this is Pro

This is standard functionality for Institutional Execution Desks. Implementing this in your own stack proves you understand market microstructure and adverse selection.

