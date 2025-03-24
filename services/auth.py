from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from core.security import oauth2_scheme
from core.config import settings
from repositories.user import UserRepository
from core.security import verify_password


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


async def authenticate_user(email: str, password: str, db: Session) -> Optional[dict]:
    user = UserRepository(db)

    if not user:
        return None

    valid_user = user.get_user_by_email(email)

    if not valid_user:
        return None

    if valid_user and verify_password(password, valid_user.hashed_password):
        return {"id": valid_user.id, "email": valid_user.email}
    return None
