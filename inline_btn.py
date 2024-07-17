from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kebab_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("1", callback_data="btn_1"),
            InlineKeyboardButton("2", callback_data="btn_2"),
            InlineKeyboardButton("3", callback_data="btn_3"),
            InlineKeyboardButton("4", callback_data="btn_4")
        ]
    ]
)

# count_kebab = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton("<", "kam"),
#             InlineKeyboardButton(f"0", "count"),
#             InlineKeyboardButton(">", "kop")
#         ]
#     ],row_width=3
# )