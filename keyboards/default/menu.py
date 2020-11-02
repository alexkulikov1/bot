from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Заказ услуги"),
        ],
        [
            KeyboardButton(text="Для проффесионалов"),
        ],
    ],
    resize_keyboard=True
)