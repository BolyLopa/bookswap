# === Stage 23: Недельный отчёт ===
# Project: BookSwap
def render_book_report(books, days=7):
    lines = []
    lines.append("WEEKLY BOOK SWAP REPORT")
    lines.append("=" * 60)
    if not books:
        lines.append("No books found.")
        return "\n".join(lines)
    lines.append(f"Reporting period: {days} days")
    lines.append("")
    for book in books:
        lines.append(render_book_row(book, days))
    return "\n".join(lines)


def render_book_row(book, days):
    title = book.get("title", "N/A")
    author = book.get("author", "N/A")
    owner = book.get("owner", "N/A")
    status = book.get("status", "N/A")
    applied = book.get("applied", 0)
    granted = book.get("granted", 0)
    lines = [
        f"Title: {title}",
        f"Author: {author}",
        f"Owner: {owner}",
        f"Status: {status}",
        f"Applied: {applied}",
        f"Granted: {granted}",
        f"Granted rate: {granted / applied * 100:.1f}%" if applied else "Granted rate: 0.0%",
        f"Active requests: {book.get('active_requests', 0)}",
        f"Pending days: {book.get('pending_days', 0)}",
        "",
    ]
    return "\n".join(lines)


def render_request_report(requests, days=7):
    lines = []
    lines.append("WEEKLY REQUEST REPORT")
    lines.append("=" * 60)
    if not requests:
        lines.append("No requests found.")
        return "\n".join(lines)
    lines.append(f"Reporting period: {days} days")
    lines.append("")
    for request in requests:
        lines.append(render_request_row(request))
    return "\n".join(lines)


def render_request_row(request):
    request_id = request.get("id", "N/A")
    book_title = request.get("book_title", "N/A")
    requester = request.get("requester", "N/A")
    owner = request.get("owner", "N/A")
    status = request.get("status", "N/A")
    created = request.get("created", "N/A")
    deadline = request.get("deadline", "N/A")
    lines = [
        f"Request ID: {request_id}",
        f"Book: {book_title}",
        f"Requester: {requester}",
        f"Owner: {owner}",
        f"Status: {status}",
        f"Created: {created}",
        f"Deadline: {deadline}",
        f"Days until deadline: {request.get('days_until_deadline', 0)}",
        "",
    ]
    return "\n".join(lines)


def summarize_report(books, requests, days=7):
    lines = []
    lines.append("WEEKLY SWAP SUMMARY")
    lines.append("=" * 60)
    total_books = len(books)
    total_requests = len(requests)
    active_requests = sum(1 for r in requests if r.get("status") == "active")
    granted_requests = sum(1 for r in requests if r.get("status") == "granted")
    lines.append(f"Total books: {total_books}")
    lines.append(f"Total requests: {total_requests}")
    lines.append(f"Active requests: {active_requests}")
    lines.append(f"Granted requests: {granted_requests}")
    if total_requests:
        lines.append(f"Grant rate: {granted_requests / total_requests * 100:.1f}%")
    else:
        lines.append("Grant rate: 0.0%")
    lines.append("")
    urgent = [r for r in requests if r.get("days_until_deadline", 99) <= 2]
    if urgent:
        lines.append("URGENT (deadline within 2 days):")
        for r in urgent:
            lines.append(f"  Request {r.get('id')}: {r.get('book_title')} by {r.get('requester')}")
    return "\n".join(lines)
