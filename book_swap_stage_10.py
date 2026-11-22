# === Stage 10: Теги ===
# Project: BookSwap
from collections import defaultdict


class Tag:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Tag({self.name!r})"

    def __eq__(self, other):
        return isinstance(other, Tag) and other.name == self.name

    def __hash__(self):
        return hash(self.name)


class Book:
    def __init__(self, title, author, owner, status):
        self.title = title
        self.author = author
        self.owner = owner
        self.status = status
        self.tags = set()

    def add_tag(self, tag):
        self.tags.add(tag)

    def remove_tag(self, tag):
        self.tags.discard(tag)

    def has_tag(self, tag):
        return tag in self.tags

    def __repr__(self):
        return (
            f"Book(title={self.title!r}, author={self.author!r}, "
            f"owner={self.owner!r}, status={self.status!r}, "
            f"tags={sorted(self.tags)!r})"
        )


def find_books_by_tag(books, tag):
    return [book for book in books if book.has_tag(tag)]


if __name__ == "__main__":
    python_books = [
        Book("Grokking Algorithms", "Aditya Bhargava", "alice", "available"),
        Book("Automate the Boring Stuff", "Al Sweigart", "bob", "reserved"),
        Book("Python Crash Course", "Eric Matthes", "carol", "available"),
    ]

    mystery_books = [
        Book("The Silent Patient", "Alex Michaelides", "dave", "available"),
        Book("Gone Girl", "Gillian Flynn", "alice", "reserved"),
        Book("Big Little Lies", "Liane Moriarty", "bob", "available"),
    ]

    all_books = python_books + mystery_books

    target = Tag("python")
    matches = find_books_by_tag(all_books, target)
    print(f"Books tagged '{target.name}':")
    for book in matches:
        print(" ", book)

    book = python_books[0]
    book.add_tag(Tag("algorithm"))
    print("After adding 'algorithm' tag:", book)

    book.remove_tag(Tag("algorithm"))
    print("After removing 'algorithm' tag:", book)
