from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable, Base):
    id: int
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool


class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(primary_key=True)
    cell_color: Mapped[str] = mapped_column(nullable=False)
    utc_time: Mapped[datetime.datetime] = mapped_column(nullable=False)