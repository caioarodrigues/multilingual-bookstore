from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)

    books = relationship("Book", back_populates="author", cascade="all, delete")
    saved_books = relationship("Book", secondary="user_saved_books", back_populates="saved_by_users", cascade="all, delete")