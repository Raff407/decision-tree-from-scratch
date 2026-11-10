# Decision Tree From Scratch

[![CI](https://github.com/Raff407/decision-tree-from-scratch/actions/workflows/ci.yml/badge.svg)](https://github.com/Raff407/decision-tree-from-scratch/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.12%20%7C%203.13-blue)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![Status](https://img.shields.io/badge/status-in%20development-orange)

A NumPy implementation of CART decision trees for classification and regression, extended to a random forest with bootstrap aggregation, random feature subsets and out-of-bag evaluation.

> **Status:** in development. The repository structure, tooling and test infrastructure are in place; implementation is proceeding stage by stage according to the roadmap below.

## Contents

- [Overview](#overview)
- [Features](#features)
- [Mathematical background](#mathematical-background)
- [Roadmap](#roadmap)
- [Project structure](#project-structure)
- [Getting started](#getting-started)
- [Experiments](#experiments)
- [Design principles](#design-principles)
- [References](#references)
- [License](#license)

## Overview

Decision trees partition the feature space with axis-aligned splits chosen to maximise the reduction in impurity. This project implements the CART algorithm from first principles, covering classification (Gini impurity or entropy) and regression (variance reduction), exhaustive threshold search, configurable stopping rules, probability estimates and feature importances. Trees are built functionally from immutable nodes.

The single tree is then extended to a random forest using bootstrap sampling, random feature subsets at each split and majority voting, with out-of-bag accuracy as a built-in validation estimate. All estimators are benchmarked against their scikit-learn counterparts.

## Features

- Impurity measures: Gini, entropy and variance
- Exhaustive split search at midpoints of distinct sorted values, plus an O(n log n) incremental splitter
- Stopping rules: `max_depth`, `min_samples_split`, `min_samples_leaf`, `min_impurity_decrease`
- `DecisionTreeClassifier` and `DecisionTreeRegressor` with `predict`, `predict_proba` and `score`
- Impurity-based feature importances and a text tree printer
- `RandomForestClassifier` with bagging, random feature subsets and out-of-bag scoring

## Mathematical background

| Component | Definition |
|---|---|
| Gini impurity | $G = 1 - \sum_k p_k^2$ |
| Entropy | $H = -\sum_k p_k \log_2 p_k$ |
| Weighted child impurity | $\frac{n_L}{n} I(L) + \frac{n_R}{n} I(R)$ |
| Impurity decrease | $I(\text{parent}) - \left(\frac{n_L}{n} I(L) + \frac{n_R}{n} I(R)\right)$ |
| Regression leaf | $\bar{y}$, with impurity $\operatorname{Var}(y)$ |
| Bootstrap | $n$ draws with replacement; $\approx 36.8\%$ of rows out-of-bag |
| Forest split candidates | $\approx \sqrt{d}$ random features per split |

Full derivations are recorded in [`docs/derivations.md`](docs/derivations.md).

## Roadmap

- [ ] **Stage 1: Impurity functions.** Gini, entropy and variance tested against hand-computed values.
- [ ] **Stage 2: Single-feature split search.** Midpoint thresholds and impurity decrease on toy data.
- [ ] **Stage 3: Tree construction.** Best split over all features, immutable nodes, prediction; Iris benchmark against scikit-learn.
- [ ] **Stage 4: Stopping rules and overfitting.** Depth against train/test accuracy on Breast Cancer; depth chosen by k-fold CV.
- [ ] **Stage 5: Efficient splitting.** Incremental O(n log n) splitter verified against the naive implementation.
- [ ] **Stage 6: Regression and importances.** Variance-reduction regressor on California Housing; feature importances; tree printer.
- [ ] **Stage 7: Random forest.** Bagging, feature subsampling and OOB score; comparison with `RandomForestClassifier`.
- [ ] **Stage 8: Packaging.** Validated public API; ≥ 80% coverage.

## Project structure

```text
decision-tree-from-scratch/
├── .github/workflows/ci.yml   # Lint, format check and tests on Python 3.12 / 3.13
├── data/                      # Downloaded datasets (git-ignored)
├── docs/derivations.md        # Mathematical derivations
├── experiments/               # Reproducible scripts that generate figures
├── figures/                   # Saved plots referenced in this README
├── src/
│   └── decision_tree/
│       ├── __init__.py  # Package metadata
│       ├── impurity.py  # Gini impurity, entropy and variance
│       ├── splitter.py  # Best-split search (naive and incremental)
│       ├── node.py      # Immutable tree node
│       ├── tree.py      # DecisionTreeClassifier and DecisionTreeRegressor
│       ├── forest.py    # RandomForestClassifier with bagging and out-of-bag scoring
│       └── viz.py       # Text and Matplotlib tree rendering
├── tests/                     # pytest suite
├── pyproject.toml             # Packaging and tool configuration
└── uv.lock                    # Locked dependency versions
```

## Getting started

### Prerequisites

- Python 3.12 or later
- [uv](https://docs.astral.sh/uv/)

### Installation

```bash
git clone https://github.com/Raff407/decision-tree-from-scratch.git
cd decision-tree-from-scratch
uv sync
```

### Running the tests

```bash
uv run pytest
```

### Linting and formatting

```bash
uv run ruff check .
uv run ruff format .
```

## Experiments

Each script in [`experiments/`](experiments/) is deterministic given its seed and writes its output to [`figures/`](figures/).

- `depth_vs_accuracy.py` — overfitting as tree depth increases
- `splitter_benchmark.py` — naive vs incremental split search
- `forest_vs_tree.py` — random forest against a single tree and scikit-learn

Results and figures will be added to this section as each stage is completed.

## Design principles

- **From scratch.** The algorithm itself uses only Python and NumPy. scikit-learn (and, where noted, PyTorch) is used solely as a reference implementation in tests and for loading datasets.
- **Test-driven.** Each stage begins with a failing test against a hand-computed value or a reference implementation. Target coverage is at least 80%.
- **No mutation.** Public functions return new arrays and objects and never modify their inputs.
- **Reproducible.** Every stochastic routine and experiment accepts an explicit random seed.
- **Validated boundaries.** Public functions check input shapes and dtypes and fail with clear error messages.

## References

1. L. Breiman, J. Friedman, R. Olshen, C. Stone — *Classification and Regression Trees*, 1984.
2. L. Breiman — *Random Forests*, Machine Learning 45(1), 2001.
3. G. James, D. Witten, T. Hastie, R. Tibshirani, J. Taylor — *An Introduction to Statistical Learning with Applications in Python*, ch. 8. <https://www.statlearning.com>
4. T. Hastie, R. Tibshirani, J. Friedman — *The Elements of Statistical Learning*, §9.2 and ch. 15.
5. scikit-learn — Decision Trees user guide. <https://scikit-learn.org/stable/modules/tree.html>

## License

Released under the [MIT License](LICENSE).
