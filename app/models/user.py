from dataclasses import Field
from typing import Literal

from pydantic import BaseModel, EmailStr

UserRole = Literal["admin", "user"]

class UserCreate(BaseModel):
    email: EmailStr
    hashed_password: str