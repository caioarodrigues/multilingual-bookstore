from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserUpdate
from core.security import hash_password
from typing import List
from models.book import Book


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()

    def get_user_by_id(self, id: int) -> User:
        return self.db.query(User).filter(User.id == id).first()

    def get_all_users(self) -> List[User]:
        return self.db.query(User).all()

    def create_user(self, user: UserCreate) -> User:
        db_user = User(
            email=user.email,
            hashed_password=hash_password(user.password),
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete_user_by_id(self, id: int):
        user = self.get_user_by_id(id)
        self.db.delete(user)
        self.db.commit()
        return user

    def update_user(self, id: int, user_data: UserUpdate) -> User:
        user = self.get_user_by_id(id)
        for key, value in user_data.items():
            setattr(user, key, value)
        self.db.commit()
        self.db.refresh(user)
        return user

    def list_saved_books(self, user_id: int):
        user = self.get_user_by_id(user_id)
        return user.saved_books

    def save_book(self, user_id: int, book_id: int):
        user = self.get_user_by_id(user_id)
        book = self.db.query(Book).filter(Book.id == book_id).first()
        user.saved_books.append(book)
        self.db.commit()
        self.db.refresh(user)
        return user.saved_books

    def get_user_created_books(self, user_id: int):
        books = self.db.query(Book).filter(Book.author_id == user_id).all()
        return books
