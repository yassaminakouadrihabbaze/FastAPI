"""create users table

Revision ID: ef50f2c8ab2c
Revises: 
Create Date: 2023-02-16 18:31:26.539681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef50f2c8ab2c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass
    # op.create_table(
    #     'user',
    #     sa.Column('id', sa.Integer(), nullable=False),
    #     sa.Column('email', sa.String(), nullable=False),
    #     sa.PrimaryKeyConstraint('id')
    # )


def downgrade() -> None:
    pass
    # op.drop_table('user')
