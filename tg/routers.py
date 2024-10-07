from aiogram import Router, F
from aiogram.types import Message
from .t import *
import tg.keyboards as kbs

router = Router()


@router.message(F.text == "/start")
async def start(message: Message):
    await message.delete()
    await message.answer_photo(caption=START, reply_markup=kbs.start_kb, photo=PHOTO_URL)

