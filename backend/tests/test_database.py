import pytest
from app.database import get_database


@pytest.mark.asyncio
async def test_database_connection():
    db = get_database()

    response = await db.command("ping")

    assert response["ok"] == 1.0