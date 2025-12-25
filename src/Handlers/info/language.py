from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.enums import ParseMode

router = Router()

@router.callback_query(F.data == "lan")
async def language(call: CallbackQuery):
    await call.message.answer("The function is currently in progress")
    await call.answer()