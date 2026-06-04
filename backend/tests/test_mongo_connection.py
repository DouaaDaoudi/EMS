import pytest
from app.db.mongo_db import get_database
from unittest.mock import MagicMock, AsyncMock

@pytest.mark.asyncio
async def test_mongo_connection_ping():
    db = get_database()

    result = await db.command("ping")

    assert result["ok"] == 1.0

    #test insert a text document
    test_doc = {"name": "Douaa", "age": "32"}    
    insert_result = await db.test_collection.insert_one(test_doc)
    assert insert_result.inserted_id is not None

    #retrieve the document and check if it matches the inserted one
    retrieved_doc = await db.test_collection.find_one({"_id": insert_result.inserted_id})
    assert retrieved_doc is not None
    assert retrieved_doc["name"] == test_doc["name"]
    assert retrieved_doc["age"] == test_doc["age"]



      # using mock
    fake_client = MagicMock()

    fake_client.admin.command = AsyncMock(
        return_value={"ok": 1.0}
    )

    result = await fake_client.admin.command("ping")

    assert result["ok"] == 1.0

# test document insertion and retrieval
@pytest.mark.asyncio
async def test_mongo_insert_and_find(test_db):
    
    test_doc = {"name": "Douaa", "age": "32"}    
    insert_result = await test_db.test_collection.insert_one(test_doc)
    assert insert_result.inserted_id is not None

    #retrieve the document and check if it matches the inserted one
    retrieved_doc = await test_db.test_collection.find_one({"_id": insert_result.inserted_id})
    assert retrieved_doc is not None
    assert retrieved_doc["name"] == test_doc["name"]
    assert retrieved_doc["age"] == test_doc["age"]
