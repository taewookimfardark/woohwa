"""empty message

Revision ID: 706236bb1036
Revises: e04a48bb1bc5
Create Date: 2017-03-12 15:19:13.581766

"""

# revision identifiers, used by Alembic.
revision = '706236bb1036'
down_revision = 'e04a48bb1bc5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bucket', sa.Column('completed_time', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bucket', 'completed_time')
    ### end Alembic commands ###
