from repositories.language import LanguageRepository
from models.language import Language
from schemas.language import LanguageCreate, LanguageUpdate

class LanguageService:
  def __init__(self, language_repository: LanguageRepository):
    self.repository = language_repository
    
  def get_language_by_id(self, id: int):
    language = self.repository.get_language_by_id(id)
    return language
  
  def get_language_by_name(self, name: str):
    language = self.repository.get_language_by_name(name)
    return language
  
  def get_language_by_abbreviation(self, abbreviation: str):
    language = self.repository.get_language_by_abbreviation(abbreviation)
    return language
  
  def get_all_languages(self):
    languages = self.repository.get_all_languages()
    return languages
  
  def insert_language(self, language: LanguageCreate):
    new_language = self.repository.insert_language(language)
    return new_language
  
  def delete_language_by_id(self, id: int):
    language = self.repository.delete_language_by_id(id)
    return language
  
  def update_language(self, id: int, language_data: LanguageUpdate):
    language = self.repository.update_language(id, language_data)
    return language