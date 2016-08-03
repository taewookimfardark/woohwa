"""empty message

Revision ID: 9aa8b3ceb041
Revises: 42a51078d588
Create Date: 2016-08-03 23:27:09.880114

"""

# revision identifiers, used by Alembic.
revision = '9aa8b3ceb041'
down_revision = '42a51078d588'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('complete_bucket', sa.Column('completecomment', sa.String(length=500), nullable=True))
    op.add_column('complete_bucket', sa.Column('completedate', sa.String(length=200), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('complete_bucket', 'completedate')
    op.drop_column('complete_bucket', 'completecomment')
    ### end Alembic commands ###
