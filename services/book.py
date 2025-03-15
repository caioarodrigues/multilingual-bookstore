from typing import Optional, List
from models.book import Book
from repositories.book import BookRepository
from schemas.book import BookCreate
from fastapi import HTTPException

class BookService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def create_book(self, book_data: BookCreate, owner_id: int) -> Book:
        return self.book_repository.create_book(book_data.dict(), owner_id)

    def get_all_books(self, start_index: int, end_index: int) -> List[Book]:
        return self.book_repository.get_all_books(start_index, end_index)