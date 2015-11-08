"""empty message

Revision ID: 1cae8335ad86
Revises: None
Create Date: 2015-11-08 18:36:07.880372

"""

# revision identifiers, used by Alembic.
revision = '1cae8335ad86'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.Unicode(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_name')
    )
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.Unicode(length=255), nullable=True),
    sa.Column('end_date', sa.Unicode(length=255), nullable=True),
    sa.Column('todo_title', sa.Unicode(length=255), nullable=True),
    sa.Column('status', sa.UnicodeText(), nullable=True),
    sa.ForeignKeyConstraint(['todo_title'], ['user.user_name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo')
    op.drop_table('user')
    ### end Alembic commands ###
