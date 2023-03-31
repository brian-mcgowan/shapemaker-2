"""Contains database abstraction resources."""


from contextlib import contextmanager, AbstractContextManager
from typing import Callable

from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


BaseORM = declarative_base()


class Database:
    """Handles setup and tear down of database sessions."""

    def __init__(self, dsn: str, echo: bool = False) -> None:
        """`Database` constructor."""
        self._engine = create_engine(dsn, echo=echo)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            )
        )

    def create_database(self) -> None:
        """Creates required database resources.

        Not intended for use in production. Use migration scripts instead.
        """
        BaseORM.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        """Managed-context session factory method."""
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
