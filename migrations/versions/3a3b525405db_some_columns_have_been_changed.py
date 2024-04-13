"""Some columns have been changed

Revision ID: 3a3b525405db
Revises: 9ae77c57fede
Create Date: 2024-03-04 15:13:53.412587

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3a3b525405db'
down_revision = '9ae77c57fede'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('department')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('department', mysql.VARCHAR(length=35), nullable=False))

    # ### end Alembic commands ###