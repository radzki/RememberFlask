import uuid
from datetime import datetime
from typing import Any

from sqlalchemy import MetaData
from sqlalchemy import text
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy_easy_softdelete.hook import IgnoredTable
from sqlalchemy_easy_softdelete.mixin import generate_soft_delete_mixin_class

# Define a database-wide constraint naming convention for our Base.
db_wide_constraint_naming_convention = {
    'ix': 'ix_%(column_0_label)s',
    # Unique Shows N (all) columns in constraint name
    'uq': 'uq_%(table_name)s_%(column_0_N_name)s',
    'ck': 'ck_%(table_name)s_%(column_0_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s',
}

# Apply the naming constraint convention to our Base
# This helps with Alembic and Database Migrations
db_metadata = MetaData(naming_convention=db_wide_constraint_naming_convention)

class DbBaseModel(DeclarativeBase):
    metadata = db_metadata

    #type_annotation_map = {dict[str, Any]: JSON}

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class PrimaryKeyMixin:
    @declared_attr
    def id(self) -> Mapped[uuid.UUID]:
        return mapped_column(
            'id',
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            default=uuid.uuid4,
            server_default=text('gen_random_uuid()'),
        )

    def __repr__(self):
        return f'<{self.__class__.__name__} PKID={self.id}>'


class BasicModel(DbBaseModel, PrimaryKeyMixin):
    """
    The default model that most database models should inherit from.
    """

    __abstract__ = True


class SoftDeleteMixin(
    generate_soft_delete_mixin_class(
        # This table will be ignored by the hook
        # even if the table has the soft-delete column
        ignored_tables=[IgnoredTable(table_schema='public', name='cars')],
    ),
):
    # type hint for autocomplete IDE support
    deleted_at: datetime
