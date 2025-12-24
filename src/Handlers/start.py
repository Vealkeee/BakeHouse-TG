from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(F.text == "/start")
async def start(message: Message):
    await message.answer('Welcome to our "Bake House"!')