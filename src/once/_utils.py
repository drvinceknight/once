"""Utility functions for inspecting and managing once stores."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from once.backends import get_backend

_DEFAULT_STORE = "_once_store.csv"


def status(store_path: str | Path = _DEFAULT_STORE) -> None:
    """Print a summary of completed experiments in a store.

    Args:
        store_path: Path to the store file (any supported extension).
            Defaults to ``_once_store.csv`` in the current directory.

    Raises:
        FileNotFoundError: If the store file does not exist.

    Example:
        ```python
        once.status()
        # [once] Store: _once_store.csv
        # [once] 42 completed experiments recorded
        # [once] Last run: 2024-11-03T14:22:01
        # [once] Key columns: alpha, beta
        ```
    """
    path = Path(store_path)
    if not path.exists():
        raise FileNotFoundError(f"Store not found: {path}")

    backend = get_backend(path)
    records = backend.load()

    print(f"[once] Store: {path}")
    print(f"[once] {len(records)} completed experiments recorded")

    if records:
        timestamps = [
            r["_once_timestamp"]
            for r in records
            if "_once_timestamp" in r and r["_once_timestamp"]
        ]
        if timestamps:
            print(f"[once] Last run: {max(timestamps)}")

        key_cols = [k for k in records[0] if k != "_once_timestamp"]
        if key_cols:
            print(f"[once] Key columns: {', '.join(key_cols)}")


def reset(
    store_path: str | Path = _DEFAULT_STORE,
    key_dict: dict[str, Any] | None = None,
) -> None:
    """Remove entries from a store.

    Args:
        store_path: Path to the store file. Defaults to ``_once_store.csv``
            in the current directory.
        key_dict: If provided, remove only this specific key combination.
            If None, clear the entire store (prompts for confirmation
            in interactive mode).

    Example:
        ```python
        # Remove one entry from the default store
        once.reset(key_dict={'alpha': '0.1', 'beta': '2'})

        # Clear the default store entirely (prompts interactively)
        once.reset()

        # Clear a named store
        once.reset('markov_runs.csv')
        ```
    """
    path = Path(store_path)
    backend = get_backend(path)

    if key_dict is None:
        if sys.stdin.isatty():
            answer = (
                input(f"[once] Clear all records in {path}? [y/N] ").strip().lower()
            )
            if answer != "y":
                print("[once] Aborted.")
                return
        backend.clear()
        print(f"[once] Store cleared: {path}")
    else:
        backend.remove(key_dict)
        print(f"[once] Removed entry: {key_dict}")
