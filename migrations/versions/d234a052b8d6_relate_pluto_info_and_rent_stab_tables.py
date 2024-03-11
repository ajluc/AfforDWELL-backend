"""relate pluto_info and rent_stab tables

Revision ID: d234a052b8d6
Revises: 3688bb518a77
Create Date: 2024-03-11 11:05:45.718623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd234a052b8d6'
down_revision = '3688bb518a77'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pluto_info', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['bbl'])

    with op.batch_alter_table('rent_stab', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'pluto_info', ['ucbbl'], ['bbl'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rent_stab', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('pluto_info', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###