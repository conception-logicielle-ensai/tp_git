from collections.abc import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from app.dao.book_dao import BookDAO
from app.db.database import SessionLocal
from app.services.book_services import BookService


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_book_service(db: Session = Depends(get_db)) -> BookService:
    return BookService(BookDAO(db))
