"""empty message

Revision ID: 83c9242615d9
Revises: f0c8b17a152b
Create Date: 2021-12-12 18:08:48.143192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83c9242615d9'
down_revision = 'f0c8b17a152b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('another')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('another',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='another_pkey')
    )
    # ### end Alembic commands ###
