"""ADD COLUMN TO POSTS TABLE

Revision ID: 57c79c8240c2
Revises: 6294731b0856
Create Date: 2022-01-09 10:34:42.753760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57c79c8240c2'
down_revision = '6294731b0856'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
