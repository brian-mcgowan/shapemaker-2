"""create shape table

Revision ID: fc2a28273861
Revises: 
Create Date: 2023-03-30 20:18:32.723676

"""
import uuid

from alembic import op
import sqlalchemy as sa

from shapemaker.utils.sqlalchemy import GUID


# revision identifiers, used by Alembic.
revision = "fc2a28273861"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "shape",
        sa.Column(
            "id",
            GUID(),
            primary_key=True,
            nullable=False,
            default=lambda: str(uuid.uuid4()),
        ),
        sa.Column(
            "created_at",
            sa.DateTime,
            nullable=False,
            default=sa.func.current_timestamp(),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            default=sa.func.current_timestamp(),
            onupdate=sa.func.current_timestamp(),
        ),
        sa.Column("name", sa.String, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("shape")
