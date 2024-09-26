import asyncio
from bot.loader import *
from db.functions import init_db

async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    init_db() # инитиализация базы данных
    asyncio.run(main())
