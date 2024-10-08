"""Add student and advisor fields to Thesis

Revision ID: aa6a51d998f7
Revises: 
Create Date: 2024-09-14 16:32:22.603160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa6a51d998f7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('thesis', schema=None) as batch_op:
        batch_op.add_column(sa.Column('student', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('advisor', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('thesis', schema=None) as batch_op:
        batch_op.drop_column('advisor')
        batch_op.drop_column('student')

    # ### end Alembic commands ###
