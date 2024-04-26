"""added  the related_questions_id in related_questions table

Revision ID: 005d41dec549
Revises: 7543dcc9f23b
Create Date: 2024-04-26 12:32:26.819746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '005d41dec549'
down_revision = '7543dcc9f23b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('related_questions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('related_question_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'questions', ['related_question_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('related_questions', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('related_question_id')

    # ### end Alembic commands ###
