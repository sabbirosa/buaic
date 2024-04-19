"""initial migration

Revision ID: be13fe63b674
Revises: efad21e1c697
Create Date: 2024-04-13 22:11:07.324815

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'be13fe63b674'
down_revision = 'efad21e1c697'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('semester',
               existing_type=mysql.VARCHAR(length=4),
               type_=sa.String(length=30),
               existing_nullable=False)
        batch_op.alter_column('joined_semester',
               existing_type=mysql.VARCHAR(length=10),
               type_=sa.String(length=30),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('joined_semester',
               existing_type=sa.String(length=30),
               type_=mysql.VARCHAR(length=10),
               existing_nullable=False)
        batch_op.alter_column('semester',
               existing_type=sa.String(length=30),
               type_=mysql.VARCHAR(length=4),
               existing_nullable=False)

    # ### end Alembic commands ###