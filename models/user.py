from sqlalchemy import Boolean, Column, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from core.database import Base

# user_saved_books = Table(
#    'user_saved_books', Base.metadata,
#    Column('user_id', Integer, ForeignKey('users.id')),
#    Column('book_id', Integer, ForeignKey('books.id'))
# )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)

    # books = relationship("Book", back_populates="owner", cascade="all, delete")
    # saved_books = relationship("Book", secondary=user_saved_books)
