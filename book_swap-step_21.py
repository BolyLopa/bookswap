# === Stage 21: Просмотр истории ===
# Project: BookSwap
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class Book:
    title: str
    author: str
    owner_id: int
    status: str = "on shelf"
    history: List[dict] = field(default_factory=list)

    def add_record(self, record: dict) -> None:
        entry = dict(record)
        entry["timestamp"] = datetime.now().isoformat()
        self.history.append(entry)

    def compact_view(self, limit: int = 5) -> str:
        lines = [f"Title: {self.title}", f"Author: {self.author}",
                 f"Owner: {self.owner_id}", f"Status: {self.status}"]
        if self.history:
            lines.append("History:")
            for entry in self.history[-limit:]:
                lines.append(f"  - {entry.get('action', 'unknown')} "
                             f"({entry.get('timestamp', '?')})")
        return "\n".join(lines)


def print_book_record(book: Book) -> None:
    print(book.compact_view())


def create_sample_book() -> Book:
    book = Book(title="The Great Gatsby", author="F. Scott Fitzgerald",
                owner_id=101)
    book.add_record({"action": "added to shelf"})
    book.add_record({"action": "borrowed", "by": 202})
    book.add_record({"action": "returned"})
    return book


if __name__ == "__main__":
    sample = create_sample_book()
    print_book_record(sample)
