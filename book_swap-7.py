# === Stage 7: Связи между сущностями ===
# Project: BookSwap
from datetime import datetime


class Request:
    def __init__(self, request_id, book_id, applicant_id, status, created_at):
        self.request_id = request_id
        self.book_id = book_id
        self.applicant_id = applicant_id
        self.status = status
        self.created_at = created_at

    def to_dict(self):
        return {
            "request_id": self.request_id,
            "book_id": self.book_id,
            "applicant_id": self.applicant_id,
            "status": self.status,
            "created_at": self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at,
        }


class RequestRepository:
    def __init__(self, requests=None):
        self._requests = requests if requests is not None else []

    def add_request(self, request):
        self._requests.append(request)

    def get_all_requests_for_book(self, book_id):
        return [request for request in self._requests if request.book_id == book_id]

    def validate_integrity(self, book_id):
        issues = []

        for request in self.get_all_requests_for_book(book_id):
            if not isinstance(request.request_id, str) or not request.request_id:
                issues.append(f"Request {request.request_id} for book {book_id} has invalid request_id")

            if not isinstance(request.applicant_id, str) or not request.applicant_id:
                issues.append(f"Request {request.request_id} for book {book_id} has invalid applicant_id")

            if request.status not in ("PENDING", "ACCEPTED", "REJECTED", "COMPLETED"):
                issues.append(f"Request {request.request_id} for book {book_id} has invalid status {request.status}")

            if isinstance(request.created_at, datetime) and request.created_at > datetime.now():
                issues.append(f"Request {request.request_id} for book {book_id} has future created_at")

        return issues


if __name__ == "__main__":
    now = datetime.now()
    repo = RequestRepository()
    repo.add_request(Request(1, "book-100", "user-7", "PENDING", now))
    repo.add_request(Request(2, "book-100", "user-9", "ACCEPTED", now))
    repo.add_request(Request(3, "book-200", "user-3", "PENDING", now))

    book_requests = repo.get_all_requests_for_book("book-100")
    print(f"Requests for book-100: {len(book_requests)}")
    for req in book_requests:
        print(req.to_dict())

    print("Integrity issues:", repo.validate_integrity("book-100"))
