# MPT Optimizer (Efficient Frontier)

A mathematical engine that uses **Modern Portfolio Theory (MPT)** to construct the Perfect Portfolio. It finds the specific combination of assets that offers the lowest possible risk for a specific target return.

## The Math
We use **Quadratic Programming** (via Python's `scipy.optimize`) to solve:

* **Minimize:** $\sigma_p^2 = \sum_i \sum_j w_i w_j \sigma_{ij}$ (Portfolio Variance)
* **Subject to:** $\sum w_i E(R_i) = R_{target}$ (Target Return)

## Workflow Logic
1.  **Input:** A basket of stocks (e.g., Tech, Pharma, Banks) and their historical correlation data.
2.  **Constraint:** "I want a 12% annual return, but I want to sleep well at night."
3.  **Solver:** The algorithm tests millions of weight combinations using gradients.
4.  **Output:** "To achieve 12% return with minimum variance, allocate: 40% JNJ, 20% MSFT, 10% GOOGL..."