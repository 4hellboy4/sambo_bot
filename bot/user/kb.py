from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

page_cnt: int = 0
photo_index: int = 0

pages = {
    0: {
        'buttons': [
            InlineKeyboardButton(text="Мастер классы", callback_data="page_20"),
            InlineKeyboardButton(text="Соревнования", callback_data="page_2"),
            InlineKeyboardButton(text="Программа форума", callback_data="page_3"),
            InlineKeyboardButton(text="Программа выставки", callback_data="page_4"),
            InlineKeyboardButton(text="Трансляция", callback_data="page_5"),
        ]
    },
    1: {
        'text': "Сообщение",
        'buttons': [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_20"),
        ]
    },
    2: {
        'text': "Соревнования",
        'file': './data/Competitions/image.jpeg',
        'buttons': [
            InlineKeyboardButton(text="Список соревнований", callback_data="page_6"),
            InlineKeyboardButton(text="Регламенты", callback_data="page_7"),
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_0"),
        ]
    },
    3: {
        'text': "Сообщение",
        'buttons': [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_0"),
        ]
    },
    4: {
        'text': "27.09.2024 с 10 до 19\n28.09.2024 с 10 до 19\n29.09.2024 с 10 до 17",
        'buttons': [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_0"),
        ]
    },
    5: {
        'text': "Сообщение",
        'buttons': [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_0"),
        ]
    },
    6: {
        'text': "Сообщение",
        'buttons': [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_2"),
        ]
    },
    7: {
        'text': "Регламенты",
        'buttons': [
            InlineKeyboardButton(text="Регламенты БЖЖ", callback_data="page_8"),
            InlineKeyboardButton(text="Регламент Киокушин турнир Соловьева", callback_data="page_9"),
            InlineKeyboardButton(text="Регламент Самбо (взр) Фестиваль Соловьева", callback_data="page_10"),
            InlineKeyboardButton(text="...", callback_data="page_11"),
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_2"),
        ]
    },
    8: {
        "file": "./data/Competitions/Sub_block/Регламент БЖЖ.pdf",
        'buttons': [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_7"),
        ]
    },
    9: {
        "file": "./data/Competitions/Sub_block/Регламент Киокушин турнир Соловьева.docx",
        'buttons': [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_7"),
        ]
    },
    10: {
        "file": "./data/Competitions/Sub_block/Регламент Самбо (взр) Фестиваль Соловьева.pdf",
        'buttons': [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_7"),
        ]
    },
    11: {
        'text': 'Регламенты',
        'buttons': [
            InlineKeyboardButton(text="Регламент вольная борьба.pdf", callback_data="page_12"),
            InlineKeyboardButton(text="Регламент греко-римская борьба.pdf", callback_data="page_13"),
            InlineKeyboardButton(text="Регламент грэпплинг.pdf", callback_data="page_14"),
            InlineKeyboardButton(text="Регламент джиу-джитсу.pdf", callback_data="page_15"),
            InlineKeyboardButton(text="Регламент дзюдо 2024 Турнир Соловьева.pdf", callback_data="page_16"),
            InlineKeyboardButton(text="Регламент Самбо (дети) Фестиваль Соловьева.pdf", callback_data="page_17"),
            InlineKeyboardButton(text="Регламент Соревнований 27 сентября 2024.pdf", callback_data="page_18"),
            InlineKeyboardButton(text="Соревнования по боксу в рамках Фестиваля единоборств им. В.А.Соловьева.pdf",
                                 callback_data="page_19"),
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_7"),
        ]
    },
    12: {
        'file': "./data/Competitions/Sub_block/Регламент вольная борьба.pdf",
        'buttons': [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_11"),
        ]
    },
    13: {
        'file': "./data/Competitions/Sub_block/Регламент греко-римская борьба.pdf",
        'buttons': [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_11"),
        ]
    },
    14: {
        'file': "./data/Competitions/Sub_block/Регламент грэпплинг.pdf",
        'buttons': [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_11"),
        ]
    },
    15: {
        'file': "./data/Competitions/Sub_block/Регламент джиу-джитсу.pdf",
        'buttons': [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_11"),
        ]
    },
    16: {
        'file': "./data/Competitions/Sub_block/Регламент дзюдо 2024 Турнир Соловьева.pdf",
        'buttons': [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_11"),
        ]
    },
    17: {
        'file': "./data/Competitions/Sub_block/Регламент Самбо (дети) Фестиваль Соловьева.pdf",
        'buttons': [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_11"),
        ]
    },
    18: {
        'file': "./data/Competitions/Sub_block/Регламент Соревнований 27 сентября 2024.pdf",
        'buttons': [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_11"),
        ]
    },
    19: {
        'file': "./data/Competitions/Sub_block/Соревнования по боксу в рамках Фестиваля единоборств им. В.А.Соловьева.pdf",
        'buttons': [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_11"),
        ]
    },
    20: {
        "file": "./data/images/Годынский.jpg",
        "text": "Годынский",
        "buttons": [
            [InlineKeyboardButton(text="➡️", callback_data='page_21')],
            InlineKeyboardButton(text="Список мастер классов", callback_data='page_1'),
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_0")
        ]
    },
    21: {
        "file": "./data/images/Горбачев.jpg",
        "text": "Горбачев",
        "buttons": [
            [InlineKeyboardButton(text="⬅️", callback_data='page_20'),
             InlineKeyboardButton(text="➡️", callback_data='page_22')],
            InlineKeyboardButton(text="Список мастер классов", callback_data='page_1'),
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_0")
        ]
    },
    22: {
        "file": "./data/images/Донцов.jpg",
        "text": "Донцов",
        "buttons": [
            [InlineKeyboardButton(text="⬅️", callback_data='page_21'),
             InlineKeyboardButton(text="➡️", callback_data='page_23')],
            InlineKeyboardButton(text="Список мастер классов", callback_data='page_1'),
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_0")
        ]
    },
    23: {
        "file": "./data/images/Магомедов.jpg",
        "text": "Магомедов",
        "buttons": [
            [InlineKeyboardButton(text="⬅️", callback_data='page_22'),
             InlineKeyboardButton(text="➡️", callback_data='page_24')],
            InlineKeyboardButton(text="Список мастер классов", callback_data='page_1'),
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_0")
        ]
    },
    24: {
        "file": "./data/images/Мухин А.jpg",
        "text": "Мухин А",
        "buttons": [
            [InlineKeyboardButton(text="⬅️", callback_data='page_23'),
             InlineKeyboardButton(text="➡️", callback_data='page_25')],
            InlineKeyboardButton(text="Список мастер классов", callback_data='page_1'),
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_0")
        ]
    },
    25: {
        "file": "./data/images/Осипов.jpeg",
        "text": "Осипов",
        "buttons": [
            [InlineKeyboardButton(text="⬅️", callback_data='page_24'),
             InlineKeyboardButton(text="➡️", callback_data='page_26')],
            InlineKeyboardButton(text="Список мастер классов", callback_data='page_1'),
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_0")
        ]
    },
    26: {
        "file": "./data/images/Прокопенко.jpg",
        "text": "Прокопенко",
        "buttons": [
            [InlineKeyboardButton(text="⬅️", callback_data='page_25'),
             InlineKeyboardButton(text="➡️", callback_data='page_27')],
            InlineKeyboardButton(text="Список мастер классов", callback_data='page_1'),
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_0")
        ]
    },
    27: {
        "file": "./data/images/Этезов.png",
        "text": "Этезов",
        "buttons": [
            [InlineKeyboardButton(text="⬅️", callback_data='page_26')],
            InlineKeyboardButton(text="Список мастер классов", callback_data='page_1'),
            InlineKeyboardButton(text="⬅️ Назад", callback_data="page_0")
        ]
    },
}

def get_keyboard_for_page(page: int = 0):
    keyboard = InlineKeyboardBuilder()

    buttons = pages[page]['buttons']
    if 20 <= page <= 27:
        keyboard.add(*buttons[0])
    for ind in range(1 if page >= 20 else 0, len(buttons)):
        keyboard.row(buttons[ind])

    return keyboard.as_markup()


def get_photos_keyboard():
    keyboard = InlineKeyboardBuilder()

    navigation_buttons = []
    if 0 < photo_index:
        navigation_buttons.append(InlineKeyboardButton(text="⬅️ Назад", callback_data=f'master_lomaster'))
    if photo_index < 7:
        navigation_buttons.append(InlineKeyboardButton(text="Вперед ➡️", callback_data=f'master_lomaster'))

    keyboard.add()
