
import pytest
from app.models.employee import EmployeeCreate
from pydantic import ValidationError
from app.models.employee import EmployeeCreate
from app.models.employee import EmployeeUpdate


#`test_employee_model_imports_and_validates_minimal_payload`
# this test check model imports correctly
#- payload is valid
#- Pydantic validation works
#- fields are stored correctly
def test_employee_model_imports_and_validates_minimal_payload():

    payload = {
        "employee_id": "EMP123",
        "name": "John Doe",
        "email": "john.doe@example.com",
        "position": "Software Engineer",
        "department": "IT",
        "status": "Active"
    }

    employee = EmployeeCreate(**payload)

    assert employee.employee_id == payload["employee_id"]
    assert employee.name == payload["name"]
    assert employee.email == payload["email"]
    assert employee.position == payload["position"]
    assert employee.department == payload["department"]
    assert employee.status == payload["status"]

#`test_employee_create_rejects_invalid_email`
#invalid email is rejected
#- Pydantic raises ValidationError
#- EmailStr validation works
#when email is invalid it raises error

def test_employee_create_rejects_invalid_email():

    invalid_payload = {
        "employee_id": "EMP123",
        "name": "John Doe",
        "email": "not an email",
        "position": "Software Engineer",
        "department": "IT",
        "status": "Active"
    }

    with pytest.raises(ValidationError):
        EmployeeCreate(**invalid_payload)


#test_employee_update_allows_all_optional_fields_none`
def test_employee_update_allows_all_optional_fields_none():

    employee = EmployeeUpdate(
        employee_id=None,
        name=None,
        email=None,
        position=None,
        department=None,
        status=None
    )

    assert employee.employee_id is None
    assert employee.name is None
    assert employee.email is None
    assert employee.position is None
    assert employee.department is None
    assert employee.status is None