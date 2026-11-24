# === Stage 15: Слияние записей ===
# Project: BookSwap
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Book:
    title: str
    author: str
    owner: str
    status: str


@dataclass
class Claim:
    claim_id: int
    book_title: str
    owner_id: str
    requested_date: str
    status: str


def merge_books(book_a: Book, book_b: Book, field_names: list[str]) -> Book:
    merged = dict(book_a)
    for name in field_names:
        if name in merged:
            merged[name] = book_b.__dict__[name]
    return Book(**merged)


def choose_winner(
    field_name: str,
    book_a: Book,
    book_b: Book,
    preference: str,
) -> Any:
    value_a = getattr(book_a, field_name)
    value_b = getattr(book_b, field_name)
    if preference == "first":
        return value_a
    if preference == "second":
        return value_b
    if preference == "by_length":
        return value_a if len(str(value_a)) >= len(str(value_b)) else value_b
    if preference == "by_author":
        author_a = getattr(book_a, "author")
        author_b = getattr(book_b, "author")
        return value_a if author_a <= author_b else value_b
    if preference == "by_owner":
        owner_a = getattr(book_a, "owner")
        owner_b = getattr(book_b, "owner")
        return value_a if owner_a <= owner_b else value_b
    raise ValueError(f"Unknown preference: {preference}")


def combine_books(
    book_a: Book,
    book_b: Book,
    field_names: list[str],
    preferences: dict[str, str],
) -> Book:
    merged = dict(book_a)
    for name in field_names:
        merged[name] = choose_winner(name, book_a, book_b, preferences.get(name, "first"))
    return Book(**merged)


if __name__ == "__main__":
    a = Book("Dune", "Frank Herbert", "alice", "available")
    b = Book("1984", "George Orwell", "bob", "reserved")

    combined = combine_books(
        a,
        b,
        field_names=["title", "author", "owner", "status"],
        preferences={
            "title": "by_length",
            "author": "by_author",
            "owner": "by_owner",
            "status": "first",
        },
    )
    for attr in ["title", "author", "owner", "status"]:
        print(f"{attr}: {getattr(combined, attr)}")
