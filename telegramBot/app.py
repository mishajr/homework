import asyncio
from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv
import os

from user_private.user_private import user_private

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))


dp = Dispatcher()

dp.include_router(user_private)


async def main():
    await bot.delete_webhook(drop_pending_updates=True) 
    await dp.start_polling(bot)


asyncio.run(main())