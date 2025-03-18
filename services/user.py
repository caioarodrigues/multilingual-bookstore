from repositories.user import UserRepository
from core.database import get_db
from schemas.user import UserCreate, UserResponse
from typing import List
from fastapi import HTTPException


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user_data: UserCreate) -> UserResponse:
        try:
            new_user = self.user_repository.create_user(user_data)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        return new_user

    def update_user(self, user_id: int, user_data: UserCreate) -> UserResponse:
        try:
            user = self.user_repository.update_user(user_id, user_data.dict())
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        return user

    def get_user_by_id(self, user_id: int) -> UserResponse:
        user = self.user_repository.get_user_by_id(user_id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return user

    def get_by_email(self, email: str) -> UserResponse:
        user = self.user_repository.get_user_by_email(email)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return user

    def get_all_users(self) -> List[UserResponse]:
        return self.user_repository.get_all_users()

    def delete_user(self, user_id: int):
        try:
            deleted_user = self.user_repository.delete_user_by_id(user_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        return deleted_user

    def list_saved_books(self, user_id: int):
        try:
            saved_books = self.user_repository.list_saved_books(user_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        return saved_books

    def save_book(self, user_id: int, book_id: int):
        try:
            saved_book = self.user_repository.save_book(user_id, book_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        return saved_book
