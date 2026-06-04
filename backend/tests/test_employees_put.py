import asyncio

VALID_EMPLOYEE = {
    "employee_id": "EMP123",
    "name": "John Doe",
    "email": "john.doe@example.com",
    "position": "Software Engineer",
    "department": "IT",
    "status": "Active"
}


async def test_update_employee_response_contains_updatedAt(client, test_db):
    await client.post("/employees", json=VALID_EMPLOYEE)

    updated_employee = VALID_EMPLOYEE.copy()
    updated_employee["position"] = "Senior Software Engineer"

    response = await client.put(
        "/employees/EMP123",
        json=updated_employee
    )

    assert response.status_code == 200

    data = response.json()

    assert "updatedAt" in data
    assert data["updatedAt"] is not None


async def test_update_employee_updatedAt_changes_on_second_update(client, test_db):
    await client.post("/employees", json=VALID_EMPLOYEE)

    first_update = VALID_EMPLOYEE.copy()
    first_update["position"] = "Developer"

    first_response = await client.put(
        "/employees/EMP123",
        json=first_update
    )

    first_updated_at = first_response.json()["updatedAt"]

    await asyncio.sleep(1)

    second_update = VALID_EMPLOYEE.copy()
    second_update["position"] = "Senior Developer"

    second_response = await client.put(
        "/employees/EMP123",
        json=second_update
    )

    second_updated_at = second_response.json()["updatedAt"]

    assert first_updated_at != second_updated_at