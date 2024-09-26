from aiogram import Router, types, F
from aiogram.filters.state import (StatesGroup, State)
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from bot import config
from bot.user.kb import get_keyboard_for_page, pages

from db.functions import *

# Создаем роутер для пользовательских команд
user = Router()

# Определение состояний для регистрации
class Registration(StatesGroup):
    fio = State()           # Состояние для ввода ФИО
    phone_number = State()  # Состояние для ввода номера телефона

# Обработчик команды "/start"
@user.message(Command(commands=['start']))
async def start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    # Проверка, существует ли пользователь в базе данных
    if not user_exists(user_id) and (user_id not in config.admins):
        await message.answer("Введите ваше ФИО:")  # Запрос ФИО у пользователя
        await state.set_state(Registration.fio.state)  # Установка состояния ввода ФИО
    else:
        await message.answer(f"Привет, {message.from_user.username}!", reply_markup=get_keyboard_for_page(0))

# Обработчик ввода ФИО
@user.message(Registration.fio)
async def process_fio(message: types.Message, state: FSMContext):
    await state.update_data(fio=message.text)  # Сохранение ФИО в состояние

    await message.answer("Теперь введите ваш номер телефона:")  # Запрос номера телефона
    await state.set_state(Registration.phone_number)  # Установка состояния ввода номера телефона

# Обработчик ввода номера телефона
@user.message(Registration.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    user_data = await state.get_data()  # Получение данных состояния
    fio = user_data.get("fio")  # Извлечение ФИО
    phone_number = message.text  # Получение номера телефона от пользователя

    add_user(message.from_user.id, fio, phone_number)  # Добавление пользователя в базу данных

    await state.clear()  # Очистка состояния

    await message.answer(f"Спасибо за регистрацию, {fio}!")  # Сообщение о завершении регистрации

    await message.answer(f"Привет, {message.from_user.username}!", reply_markup=get_keyboard_for_page(0))

# Обработчик нажатий на кнопки для переключения страниц
@user.callback_query(F.data.startswith('page_'))
async def go_page(callback_query: types.CallbackQuery):
    next_page = int(callback_query.data.split('_')[1])  # Получение номера следующей страницы
    await callback_query.message.delete()  # Удаление текущего сообщения

    # Обработка различных диапазонов страниц для отправки соответствующего контента
    if next_page == 2:
        data = FSInputFile(f'{pages[next_page]['file']}')  # Получение файла для страницы
        await callback_query.message.answer_photo(
            photo=data,
            reply_markup=get_keyboard_for_page(next_page)
        )
    elif 8 <= next_page <= 10 or 12 <= next_page <= 19:
        data = FSInputFile(f'{pages[next_page]['file']}')  # Получение документа
        await callback_query.message.answer_document(
            document=data,
            reply_markup=get_keyboard_for_page(next_page)
        )
    elif 20 <= next_page <= 27:
        data = FSInputFile(pages[next_page]['file'])  # Получение файла для фото
        text = pages[next_page]['text']  # Получение текста для подписи
        await callback_query.message.answer_photo(
            caption=text,
            photo=data,
            reply_markup=get_keyboard_for_page(next_page)
        )
    else:
        # Определение текста для ответа в зависимости от наличия текста на странице
        if 'text' in pages[next_page]:
            text = pages[next_page]['text']
        else:
            text = f'Привет, {callback_query.from_user.username}!'
        await callback_query.message.answer(
            text=text,
            reply_markup=get_keyboard_for_page(next_page)
        )
