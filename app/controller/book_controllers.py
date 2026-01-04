from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_book_service
from app.dto.book_dto import BookCreate, BookRead
from app.services.book_services import BookService

book_router = APIRouter(prefix="/books", tags=["Books"])


@book_router.get("/", response_model=list[BookRead])
def get_books(service: BookService = Depends(get_book_service)):
    return service.list_books()


@book_router.get("/{book_id}", response_model=BookRead)
def get_book(book_id: int, service: BookService = Depends(get_book_service)):
    book = service.get_book(book_id)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )

    return book


@book_router.post(
    "/",
    response_model=BookRead,
    status_code=status.HTTP_201_CREATED,
)
def create_book(
    book: BookCreate,
    service: BookService = Depends(get_book_service),
):
    return service.add_book(
        title=book.title,
        author=book.author,
    )
