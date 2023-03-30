"""Contains `Shape` models."""


from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, String

from shapemaker.models.base import BaseDataModel, BaseDataORM


class Shape(BaseDataModel):
    """Geospatial geometry container class."""

    name: str

    class Config:
        """Pydantic BaseModel behavior configuration."""

        orm_mode = True


class ShapeCreateDTO(BaseModel):
    """`Shape` creation data transfer object."""

    name: str


class ShapeUpdateDTO(BaseModel):
    """`Shape` modification data transfer object."""

    name: Optional[str]


class ShapeORM(BaseDataORM):
    """`Shape` object-relational mapping."""

    __tablename__ = "shape"

    name = Column(String, nullable=False)
