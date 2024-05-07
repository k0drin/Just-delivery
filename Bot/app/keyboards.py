import requests
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


response = requests.get("http://127.0.0.1:8000/api/v1/category/")
categories = response.json()
  

main_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Категорії товарів', callback_data='product_categories')],
                                              [KeyboardButton(text='Мої закази', callback_data='my_orders')]],
                                    resize_keyboard=True,
                                    input_field_placeholder='Оберіть товар')


category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=f"{index + 1}. {category['title']}", callback_data="product_categories")] 
        for index, category in enumerate(categories)
    ]
)
                                                      






