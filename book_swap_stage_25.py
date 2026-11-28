# === Stage 25: Скользящее среднее ===
# Project: BookSwap
"""
module: moving_average
topic : sliding average over a numeric series tied to a "book"
stage : stage 25 of 88
"""

import statistics
from collections import deque

# deque keeps only the last `window` samples, so memory stays bounded.
_WINDOW = 5


def moving_average(values, window=_WINDOW):
    """Return the sliding average of ``values`` using a trailing ``window``.

    Each element of the result corresponds to the average of the most recent
    ``window`` values (inclusive of the current value).  The first ``window - 1``
    results are ``None`` because a full window is not available yet.

    Parameters
    ----------
    values : iterable of (int | float)
        The numeric series.  Non-numeric items are skipped so a stray ``None``
        or empty field in the source data never breaks the calculation.
    window : int
        Size of the trailing window.  Must be a positive integer.

    Returns
    -------
    list of (int | float | None)
        The computed averages.

    Examples
    --------
    >>> moving_average([1, 2, 3, 4, 5])
    [None, None, None, None, 3.0]
    >>> moving_average([10, 20, 30, 40, 50], window=3)
    [None, None, 20.0, 30.0, 40.0]
    """

    if window <= 0:
        raise ValueError("window must be a positive integer")

    buffer = deque(maxlen=window)
    result = []

    for value in values:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            # ignore non-numeric samples silently
            continue
        buffer.append(value)
        if len(buffer) < window:
            result.append(None)
        else:
            result.append(statistics.fmean(buffer))

    return result
