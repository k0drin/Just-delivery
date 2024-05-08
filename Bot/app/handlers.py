from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
import requests

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


@router.callback_query(F.data.startswith("category:"))
async def item_list(callback: CallbackQuery):
    category_id = callback.data.split(":")[1]
    Items_data = requests.get(f"http://127.0.0.1:8000/api/v1/items/{category_id}/")
    items_resp = Items_data.json()
    filter = '\n'.join([f"{item['name']}: {item['price']}" for item in items_resp]) 
    print(filter,"\n",)
    await callback.message.answer(filter)
    
    
    

