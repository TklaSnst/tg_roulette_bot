from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import BigInteger
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable, Base):
    tg_id: Mapped[int] = mapped_column(nullable=False, primary_key=True)
    tg_fullname: Mapped[str] = mapped_column(default=None)
    balance: Mapped[float]
    is_superuser: Mapped[bool] = mapped_column(default=False)


class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(primary_key=True)
    cell_color: Mapped[str] = mapped_column(nullable=False)
    utc_time: Mapped[datetime.datetime] = mapped_column(nullable=False)