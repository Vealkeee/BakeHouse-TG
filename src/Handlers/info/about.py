from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.enums import ParseMode

from src.Handlers.keyboards import (
    info_kb, info_back
)

router = Router()

@router.callback_query(F.data == "info")
async def infoPanel(call: CallbackQuery):
    await call.message.answer("<b>⚙️ INFO</b>\n\n" \
                              "Choose following option:\n\n" \
                              "1. About - contact, bakery info.\n" \
                              "2. Language - change to preferable one.", reply_markup=info_kb, parse_mode=ParseMode.HTML)
    await call.answer()

@router.callback_query(F.data == "about")
async def aboutMe(call: CallbackQuery):
    await call.message.edit_text("Welcome to Golden Crumb Bakery, where every loaf, pastry, and cake is baked with heart. What started as a small passion for homemade treats has grown into a cozy neighborhood bakery dedicated to fresh ingredients, traditional recipes, and warm smiles.\n\n" \
                                "We believe the best flavors come from simplicity—real butter, quality flour, fresh eggs, and just the right amount of sweetness. From flaky croissants and artisan breads to custom cakes and seasonal desserts, everything is baked fresh daily in our kitchen.\n\n" \
                                "At Golden Crumb Bakery, we’re more than just a shop—we’re a place where mornings begin with the smell of warm bread and celebrations are made sweeter. Whether you’re stopping by for your daily treat or ordering something special, we’re always happy to serve you.\n\n" \

                                "📍 Address: 123 Sweet Street, Flourville, CA 90000\n" \
                                "📞 Phone: (555) 123-4567\n" \
                                "📧 Email: hello@goldencrumbbakery.fake\n" \
                                
                                "🕒 Hours: Mon–Sat: 7:00 AM – 6:00 PM | Sun: 8:00 AM – 2:00 PM", reply_markup=info_back)
    await call.answer()

@router.callback_query(F.data == "info_back")
async def backFunc(call: CallbackQuery):
    await call.message.edit_text("<b>⚙️ INFO</b>\n\n" \
                              "Choose following option:\n\n" \
                              "1. About - contact, bakery info.\n" \
                              "2. Language - change to preferable one.", reply_markup=info_kb, parse_mode=ParseMode.HTML)
    await call.answer()