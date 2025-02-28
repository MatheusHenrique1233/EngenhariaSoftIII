"""Adiciona campos nome, sobrenome e bairro à tabela ocorrencia

Revision ID: 6793dd0d167a
Revises: 4283b7809499
Create Date: 2024-10-13 00:42:28.511398

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6793dd0d167a'
down_revision = '4283b7809499'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ocorrencia', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nome', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('sobrenome', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('bairro', sa.String(length=100), nullable=False))
        batch_op.drop_column('localizacao')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ocorrencia', schema=None) as batch_op:
        batch_op.add_column(sa.Column('localizacao', mysql.VARCHAR(length=255), nullable=False))
        batch_op.drop_column('bairro')
        batch_op.drop_column('sobrenome')
        batch_op.drop_column('nome')

    # ### end Alembic commands ###
