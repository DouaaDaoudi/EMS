from motor.motor_asyncio import AsyncIOMotorClient
from app.core.settings import settings

client = AsyncIOMotorClient(settings.MONGO_URI)

database = client[settings.MONGO_DB_NAME]


def get_database():
    return database