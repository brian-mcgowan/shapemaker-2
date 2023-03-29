"""Application factory module."""


from importlib.metadata import version

from fastapi import FastAPI

from shapemaker.config import ApplicationConfig
from shapemaker.containers import ApplicationContainer
from shapemaker.utils import ping


def main() -> FastAPI:
    """Creates an application instance."""
    container = ApplicationContainer()
    container.config.from_pydantic(ApplicationConfig())

    app = FastAPI(
        title="Shapemaker",
        version=version("shapemaker"),
        description="Geospatial geometry storage and retrieval",
    )

    app.include_router(ping.router)
    app.container = container

    return app
