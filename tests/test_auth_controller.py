# we test registration, login, token generation, rejecting wrong password, missing user
import pytest
from fastapi import HTTPException

from app.controllers.auth_controller import register_user, login_user
from app.repositories.user_repository import users_db


def setup_function():
    users_db.clear()



def test_register_user_success():
    response = register_user(
            email="test@example.com",
            password="password123" 
        )
    
    assert response == {"message": "User registered successfully"}
    assert len(users_db) == 1
    assert users_db[0]["email"] == "test@example.com"
    assert users_db[0]["hashed_password"] != "password123"


def test_register_duplicate_user_raises_400():
    register_user(
        email="test@example.com",
        password="password123"
    )

    with pytest.raises(HTTPException) as error:
        register_user(
            email="test@example.com",
            password="password123"
        )

    assert error.value.status_code == 400
    assert error.value.detail == "Email already registered"


def test_login_user_success_returns_token():
    register_user(
        email="test@example.com",
        password="password123"
    )

    response = login_user(
        email="test@example.com",
        password="password123"
    )

    assert "access_token" in response
    assert response["token_type"] == "bearer"


def test_login_user_wrong_email_raises_401():
    with pytest.raises(HTTPException) as error:
        login_user(
            email="wrong@example.com",
            password="password123"
        )

    assert error.value.status_code == 401
    assert error.value.detail == "Invalid email or password"


def test_login_user_wrong_password_raises_401():
    register_user(
        email="test@example.com",
        password="password123"
    )

    with pytest.raises(HTTPException) as error:
        login_user(
            email="test@example.com",
            password="wrongpassword"
        )

    assert error.value.status_code == 401
    assert error.value.detail == "Invalid email or password"