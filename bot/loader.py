from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from bot.admin.handlers import admin
from bot.user.handlers import user
from bot.config import *

load_dotenv()

# создание диспатчера и добавление раутов
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(admin)
dp.include_router(user)

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML')) # создание бота



