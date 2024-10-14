from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup)
from aiogram.types.web_app_info import WebAppInfo
from fastapi.templating import Jinja2Templates
import dotenv
import os


templates = Jinja2Templates(directory="front")
dotenv.load_dotenv()


start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="open",
                          web_app=WebAppInfo(url=f"{os.getenv("WEBHOOK_URL")}/page/base"))],
    [InlineKeyboardButton(text="another...", callback_data="open_smthng")]
])
