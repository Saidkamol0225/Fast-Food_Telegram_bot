from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Share Contact", request_contact=True)
        ]
    ], resize_keyboard=True
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Order"),
            KeyboardButton("Button")
        ],
        [
            KeyboardButton("Button"),
            KeyboardButton("Button")
        ]
    ], resize_keyboard=True
)