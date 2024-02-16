from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.domain.model import PrimaryKeyMixin


class Account(PrimaryKeyMixin):
    name: Mapped[str] = mapped_column(String(32))
