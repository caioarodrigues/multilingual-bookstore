from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from core.database import Base

book_language = Table(
    "book_language",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id", ondelete="CASCADE")),
    Column("language_id", Integer, ForeignKey("languages.id", ondelete="CASCADE")),
)

user_saved_books = Table(
    "user_saved_books",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE")),
    Column("book_id", Integer, ForeignKey("books.id", ondelete="CASCADE")),
    Column("language_id", Integer, ForeignKey("languages.id", ondelete="CASCADE")),
)


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author_id = Column(
        Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    chapters_count = Column(Integer, nullable=False, default=0)

    author = relationship("User", back_populates="books")
    chapters = relationship(
        "Chapter", back_populates="book", cascade="all, delete-orphan"
    )
    languages = relationship("Language", secondary=book_language, backref="books")
    saved_by_users = relationship(
        "User", secondary=user_saved_books, back_populates="saved_books"
    )
