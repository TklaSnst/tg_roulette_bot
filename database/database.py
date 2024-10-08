from sqlalchemy.ext.asyncio import (async_sessionmaker, create_async_engine, AsyncSession)
from .models import Base
import dotenv
import os

dotenv.load_dotenv()

engine = create_async_engine(os.getenv("DATABASE_URL"))
session = async_sessionmaker(engine)


async def create_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
