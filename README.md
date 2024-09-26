# Telegram Bot

Этот проект представляет собой Telegram-бота, реализованного с использованием библиотеки Aiogram. Бот поддерживает регистрацию пользователей и взаимодействие с администратором.

## Установка

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. добавьте бот токен в файл `.env`
4. Настройте файл конфигурации `config.py`:
   - Укажите идентификаторы администраторов.
   - Добавьте токен бота.

## Структура проекта

```
/bot
    /admin
    /user
    /kb
    config.py
    main.py
/db
    functions.py
/requirements.txt
```

## Запуск

Запустите бота с помощью:
```bash
python -m venv venv
pip install -r requirements.txt
python main.py
```

## Команды

- `/start` — начать взаимодействие с ботом.
- Команды для администратора (доступные после аутентификации).