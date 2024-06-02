"""create user table

Revision ID: bec08a730fbf
Revises: 
Create Date: 2024-01-12 22:03:15.062882

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bec08a730fbf"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.String(50)),
        sa.Column("last_name", sa.String(50)),
        sa.Column("email", sa.String(256)),
        sa.Column("created", sa.TIMESTAMP),
    ),


def downgrade() -> None:
    op.drop_table("users")
