"""Contains dependency injection containers."""


from dependency_injector import containers, providers

from shapemaker.database import Database
from shapemaker.repositories.shape import ShapeRepository
from shapemaker.services.shape import ShapeService


class ApplicationContainer(containers.DeclarativeContainer):
    """Application dependency injection container."""

    config = providers.Configuration()

    database = providers.Singleton(
        Database,
        dsn=config.database.dsn,
        echo=False if config.production else True,
    )

    shape_repository = providers.Factory(
        ShapeRepository,
        session_factory=database.provided.session,
    )

    shape_service = providers.Factory(
        ShapeService,
        shape_repository=shape_repository,
    )
