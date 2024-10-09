from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
import datetime


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTableUUID, Base):
    username: Mapped[str] = mapped_column(nullable=False)
    registered_at: Mapped[datetime.datetime] = mapped_column(default=datetime.UTC)
