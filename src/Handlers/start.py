from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode

from src.Handlers.keyboards import start_kb

router = Router()

@router.message(F.text == "/start")
async def start(message: Message):
    await message.answer("🥪 <b>Welcome to our Bakehouse!</b>\n\n" \
                         "Our bakery — is a place for fresh pastries and delicious pies made with care. " \
                         "From golden crusts to rich fillings, we create flavors that feel warm, familiar, and truly homemade!\n\n" \
                         "What do you want specifically?", reply_markup=start_kb, parse_mode=ParseMode.HTML)