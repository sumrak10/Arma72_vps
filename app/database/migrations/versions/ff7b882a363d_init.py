"""init

Revision ID: ff7b882a363d
Revises: d363cf307ae8
Create Date: 2023-07-24 19:52:31.261114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff7b882a363d'
down_revision = 'd363cf307ae8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products_in_orders', sa.Column('product_img', sa.String(length=1024), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products_in_orders', 'product_img')
    # ### end Alembic commands ###
