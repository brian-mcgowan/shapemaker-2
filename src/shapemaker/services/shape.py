"""Data persistence abstract for `Shape` objects."""

from typing import List
from uuid import UUID

from shapemaker.models.shape import Shape, ShapeCreateDTO, ShapeUpdateDTO
from shapemaker.repositories.shape import ShapeRepository


class ShapeService:
    """Handles `Shape` business objects."""

    def __init__(self, shape_repository: ShapeRepository) -> None:
        """`ShapeService` constructor."""
        self._repository = shape_repository

    def create(self, shape_dto: ShapeCreateDTO) -> Shape:
        """Creates a `Shape` object."""
        return self._repository.create(shape_dto)

    def delete_by_id(self, shape_id: UUID) -> None:
        """Deletes a `Shape` object."""
        self._repository.delete_by_id(shape_id)

    def get_by_id(self, shape_id: UUID) -> Shape:
        """Retrieves a `Shape` object."""
        return self._repository.get_by_id(shape_id)

    def get_all(self) -> List[Shape]:
        """Retrieves a list of `Shape` objects."""
        return self._repository.get_all()

    def replace_by_id(self, shape_id: UUID, shape_dto: ShapeCreateDTO) -> None:
        """Replaces a `Shape` object."""
        self._repository.replace_by_id(shape_id, shape_dto)

    def update_by_id(self, shape_id: UUID, shape_dto: ShapeUpdateDTO) -> None:
        """Partially updates a `Shape` object."""
        self._repository.update_by_id(shape_id, shape_dto)
