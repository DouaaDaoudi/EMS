import os

os.environ["TESTING"] = "1"
os.environ["MONGO_URI"] = "mongodb://localhost:27017"
os.environ["DATABASE_NAME"] = "test_employee_db"

import pytest_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest_asyncio.fixture(scope="session")
async def mongo_client():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    yield client
    client.close()


@pytest_asyncio.fixture(scope="function")
async def test_db(mongo_client):
    db = mongo_client["test_employee_db"]

    await db.users.delete_many({})
    await db.employees.delete_many({})

    yield db

    await db.users.delete_many({})
    await db.employees.delete_many({})


@pytest_asyncio.fixture(scope="session")
async def client():
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as ac:
        yield ac