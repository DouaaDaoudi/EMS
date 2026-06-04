from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.core.settings import settings
from app.repositories.user_repository import get_user_by_email


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        user = await get_user_by_email(email)

        if not user:
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        user["_id"] = str(user["_id"])

        return {
            "id": user["_id"],
            "email": user["email"],
            "role": user.get("role", "user")
        }

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )