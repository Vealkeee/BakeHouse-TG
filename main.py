import os
import aiogram
import asyncio

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from rich.console import Console

from src.Handlers import start


load_dotenv()
console = Console()
TOKEN = os.getenv("TOKEN")

async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(
        start.router
    )

    console.print(f"[bold green]BOT ID: {bot.id}\n" \
                   f"BOT TOKEN: {TOKEN}[bold green]\n" \
                   "The bot is now ready to use!")
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())