from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

service = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Всё для квартиры"),
            KeyboardButton(text="Маникюр")
        ],
        [
            KeyboardButton(text="Репетитор"),
            KeyboardButton(text="Такси")
        ],
    ],
    resize_keyboard=True
)