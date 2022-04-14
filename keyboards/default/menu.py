from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Rose")
        ],
        [
            KeyboardButton(text="Lotus")
        ],
        [
            KeyboardButton(text="Jasmine")
        ]
    ],
    resize_keyboard=True
)