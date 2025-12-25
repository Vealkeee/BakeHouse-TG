__all__ = ("router")

from aiogram import Router

from src.Handlers import start
from src.Handlers.info import about, language
from src.Handlers.shop import menu

router = Router()

router.include_routers(
    start.router,
    about.router,
    language.router,
    menu.router
)