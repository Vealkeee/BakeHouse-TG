from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums import ParseMode

from src.scrapper.scrap import get_assorti

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
    await call.message.edit_text('🥧 <b>Choose of "Savouries & Bakes"!</b>\n\n' \
                              "Choose one of the following cattegories!", parse_mode=ParseMode.HTML, reply_markup=Food_category)
    await call.answer()
    
@router.callback_query(F.data == "drinks_menu")
async def drink(call: CallbackQuery):
    await call.message.edit_text('🧋 <b>Choose of "Drinks & Snacks"</b>\n\n' \
                              "Choose one of the following cattegories!", parse_mode=ParseMode.HTML, reply_markup=Drinks_category)
    await call.answer()

@router.callback_query(F.data == "menu_back")
async def back_func(call: CallbackQuery):
    await call.message.edit_text("🥖 <b>Welcome to our Menu!</b>\n\n" \
                              "Choose one of the following cattegories!", reply_markup=categories, parse_mode=ParseMode.HTML)
    await call.answer()



@router.callback_query(F.data == "bakes")
async def bakes_assorty(call: CallbackQuery):
    bakes = InlineKeyboardBuilder()
    names = await get_assorti.get_bakes()

    for i in range(len(names)):
        bakes.add(InlineKeyboardButton(text=f"{names[i]}", callback_data=f"{names[i]}"))
    
    bakes.add(InlineKeyboardButton(text=f"❌ Previous", callback_data=f"menu_back"))
    bakes_kb = bakes.adjust(2).as_markup()

    await call.message.edit_text("🥧 <b>Bake's menu</b>\n\n" \
                                 "Choose the Bake which you prefer the most!", reply_markup=bakes_kb, parse_mode=ParseMode.HTML)
    await call.answer()

@router.callback_query(F.data == "pizza")
async def bakes_assorty(call: CallbackQuery):
    pizza = InlineKeyboardBuilder()
    names = await get_assorti.get_pizza()

    for i in range(len(names)):
        pizza.add(InlineKeyboardButton(text=f"{names[i]}", callback_data=f"{names[i]}"))
    
    pizza.add(InlineKeyboardButton(text=f"❌ Previous", callback_data=f"menu_back"))
    pizza_kb = pizza.adjust(2).as_markup()

    await call.message.edit_text("🥧 <b>Bake's menu</b>\n\n" \
                                 "Choose the Bake which you prefer the most!", reply_markup=pizza_kb, parse_mode=ParseMode.HTML)
    await call.answer()