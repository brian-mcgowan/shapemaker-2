"""Contains dependency injection containers."""


from dependency_injector import containers, providers


class ApplicationContainer(containers.DeclarativeContainer):
    """Application dependency injection container."""

    config = providers.Configuration()
