"""Data persistence abstract for `Shape` objects."""


import uuid
from contextlib import AbstractContextManager
from typing import Callable, List, Type
from uuid import UUID

from sqlalchemy.orm import Session

from shapemaker.models.shape import Shape, ShapeCreateDTO, ShapeUpdateDTO, ShapeORM
from shapemaker.utils.errors import NotFoundError


class ShapeNotFoundError(NotFoundError):
    """Indicates failure to find a `Shape` resource."""

    entity_type = Shape.__name__


class ShapeRepository:
    """Handles `Shape` persistence operations."""

    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        """`ShapeRepository` constructor."""
        self.session_factory = session_factory

    @staticmethod
    def _create_resource(session: Session, shape_dto: ShapeCreateDTO) -> ShapeORM:
        """Creates a `ShapeORM` resource in the database without committing."""
        shape_orm = ShapeORM(**shape_dto.dict())
        session.add(shape_orm)
        return shape_orm

    @staticmethod
    def _delete_by_id(session: Session, resource_id: uuid.UUID) -> None:
        """Removes a `Shape` resource from the database."""
        shape_orm = ShapeRepository._get_by_id(session, resource_id)
        if not shape_orm:
            raise ShapeNotFoundError(resource_id)
        session.delete(shape_orm)

    @staticmethod
    def _get_by_id(session: Session, resource_id: uuid.UUID) -> Type[ShapeORM]:
        """Retrieves a `ShapeORM` resource from the database."""
        shape_orm = (
            session.query(ShapeORM).filter(ShapeORM.id == str(resource_id)).first()
        )
        if not shape_orm:
            raise ShapeNotFoundError(resource_id)
        return shape_orm

    def create(self, shape_dto: ShapeCreateDTO) -> Shape:
        """Creates a `Shape` resource in the database."""
        with self.session_factory() as session:
            shape_orm = self._create_resource(session, shape_dto)
            session.commit()
            session.refresh(shape_orm)
            return Shape.from_orm(shape_orm)

    def delete_by_id(self, resource_id: UUID) -> None:
        """Removes a `Shape` resource from the database."""
        with self.session_factory() as session:
            self._delete_by_id(session, resource_id)
            session.commit()

    def get_by_id(self, resource_id: uuid.UUID) -> Shape:
        """Retrieves a `Shape` resource from the database."""
        with self.session_factory() as session:
            shape_orm = self._get_by_id(session, resource_id)
            return Shape.from_orm(shape_orm)

    def get_all(self) -> List[Shape]:
        """Retrieves all `Shape` resources from the database as a list."""
        with self.session_factory() as session:
            shape_orm_list = session.query(ShapeORM).all()
            return [Shape.from_orm(shape_orm) for shape_orm in shape_orm_list]

    def replace_by_id(self, resource_id: uuid.UUID, resource: ShapeCreateDTO) -> None:
        """Replaces a `Shape` resource in the database."""
        with self.session_factory() as session:
            shape_orig = self._get_by_id(session, resource_id)
            for k, v in resource.dict().items():
                setattr(shape_orig, k, v)
            session.commit()

    def update_by_id(self, resource_id: uuid.UUID, resource: ShapeUpdateDTO) -> None:
        """Partially updates a `Shape` resource in the database."""
        with self.session_factory() as session:
            shape_orig = self._get_by_id(session, resource_id)
            for k, v in resource.dict().items():
                setattr(shape_orig, k, v)
            session.commit()
