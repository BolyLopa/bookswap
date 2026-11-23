# === Stage 13: Быстрые фильтры ===
# Project: BookSwap
from datetime import datetime, timedelta


def today_record(record):
    return record["due_date"] == datetime.now().date()


def this_week_record(record, now=None):
    if now is None:
        now = datetime.now()
    start = now.date() - timedelta(days=now.weekday())
    end = start + timedelta(days=6)
    return start <= record["due_date"].date() <= end


def overdue_record(record, now=None):
    if now is None:
        now = datetime.now()
    return record["due_date"] < now.date()


def filter_records(records, filter_type):
    if filter_type == "today":
        return [r for r in records if today_record(r)]
    elif filter_type == "this_week":
        return [r for r in records if this_week_record(r)]
    elif filter_type == "overdue":
        return [r for r in records if overdue_record(r)]
    return []


if __name__ == "__main__":
    sample = [
        {"title": "A", "due_date": datetime.now().date()},
        {"title": "B", "due_date": datetime.now().date() + timedelta(days=5)},
        {"title": "C", "due_date": datetime.now().date() + timedelta(days=30)},
        {"title": "D", "due_date": datetime.now().date() - timedelta(days=1)},
    ]
    print(filter_records(sample, "today"))
    print(filter_records(sample, "this_week"))
    print(filter_records(sample, "overdue"))
