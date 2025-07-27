from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.config import settings
from app.api.v1 import auth, root, user, room, schedule, seat, movie
import toml
import uvicorn
from fastapi.staticfiles import StaticFiles


def create_app():
    with open("pyproject.toml", "r") as f:
        data = toml.load(f)

    project_version = data["project"]["version"]
    app = FastAPI(version=project_version)

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        # Startup code here
        print("Starting up...")

        yield  # This is where the app runs

        # Shutdown code here
        print("Shutting down...")

    # app.add_middleware(JWTAuthMiddleware)  # type: ignore

    # app = FastAPI(version=project_version)

    # Register static folder
    app.mount(settings.STATIC_API_PATH, StaticFiles(directory=settings.STATIC_STORAGE_DIR), name="static")

    # Register routers
    app.include_router(root.router, prefix=settings.API_V1_STR)
    app.include_router(auth.router, prefix=settings.API_V1_STR)
    app.include_router(user.router, prefix=settings.API_V1_STR)
    app.include_router(room.router, prefix=settings.API_V1_STR)
    app.include_router(movie.router, prefix=settings.API_V1_STR)
    app.include_router(seat.router, prefix=settings.API_V1_STR)
    app.include_router(schedule.router, prefix=settings.API_V1_STR)
    return app

def run_app(app: FastAPI):
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False, lifespan="on")

def create_run_app():
    run_app(create_app())