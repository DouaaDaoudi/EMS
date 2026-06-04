from fastapi import APIRouter
from pydantic import BaseModel, EmailStr, Field
from app.controllers.auth_controller import register_user, login_user

router = APIRouter(prefix="/auth", tags=["Auth"])


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=72)


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=72)


@router.post("/login")
async def login(request: LoginRequest):
    return await login_user(request.email, request.password)


@router.post("/register")
async def register(request: RegisterRequest):
    return await register_user(request.email, request.password)