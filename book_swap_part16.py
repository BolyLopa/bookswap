# === Stage 16: Массовое обновление ===
# Project: BookSwap
from typing import Callable, Iterable, TypeVar, List

T = TypeVar("T")


def filter_by_condition(
    items: Iterable[T],
    predicate: Callable[[T], bool],
) -> List[T]:
    return [item for item in items if predicate(item)]


def preview_changes(
    items: Iterable[T],
    predicate: Callable[[T], bool],
    mutation: Callable[[T], None],
) -> List[T]:
    matches = filter_by_condition(items, predicate)
    if not matches:
        return matches
    for item in matches:
        mutation(item)
    return matches
