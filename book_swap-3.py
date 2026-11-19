# === Stage 3: Хранилище в памяти ===
# Project: BookSwap
from typing import Dict, List, Optional


class Book:
    def __init__(self, book_id: str, title: str, author: str, owner: str,
                 condition: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.owner = owner
        self.condition = condition

    def __repr__(self) -> str:
        return (f"Book(id={self.book_id!r}, title={self.title!r}, "
                f"author={self.author!r}, owner={self.owner!r}, "
                f"condition={self.condition!r})")


class BookStore:
    def __init__(self) -> None:
        self._books: Dict[str, Book] = {}

    def add_book(self, book: Book) -> Book:
        if book.book_id in self._books:
            raise ValueError(f"Book id {book.book_id!r} already exists")
        self._books[book.book_id] = book
        return book

    def get_book(self, book_id: str) -> Optional[Book]:
        return self._books.get(book_id)

    def list_books(self) -> List[Book]:
        return list(self._books.values())

    def list_books_by_owner(self, owner: str) -> List[Book]:
        return [book for book in self._books.values() if book.owner == owner]

    def update_condition(self, book_id: str, condition: str) -> bool:
        book = self.get_book(book_id)
        if book is None:
            return False
        book.condition = condition
        return True


if __name__ == "__main__":
    store = BookStore()
    store.add_book(Book("b1", "1984", "George Orwell", "alice", "new"))
    store.add_book(Book("b2", "Dune", "Frank Herbert", "bob", "used"))
    print(store.list_books())
    print(store.get_book("b2"))
    print(store.list_books_by_owner("alice"))
    print(store.update_condition("b1", "damaged"))
    print(store.get_book("b1"))
