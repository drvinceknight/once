# Re-run Everything

To clear the store and re-run all experiments from scratch:

```python
once.reset()
# [once] Clear all records in _once_store.csv? [y/N] y
```

In non-interactive environments (CI, scripts) the prompt is skipped and the store is cleared immediately.
