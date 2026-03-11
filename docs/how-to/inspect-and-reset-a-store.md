# Inspect a Store

## Check progress with `once.status()`

```python
import once

once.status()                  # default store
once.status('markov_runs.csv') # named store
```

Output:

```
[once] Store: _once_store.csv
[once] 142 completed experiments recorded
[once] Last run: 2024-11-03T14:22:01
[once] Key columns: alpha, beta, n_steps
```

## Inspect the store directly

The store is a plain file — you can load it as a list of dicts and work with it however you like:

```python
from once.backends import get_backend
from pathlib import Path

backend = get_backend(Path('_once_store.csv'))
records = backend.load()
print(records[:3])
```
