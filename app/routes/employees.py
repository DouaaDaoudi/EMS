from fastapi import APIRouter
from app.models.employee import EmployeeCreate, EmployeeUpdate
from app.controllers.employees import EmployeeController

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/", status_code=201)
async def create_employee(employee: EmployeeCreate):
    return await EmployeeController.create_employee(employee)


@router.get("/")
async def get_employees():
    return await EmployeeController.get_employees()


@router.get("/{employee_id}")
async def get_employee(employee_id: str):
    return await EmployeeController.get_employee(employee_id)


@router.delete("/{employee_id}")
async def delete_employee(employee_id: str):
    return await EmployeeController.delete_employee(employee_id)


@router.put("/{employee_id}")
async def update_employee(employee_id: str, updated_employee: EmployeeUpdate):
    return await EmployeeController.update_employee(employee_id, updated_employee)