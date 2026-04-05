# Risk Parity Allocator

An asset allocation strategy that focuses on allocation of **Risk**, not Capital.

## The Problem

In a Balanced 50/50 portfolio of Stocks and Bonds:

* Stocks ($\\sigma=20%$) contribute 90% of the risk.
* Bonds ($\\sigma=4%$) contribute 10% of the risk.
* *Result:* You are effectively just holding Stocks.

## The Solution (Inverse Volatility)

We allocate capital inversely to volatility:

* **Stocks:** High Vol -> Low Weight (e.g., 18%).
* **Bonds:** Low Vol -> High Weight (e.g., 82%).
* *Result:* Both assets now contribute equally to the portfolio's variance. If stocks crash, the massive bond position cushions the blow effectively.

