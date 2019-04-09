"""empty message

Revision ID: 694a281af0a8
Revises: cbf72dcb80e3
Create Date: 2016-08-28 10:37:31.704298

"""

# revision identifiers, used by Alembic.
revision = '694a281af0a8'
down_revision = 'cbf72dcb80e3'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_system_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['custom_sys_role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_system_role')
    ### end Alembic commands ###
