from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
import requests

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Вітаю👋<b> {message.from_user.full_name}</b>. Це бот для доставки від компанії Just-Delivery🚀",
        parse_mode=ParseMode.HTML, reply_markup=kb.main_keyboard
    )           

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Тут повинен бути типу readme")


@router.message(F.text=='Категорії товарів')
async def cat(message: Message):
        await message.answer(f"Список категорій:", reply_markup=kb.category_keyboard)      



















