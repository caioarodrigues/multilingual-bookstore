from fastapi import APIRouter, Depends, HTTPException
from services.user import UserService
from repositories.user import UserRepository
from core.database import get_db
from schemas.user import UserCreate, UserResponse, UserDefaultSchema
from schemas.book import BookResponse
from sqlalchemy.orm import Session
from typing import List

user_router = APIRouter(prefix="/users", tags=["users"])


def get_user_service(db: Session = Depends(get_db)):
    return UserService(UserRepository(db))


@user_router.post("/", response_model=UserDefaultSchema)
def create_user(
    user_data: UserCreate, user_service: UserService = Depends(get_user_service)
):
    return user_service.create_user(user_data)


@user_router.post("/books/save")
def save_book(
    user_id: int, book_id: int, user_service: UserService = Depends(get_user_service)
):
    return user_service.save_book(user_id, book_id)


@user_router.get("/books/list-all")
def list_saved_books(
    user_id: int, user_service: UserService = Depends(get_user_service)
):
    return user_service.list_saved_books(user_id)


@user_router.get("/me", response_model=UserDefaultSchema)
def get_self_info(user_id: int, user_service: UserService = Depends(get_user_service)):
    return user_service.get_user_by_id(user_id)


@user_router.get("/{id}/books", response_model=List[BookResponse])
def get_user_created_books(
    id: int, user_service: UserService = Depends(get_user_service)
):
    return user_service.get_user_created_books(id)


@user_router.get("/list-all", response_model=List[UserDefaultSchema])
def get_all_users(user_service: UserService = Depends(get_user_service)):
    return user_service.get_all_users()


@user_router.get("/{user_id}", response_model=UserDefaultSchema)
def get_user_by_id(user_id: int, user_service: UserService = Depends(get_user_service)):
    return user_service.get_user_by_id(user_id)


@user_router.delete("/{user_id}")
def delete_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    return user_service.delete_user(user_id)


@user_router.patch("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user_data: UserCreate,
    user_service: UserService = Depends(get_user_service),
):
    return user_service.update_user(user_id, user_data)
