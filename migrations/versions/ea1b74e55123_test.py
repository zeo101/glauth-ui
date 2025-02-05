"""test

Revision ID: ea1b74e55123
Revises: 
Create Date: 2021-03-30 10:21:16.032322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea1b74e55123'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('gidnumber', sa.Integer(), nullable=False),
    sa.Column('primary', sa.Boolean(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('gidnumber')
    )
    op.create_index(op.f('ix_group_name'), 'group', ['name'], unique=True)
    op.create_table('settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('debug', sa.Boolean(), nullable=False),
    sa.Column('ldap_enabled', sa.Boolean(), nullable=True),
    sa.Column('ldap_listen', sa.String(length=40), nullable=True),
    sa.Column('ldaps_enabled', sa.Boolean(), nullable=True),
    sa.Column('ldaps_listen', sa.String(length=40), nullable=True),
    sa.Column('ldaps_cert', sa.String(length=40), nullable=True),
    sa.Column('ldaps_key', sa.String(length=40), nullable=True),
    sa.Column('basedn', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('included_groups',
    sa.Column('include_id', sa.Integer(), nullable=True),
    sa.Column('included_in_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['include_id'], ['group.gidnumber'], ),
    sa.ForeignKeyConstraint(['included_in_id'], ['group.gidnumber'], )
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('mail', sa.String(length=50), nullable=True),
    sa.Column('givenname', sa.String(length=40), nullable=True),
    sa.Column('surname', sa.String(length=40), nullable=True),
    sa.Column('uidnumber', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('password_hash', sa.String(length=64), nullable=False),
    sa.Column('primarygroup', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['primarygroup'], ['group.gidnumber'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uidnumber')
    )
    op.create_index(op.f('ix_user_mail'), 'user', ['mail'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('othergroups_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['group.gidnumber'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.gidnumber'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('othergroups_users')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_mail'), table_name='user')
    op.drop_table('user')
    op.drop_table('included_groups')
    op.drop_table('settings')
    op.drop_index(op.f('ix_group_name'), table_name='group')
    op.drop_table('group')
    # ### end Alembic commands ###
