from fastapi import APIRouter, Depends, HTTPException
from services.book import BookService
from repositories.book import BookRepository
from core.database import get_db
from schemas.book import BookCreate, BookResponse
from sqlalchemy.orm import Session
from models.user import User
from typing import List

book_router = APIRouter(prefix="/books", tags=["books"])

def get_book_service(db: Session = Depends(get_db)):
    return BookService(BookRepository(db))

@book_router.post("/add", response_model=BookResponse)
def create_book(
    book_data: BookCreate,
    user_id: int,
    book_service: BookService = Depends(get_book_service),
):
    return book_service.create_book(book_data, user_id)

@book_router.get("/", response_model=List[BookResponse])
def get_all_books(book_service: BookService = Depends(get_book_service), start_index: int = 0, end_index: int = 10):
    return book_service.get_all_books(start_index, end_index)