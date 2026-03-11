"""once — persistent memoization by parameter identity.

Decorates experiment functions so they skip already-completed runs on restart.

Example:
    ```python
    import once

    @once.once(store='_once_store.csv', key=['alpha', 'beta'])
    def run_experiment(alpha, beta, n_steps):
        ...  # expensive computation
    ```
"""

from once._decorator import once
from once._utils import reset, status

__all__ = ["once", "status", "reset"]
