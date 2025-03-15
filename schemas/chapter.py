from typing import Optional
from pydantic import BaseModel


class ChapterBase(BaseModel):
    title: str
    content: str
    language_id: int


class ChapterCreate(ChapterBase):
    book_id: int


class ChapterUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    language_id: Optional[int] = None


class ChapterInDBBase(ChapterBase):
    id: int
    book_id: int

    class Config:
        from_attributes = True


class Chapter(ChapterInDBBase):
    pass