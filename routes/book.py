from fastapi import APIRouter, Depends, HTTPException
from services.book import BookService
from repositories.book import BookRepository
from core.database import get_db
from core.dependencies import get_current_active_user
from schemas.book import BookCreate, BookResponse
from sqlalchemy.orm import Session
from models.user import User
from typing import List

book_router = APIRouter(prefix="/books", tags=["books"])


def get_book_service(db: Session = Depends(get_db)):
    return BookService()


@book_router.post("/add", response_model=BookResponse)
def create_book(
    book_input: BookCreate,
    db: Session = Depends(get_db),
    # current_user: User = Depends(get_current_active_user),
    book_service: BookService = Depends(get_book_service),
):
    # if book_input.author_id is None:
    #    book_input.author_id = current_user.id

    return book_service.create(db, book_input)


@book_router.get("/", response_model=List[BookResponse])
def get_all_books(
    book_service: BookService = Depends(get_book_service),
    db: Session = Depends(get_db),
    start_index: int = 0,
    end_index: int = 10,
):
    return book_service.get_multi(db=db, skip=start_index, limit=end_index)


@book_router.get("/{book_id}", response_model=BookResponse)
def get_book_by_id(
    book_id: int,
    book_service: BookService = Depends(get_book_service),
    db: Session = Depends(get_db),
):
    book = book_service.get(db=db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@book_router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    book_input: BookCreate,
    book_service: BookService = Depends(get_book_service),
    db: Session = Depends(get_db),
    # current_user: User = Depends(get_current_active_user),
):
    book = book_service.get(db=db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    # if book.author_id != current_user.id:
    #    raise HTTPException(
    #        status_code=403, detail="Not authorized to update this book"
    #    )
    return book_service.update(db=db, book_id=book_id, book_in=book_input)


@book_router.delete("/{book_id}", response_model=BookResponse)
def delete_book(
    book_id: int,
    book_service: BookService = Depends(get_book_service),
    db: Session = Depends(get_db),
    # current_user: User = Depends(get_current_active_user),
):
    book = book_service.get(db=db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    # if book.author_id != current_user.id:
    #    raise HTTPException(
    #        status_code=403, detail="Not authorized to delete this book"
    #    )
    return book_service.delete(db=db, book_id=book_id)
