"""Contains base models."""


import datetime
import uuid

from pydantic import BaseModel
from sqlalchemy import Column, DateTime
from sqlalchemy.sql.functions import func

from shapemaker.database import BaseORM
from shapemaker.utils.sqlalchemy import GUID


class BaseDataModel(BaseModel):
    """Parent class for application data models."""

    id: uuid.UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime


class BaseDataORM(BaseORM):
    """Parent class for application object-relational mappings."""

    __abstract__ = True

    id = Column(
        GUID(), primary_key=True, nullable=False, default=lambda: str(uuid.uuid4())
    )
    created_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    updated_at = Column(
        DateTime,
        nullable=False,
        default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )
