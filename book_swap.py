# === Stage 1: Каркас модуля ===
# Project: BookSwap
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    owner: str
    status: str


def create_demo_books() -> list:
    return [
        Book("Atomic Habits", "James Clear", "Alice", "available"),
        Book("The Pragmatic Programmer", "Hunt and Thomas", "Bob", "reserved"),
        Book("Clean Code", "Robert C. Martin", "Carol", "available"),
    ]


def main() -> None:
    books = create_demo_books()
    for book in books:
        print(f"{book.title} by {book.author} — owner: {book.owner}, status: {book.status}")


if __name__ == "__main__":
    main()
