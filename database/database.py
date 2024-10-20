from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from .models import Base
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_async_engine(os.getenv("DATABASE_URL"))
async_session = async_sessionmaker(engine)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
