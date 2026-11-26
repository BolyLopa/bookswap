# === Stage 20: История изменений ===
# Project: BookSwap
from datetime import datetime


class ChangeRecord:
    def __init__(self, change_type, description, timestamp):
        self.change_type = change_type
        self.description = description
        self.timestamp = timestamp

    def __repr__(self):
        return (
            f"ChangeRecord(change_type={self.change_type!r}, "
            f"description={self.description!r}, "
            f"timestamp={self.timestamp!r})"
        )


def make_change_record(change_type, description, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now()
    return ChangeRecord(change_type, description, timestamp)


def format_change_record(record):
    return (
        f"{record.timestamp.isoformat()} | {record.change_type} | {record.description}"
    )


def log_change(book, change_type, description, history=None):
    if history is None:
        history = []
    record = make_change_record(change_type, description)
    history.append(record)
    return history
