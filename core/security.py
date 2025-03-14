from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from core.config import settings
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from core.database import get_db
from models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


# def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#    credentials_exception = HTTPException(
#        status_code=401,
#        detail="Could not validate credentials"
#    )
#    try:
#        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
#        user_id: int = payload.get("sub")
#        if user_id is None:
#            raise credentials_exception
#    except JWTError:
#        raise credentials_exception
#
#    user = UserRepository(db).get_user(user_id)
#    if user is None:
#        raise credentials_exception
#    return user
#
# def get_current_admin(current_user: User = Depends(get_current_user)):
#    if not current_user.is_admin:
#        raise HTTPException(status_code=403, detail="Permission denied")
#    return current_user
