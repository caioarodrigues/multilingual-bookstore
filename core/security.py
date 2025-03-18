from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from core.config import settings
from passlib.context import CryptContext
from core.database import get_db
from datetime import datetime, timedelta
from core.config import settings
import bcrypt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")


def verify_password(password: str, hashed: str) -> bool:
    try:
        encoded_pw = password.encode("utf-8")
        encoded_hashed = hashed.encode("utf-8")

        return encoded_hashed == encoded_pw
    except ValueError:
        print("Error checking password: \n" + ValueError)
        return False


def create_token(user: dict) -> str:
    payload = {"user_id": user["id"], "exp": datetime.utcnow() + timedelta(hours=2)}
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def verify_token(token: str) -> bool:
    try:
        jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return True
    except jwt.PyJWTError:
        return False
