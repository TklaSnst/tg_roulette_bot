from sqlalchemy.ext.asyncio import AsyncSession
from .models import User
from sqlalchemy import select


async def create_user(async_session: AsyncSession, user_add: User):
    async with async_session() as session:
        stmt = select(User).where(User.tg_id == user_add.tg_id)
        result = await session.execute(stmt)
        user = result.scalar()
        if user is None:
            session.add(user_add)
            await session.commit()
            # await session.refresh(user_add)


async def get_user_by_tg_id(async_session: AsyncSession, user_add: User):
    async with async_session() as session:
        stmt = select(User).where(User.tg_id == user_add.tg_id)
        result = await session.execute(stmt)
        user = result.scalar()
        return user


async def get_user_by_id(async_session: AsyncSession, user_add: User):
    async with async_session() as session:
        stmt = select(User).where(User.id == user_add.id)
        result = await session.execute(stmt)
        user = result.scalar()
        return user
