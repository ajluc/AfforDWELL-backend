"""add PLUTO model

Revision ID: 91db6e9e3ab1
Revises: a3cbc3c7c9aa
Create Date: 2024-03-10 15:41:44.180198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91db6e9e3ab1'
down_revision = 'a3cbc3c7c9aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pluto_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('zipcode', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('unitsres', sa.String(length=255), nullable=True),
    sa.Column('unitstotal', sa.String(length=255), nullable=True),
    sa.Column('yearbuilt', sa.String(length=255), nullable=True),
    sa.Column('bbl', sa.Integer(), nullable=True),
    sa.Column('latitude', sa.String(length=255), nullable=True),
    sa.Column('longitude', sa.String(length=255), nullable=True),
    sa.Column('version', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pluto_info')
    # ### end Alembic commands ###
