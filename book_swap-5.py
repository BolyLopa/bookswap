# === Stage 5: Удаление и восстановление ===
# Project: BookSwap
from datetime import datetime
from typing import Optional


class BookState:
    ACTIVE = "active"
    SOFT_DELETED = "soft_deleted"


class Book:
    def __init__(self, title: str, author: str, owner_id: str):
        self.id = None
        self.title = title
        self.author = author
        self.owner_id = owner_id
        self.state = BookState.ACTIVE
        self.created_at = datetime.now()
        self.deleted_at: Optional[datetime] = None

    def delete(self) -> bool:
        if self.state != BookState.ACTIVE:
            return False
        self.state = BookState.SOFT_DELETED
        self.deleted_at = datetime.now()
        return True

    def restore(self) -> bool:
        if self.state != BookState.SOFT_DELETED:
            return False
        self.state = BookState.ACTIVE
        self.deleted_at = None
        return True

    def is_deleted(self) -> bool:
        return self.state == BookState.SOFT_DELETED

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title!r}, state={self.state})"
