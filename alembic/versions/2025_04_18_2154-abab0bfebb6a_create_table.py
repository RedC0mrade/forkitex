"""Create table

Revision ID: abab0bfebb6a
Revises:
Create Date: 2025-04-18 21:54:15.124720

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "abab0bfebb6a"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "tron_requests",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("wallet_address", sa.String(), nullable=False),
        sa.Column(
            "timestamp",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_tron_requests")),
    )
    op.create_index(
        op.f("ix_tron_requests_wallet_address"),
        "tron_requests",
        ["wallet_address"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        op.f("ix_tron_requests_wallet_address"), table_name="tron_requests"
    )
    op.drop_table("tron_requests")
