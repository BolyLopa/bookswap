# === Stage 22: Общая сводка ===
# Project: BookSwap
from collections import Counter


def summarize_books(books):
    """Return a summary of the collection: total count, authors distribution and the most recent records."""
    if not books:
        return {"total": 0, "authors": {}, "recent": []}

    total = len(books)
    authors = Counter(book["author"] for book in books)
    most_recent = sorted(books, key=lambda book: book["updated_at"], reverse=True)[:5]

    return {
        "total": total,
        "authors": dict(authors.most_common()),
        "recent": most_recent,
    }


def top_authors(books, limit=3):
    """Return the authors with the most books, ordered from most to least frequent."""
    if not books:
        return []

    authors = Counter(book["author"] for book in books)
    return authors.most_common(limit)


def latest_books(books, limit=5):
    """Return the most recently updated books, ordered from newest to oldest."""
    if not books:
        return []

    return sorted(books, key=lambda book: book["updated_at"], reverse=True)[:limit]
