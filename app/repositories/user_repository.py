from app.database import users_collection


async def save_user(user: dict):
    await users_collection.insert_one(user)
    return user


async def get_user_by_email(email: str):
    return await users_collection.find_one({"email": email})