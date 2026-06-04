from fastapi import APIRouter, Depends, HTTPException
from app.repositories.user_repository import get_all_users
from app.dependencies.auth_dependencies import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


def require_admin(current_user=Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return current_user


@router.get("/")
async def list_users(
    current_user=Depends(require_admin)
):
    return await get_all_users()