from fastapi.testclient import TestClient
from fastapi import FastAPI
from app.main import app, create_app

# 3. test_create_app_returns_fastapi_instance
def test_create_app_returns_fastapi_instance():

    app_instance = create_app()

    assert isinstance(app_instance, FastAPI)


# 4 test_app_includes_health_route`
def test_app_includes_health_route():

    routes = [route.path for route in app.routes]

    assert "/health" in routes

# 5 test_app_loads_settings_into_state
def test_app_loads_settings_into_state():

    app_instance = create_app()

    assert app_instance.state.settings is not None