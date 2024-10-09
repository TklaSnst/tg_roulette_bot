from contextlib import asynccontextmanager
from aiogram.types import Update, Message
from aiogram.client.default import DefaultBotProperties
from aiogram import Dispatcher, Bot, F
from aiogram.enums import ParseMode
from dotenv import load_dotenv, find_dotenv
from database.database import create_tables, drop_tables
from api.routers import fastapi_users, auth_backend
from api.users.schemas import (UserCreate, UserRead, UserUpdate)
import os
import uvicorn
from fastapi import FastAPI, Request
from tg.t import *
import tg.keyboards as kbs


load_dotenv(find_dotenv())
bot = Bot(os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    await create_tables()
    print('Tables are new and clean')
    await bot.set_webhook(f"{os.getenv('WEBHOOK_URL')}/webhook",
                          allowed_updates=dp.resolve_used_update_types(),
                          drop_pending_updates=True)
    yield
    print('Shutdown')


app = FastAPI(lifespan=lifespan)
app.include_router(
    fastapi_users.get_auth_router(auth_backend, requires_verification=True),
    prefix="/auth/jwt",
    tags=["fastapo_users_auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app = FastAPI()
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app = FastAPI()
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@app.post('/webhook')
async def webhook(request: Request):
    update = Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)


@dp.message(F.text == "/start")
async def start(message: Message):
    await message.delete()
    await message.answer_photo(caption=START, reply_markup=kbs.start_kb, photo=PHOTO_URL)

