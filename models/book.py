from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from core.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    # chapters = relationship("Chapter", back_populates="book")
    # languages = relationship("Language", secondary="languages")
    # saved_by = relationship("User", secondary="user_saved_books")
