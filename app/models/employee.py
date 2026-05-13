from pydantic import BaseModel, EmailStr
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    department: str
