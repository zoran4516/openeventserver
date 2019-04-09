"""empty message

Revision ID: 82cdc4ac5d20
Revises: 1959f5049425
Create Date: 2018-07-17 12:01:24.401782

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '82cdc4ac5d20'
down_revision = '1959f5049425'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('settings', sa.Column('cookie_policy', sa.String(), nullable=True))
    op.add_column('settings', sa.Column('cookie_policy_link', sa.String(), nullable=True))
    op.drop_column('users', 'has_accepted_cookie_policy')
    # ### end Alembic commands ###
    settings_table = sa.sql.table('settings', sa.Column('cookie_policy', sa.String()),
                                  sa.Column('cookie_policy_link', sa.String()))
    op.execute(settings_table.update()
               .where(settings_table.c.cookie_policy.is_(None))
               .values({'cookie_policy': "This website, and certain approved third parties, use functional, "
                                         "analytical and tracking cookies (or similar technologies) to understand your "
                                         "event preferences and provide you with a customized experience. "
                                         "By closing this banner or by continuing to use the site, you agree. "
                                         "For more information please review our cookie policy.",
                        'cookie_policy_link': 'http://next.cookie-policy.eventyay.com'}))


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('has_accepted_cookie_policy', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('settings', 'cookie_policy_link')
    op.drop_column('settings', 'cookie_policy')
    # ### end Alembic commands ###
