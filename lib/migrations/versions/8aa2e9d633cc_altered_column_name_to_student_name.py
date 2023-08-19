"""Altered column "name" to "student_name"

Revision ID: 8aa2e9d633cc
Revises: 6c94a461b1f7
Create Date: 2023-08-18 21:09:21.456918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8aa2e9d633cc'
down_revision = '6c94a461b1f7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name = 'student_name')


def downgrade() -> None:
    op.alter_column('students', 'student_name', new_column_name = 'name')
