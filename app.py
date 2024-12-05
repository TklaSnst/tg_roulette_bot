from users.auth import fastapi_users
from contextlib import asynccontextmanager
from aiogram.types import Update, Message, CallbackQuery
from aiogram.client.default import DefaultBotProperties
from aiogram import Dispatcher, Bot, F
from aiogram.enums import ParseMode
from dotenv import load_dotenv, find_dotenv
from fastapi.staticfiles import StaticFiles
from users.auth import auth_backend
from database.database import create_tables, drop_tables, async_session
from database.crud import (create_user, get_list_of_users)
from users.user_schemas import UserCreate
from database.models import User
import os
from fastapi import FastAPI, Request
from tg.t import *
from tg.keyboards import get_start_kb

from front.pages.pages_router import router as pages_router


load_dotenv(find_dotenv())
bot = Bot(os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await drop_tables()
    # print("tables dropped")
    await create_tables()
    print('Tables are ready')
    await bot.set_webhook(f"{os.getenv('WEBHOOK_URL')}/webhook",
                          allowed_updates=dp.resolve_used_update_types(),
                          drop_pending_updates=True)
    print("bot is ready")
    yield
    print('Shutdown')


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(pages_router)
app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)


@app.post('/webhook')
async def webhook(request: Request):
    update = Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)


@dp.message(F.text == "/start")
async def start(message: Message):
    user_create = UserCreate(
        tg_fullname=message.from_user.full_name,
        tg_id=message.from_user.id,
        balance=100,
        is_superuser=False,
    )
    data = User(**user_create.model_dump())
    await create_user(async_session=async_session, user_add=data)
    await message.answer_photo(caption=START,
                               reply_markup=await get_start_kb(message.from_user.id),
                               photo=PHOTO_URL)


@dp.callback_query(F.data == "list of users")
async def get_all_users(callback: CallbackQuery):
    if callback.from_user.id == os.getenv("ADMIN1TGID"):
        t = await get_list_of_users(async_session=async_session)
        print(t)
        await callback.message.answer(text=t)
    else:
        await callback.message.answer(text="U are not admin!!!")
