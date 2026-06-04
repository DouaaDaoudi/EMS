import pytest


async def test_register_user_success(client, test_db):
    user = {
        "email": "test_success12345678@example.com",
        "password": "password123"
    }

    response = await client.post("/auth/register", json=user)

    assert response.status_code in [200, 201]
    assert response.json() == {"message": "User registered successfully"}


async def test_register_duplicate_user_raises_400(client, test_db):
    user = {
        "email": "duplicate_controller@example.com",
        "password": "password123"
    }

    first_response = await client.post("/auth/register", json=user)
    assert first_response.status_code in [200, 201]

    second_response = await client.post("/auth/register", json=user)

    assert second_response.status_code in [400, 409]


async def test_login_user_success_returns_token(client, test_db):
    user = {
        "email": "login_controller@example.com",
        "password": "password123"
    }

    await client.post("/auth/register", json=user)

    response = await client.post("/auth/login", json=user)

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


async def test_login_user_wrong_email_raises_401(client, test_db):
    response = await client.post(
        "/auth/login",
        json={
            "email": "wrong_controller@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password"


async def test_login_user_wrong_password_raises_401(client, test_db):
    user = {
        "email": "wrongpass_controller@example.com",
        "password": "password123"
    }

    await client.post("/auth/register", json=user)

    response = await client.post(
        "/auth/login",
        json={
            "email": "wrongpass_controller@example.com",
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password"