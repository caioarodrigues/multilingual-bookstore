from fastapi import APIRouter, Depends, HTTPException
from services.book import BookService
from repositories.book import BookRepository
from core.database import get_db
from schemas.book import BookCreate, BookResponse
from sqlalchemy.orm import Session
from models.user import User

# from core.security import get_current_user

book_router = APIRouter(prefix="/books", tags=["books"])


@book_router.post("/author_id={user_id}", response_model=BookResponse)
def create_book(
    book_data: BookCreate,
    user_id: int,
    db: Session = Depends(get_db),
    # current_user: User = Depends(get_current_user)
):
    book_service = BookService(BookRepository(db))
    return book_service.create_book(book_data, user_id)
