from typing import Dict, Any
from fastapi import APIRouter, Depends

from app.dependencies import get_limiter_service, get_hello_service, get_world_service
from app.services.limiter import RequestLimiterService
from app.services.business import HelloService, WorldService

router = APIRouter()


@router.get("/hello", response_model=Dict[str, Any])
async def hello_endpoint(
    limiter: RequestLimiterService = Depends(get_limiter_service),
    hello_service: HelloService = Depends(get_hello_service),
) -> Dict[str, Any]:
    return await limiter.with_limit(hello_service.get_hello_message)


@router.get("/world", response_model=Dict[str, Any])
async def world_endpoint(
    limiter: RequestLimiterService = Depends(get_limiter_service),
    world_service: WorldService = Depends(get_world_service),
) -> Dict[str, Any]:
    return await limiter.with_limit(world_service.get_world_message)


@router.get("/health", response_model=Dict[str, str])
async def health_check() -> Dict[str, str]:
    return {"status": "ok"}
