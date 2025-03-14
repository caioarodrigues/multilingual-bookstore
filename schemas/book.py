from pydantic import BaseModel
from typing import List, Optional


class ChapterBase(BaseModel):
    title: str
    content: str


class BookCreate(BaseModel):
    title: str
    chapters: List[ChapterBase]
    languages: List[str]


class BookResponse(BookCreate):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
