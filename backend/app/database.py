from app.db.mongo_db import database

users_collection = database["users"]
employees_collection = database["employees"]


def get_database():
    return database