
import pytest

VALID_EMPLOYEE = {
    "employee_id": "EMP12345",
    "name": "John Doe",
    "email": "john.doe@example.com",
    "position": "Software Engineer",
    "department": "IT",
    "status": "Active",
    "createdAt": "2024-06-01T12:00:00Z"
}
"""
async def test_create_employee_returns_201_and_shape(client, test_db):
    response = await client.post("/employees", json=VALID_EMPLOYEE)

    assert response.status_code == 201
    assert response.json() == VALID_EMPLOYEE


# creating test for too short employee name
async def test_create_employee_with_short_name_returns_422(client, test_db):
    invalid_employee = VALID_EMPLOYEE.copy()
    invalid_employee["name"] = "J"

    response = await client.post("/employees", json=invalid_employee)

    assert response.status_code == 422  


async def test_create_employee_duplicate_rejected_by_db_index(client, test_db):
    first_response = await client.post("/employees", json=VALID_EMPLOYEE)

    assert first_response.status_code == 201

    duplicate_response = await client.post("/employees", json=VALID_EMPLOYEE)

    assert duplicate_response.status_code in [400, 409]


async def test_employees_collection_has_unique_index_on_employee_id(test_db):
    indexes = await test_db.employees.index_information()

    employee_id_index_found = False

    for index in indexes.values():
        keys = index.get("key", [])

        if keys == [("employee_id", 1)] and index.get("unique") is True:
            employee_id_index_found = True
            break

    assert employee_id_index_found


async def test_create_employee_server_generates_createdAt(client, test_db):
    employee = VALID_EMPLOYEE.copy()

    employee.pop("createdAt")

    response = await client.post("/employees", json=employee)

    assert response.status_code == 201

    data = response.json()

    assert "createdAt" in data
    assert data["createdAt"] is not None



async def test_create_employee_ignores_client_provided_createdAt(client, test_db):
    employee = VALID_EMPLOYEE.copy()

    employee["createdAt"] = "2000-01-01T00:00:00Z"

    response = await client.post("/employees", json=employee)

    assert response.status_code == 201

    data = response.json()

    assert data["createdAt"] != "2000-01-01T00:00:00Z"
    """