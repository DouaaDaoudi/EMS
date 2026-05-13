from fastapi.testclient import TestClient
from fastapi import FastAPI
from app.main import app, create_app


client = TestClient(app)


# 1. test_health_endpoint_returns_ok
def test_health_check():

    response = client.get("/health")

    assert response.status_code == 200

    # 2. test_health_endpoint_returns_json_content_type
    assert response.json() == {"status": "ok"}


        