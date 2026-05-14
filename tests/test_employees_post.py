
import pytest

VALID_EMPLOYEE = {
    "employee_id": "EMP123",
    "name": "John Doe",
    "email": "john.doe@example.com",
    "position": "Software Engineer",
    "department": "IT",
    "status": "Active",
    "createdAt": "2024-06-01T12:00:00Z"
}

async def test_create_employee_returns_201_and_shape(client, test_db):
    response = await client.post("/employees/", json=VALID_EMPLOYEE)

    assert response.status_code == 201
    assert response.json() == VALID_EMPLOYEE


# creating test for too short employee name
async def test_create_employee_with_short_name_returns_422(client, test_db):
    invalid_employee = VALID_EMPLOYEE.copy()
    invalid_employee["name"] = "J"

    response = await client.post("/employees/", json=invalid_employee)

    assert response.status_code == 422  
