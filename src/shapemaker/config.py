"""Contains configuration objects for reading values from the environment."""


from pydantic import BaseSettings


class DatabaseConfig(BaseSettings):
    """Database configuration."""

    dsn: str = "sqlite:///shapemaker.db"

    class Config:
        """Pydantic BaseSettings behavior configuration."""

        env_prefix = "sm_db_"


class ApplicationConfig(BaseSettings):
    """Application configuration."""

    production: bool

    database: DatabaseConfig = DatabaseConfig()

    class Config:
        """Pydantic BaseSettings behavior configuration."""

        env_prefix = "sm_"
