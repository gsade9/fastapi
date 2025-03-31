"""add column to posts table

Revision ID: 75de8f202d2e
Revises: 2b77114dacc8
Create Date: 2025-03-31 17:21:36.623850

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75de8f202d2e'
down_revision: Union[str, None] = '2b77114dacc8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
