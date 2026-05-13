from fastapi import APIRouter, HTTPException
from app.models.employee import Employee
from app.db.mongo_db import get_database

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/")
async def create_employee(employee: Employee):
    db = get_database()

    employee_data = employee.model_dump()

    existing_employee = await db["employees"].find_one({"id": employee.id})

    if existing_employee:
        raise HTTPException(status_code=400, detail="Employee ID already exists")

    await db["employees"].insert_one(employee_data)

    return {
        "message": "Employee created successfully",
        "employee": employee_data
    }


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
        {"id": employee_id},
        {"_id": 0}
    )

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee