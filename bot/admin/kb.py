from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Функция для создания клавиатуры для админ-приложения
def get_keyboard_for_admin():
    # Инициализация сборщика клавиатуры
    keyboard = InlineKeyboardBuilder()

    # Добавление кнопки "Сделать выгрузку" с указанием callback_data
    keyboard.add(InlineKeyboardButton(text='Сделать выгрузку', callback_data='admin_btn'))

    # Возвращение клавиатуры в виде объекта InlineKeyboardMarkup
    return keyboard.as_markup()
