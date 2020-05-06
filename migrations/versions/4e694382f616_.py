"""empty message

Revision ID: 4e694382f616
Revises: 545fe1ae767c
Create Date: 2020-05-06 13:53:37.342639

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4e694382f616'
down_revision = '545fe1ae767c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('buglist', 'buggrade')
    op.drop_column('buglist', 'bugtype')
    op.add_column('bugtype', sa.Column('buggradeid', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bugtype', 'buggradeid')
    op.add_column('buglist', sa.Column('bugtype', mysql.TEXT(), nullable=True))
    op.add_column('buglist', sa.Column('buggrade', mysql.VARCHAR(length=10), nullable=True))
    # ### end Alembic commands ###
