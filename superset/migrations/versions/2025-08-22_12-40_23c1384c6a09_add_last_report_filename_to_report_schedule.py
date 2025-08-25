"""add last_report_filename to report_schedule

Revision ID: 23c1384c6a09
Revises: 363a9b1e8992
Create Date: 2025-08-22 12:40:00.000000

"""
import sqlalchemy as sa

from superset.migrations.shared.utils import add_columns, drop_columns

# revision identifiers, used by Alembic.
revision = "23c1384c6a09"
down_revision = "363a9b1e8992"
branch_labels = None
depends_on = None

def upgrade():
    add_columns("report_schedule", sa.Column("last_report_filename", sa.String(length=512), nullable=True))

def downgrade():
    drop_columns("report_schedule", "last_report_filename")
