from pydantic import BaseModel


class Settings:
    DATABASE_URL: str = "sqlite:///./multilingual-bookstore.db"
    SECRET_KEY: str
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()
