from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup)
from aiogram.types.web_app_info import WebAppInfo


start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="open",
                          web_app=WebAppInfo(url='https://www.youtube.com/'))],
    [InlineKeyboardButton(text="another...", callback_data="open_smthng")]
])
