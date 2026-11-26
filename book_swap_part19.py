# === Stage 19: Смена статуса ===
# Project: BookSwap
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class BookStatus(str, Enum):
    AVAILABLE = "available"
    RESERVED = "reserved"
    LOANED = "loaned"
    RETURNED = "returned"
    EXCHANGED = "exchanged"


# Allowed transitions keyed by source status.
# Each value is a tuple of (target status, default reason).
ALLOWED_TRANSITIONS: dict[BookStatus, dict[BookStatus, str]] = {
    BookStatus.AVAILABLE: {
        BookStatus.RESERVED: "book requested by another participant",
        BookStatus.LOANED: "book handed over for exchange",
    },
    BookStatus.RESERVED: {
        BookStatus.LOANED: "reservation accepted, book handed over",
        BookStatus.AVAILABLE: "reservation withdrawn",
    },
    BookStatus.LOANED: {
        BookStatus.RETURNED: "book returned to owner",
        BookStatus.EXCHANGED: "exchange completed",
    },
    BookStatus.RETURNED: {
        BookStatus.AVAILABLE: "book back on shelf",
    },
    BookStatus.EXCHANGED: {
        BookStatus.AVAILABLE: "book back on shelf",
    },
}


@dataclass
class Book:
    title: str
    author: str
    owner: str
    status: BookStatus = BookStatus.AVAILABLE
    history: list[tuple[BookStatus, str | None]] = field(default_factory=list)


class InvalidTransitionError(ValueError):
    """Raised when a requested status change is not permitted."""


def change_book_status(book: Book, new_status: BookStatus, reason: str | None = None) -> BookStatus:
    """Attempt to change the status of a book.

    Validates the transition and records the reason in the book history.
    Returns the book's new status or raises InvalidTransitionError.
    """
    current = book.status

    if current == new_status:
        raise InvalidTransitionError(
            f"status already '{new_status.value}' for book '{book.title}'"
        )

    if new_status not in ALLOWED_TRANSITIONS.get(current, {}):
        raise InvalidTransitionError(
            f"transition from '{current.value}' to '{new_status.value}' "
            f"is not allowed for book '{book.title}'"
        )

    book.status = new_status
    book.history.append((new_status, reason))
    return new_status
