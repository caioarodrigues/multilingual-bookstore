from fastapi import APIRouter, Depends, HTTPException
from services.user import UserService
from repositories.user import UserRepository
from core.database import get_db
from schemas.user import UserCreate, UserResponse
from sqlalchemy.orm import Session
from typing import List

user_router = APIRouter()
user_router.tags = ["users"]


def get_user_service(db: Session = Depends(get_db)):
    return UserService(UserRepository(db))


@user_router.post("/", response_model=UserResponse)
def create_user(
    user_data: UserCreate, user_service: UserService = Depends(get_user_service)
):
    return user_service.create_user(user_data)


@user_router.get("/", response_model=List[UserResponse])
def get_all_users(user_service: UserService = Depends(get_user_service)):
    return user_service.get_all_users()


@user_router.get("/{user_id}", response_model=UserResponse)
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
