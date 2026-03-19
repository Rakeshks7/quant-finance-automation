# Kelly Criterion Sizing

A position sizing algorithm based on Information Theory. It dynamically adjusts bet sizes based on the strategy's Edge ($p$) and Odds ($b$).

## The Formula

$$f^\* = p - \\frac{1-p}{b}$$

* **Win Rate ($p$):** 55% (0.55)
* **Win/Loss Ratio ($b$):** 1.25
* **Result:** $0.55 - (0.45 / 1.25) = 0.55 - 0.36 = 0.19$ (19%)

## Fractional Kelly

Betting 19% of your account on one trade is mathematically optimal but psychologically impossible (drawdowns are huge).

* **Half-Kelly:** We multiply the result by 0.5.
* **Target:** 9.5% Position Size.

## Workflow Logic

1. **Input:** Trade Signal + Account Equity.
2. **Stats:** Fetches the strategy's historical Win Rate/Ratio.
3. **Math:** Computes $f^\*$.
4. **Output:** Returns the exact quantity to trade.

