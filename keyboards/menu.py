from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
async def menu_markup():
    drinks=KeyboardButton(text='drinks')
    food=KeyboardButton(text='food')
    salad=KeyboardButton(text='salad')
    keyboard=ReplyKeyboardMarkup(
        keyboard=[[drinks, food, salad]]
    )
    return keyboard