import pytest


@pytest.mark.asyncio
async def test_mongo_connection_ping(test_db):

    collection = test_db["people"]

    result = await test_db.command("ping")

    assert result["ok"] == 1.0

    # clear collection after test
    await collection.delete_many({})