from config import bot,media_image
import sqlite3
from aiogram import Router, types
from aiogram.filters import Command
import os
import random
from aiogram.types import FSInputFile
from keyboards.start import start_markup
router = Router()

@router.message(Command('start'))
async def start(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'hello {message.from_user.first_name}',
        reply_markup=await start_markup()
    )

@router.message(Command('myinfo'))
async def myinfo(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'ur id: {message.from_user.id}\n'
             f'ur first_name: {message.from_user.first_name}\n'
             f'ur user_name: {message.from_user.username}\n'
    )

@router.message(Command('random_pic'))
async def random_pic(message: types.Message):
    files=os.listdir(media_image)
    random1=random.choice(files)
    photo= FSInputFile(media_image+random1)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo,
    )