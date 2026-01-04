from app.dao.book_dao import BookDAO
from app.models.book_models import Book


class BookService:
    def __init__(self, dao: BookDAO) -> None:
        self._dao = dao

    def list_books(self) -> list[Book]:
        return self._dao.list()

    def get_book(self, book_id: int) -> Book | None:
        return self._dao.get_by_id(book_id)

    def add_book(self, title: str, author: str) -> Book:
        return self._dao.create(title=title, author=author)
