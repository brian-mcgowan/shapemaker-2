"""SQLAlchemy custom data type handlers."""


import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import CHAR, TypeDecorator


class GUID(TypeDecorator):
    """Engine-agnostic GUID type.

    Uses Postgres-native UUID type if available or a 32 character string
    representing the UUID's numeric value in hexadecimal form.
    """

    cache_ok = True

    impl = CHAR

    def load_dialect_impl(self, dialect):
        """Loads the appropriate type descriptor for the target database."""
        if dialect.name == "postgresql":
            return dialect.type_descriptor(UUID())
        return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        """Converts Python values in database types."""
        if value is None:
            return value
        elif dialect.name == "postgresql":
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return f"{uuid.UUID(value).int:32x}"
            return f"{value.int:32x}"

    def process_result_value(self, value, dialect):
        """Converts query results into Python types."""
        if value is None:
            return value
        if not isinstance(value, uuid.UUID):
            value = uuid.UUID(value)
        return value
