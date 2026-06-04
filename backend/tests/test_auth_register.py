import pytest


async def test_login_success(client, test_db):
    await client.post(
        "/auth/register",
        json={
            "email": "test@example.com",
            "password": "password123"
        }
    )

    response = await client.post(
        "/auth/login",
        json={
            "email": "test@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


async def test_users_collection_has_unique_index_on_email(test_db):
    indexes = await test_db.users.index_information()

    email_index_found = False

    for index in indexes.values():
        keys = index.get("key", [])

        if keys == [("email", 1)] and index.get("unique") is True:
            email_index_found = True
            break

    assert email_index_found


async def test_register_duplicate_email_rejected_by_db_index(client, test_db):
    user = {
        "email": "duplicate@example.com",
        "password": "password123"
    }

    first_response = await client.post("/auth/register", json=user)

    assert first_response.status_code in [200, 201]

    second_response = await client.post("/auth/register", json=user)

    assert second_response.status_code in [400, 409]