from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base


class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    book_id = Column(Integer, ForeignKey("books.id"))
    language_id = Column(Integer, ForeignKey("languages.id"))

    book = relationship("Book", back_populates="chapters")
    language = relationship("Language")
