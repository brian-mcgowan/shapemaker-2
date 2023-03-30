"""Custom application exceptions."""


from uuid import UUID


class NotFoundError(Exception):
    """Parent class for fail-to-find type errors."""

    entity_type: str

    def __init__(self, entity_id: UUID) -> None:
        """`NotFoundError` constructor."""
        super().__init__(f"{self.entity_type} '{entity_id}' not found")
