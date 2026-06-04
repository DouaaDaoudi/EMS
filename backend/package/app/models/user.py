from typing import Literal
from pydantic import BaseModel, EmailStr

UserRole = Literal["admin", "user"]


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserInDB(BaseModel):
    email: EmailStr
    hashed_password: str
    role: UserRole = "user"