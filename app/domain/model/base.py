from uuid import UUID

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class BaseModel(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    pass

class PrimaryKeyMixin(BaseModel):
    id = Mapped[UUID] = mapped_column(primary_key=True)
