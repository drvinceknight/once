"""Storage backends for the once library."""

from __future__ import annotations

from pathlib import Path

from once.backends._base import BaseBackend
from once.backends._csv import CsvBackend
from once.backends._json import JsonBackend
from once.backends._sqlite import SqliteBackend

__all__ = ["BaseBackend", "CsvBackend", "JsonBackend", "SqliteBackend", "get_backend"]

_EXTENSION_MAP: dict[str, type[BaseBackend]] = {
    ".csv": CsvBackend,
    ".json": JsonBackend,
    ".sqlite": SqliteBackend,
    ".db": SqliteBackend,
}


def get_backend(path: Path) -> BaseBackend:
    """Return the appropriate backend for the given file path.

    The backend is selected based on the file extension:

    - ``.csv`` → :class:`~once.backends._csv.CsvBackend`
    - ``.parquet`` → :class:`~once.backends._parquet.ParquetBackend`
    - ``.sqlite`` / ``.db`` → :class:`~once.backends._sqlite.SqliteBackend`
    - ``.json`` → :class:`~once.backends._json.JsonBackend`

    Args:
        path: Path to the store file.

    Returns:
        A backend instance for the given file extension.

    Raises:
        ValueError: If the file extension is not supported.
    """
    ext = path.suffix.lower()

    if ext == ".parquet":
        from once.backends._parquet import ParquetBackend

        return ParquetBackend(path)

    cls = _EXTENSION_MAP.get(ext)
    if cls is None:
        supported = ", ".join(sorted(_EXTENSION_MAP) + [".parquet"])
        raise ValueError(
            f"Unsupported store extension: {ext!r}. Supported: {supported}"
        )
    return cls(path)
