# once

A Python library for making parameter sweeps safely resumable.

When a long-running experiment script is re-run — whether after a crash, a time limit, or deliberately to extend a sweep — `once` automatically skips any parameter combinations that have already been completed.

```python
import once

@once.once(store='markov_runs.csv', key=['alpha', 'n_states', 'seed'])
def solve_markov(alpha, n_states, seed, n_iter=10_000):
    # expensive computation
    ...

for alpha in alphas:
    for n_states in [10, 50, 100]:
        for seed in range(20):
            solve_markov(alpha=alpha, n_states=n_states, seed=seed)
```

On restart, any already-completed `(alpha, n_states, seed)` combinations are skipped:

```
[once] Skipping solve_markov(alpha=0.01, n_states=10, seed=0)
[once] Skipping solve_markov(alpha=0.01, n_states=10, seed=1)
...
```

## Installation

```bash
uv add once
# or: python -m pip install once
```

With Parquet support:

```bash
uv add once[parquet]
# or: python -m pip install once[parquet]
```

## Usage

**Zero config** — uses `_once_store.csv` in the current directory, all parameters as the key:

```python
@once.once
def run_experiment(alpha, seed):
    ...
```

**Named store** — backend selected from file extension (`.csv`, `.json`, `.sqlite`, `.parquet`):

```python
@once.once(store='runs.sqlite')
def run_experiment(alpha, seed):
    ...
```

**Key subset** — only `alpha` and `seed` determine whether a run is skipped; `n_iter` is ignored:

```python
@once.once(store='runs.csv', key=['alpha', 'seed'])
def run_experiment(alpha, seed, n_iter=1000):
    ...
```

## Utilities

```python
once.status()            # print a summary of completed runs
once.reset()             # clear the store
once.reset(key_dict={'alpha': '0.1', 'seed': '42'})  # remove one entry
```

## Storage backends

| Extension | Backend | Notes |
|-----------|---------|-------|
| `.csv` | pandas CSV | Default. Human-readable. |
| `.json` | stdlib json | No extra dependencies. |
| `.sqlite` | stdlib sqlite3 | Best for large stores and parallel workers. |
| `.parquet` | pandas + pyarrow | Requires `once[parquet]`. |

## Documentation

Full documentation including how-to guides, API reference, and explanation of design decisions:

```bash
uv run mkdocs serve
```
