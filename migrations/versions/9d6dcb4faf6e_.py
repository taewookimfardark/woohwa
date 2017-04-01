"""empty message

Revision ID: 9d6dcb4faf6e
Revises: ac5555cba75b
Create Date: 2017-03-23 18:52:45.239738

"""

# revision identifiers, used by Alembic.
revision = '9d6dcb4faf6e'
down_revision = 'ac5555cba75b'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('gender', sa.Enum('MALE', 'FEMALE'), nullable=True))
    op.drop_column('user', 'status')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('status', mysql.ENUM(u'MALE', u'FEMALE'), nullable=True))
    op.drop_column('user', 'gender')
    ### end Alembic commands ###
