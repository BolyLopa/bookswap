# === Stage 9: Сортировка записей ===
# Project: BookSwap
def sort_books_by_title(books, reverse=False):
    return sorted(books, key=lambda book: book["title"], reverse=reverse)


def sort_books_by_created_at(books, reverse=False):
    return sorted(books, key=lambda book: book["created_at"], reverse=reverse)


def sort_books(books, field="title", reverse=False):
    if field == "title":
        return sort_books_by_title(books, reverse=reverse)
    if field == "created_at":
        return sort_books_by_created_at(books, reverse=reverse)
    raise ValueError(f"Unknown sort field: {field!r}")
