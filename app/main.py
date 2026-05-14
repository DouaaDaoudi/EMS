from fastapi import FastAPI
from app.db.mongo_db import get_database
from app.core.settings import settings
from app.routes.employees import router as employees_router


def create_app():

    app = FastAPI(title="Employee Database API")

    app.state.settings = settings
    app.include_router(employees_router)
    # we need health_router included

    

    # storesettings into app state
    app.state.settings = settings

    @app.get("/health")
    def health_check():
        return {"status": "ok"}

    @app.get("/db-health")
    async def db_health_check():
        db = get_database()

        result = await db.command("ping")

        return {
            "database": "connected",
            "ok": result["ok"]
        }

    return app


app = create_app()