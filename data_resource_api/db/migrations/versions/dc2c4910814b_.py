"""empty message

Revision ID: dc2c4910814b
Revises: 6efc2e60d0bd
Create Date: 2019-03-22 13:38:06.252629

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'dc2c4910814b'
down_revision = '6efc2e60d0bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pathways_programs',
    sa.Column('program_id', sa.Integer(), nullable=False),
    sa.Column('program_provider', sa.String(length=140), nullable=False),
    sa.Column('provider_url', sa.String(length=256), nullable=False),
    sa.Column('provider_address', sa.String(length=1024), nullable=False),
    sa.Column('major', sa.String(length=256), nullable=False),
    sa.Column('program_name', sa.String(length=256), nullable=False),
    sa.Column('program_url', sa.String(length=256), nullable=False),
    sa.Column('program_description', sa.String(length=4096), nullable=False),
    sa.Column('program_potential_outcome', sa.String(length=256), nullable=False),
    sa.Column('program_fees', sa.Integer(), nullable=False),
    sa.Column('salary_paid', sa.Integer(), nullable=False),
    sa.Column('program_length', sa.String(length=256), nullable=False),
    sa.Column('cost_of_books_and_supplies', sa.Integer(), nullable=False),
    sa.Column('credential_earned', sa.String(length=256), nullable=False),
    sa.Column('accreditation_name', sa.String(length=256), nullable=False),
    sa.Column('provider_id', sa.String(length=140), nullable=True),
    sa.Column('provider_latitude', sa.Integer(), nullable=True),
    sa.Column('provider_longitude', sa.Integer(), nullable=True),
    sa.Column('program_address', sa.String(length=1024), nullable=True),
    sa.Column('total_units', sa.Integer(), nullable=True),
    sa.Column('unit_cost', sa.Integer(), nullable=True),
    sa.Column('is_preparation', sa.Boolean(), nullable=True),
    sa.Column('is_occupational_requirement', sa.Boolean(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('is_diploma_required', sa.Boolean(), nullable=True),
    sa.Column('prerequisites', sa.String(length=4096), nullable=True),
    sa.Column('financial_aid5', sa.Integer(), nullable=True),
    sa.Column('financial_aid4', sa.Integer(), nullable=True),
    sa.Column('financial_aid3', sa.Integer(), nullable=True),
    sa.Column('financial_aid2', sa.Integer(), nullable=True),
    sa.Column('financial_aid1', sa.Integer(), nullable=True),
    sa.Column('optional_fields', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('user_provided_fields', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('program_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pathways_programs')
    # ### end Alembic commands ###
