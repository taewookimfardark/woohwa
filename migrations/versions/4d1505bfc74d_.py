"""empty message

Revision ID: 4d1505bfc74d
Revises: 028c762ec2a4
Create Date: 2017-03-03 00:44:49.059110

"""

# revision identifiers, used by Alembic.
revision = '4d1505bfc74d'
down_revision = '028c762ec2a4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bucket', sa.Column('profile_image', sa.String(length=1024), nullable=True))
    op.add_column('bucket', sa.Column('profile_image_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bucket', 'profile_image_id')
    op.drop_column('bucket', 'profile_image')
    ### end Alembic commands ###
