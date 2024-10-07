from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="open", callback_data="open_web")],
    [InlineKeyboardButton(text="another...", callback_data="open_smthng")]
])
