from app.database import users_collection

async def save_user(user: dict):
    await users_collection.insert_one(user)
    return user


async def get_user_by_email(email: str):
    return await users_collection.find_one({"email": email})


async def get_all_users():
    users = []
    cursor = users_collection.find({}, {"hashed_password": 0})

    async for user in cursor:
        user["_id"] = str(user["_id"])
        users.append(user)

    return users