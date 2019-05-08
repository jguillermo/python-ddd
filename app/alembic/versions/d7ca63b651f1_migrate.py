"""migrate

Revision ID: d7ca63b651f1
Revises: 
Create Date: 2019-05-08 17:19:40.447681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7ca63b651f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reto_user',
    sa.Column('id', sa.CHAR(length=36), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('last_name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reto_user')
    # ### end Alembic commands ###
