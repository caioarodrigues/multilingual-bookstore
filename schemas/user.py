from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional, List
from schemas.book import Book


class UserBase(BaseModel):
    email: EmailStr


class UserLogin(UserBase):
    password: str


class UserInDB(UserBase):
    id: int
    is_admin: bool

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str

    @field_validator("password")
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return v


class UserDefaultSchema(UserInDB):
    pass


class UserResponse(UserInDB):
    token: str


class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None

    class Config:
        orm_mode = True


class UserWithBooks(UserInDB):
    books: List[Book] = []
