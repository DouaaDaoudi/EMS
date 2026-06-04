from fastapi import APIRouter, Depends, HTTPException
from app.models.employee import EmployeeCreate, EmployeeUpdate
from app.controllers.employees import EmployeeController
from app.dependencies.auth_dependencies import get_current_user

router = APIRouter(prefix="/employees", tags=["Employees"])


def require_admin(current_user=Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return current_user


@router.post("/", status_code=201)
async def create_employee(
    employee: EmployeeCreate,
    current_user=Depends(require_admin)
):
    return await EmployeeController.create_employee(employee)


@router.get("/")
async def get_employees(
    current_user=Depends(get_current_user)
):
    return await EmployeeController.get_employees()


@router.get("/{employee_id}")
async def get_employee(
    employee_id: str,
    current_user=Depends(get_current_user)
):
    return await EmployeeController.get_employee(employee_id)


@router.delete("/{employee_id}")
async def delete_employee(
    employee_id: str,
    current_user=Depends(require_admin)
):
    return await EmployeeController.delete_employee(employee_id)


@router.put("/{employee_id}")
async def update_employee(
    employee_id: str,
    updated_employee: EmployeeUpdate,
    current_user=Depends(require_admin)
):
    return await EmployeeController.update_employee(employee_id, updated_employee)