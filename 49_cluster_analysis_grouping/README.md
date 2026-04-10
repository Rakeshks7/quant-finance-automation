# Cluster Analysis (Asset Grouping)

An **Unsupervised Machine Learning** workflow that discovers hidden relationships between assets.

## The Logic

Humans label assets by industry (This is a Bank, This is Oil).
Algorithms label assets by behavior (These two tickers move up/down at the exact same time).

## How it works (K-Means)

1. **Input:** We feed the algorithm 90 days of returns for 50 assets.
2. **Vectorization:** Each asset becomes a point in multi-dimensional space.
3. **Clustering:** The algorithm draws circles (clusters) around points that are close together.
4. **Discovery:**

   * *Expectation:* Gold clusters with Silver.
   * *Reality Check:* Sometimes Gold clusters with Tech stocks (liquidity crisis). If this happens, your diversified portfolio is actually highly concentrated risk.

