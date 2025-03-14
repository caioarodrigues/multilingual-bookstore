from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    is_admin: bool

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None

    class Config:
        orm_mode = True
