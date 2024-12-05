from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup)
from aiogram.types.web_app_info import WebAppInfo
from fastapi.templating import Jinja2Templates
import dotenv
import os


templates = Jinja2Templates(directory="front")
dotenv.load_dotenv()


async def get_start_kb(tg_id):
    start_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="open",
                              web_app=WebAppInfo(url=f"{os.getenv("WEBHOOK_URL")}/page/base/?tg_id={tg_id}"))],
        [InlineKeyboardButton(text="another...", callback_data="open_smthng")]
    ])

    start_kb_admin = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="open",
                              web_app=WebAppInfo(url=f"{os.getenv("WEBHOOK_URL")}/page/base/?tg_id={tg_id}"))],
        [InlineKeyboardButton(text="Список пользователей", callback_data="list of users")],
        [InlineKeyboardButton(text="Заблокировать пользователя", callback_data="ban_user")],
        [InlineKeyboardButton(text="добавтиь админа", callback_data="add_admin")],
        [InlineKeyboardButton(text="another...", callback_data="open_smthng")]
    ])
    if tg_id == os.getenv("ADMIN1TGID"):
        return start_kb_admin
    else:
        return start_kb
