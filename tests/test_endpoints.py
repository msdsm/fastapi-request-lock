import pytest
from fastapi.testclient import TestClient

from app.main import create_app
from app.dependencies import (
    get_limiter_service,
)


class MockLimiterService:
    async def with_limit(self, func, *args, **kwargs):
        return await func(*args, **kwargs)


@pytest.fixture
def client():
    app = create_app()

    app.dependency_overrides[get_limiter_service] = lambda: MockLimiterService()

    return TestClient(app)


class TestEndpoints:
    def test_hello_endpoint(self, client):
        response = client.get("/hello")

        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Hello!"
        assert data["service"] == "hello"

    def test_world_endpoint(self, client):
        response = client.get("/world")

        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "World!"
        assert data["service"] == "world"

    def test_health_check(self, client):
        response = client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
