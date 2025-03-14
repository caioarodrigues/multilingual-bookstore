from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException
from core.security import oauth2_scheme
from core.config import settings
from repositories.user import UserRepository
from core.security import verify_password


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def authenticate_user(username: str, password: str, db):
    user = UserRepository(db).get_user_by_email(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
