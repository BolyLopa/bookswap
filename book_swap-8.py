# === Stage 8: Генерация идентификаторов ===
# Project: BookSwap
"""BookSwap identifier utilities.

Generates unique, prefixed identifiers for books, participants, requests,
and deadlines, with collision detection against already-issued identifiers.
"""

PREFIX_BOOK = "BK"
PREFIX_USER = "US"
PREFIX_REQUEST = "RS"
PREFIX_DEADLINE = "DL"

MAX_ATTEMPTS = 1000


def _is_hex_char(value):
    return value.isalnum() and value.isascii()


def _generate_candidate(prefix, length):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = int.from_bytes(__import__("secrets").token_bytes(length), "big")
    candidate = alphabet[index % len(alphabet) ** length]
    while not _is_hex_char(candidate):
        index = int.from_bytes(__import__("secrets").token_bytes(length), "big")
        candidate = alphabet[index % len(alphabet) ** length]
    return candidate


def generate_unique_id(prefix, length=8, existing=None):
    existing = set(existing or [])
    for _ in range(MAX_ATTEMPTS):
        candidate = _generate_candidate(prefix, length)
        full_id = f"{prefix}-{candidate}"
        if full_id not in existing:
            return full_id
    raise ValueError("Failed to generate a unique identifier after maximum attempts")


def create_book_id(existing_ids):
    return generate_unique_id(PREFIX_BOOK, existing_ids)


def create_user_id(existing_ids):
    return generate_unique_id(PREFIX_USER, existing_ids)


def create_request_id(existing_ids):
    return generate_unique_id(PREFIX_REQUEST, existing_ids)


def create_deadline_id(existing_ids):
    return generate_unique_id(PREFIX_DEADLINE, existing_ids)


if __name__ == "__main__":
    used = set()
    sample_ids = [
        create_book_id(used),
        create_user_id(used),
        create_request_id(used),
        create_deadline_id(used),
    ]
    for identifier in sample_ids:
        print(identifier)
        used.add(identifier)
