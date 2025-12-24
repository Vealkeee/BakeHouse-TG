from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🥧 MENU", callback_data="menu")
        ],
        [
            InlineKeyboardButton(text="⚙️ INFO", callback_data="info")
        ]
    ]
)