from sqlalchemy.orm import Session
from models.language import Language
from schemas.language import LanguageCreate, LanguageUpdate
from typing import List

class LanguageRepository:
  def __init__(self, db: Session):
    self.db = db
    
  def get_language_by_id(self, id: int) -> Language:
    return self.db.query(Language).filter(Language.id == id).first()
  
  def get_language_by_name(self, name: str) -> Language:
    return self.db.query(Language).filter(Language.name == name).first()
  
  def get_language_by_abbreviation(self, abbreviation: str) -> Language:
    return self.db.query(Language).filter(Language.abbreviation == abbreviation).first()
  
  def get_all_languages(self) -> List[Language]:
    return self.db.query(Language).all()
  
  def insert_language(self, language: LanguageCreate) -> Language:
    db_language = Language(
      name=language.name,
      abbreviation=language.abbreviation
    )
    self.db.add(db_language)
    self.db.commit()
    self.db.refresh(db_language)
    return db_language
  
  def delete_language_by_id(self, id: int):
    language = self.get_language_by_id(id)
    
    if not language:
      return None

    self.db.delete(language)
    self.db.commit()
    return language
  
  def update_language(self, id: int, language_data: LanguageUpdate) -> Language:
    language = self.get_language_by_id(id)
    for key, value in language_data:
      setattr(language, key, value)
    self.db.commit()
    self.db.refresh(language)
    return language