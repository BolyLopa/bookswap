# === Stage 4: Редактирование записей ===
# Project: BookSwap
"""BookSwap stage 4: editing the 'book' entity by its identifier.

This module adds an update operation for the 'book' entity. Only
permitted fields may be modified. The change is validated before being
applied so that a request cannot silently corrupt an existing record.
"""

ALLOWED_BOOK_FIELDS = ("title", "author", "owner", "status")


class BookEntityError(Exception):
    """Raised when a book update request is invalid."""


def update_book_by_id(books, book_id, changes):
    """Return the books mapping after applying a valid edit.

    The function validates the incoming request and mutates the
    provided 'books' mapping in place. It does not create new entries;
    only an existing record can be edited.

    Parameters
    ----------
    books:
        Mapping of book identifier to a mutable book record.
    book_id:
        Identifier of the book that should be updated.
    changes:
        Mapping of field name to new value.

    Returns
    -------
    dict
        The same 'books' mapping, modified in place.

    Raises
    ------
    BookEntityError
        If 'changes' is empty, contains unknown fields, or if the
        requested 'book_id' does not exist.
    """
    if not isinstance(changes, dict):
        raise BookEntityError("changes must be a mapping of field to value")

    if not changes:
        raise BookEntityError("no fields were provided for the update")

    for field in changes:
        if field not in ALLOWED_BOOK_FIELDS:
            raise BookEntityError(
                "field {!r} is not allowed for a book update".format(field)
            )

    if book_id not in books:
        raise BookEntityError("book with id {!r} does not exist".format(book_id))

    for field, value in changes.items():
        books[book_id][field] = value

    return books
