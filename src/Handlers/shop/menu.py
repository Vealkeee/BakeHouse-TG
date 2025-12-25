from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.enums import ParseMode

from src.Handlers.keyboards import (
    categories,
    Food_category,
    Drinks_category
)

router = Router()

@router.callback_query(F.data == "menu")
async def categories_menu(call: CallbackQuery):
    await call.message.answer("🥖 <b>Welcome to our Menu!</b>\n\n" \
                              "Choose one of the following cattegories!", reply_markup=categories, parse_mode=ParseMode.HTML)
    await call.answer()
    
@router.callback_query(F.data == "food_menu")
async def food(call: CallbackQuery):
    await call.message.answer('🥧 <b>Choose of "Savouries & Bakes"!</b>\n\n' \
                              "Choose one of the following cattegories!", parse_mode=ParseMode.HTML, reply_markup=Food_category)
    await call.answer()
    
@router.callback_query(F.data == "drinks_menu")
async def drink(call: CallbackQuery):
    await call.message.answer('🧋 <b>Choose of "Drinks & Snacks"</b>\n\n' \
                              "Choose one of the following cattegories!", parse_mode=ParseMode.HTML, reply_markup=Drinks_category)
    await call.answer()