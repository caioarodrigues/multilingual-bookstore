from typing import Optional, List
from sqlalchemy.orm import Session
from models.book import Book


class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_book(self, book_id: int) -> Optional[Book]:
        return self.db.query(Book).filter(Book.id == book_id).first()

    def get_all_books(self, start_index: int, end_index: int) -> List[Book]:
        return self.db.query(Book).slice(start_index, end_index).all()

    def create_book(self, book_data: dict, owner_id: int) -> Book:
        db_book = Book(**book_data, owner_id=owner_id)
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)
        return db_book
