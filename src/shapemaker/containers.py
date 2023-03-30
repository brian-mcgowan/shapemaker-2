"""Contains dependency injection containers."""


from dependency_injector import containers, providers

from shapemaker.database import Database


class ApplicationContainer(containers.DeclarativeContainer):
    """Application dependency injection container."""

    config = providers.Configuration()

    database = providers.Singleton(
        Database,
        dsn=config.database.dsn,
        echo=False if config.production else True,
    )
