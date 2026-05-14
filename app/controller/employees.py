from app.models.employee import EmployeeResponse
from app.models.employee import EmployeeCreate
from app.db.mongo_db import get_database
from fastapi import HTTPException

class EmployeeController :
    @staticmethod
    async def create_employee(employee: EmployeeCreate) :

        db = get_database()
        employee_data = employee.model_dump()
        existing_employee = await db["employees"].find_one({"employee_id": employee.employee_id})

        if existing_employee:
                raise HTTPException(
                    status_code=400,
                    detail="Employee ID already exists"
                )

        result = await db["employees"].insert_one(employee_data)

        return {
            "message": "Employee created successfully",
            "employee": employee.model_dump(),
            "id": str(result.inserted_id)
        }
