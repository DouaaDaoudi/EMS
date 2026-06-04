from fastapi import HTTPException
from app.repositories.user_repository import get_user_by_email, save_user
from app.core.security import hash_password, verify_password, create_access_token


async def register_user(email: str, password: str):
    existing_user = await get_user_by_email(email)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed_password = hash_password(password)

    new_user = {
        "email": email,
        "hashed_password": hashed_password,
        "role": "user"
    }

    await save_user(new_user)

    return {"message": "User registered successfully"}


async def login_user(email: str, password: str):
    user = await get_user_by_email(email)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(password, user["hashed_password"]):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(
        data={
            "sub": email,
            "role": user.get("role", "user")
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user.get("role", "user")
    }