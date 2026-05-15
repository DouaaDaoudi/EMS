import os

# Set test environment BEFORE importing app
os.environ["TESTING"] = "1"
os.environ["MONGO_URI"] = "mongodb://localhost:27017"
os.environ["DATABASE_NAME"] = "test_employee_db"
# this should be used before importing the main to make sure all the test are running



import pytest_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from httpx import AsyncClient, ASGITransport
from app.main import app
@pytest_asyncio.fixture
async def test_db():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["test_employee_db"]

    yield db

    # await db["test_collection"].delete_many({})
    client.close()

@pytest_asyncio.fixture
async def client():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as ac:

        yield ac