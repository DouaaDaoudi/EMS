import datetime

from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Request/Response patterns models for Employee collection
class Employee(BaseModel):
    employee_id: int
    name: str
    email: EmailStr
    department: str
    position : str
    status : str = "Active"
createdAt: datetime.datetime = Field(
    default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
)
class EmployeeCreate(BaseModel):
    employee_id: str = Field(...,example="EMP123")
    name: str = Field(...,example="John Doe")
    email: EmailStr = Field(...,example="john.doe@example.com")
    position: str = Field(...,example="Software Engineer")
    department: str = Field(...,example="IT")
    createdAt : datetime.datetime = Field(default_factory= lambda: datetime.datetime.now(datetime.timezone.utc))
    status : str = Field(...,example="Active")


class EmployeeUpdate(BaseModel):
    employee_id: Optional[str] = Field(...,example="EMP123")
    name: Optional[str] = Field(...,example="John Doe")
    email: Optional[EmailStr] = Field(...,example="john.doe@example.com")
    position: Optional[str] = Field(...,example="Software Engineer")
    department: Optional[str] = Field(...,example="IT")
    updatedAt : Optional[datetime.datetime] = Field(default_factory= lambda: datetime.datetime.now(datetime.timezone.utc))
    status : Optional[str] = Field(...,example="Active")


class EmployeeResponse(BaseModel):
   employeeId: str
   createdAt: datetime.datetime = Field(default_factory= lambda: datetime.datetime.now(datetime.timezone.utc))