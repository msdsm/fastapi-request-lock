import asyncio
from abc import ABC, abstractmethod
from typing import Any, Callable, Coroutine


class RequestLimiterService(ABC):
    @abstractmethod
    async def with_limit(
        self,
        func: Callable[..., Coroutine[Any, Any, Any]],
        *args,
        **kwargs,
    ) -> Any:
        pass


class AsyncioLockLimiterService(RequestLimiterService):
    def __init__(self):
        self._lock = asyncio.Lock()

    async def with_limit(
        self,
        func: Callable[..., Coroutine[Any, Any, Any]],
        *args,
        **kwargs,
    ) -> Any:
        async with self._lock:
            return await func(*args, **kwargs)


class SemaphoreLimiterService(RequestLimiterService):
    def __init__(self, max_concurrent: int):
        self._semaphore = asyncio.Semaphore(max_concurrent)

    async def with_limit(
        self,
        func: Callable[..., Coroutine[Any, Any, Any]],
        *args,
        **kwargs,
    ) -> Any:
        async with self._semaphore:
            return await func(*args, **kwargs)
