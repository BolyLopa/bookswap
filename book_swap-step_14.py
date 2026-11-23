# === Stage 14: Поиск дубликатов ===
# Project: BookSwap
from dataclasses import dataclass
from typing import Iterable, Iterator


@dataclass(frozen=True)
class Book:
    title: str
    author: str
    owner: str
    state: str


def normalize(value: str) -> str:
    """Lowercase, strip whitespace, and remove punctuation from a string."""
    return "".join(ch for ch in value.lower().strip() if ch.isalnum())


def book_signature(book: Book) -> str:
    """Build a normalized, comparison-stable signature for a book."""
    return "||".join(
        normalize(field) for field in (book.title, book.author, book.owner, book.state)
    )


def find_duplicates(books: Iterable[Book]) -> list[tuple[Book, ...]]:
    """Return groups of two or more books that share the same signature.

    Each group is a tuple of the identical books, preserving first-seen order.
    """
    groups: dict[str, list[Book]] = {}
    for book in books:
        key = book_signature(book)
        groups.setdefault(key, []).append(book)
    return [books_in_group for books_in_group in groups.values() if len(books_in_group) > 1]


def iter_duplicate_pairs(books: Iterable[Book]) -> Iterator[tuple[Book, Book]]:
    """Yield every pair of duplicate books found among the given books."""
    for group in find_duplicates(books):
        for first, second in zip(group, group[1:]):
            yield first, second
