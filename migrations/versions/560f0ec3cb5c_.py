"""empty message

Revision ID: 560f0ec3cb5c
Revises: 
Create Date: 2020-11-15 22:56:04.957241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '560f0ec3cb5c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('ip', sa.String(length=100), nullable=False),
                    sa.Column('country', sa.String(length=100), nullable=False),
                    sa.Column('distance', sa.Integer(), nullable=True),
                    sa.Column('iso_code', sa.String(length=2), nullable=False),
                    sa.Column('timestamp', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id'))
    op.create_table('logs',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('ip', sa.String(length=100), nullable=False),
                    sa.Column('user_id', sa.String(length=100), nullable=False),
                    sa.Column('timestamp', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id'))
    pass


def downgrade():
    op.drop_table('users')
    op.drop_table('logs')
    pass
