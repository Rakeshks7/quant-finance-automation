# Yield Curve Inversion Monitor

A macro-economic watchdog that tracks the spread between long-term and short-term interest rates to predict economic downturns.

## The Logic

* **Normal Curve:** Investors demand higher interest for locking money away for 10 years (Risk Premium). So, 10Y > 2Y.
* **Inverted Curve:** Investors expect future rates to fall (due to a crash), so they rush into long-term bonds, driving 10Y yields *below* 2Y yields.

## Workflow

1. **Input:** US 10-Year Note Yield (3.85%) and US 2-Year Note Yield (4.10%).
2. **Calculation:** $Spread = 3.85 - 4.10 = -0.25%$.
3. **Signal:** **NEGATIVE**. The market is screaming that a recession is imminent.
4. **Action:** The bot triggers a "Defensive Rotation," selling high-beta stocks and buying Gold or Short-Term Treasuries.

