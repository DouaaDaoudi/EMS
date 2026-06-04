from motor.motor_asyncio import AsyncIOMotorClient
from app.core.settings import settings

client = AsyncIOMotorClient(settings.mongo_uri)

database = client[settings.database_name]


def get_database():
    return database