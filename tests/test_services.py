import pytest
from unittest.mock import AsyncMock
from app.services.limiter import AsyncioLockLimiterService, SemaphoreLimiterService
from app.services.business import HelloService, WorldService


class TestLimiterServices:
    @pytest.mark.asyncio
    async def test_asyncio_lock_limiter_service(self):
        limiter = AsyncioLockLimiterService()
        mock_func = AsyncMock(return_value="test_result")

        result = await limiter.with_limit(mock_func, "arg1", kwarg1="value1")

        assert result == "test_result"
        mock_func.assert_called_once_with("arg1", kwarg1="value1")

    @pytest.mark.asyncio
    async def test_semaphore_limiter_service(self):
        limiter = SemaphoreLimiterService(max_concurrent=2)
        mock_func = AsyncMock(return_value="test_result")

        result = await limiter.with_limit(mock_func)

        assert result == "test_result"

        mock_func.assert_called_once()


class TestBusinessServices:
    @pytest.mark.asyncio
    async def test_hello_service(self):
        service = HelloService()
        result = await service.get_hello_message()

        assert result["message"] == "Hello!"
        assert result["service"] == "hello"
        assert "timestamp" in result
        assert result["processing_time"] == "2 seconds"

    @pytest.mark.asyncio
    async def test_world_service(self):
        service = WorldService()
        result = await service.get_world_message()

        assert result["message"] == "World!"
        assert result["service"] == "world"
        assert "timestamp" in result
        assert result["processing_time"] == "1 second"
