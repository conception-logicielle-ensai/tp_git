
from sqlalchemy.orm import Session

from app.models.book_models import Book


class BookDAO:
    def __init__(self, session: Session) -> None:
        self.session = session

    def list(self) -> list[Book]:
        return self.session.query(Book).all()

    def get_by_id(self, book_id: int) -> Book | None:
        return self.session.get(Book, book_id)

    def create(self, title: str, author: str) -> Book:
        book = Book(title=title, author=author)
        self.session.add(book)
        self.session.commit()
        self.session.refresh(book)
        return book
