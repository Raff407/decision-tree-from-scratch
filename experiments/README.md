# Experiments

Standalone scripts that reproduce the figures in the project README. Each script
accepts a `--seed` argument and saves its output to `../figures/`.

Run any script with:

```bash
uv run python experiments/<script>.py --seed 0
```

## Planned scripts

- `depth_vs_accuracy.py` — overfitting as tree depth increases
- `splitter_benchmark.py` — naive vs incremental split search
- `forest_vs_tree.py` — random forest against a single tree and scikit-learn
