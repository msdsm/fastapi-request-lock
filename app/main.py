from fastapi import FastAPI
from app.routers import endpoints


def create_app() -> FastAPI:
    app = FastAPI(
        title="Request Limiter API",
        description="An API to demonstrate request limiting with FastAPI",
        version="1.0.0",
    )

    # Include routers
    app.include_router(endpoints.router)

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)