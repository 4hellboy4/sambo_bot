import sqlite3

# Функция для инициализации базы данных и создания таблицы пользователей
def init_db():
    # Подключение к базе данных (или создание новой, если она не существует)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Создание таблицы пользователей, если она еще не существует
    cursor.execute('''
     CREATE TABLE IF NOT EXISTS users (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         user_id INTEGER UNIQUE,
         fio TEXT,
         phone_number TEXT
     )
     ''')

    # Сохранение изменений в базе данных
    conn.commit()
    # Закрытие соединения с базой данных
    conn.close()


# Функция для проверки существования пользователя по его идентификатору
def user_exists(user_id):
    # Подключение к базе данных
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Выполнение запроса на выборку, чтобы проверить, существует ли пользователь
    cursor.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()  # Получение результата запроса

    # Закрытие соединения с базой данных
    conn.close()

    # Возвращение True, если пользователь существует, иначе False
    return user is not None


# Функция для добавления нового пользователя в базу данных
def add_user(user_id, fio, phone_number):
    # Подключение к базе данных
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Выполнение запроса на добавление нового пользователя
    cursor.execute("INSERT INTO users (user_id, fio, phone_number) VALUES (?, ?, ?)", (user_id, fio, phone_number))

    # Сохранение изменений в базе данных
    conn.commit()
    # Закрытие соединения с базой данных
    conn.close()
