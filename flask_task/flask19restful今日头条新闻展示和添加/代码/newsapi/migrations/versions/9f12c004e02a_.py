"""empty message

Revision ID: 9f12c004e02a
Revises: 76afa0ac8ddf
Create Date: 2020-06-11 09:42:59.361283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f12c004e02a'
down_revision = '76afa0ac8ddf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=True),
    sa.Column('content', sa.String(length=255), nullable=False),
    sa.Column('love_num', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('news_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['news_id'], ['news.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('news', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'news', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'news', type_='foreignkey')
    op.drop_column('news', 'user_id')
    op.drop_table('comment')
    # ### end Alembic commands ###
