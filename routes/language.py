from fastapi import APIRouter, Depends
from repositories.language import LanguageRepository
from services.language import LanguageService
from core.database import get_db
from schemas.language import LanguageCreate, LanguageUpdate
from typing import List

language_router = APIRouter(prefix="/languages", tags=["languages"])

def get_language_service(db = Depends(get_db)):
  return LanguageService(LanguageRepository(db))

@language_router.get("/", response_model=List[LanguageCreate])
def get_all_languages(language_service: LanguageService = Depends(get_language_service)):
  return language_service.get_all_languages()

@language_router.get("/{id}", response_model=LanguageCreate)
def get_language_by_id(id: int, language_service: LanguageService = Depends(get_language_service)):
  return language_service.get_language_by_id(id)

@language_router.post("/", response_model=LanguageCreate)
def insert_language(language: LanguageCreate, language_service: LanguageService = Depends(get_language_service)):
  return language_service.insert_language(language)

@language_router.delete("/{id}", response_model=LanguageCreate)
def delete_language_by_id(id: int, language_service: LanguageService = Depends(get_language_service)):
  return language_service.delete_language_by_id(id)

@language_router.put("/{id}", response_model=LanguageCreate)
def update_language(id: int, language: LanguageUpdate, language_service: LanguageService = Depends(get_language_service)):
  return language_service.update_language(id, language)