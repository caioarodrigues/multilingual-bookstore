from typing import List, Dict, Any, Optional
from sqlalchemy.orm import Session, joinedload
from models.book import Book, book_language, user_saved_books
from models.language import Language
from schemas.book import BookCreate, BookUpdate, BookSave
from .base import BaseRepository


class BookRepository(BaseRepository[Book, BookCreate, BookUpdate]):
    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100, filters: Dict[str, Any] = {}
    ) -> List[Book]:
        query = db.query(self.model)
        for field, value in filters.items():
            query = query.filter(getattr(self.model, field) == value)
        books = query.offset(skip).limit(limit).all()
        
        return books

    def create_with_languages(
        self, db: Session, *, obj_in: BookCreate
    ) -> Book:
        db_obj = Book(
            title=obj_in.title,
            chapters_count=obj_in.chapters_count,
            author_id=obj_in.author_id
        )
        
        db.add(db_obj)
        db.flush()  
        
        for lang_id in obj_in.language_ids:
            stmt = book_language.insert().values(
                book_id=db_obj.id, language_id=lang_id
            )
            db.execute(stmt)
            
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update_with_languages(
        self, db: Session, *, db_obj: Book, obj_in: BookUpdate
    ) -> Book:
        update_data = obj_in.dict(exclude_unset=True, exclude={"language_ids"})
        for field, value in update_data.items():
            setattr(db_obj, field, value)
            
        if obj_in.language_ids is not None:
            db.execute(
                book_language.delete().where(
                    book_language.c.book_id == db_obj.id
                )
            )
            
            for lang_id in obj_in.language_ids:
                stmt = book_language.insert().values(
                    book_id=db_obj.id, language_id=lang_id
                )
                db.execute(stmt)
                
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def get_with_details(self, db: Session, id: int) -> Optional[Book]:
        return (
            db.query(Book)
            .filter(Book.id == id)
            .options(
                joinedload(Book.chapters),
                joinedload(Book.languages)
            )
            .first()
        )
        
    def save_for_user(
        self, db: Session, *, user_id: int, book_save: BookSave
    ) -> Book:
        db.execute(
            user_saved_books.delete().where(
                (user_saved_books.c.user_id == user_id) &
                (user_saved_books.c.book_id == book_save.book_id)
            )
        )
        
        for lang_id in book_save.language_ids:
            stmt = user_saved_books.insert().values(
                user_id=user_id,
                book_id=book_save.book_id,
                language_id=lang_id
            )
            db.execute(stmt)
            
        db.commit()
        return self.get(db, id=book_save.book_id)
    
    def get_saved_books_for_user(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Dict[str, Any]]:
        result = []
        
        query = (
            db.query(Book, Language)
            .join(user_saved_books, Book.id == user_saved_books.c.book_id)
            .join(Language, Language.id == user_saved_books.c.language_id)
            .filter(user_saved_books.c.user_id == user_id)
            .offset(skip)
            .limit(limit)
        )
        
        books_map = {}
        for book, language in query:
            if book.id not in books_map:
                books_map[book.id] = {
                    "book": book,
                    "languages": []
                }
            books_map[book.id]["languages"].append(language)
            
        for book_id, data in books_map.items():
            result.append({
                "id": data["book"].id,
                "title": data["book"].title,
                "author_id": data["book"].author_id,
                "chapters_count": data["book"].chapters_count,
                "languages": data["languages"]
            })
            
        return result