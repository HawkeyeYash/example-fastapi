"""add content column to posts table

Revision ID: f6554ff7f996
Revises: 2134c0bfc276
Create Date: 2024-08-19 15:08:04.864976

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6554ff7f996'
down_revision: Union[str, None] = '2134c0bfc276'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
