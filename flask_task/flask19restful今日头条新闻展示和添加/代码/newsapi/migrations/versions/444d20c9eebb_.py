"""empty message

Revision ID: 444d20c9eebb
Revises: 9f12c004e02a
Create Date: 2020-06-11 10:42:59.160504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '444d20c9eebb'
down_revision = '9f12c004e02a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('desc', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'desc')
    # ### end Alembic commands ###
