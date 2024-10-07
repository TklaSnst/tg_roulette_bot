from aiogram import Dispatcher, Bot
import asyncio
from aiogram.methods import DeleteWebhook
from tg.routers import router
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()
dp.include_router(router)


async def main():
    await dp.start_polling(bot, DeleteWebhook=True)


if __name__ == "__main__":
    asyncio.run(main())
