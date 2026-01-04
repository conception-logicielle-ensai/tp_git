from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )
    title: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    author: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    available: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )
