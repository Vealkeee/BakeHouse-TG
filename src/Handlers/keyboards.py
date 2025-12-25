from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🥧 MENU", callback_data="menu"),
            InlineKeyboardButton(text="⚙️ INFO", callback_data="info")
        ],
        [
            InlineKeyboardButton(text="👤 My Account", callback_data="account")
        ]
    ]
)

info_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📖 About", callback_data="about")
        ],
        [
            InlineKeyboardButton(text="🗺️ Language", callback_data="lan")
        ]
    ]
)

info_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="❌ Previous", callback_data="info_back")
        ]
    ]
)

categories = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🥐 Savouries & Bakes", callback_data="food_menu")
        ],
        [
            InlineKeyboardButton(text="☕ Drinks & Snacks", callback_data="drinks_menu")
        ]
    ]
)

Food_category = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🥐 Bakes", callback_data="bakes"),
            InlineKeyboardButton(text="🥖 Pizza", callback_data="pizza")
        ],
        [
            InlineKeyboardButton(text="❌ Previous", callback_data="menu_back")
        ]
    ]
)

Drinks_category = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="☕ Drinks", callback_data="drink"),
            InlineKeyboardButton(text="🍫 Snacks", callback_data="Snacks")
        ],
        [
            InlineKeyboardButton(text="❌ Previous", callback_data="menu_back")
        ]
    ]
)