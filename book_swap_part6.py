# === Stage 6: Связанная сущность ===
# Project: BookSwap
import uuid


class Request:
    def __init__(self, book_id, owner_id, title, author):
        self.id = str(uuid.uuid4())
        self.book_id = book_id
        self.owner_id = owner_id
        self.title = title
        self.author = author
        self.status = "pending"

    def accept(self):
        self.status = "accepted"

    def reject(self):
        self.status = "rejected"

    def __repr__(self):
        return f"Request(id={self.id}, book_id={self.book_id}, owner_id={self.owner_id}, title={self.title}, status={self.status})"


def add_request(requests, book_id, owner_id, title, author):
    new_request = Request(book_id, owner_id, title, author)
    requests.append(new_request)
    return new_request


def find_request(requests, book_id, owner_id):
    for request in requests:
        if request.book_id == book_id and request.owner_id == owner_id:
            return request
    return None


def pending_requests(requests):
    return [request for request in requests if request.status == "pending"]


def accepted_requests(requests):
    return [request for request in requests if request.status == "accepted"]


def reject_request(requests, book_id, owner_id):
    request = find_request(requests, book_id, owner_id)
    if request:
        request.reject()
    return request


def requests_for_book(requests, book_id):
    return [request for request in requests if request.book_id == book_id]


if __name__ == "__main__":
    sample_requests = []
    request = add_request(sample_requests, "book-001", "user-123", "The Great Gatsby", "F. Scott Fitzgerald")
    print(request)
    print(pending_requests(sample_requests))
    print(requests_for_book(sample_requests, "book-001"))
