from typing import Optional
from pydantic import BaseModel, field_validator


class LanguageBase(BaseModel):
    name: str
    abbreviation: str

    @field_validator("abbreviation")
    def abbreviation_format(cls, v):
        if not v.islower() or len(v) != 2:
            raise ValueError("Abbreviation must be a 2-letter lowercase code")
        return v


class LanguageCreate(LanguageBase):
    pass


class LanguageResponse(LanguageBase):
    id: int


class LanguageUpdate(BaseModel):
    name: Optional[str] = None
    abbreviation: Optional[str] = None

    @field_validator("abbreviation")
    def abbreviation_format(cls, v):
        if v is not None and (not v.islower() or len(v) != 2):
            raise ValueError("Abbreviation must be a 2-letter lowercase code")
        return v


class LanguageInDBBase(LanguageBase):
    id: int

    class Config:
        from_attributes = True


class Language(LanguageInDBBase):
    pass
