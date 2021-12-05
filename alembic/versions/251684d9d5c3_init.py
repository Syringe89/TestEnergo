"""init

Revision ID: 251684d9d5c3
Revises: 
Create Date: 2021-12-05 13:59:20.015856

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '251684d9d5c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('device',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('dev_type', sa.String(length=120), nullable=True),
    sa.Column('dev_id', postgresql.MACADDR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('endpoint',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('device_id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['device_id'], ['device.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('endpoint')
    op.drop_table('device')
    # ### end Alembic commands ###
