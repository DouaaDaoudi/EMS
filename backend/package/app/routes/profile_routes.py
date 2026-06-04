from fastapi import APIRouter, Depends
from app.dependencies.auth_dependencies import get_current_user

router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return current_user