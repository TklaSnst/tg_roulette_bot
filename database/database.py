from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import (async_sessionmaker, create_async_engine, AsyncSession)
from .models import Base, User
import dotenv
import os

dotenv.load_dotenv()

engine = create_async_engine(os.getenv("DATABASE_URL"))
session = async_sessionmaker(engine, expire_on_commit=False)


async def create_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def get_user_db(async_session: AsyncSession):
    yield SQLAlchemyUserDatabase(async_session, User)
