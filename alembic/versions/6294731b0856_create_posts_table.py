"""create posts table

Revision ID: 6294731b0856
Revises: 
Create Date: 2022-01-09 10:19:30.659783

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6294731b0856'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
