from fastapi import APIRouter, Depends, HTTPException
from services.auth import authenticate_user, create_access_token
from schemas.auth import AuthResponse
from schemas.user import UserLogin, UserResponse
from repositories.user import UserRepository
from core.database import get_db
from core.security import create_token
from sqlalchemy.orm import Session

auth_router = APIRouter(tags=["authentication"])


@auth_router.post("/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    user = await authenticate_user(email=user.email, password=user.password, db=db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token(user)
    return {"user": user, "token": token}
