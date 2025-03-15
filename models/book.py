from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from core.database import Base

book_language = Table(
    'book_language', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('language_id', Integer, ForeignKey('languages.id'))
)

user_saved_books = Table(
    'user_saved_books', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('language_id', Integer, ForeignKey('languages.id'))
)

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    chapters_count = Column(Integer, nullable=False)
    
    author = relationship("User", back_populates="books")
    chapters = relationship("Chapter", back_populates="book", cascade="all, delete")
    languages = relationship("Language", secondary=book_language, backref="books")
    saved_by_users = relationship("User", secondary=user_saved_books, back_populates="saved_books")