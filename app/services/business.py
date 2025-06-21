import asyncio
from typing import Dict, Any
from datetime import datetime


class HelloService:
    async def get_hello_message(self) -> Dict[str, Any]:
        await asyncio.sleep(2)

        return {
            "message": "Hello!",
            "service": "hello",
            "timestamp": datetime.now().isoformat(),
            "processing_time": "2 seconds",
        }


class WorldService:
    async def get_world_message(self) -> Dict[str, Any]:
        await asyncio.sleep(1)

        return {
            "message": "World!",
            "service": "world",
            "timestamp": datetime.now().isoformat(),
            "processing_time": "1 second",
        }
