# Install once

## Standard install

```bash
uv add once
# or: python -m pip install once
```

## With Parquet support

```bash
uv add once[parquet]
# or: python -m pip install once[parquet]
```

Parquet support requires `pyarrow` and enables the `.parquet` backend. See [Choose a Backend](choose-a-backend.md) for when this is useful.
