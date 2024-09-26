from aiogram import Router, types
from bot import config
from bot.admin.kb import get_keyboard_for_admin

# Создаем роутер для администраторских команд
admin = Router()

# Обработчик сообщений для команды "/admin"
@admin.message(lambda message: message.text == "/admin" and message.from_user.id in config.admins)
async def manage_orders(message: types.Message):
    # Отправка сообщения о том, что админ-приложение открыто
    await message.reply("Вы открыли админ приложение")
    # Приветствие администратора с клавиатурой
    await message.answer('Привет, Админ', reply_markup=get_keyboard_for_admin())

# Обработчик нажатий на кнопки в админ меню
@admin.callback_query(lambda callback_query: callback_query.data == "admin_btn" and callback_query.from_user.id in config.admins)
async def manage_admin_options(callback_query: types.CallbackQuery):
    # Ответ на нажатие кнопки с уведомлением о будущей функции
    await callback_query.message.reply("Скоро мы добавим возможность выгрузки!")
