from typing import List, Dict, Any, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from repositories.book import BookRepository
from models.book import Book
from schemas.book import (
    BookCreate,
    BookUpdate,
    Book as BookSchema,
    BookWithDetails,
    BookSave,
)


class BookService:
    def __init__(self):
        self.repository = BookRepository(Book)

    def get(self, db: Session, book_id: int) -> BookSchema:
        book = self.repository.get(db, id=book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Book with ID {book_id} not found",
            )
        return book

    def get_with_details(self, db: Session, book_id: int) -> BookWithDetails:
        book = self.repository.get_with_details(db, id=book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Book with ID {book_id} not found",
            )
        return book

    def get_multi(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 100,
        author_id: Optional[int] = None,
    ) -> List[BookSchema]:
        filters = {}
        if author_id is not None:
            filters["author_id"] = author_id
        return self.repository.get_multi(db, skip=skip, limit=limit, filters=filters)

    def create(self, db: Session, book_in: BookCreate) -> BookSchema:
        return self.repository.create_with_languages(db, obj_in=book_in)

    def update(self, db: Session, book_id: int, book_in: BookUpdate) -> BookSchema:
        book = self.repository.get(db, id=book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Book with ID {book_id} not found",
            )
        return self.repository.update_with_languages(db, db_obj=book, obj_in=book_in)

    def delete(self, db: Session, book_id: int) -> BookSchema:
        book = self.repository.get(db, id=book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Book with ID {book_id} not found",
            )
        return self.repository.remove(db, id=book_id)

    def save_for_user(
        self, db: Session, user_id: int, book_save: BookSave
    ) -> BookSchema:
        book = self.repository.get(db, id=book_save.book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Book with ID {book_save.book_id} not found",
            )
        return self.repository.save_for_user(db, user_id=user_id, book_save=book_save)

    def get_saved_books_for_user(
        self, db: Session, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Dict[str, Any]]:
        return self.repository.get_saved_books_for_user(
            db, user_id=user_id, skip=skip, limit=limit
        )
