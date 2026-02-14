#  Factor Exposure Monitor

A risk analysis tool that uses statistical regression to uncover "Hidden Betas." It answers the question: *"Are we accidentally betting on Oil/Tech/Rates instead of our actual strategy?"*

## Workflow Logic
1.  **Trigger:** Daily Schedule.
2.  **Input:**
    * Portfolio Returns (Dependent Variable $Y$).
    * Factor Returns (Independent Variable $X$) defined in `factor_config.json`.
3.  **Math Engine (Python):**
    * Runs a **Linear Regression** ($Y = \alpha + \beta X + \epsilon$).
    * Calculates the coefficient $\beta$ (Beta).
4.  **Logic:**
    * If $\beta > 0.5$ (Strong Positive Correlation), it means your portfolio is effectively tracking that factor.
5.  **Output:** Sends a warning to re-balance or hedge.

## Why this is critical
In 2022, many "Diversified" Tech portfolios realized they were just "Short Interest Rates." When rates rose, everything crashed together. This bot identifies that correlation risk early.