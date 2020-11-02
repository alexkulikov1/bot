from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

flat = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Сантехник"),
            KeyboardButton(text="Приёмка квартиры")
        ],
    ],
    resize_keyboard=True
)