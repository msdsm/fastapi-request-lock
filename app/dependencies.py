from functools import lru_cache

from app.services.limiter import RequestLimiterService, AsyncioLockLimiterService
from app.services.business import HelloService, WorldService


@lru_cache()
def get_limiter_service() -> RequestLimiterService:
    return AsyncioLockLimiterService()


@lru_cache()
def get_hello_service() -> HelloService:
    return HelloService()


@lru_cache()
def get_world_service() -> WorldService:
    return WorldService()
