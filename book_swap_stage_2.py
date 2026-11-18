# === Stage 2: Проверка полей ===
# Project: BookSwap
def normalize_book_title(value):
    if value is None:
        raise ValueError("Title must be provided.")
    text = str(value).strip()
    if not text:
        raise ValueError("Title cannot be empty.")
    if len(text) > 200:
        raise ValueError("Title is too long (max 200 characters).")
    return text


def normalize_author(value):
    if value is None:
        raise ValueError("Author must be provided.")
    text = str(value).strip()
    if not text:
        raise ValueError("Author cannot be empty.")
    if len(text) > 150:
        raise ValueError("Author is too long (max 150 characters).")
    return text


def normalize_owner(value):
    if value is None:
        raise ValueError("Owner must be provided.")
    text = str(value).strip()
    if not text:
        raise ValueError("Owner cannot be empty.")
    return text


def normalize_condition(value):
    allowed = {"available", "reserved", "borrowed", "damaged", "lost"}
    if value is None:
        raise ValueError("Condition must be provided.")
    text = str(value).strip().lower()
    if not text:
        raise ValueError("Condition cannot be empty.")
    if text not in allowed:
        raise ValueError(
            f"Condition must be one of: {', '.join(sorted(allowed))}."
        )
    return text


def validate_book(book):
    title = book.get("title")
    author = book.get("author")
    owner = book.get("owner")
    condition = book.get("condition")

    problems = []

    try:
        normalized_title = normalize_book_title(title)
    except ValueError as error:
        problems.append(error)

    try:
        normalized_author = normalize_author(author)
    except ValueError as error:
        problems.append(error)

    if owner is None:
        problems.append(ValueError("Owner must be provided."))
    elif not str(owner).strip():
        problems.append(ValueError("Owner cannot be empty."))

    try:
        normalized_condition = normalize_condition(condition)
    except ValueError as error:
        problems.append(error)

    if problems:
        message = "Invalid book:"
        for problem in problems:
            message += f"\n  - {problem}"
        raise ValueError(message)

    return {
        "title": normalized_title,
        "author": normalized_author,
        "owner": str(owner).strip(),
        "condition": normalized_condition,
    }
