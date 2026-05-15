from fastapi import HTTPException
from app.db.mongo_db import get_database
from app.models.employee import EmployeeCreate, EmployeeUpdate


class EmployeeController:

    @staticmethod
    async def create_employee(employee: EmployeeCreate):
        db = get_database()

        employee_dict = employee.model_dump()

        await db["employees"].insert_one(employee_dict.copy())

        return {
            "message": "Employee created successfully",
            "employee": employee_dict
        }

    @staticmethod
    async def get_employees():
        db = get_database()

        employees = []
        cursor = db["employees"].find({}, {"_id": 0})

        async for employee in cursor:
            employees.append(employee)

        return employees

    @staticmethod
    async def get_employee(employee_id: str):
        db = get_database()

        employee = await db["employees"].find_one(
            {"employee_id": employee_id},
            {"_id": 0}
        )

        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")

        return employee

    @staticmethod
    async def delete_employee(employee_id: str):
        db = get_database()

        result = await db["employees"].delete_one(
            {"employee_id": employee_id}
        )

        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Employee not found")

        return {"message": "Employee deleted successfully"}

    @staticmethod
    async def update_employee(employee_id: str, updated_employee: EmployeeUpdate):
        db = get_database()

        update_data = updated_employee.model_dump(exclude_unset=True)

        result = await db["employees"].update_one(
            {"employee_id": employee_id},
            {"$set": update_data}
        )

        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Employee not found")

        return {
            "message": "Employee updated successfully",
            "updated_fields": update_data
        }