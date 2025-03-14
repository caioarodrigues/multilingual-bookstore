from fastapi import APIRouter, Depends, HTTPException
from services.auth import authenticate_user, create_access_token
from schemas.token import Token
from repositories.user import UserRepository
from core.database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

auth_router = APIRouter(tags=["authentication"])


@auth_router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
