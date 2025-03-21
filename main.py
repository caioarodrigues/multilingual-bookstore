from fastapi import FastAPI
from core.config import settings
from core.database import engine, Base
from routes.book import book_router
from routes.user import user_router
from routes.auth import auth_router
from routes.language import language_router
from models.language import Language
from models.user import User
from models.book import Book
from models.chapter import Chapter

app = FastAPI(title="Multilingual Bookstore API")

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(book_router)
app.include_router(language_router)
app.include_router(user_router)
