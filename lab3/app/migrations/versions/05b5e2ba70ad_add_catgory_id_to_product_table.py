"""add catgory id to product table

Revision ID: 05b5e2ba70ad
Revises: 8950e96231a2
Create Date: 2023-10-23 13:01:19.678640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05b5e2ba70ad'
down_revision = '8950e96231a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cat_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_cat_id_categories', 'categories', ['cat_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('cat_id')

    # ### end Alembic commands ###
