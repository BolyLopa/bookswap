# === Stage 12: Постраничный вывод ===
# Project: BookSwap
def paginate_books(books, page=1, page_size=10):
    if page < 1:
        page = 1
    if page_size < 1:
        page_size = 1
    total = len(books)
    start = (page - 1) * page_size
    end = start + page_size
    return books[start:end], total, page
