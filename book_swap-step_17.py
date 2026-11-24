# === Stage 17: Избранное ===
# Project: BookSwap
from datetime import datetime


class Book:
    def __init__(self, title, author, owner, condition):
        self.title = title
        self.author = author
        self.owner = owner
        self.condition = condition
        self.is_favorite = False
        self.favorite_added_at = None

    def add_favorite(self):
        if self.is_favorite:
            return
        self.is_favorite = True
        self.favorite_added_at = datetime.now()

    def remove_favorite(self):
        if not self.is_favorite:
            return
        self.is_favorite = False
        self.favorite_added_at = None

    def __repr__(self):
        return f"Book(title={self.title!r}, is_favorite={self.is_favorite})"


class FavoriteBookList:
    def __init__(self):
        self._books = []

    def add(self, book):
        if book in self._books:
            return
        self._books.append(book)

    def remove(self, book):
        if book in self._books:
            self._books.remove(book)

    def __contains__(self, book):
        return book in self._books

    def __len__(self):
        return len(self._books)

    def __iter__(self):
        return iter(self._books)

    def __repr__(self):
        return f"FavoriteBookList(count={len(self._books)})"


if __name__ == "__main__":
    my_book = Book("1984", "George Orwell", "alice", "good")
    their_book = Book("Dune", "Frank Herbert", "bob", "good")

    list_of_favorites = FavoriteBookList()

    my_book.add_favorite()
    their_book.remove_favorite()

    list_of_favorites.add(my_book)
    list_of_favorites.add(their_book)

    print(my_book)
    print(their_book)
    print(my_book.is_favorite)
    print(their_book.is_favorite)
    print(list_of_favorites)
    print(list(my_book.favorite_added_at))
    print(my_book.favorite_added_at)

    list_of_favorites.remove(my_book)
    print(list_of_favorites)

    list_of_favorites.add(my_book)
    list_of_favorites.add(my_book)
    print(list_of_favorites)
