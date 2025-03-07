"""empty message

Revision ID: 44ace4c6aa95
Revises: 86f781860a71
Create Date: 2024-10-13 02:30:26.882553

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '44ace4c6aa95'
down_revision = '86f781860a71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ocorrencia', schema=None) as batch_op:
        batch_op.drop_column('endereco')

    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('endereco', sa.String(length=255), nullable=False))
        batch_op.drop_column('rua')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rua', mysql.VARCHAR(length=100), nullable=False))
        batch_op.drop_column('endereco')

    with op.batch_alter_table('ocorrencia', schema=None) as batch_op:
        batch_op.add_column(sa.Column('endereco', mysql.VARCHAR(length=255), nullable=False))

    # ### end Alembic commands ###
