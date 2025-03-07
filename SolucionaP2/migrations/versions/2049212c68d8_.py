"""empty message

Revision ID: 2049212c68d8
Revises: 4260f78859b1
Create Date: 2024-10-13 22:19:06.280933

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2049212c68d8'
down_revision = '4260f78859b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ocorrencia', schema=None) as batch_op:
        batch_op.alter_column('bairro',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ocorrencia', schema=None) as batch_op:
        batch_op.alter_column('bairro',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)

    # ### end Alembic commands ###
