"""Add a column

Revision ID: 1923facbcf79
Revises: bcd349efbf5c
Create Date: 2023-09-26 18:16:29.060271

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1923facbcf79'
down_revision: Union[str, None] = 'bcd349efbf5c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
