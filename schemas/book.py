from typing import List, Optional
from pydantic import BaseModel, Field
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .chapter import Chapter

class LanguageBase(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class BookBase(BaseModel):
    title: str
    chapters_count: int = Field(ge=0)


class BookCreate(BookBase):
    author_id: Optional[int] = None
    language_ids: List[int]


class BookUpdate(BaseModel):
    title: Optional[str] = None
    chapters_count: Optional[int] = Field(default=None, ge=0)
    author_id: Optional[int] = None
    language_ids: Optional[List[int]] = None


class BookResponse(BookBase):
    id: int
    author_id: Optional[int]
    languages: List[LanguageBase] = []


class BookInDBBase(BookBase):
    id: int
    author_id: Optional[int]

    class Config:
        from_attributes = True


class Book(BookInDBBase):
    languages: List[LanguageBase] = []


class BookWithDetails(Book):
    chapters: List["Chapter"] = []

class BookSave(BaseModel):
    book_id: int
    language_ids: List[int]
