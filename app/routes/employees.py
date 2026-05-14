from fastapi import APIRouter, HTTPException
from app.models.employee import Employee, EmployeeCreate
from app.db.mongo_db import get_database

from app.controller.employees import EmployeeController


router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/", status_code=201)
async def create_employee(employee: EmployeeCreate):
    return await EmployeeController.create_employee(employee)


@router.get("/")
async def get_employees():
    db = get_database()

    employees = []

    cursor = db["employees"].find({}, {"_id": 0})

    async for employee in cursor:
        employees.append(employee)

    return employees


@router.get("/{employee_id}")
async def get_employee(employee_id: int):
    db = get_database()

    employee = await db["employees"].find_one(
        {"employee_id": employee_id},
        {"_id": 0}
    )

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee