from sqlalchemy.ext.asyncio import AsyncSession
from .models import User, Game
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


async def get_user_by_tg_id(async_session: AsyncSession, tg_id: int):
    async with async_session() as session:
        stmt = select(User).where(User.tg_id == tg_id)
        result = await session.execute(stmt)
        user = result.scalar()
        return user


async def get_list_of_users(async_session: AsyncSession):
    async with async_session() as session:
        text = ""
        i = 1
        stmt = select(User)
        result = await session.execute(stmt)
        users = result.scalars()
        for user in users:
            text += f"{i}- name: {user.tg_fullname}, tg_id: {user.tg_id}, balance: {user.balance}\n"
        return text


async def get_user_balance(async_session: AsyncSession, tg_id: int):
    async with async_session() as session:
        stmt = select(User).where(User.tg_id == tg_id)
        result = await session.execute(stmt)
        user = result.scalar()
        return user.balance


async def patch_user_balance(async_session: AsyncSession, tg_id: int, bet: int = 0):
    async with async_session() as session:
        try:
            stmt = select(User).where(User.tg_id == tg_id)
            result = await session.execute(stmt)
            user = result.scalar()
            if user.balance < bet:
                return 0
            else:
                user.balance -= bet
                a = user.balance
                await session.commit()
                return a
        except Exception as e:
            session.rollback()
            raise e


async def user_win(async_session: AsyncSession, tg_id: int, bet: int, coeff: int):
    async with async_session() as session:
        try:
            stmt = select(User).where(User.tg_id == tg_id)
            result = await session.execute(stmt)
            user = result.scalar()
            user.balance += coeff * bet
            bal = user.balance
            await session.commit()
            return bal
        except Exception as e:
            raise e


async def create_game(async_session: AsyncSession, game: Game):
    async with async_session() as session:
        session.add(game)
        await session.commit()
