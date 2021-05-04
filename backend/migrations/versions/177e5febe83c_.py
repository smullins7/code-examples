"""empty message

Revision ID: 177e5febe83c
Revises: 02b52ee4dfbc
Create Date: 2021-03-29 14:06:39.991021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '177e5febe83c'
down_revision = '02b52ee4dfbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###