"""Your migration message

Revision ID: 031aaced6611
Revises: 708538ba9c2b
Create Date: 2024-03-02 21:51:17.853203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '031aaced6611'
down_revision = '708538ba9c2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company', sa.Column('class_type', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('company', 'class_type')
    # ### end Alembic commands ###
