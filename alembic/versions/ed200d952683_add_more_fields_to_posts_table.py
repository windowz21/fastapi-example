"""add more fields to posts table

Revision ID: ed200d952683
Revises: 74edfbda01a5
Create Date: 2022-01-09 12:39:35.075062

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ed200d952683'
down_revision = '74edfbda01a5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable='False', server_default='True'), )
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone='True'), nullable='False',
                                     server_default=sa.text('now()')), )
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
