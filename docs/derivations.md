# Derivations — Decision Tree From Scratch

This document records the mathematical derivations underpinning the implementation,
written out in full before the corresponding code.

## Summary of results

| Component | Definition |
|---|---|
| Gini impurity | $G = 1 - \sum_k p_k^2$ |
| Entropy | $H = -\sum_k p_k \log_2 p_k$ |
| Weighted child impurity | $\frac{n_L}{n} I(L) + \frac{n_R}{n} I(R)$ |
| Impurity decrease | $I(\text{parent}) - \left(\frac{n_L}{n} I(L) + \frac{n_R}{n} I(R)\right)$ |
| Regression leaf | $\bar{y}$, with impurity $\operatorname{Var}(y)$ |
| Bootstrap | $n$ draws with replacement; $\approx 36.8\%$ of rows out-of-bag |
| Forest split candidates | $\approx \sqrt{d}$ random features per split |

## Stage 1: Impurity functions

_To be completed._

## Stage 2: Single-feature split search

_To be completed._

## Stage 3: Tree construction

_To be completed._

## Stage 4: Stopping rules and overfitting

_To be completed._

## Stage 5: Efficient splitting

_To be completed._

## Stage 6: Regression and importances

_To be completed._

## Stage 7: Random forest

_To be completed._

## Stage 8: Packaging

_To be completed._
