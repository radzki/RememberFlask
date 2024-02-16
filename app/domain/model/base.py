from uuid import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.declarative import declared_attr

class BaseModel(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    
    pass

class PrimaryKeyMixin(BaseModel):
    id = Mapped[UUID] = mapped_column(primary_key=True)