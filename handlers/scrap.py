from config import bot,media_image
import sqlite3
from aiogram import Router, types
from aiogram.filters import Command
import os
import random
from aiogram.types import FSInputFile, CallbackQuery
from keyboards.menu import menu_markup
from database.a_db import AsyncDatabase
from database import queries
from scraper.scrap import SerialScraper
from scraper.async_scrap import AsyncSerialScraper
router = Router()

# @router.callback_query(lambda call:call.data=='serial')
# async def english_handler(call: CallbackQuery,data=SerialScrapper()):
#     links=data.scrape_data()
#     await bot.send_message(
#         chat_id=call.from_user.id,
#         text=links,
#     )

@router.callback_query(lambda call:call.data=='serial')
async def english_handler(call: CallbackQuery,data=AsyncSerialScraper()):
    links=await data.scrape_data()
    await bot.send_message(
        chat_id=call.from_user.id,
        text=links,
    )
