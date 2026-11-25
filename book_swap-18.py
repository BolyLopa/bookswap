# === Stage 18: Статусы записей ===
# Project: BookSwap
from enum import Enum


class BookStatus(Enum):
    """Lifecycle statuses for a book."""

    NEW = "new"
    BORROWED = "borrowed"
    EXCHANGED = "exchanged"
    DAMAGED = "damaged"
    WITHDRAWN = "withdrawn"


def valid_transitions(statuses):
    """Return allowed next statuses for a given current status."""

    transitions = {
        BookStatus.NEW: {BookStatus.BORROWED, BookStatus.WITHDRAWN},
        BookStatus.BORROWED: {BookStatus.EXCHANGED, BookStatus.DAMAGED, BookStatus.WITHDRAWN},
        BookStatus.EXCHANGED: {BookStatus.NEW, BookStatus.WITHDRAWN},
        BookStatus.DAMAGED: {BookStatus.WITHDRAWN},
        BookStatus.WITHDRAWN: set(),
    }

    return transitions.get(status, set())


def can_transition(current_status, next_status):
    """Check whether next_status is a valid transition from current_status."""

    if not isinstance(current_status, BookStatus):
        return False
    if not isinstance(next_status, BookStatus):
        return False
    return next_status in valid_transitions(current_status)


def next_status_options(current_status):
    """Return a sorted list of allowed next statuses for a current status."""

    return sorted(valid_transitions(current_status), key=lambda s: s.name)


def transition_book(book_status, next_status):
    """Attempt a status transition and report validity."""

    if not can_transition(book_status, next_status):
        return False, f"Invalid transition: {book_status.value} -> {next_status.value}"
    return True, f"Transition allowed: {book_status.value} -> {next_status.value}"


def transition_status(current_status, next_status):
    """Return the resulting status if valid, otherwise raise ValueError."""

    if not can_transition(current_status, next_status):
        raise ValueError(
            f"Invalid transition: {current_status.value} -> {next_status.value}"
        )
    return next_status
