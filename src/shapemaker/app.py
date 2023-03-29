"""Application factory module."""


from importlib.metadata import version

from fastapi import FastAPI

from shapemaker.utils import ping


def main() -> FastAPI:
    """Creates an application instance."""
    app = FastAPI(
        title="Shapemaker",
        version=version("shapemaker"),
        description="Geospatial geometry storage and retrieval",
    )

    app.include_router(ping.router)

    return app
