from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.mongo_db import get_database
from app.core.settings import settings
from app.routes.employees import router as employees_router
from app.routes.auth_routes import router as auth_router
from app.routes.profile_routes import router as profile_router
from app.routes.user_routes import router as users_router


def create_app():
    app = FastAPI(title="Employee Database API")

    allowed_origins = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://d25cj3offj6s6j.cloudfront.net",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.state.settings = settings

    app.include_router(employees_router)
    app.include_router(auth_router)
    app.include_router(profile_router)
    app.include_router(users_router)

    @app.get("/health")
    def health_check():
        return {"status": "ok"}

    @app.get("/db-health")
    async def db_health_check():
        db = get_database()
        result = await db.command("ping")

        return {
            "database": "connected",
            "ok": result["ok"],
        }

    return app


app = create_app()