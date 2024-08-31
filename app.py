import asyncio
from aiogram import Bot, Dispatcher

from key import API_TOKEN
from handlers import router


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())