from pydantic import BaseModel
from typing import Dict


class AuthResponse(BaseModel):
    user: Dict[str, str | int]
    access_token: str
