from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.domain.model import BasicModel


class User(BasicModel):
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str]
