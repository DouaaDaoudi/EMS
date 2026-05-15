from fastapi.testclient import TestClient
from app.core.security import hash_password
from app.main import app

client = TestClient(app)


def test_login_success():
    
    client.post("/auth/register", json={"email": "test@example.com", "password": "password123"})
    
    response = client.post(
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