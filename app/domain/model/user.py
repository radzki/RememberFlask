from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.domain.model import BasicModel
from app.domain.model import SoftDeleteMixin


class User(BasicModel, SoftDeleteMixin):
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str]
