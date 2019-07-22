"""followers

Revision ID: 065755ff5ea3
Revises: ff825d498954
Create Date: 2019-07-21 19:57:34.922905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '065755ff5ea3'
down_revision = 'ff825d498954'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
