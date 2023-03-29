"""Contains configuration objects for reading values from the environment."""


from pydantic import BaseSettings


class ApplicationConfig(BaseSettings):
    """Application configuration."""

    production: bool

    class Config:
        """Pydantic BaseSettings behavior configuration."""

        env_prefix = "sm_"
