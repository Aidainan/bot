from config import bot,media_image
import sqlite3
from aiogram import Router, types
from aiogram.filters import Command
import os
import random
from aiogram.types import FSInputFile
from keyboards.start import start_markup
router = Router()

@router.callback_query(lambda call: call.data == 'about_us')
async def about_us_handler(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='we dont have info',
    )