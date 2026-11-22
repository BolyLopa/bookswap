# === Stage 11: Группировка ===
# Project: BookSwap
from collections import defaultdict


def group_books_by_author(books):
    groups = defaultdict(list)
    counts = defaultdict(int)
    for book in books:
        author = book["author"]
        groups[author].append(book)
        counts[author] += 1
    return groups, counts


def print_author_summary(books):
    groups, counts = group_books_by_author(books)
    for author in sorted(counts, key=lambda name: (-counts[name], name)):
        print(f"{author}: {counts[author]} book(s)")


if __name__ == "__main__":
    sample_books = [
        {"title": "Dune", "author": "Herbert", "owner": "Alice", "state": "read"},
        {"title": "Neuromancer", "author": "Gibson", "owner": "Bob", "state": "new"},
        {"title": "Foundation", "author": "Asimov", "owner": "Carol", "state": "read"},
        {"title": "I, Robot", "author": "Asimov", "owner": "Dave", "state": "new"},
        {"title": "The Hitchhiker's Guide", "author": "Douglas Adams", "owner": "Eve", "state": "read"},
        {"title": "Slaughterhouse-Five", "author": "Vonnegut", "owner": "Frank", "state": "new"},
    ]
    print_author_summary(sample_books)
