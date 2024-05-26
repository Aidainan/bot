from config import bot,media_image
import sqlite3
from aiogram import Router, types
from aiogram.filters import Command
import os
import random
from aiogram.types import FSInputFile
from keyboards.menu import menu_markup
from database.a_db import AsyncDatabase
from database import queries
router = Router()

@router.callback_query(lambda call: call.data == 'menu')
async def menu_handler(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='here is menu',
        reply_markup=await menu_markup()
    )

@router.message(lambda m:m.text=='drinks')
async def drinks_handler(m:types.Message,db=AsyncDatabase()):
    datab=await db.execute_query(query=queries.SELECT_FOOD,
                          params=(m.text,),
                          fetch='all')
    print(datab)
    if datab:
        for i in datab:
            photo = FSInputFile(i['photo'])
            await bot.send_photo(
                chat_id=m.from_user.id,
                photo=photo,
                caption=f'name: {i["namee"]}\n'
                        f'price: {i["price"]}\n',
            )
    else:
        await bot.send_message(
            chat_id=m.from_user.id,
            text=f'no {m.text} yet'
        )

@router.message(lambda m:m.text=='food')
async def drinks_handler(m:types.Message,db=AsyncDatabase()):
    datab=await db.execute_query(query=queries.SELECT_FOOD,
                          params=(m.text,),
                          fetch='all')
    print(datab)
    if datab:
        for i in datab:
            photo = FSInputFile(i['photo'])
            await bot.send_photo(
                chat_id=m.from_user.id,
                photo=photo,
                caption=f'name: {i["namee"]}\n'
                        f'price: {i["price"]}\n',
            )
    else:
        await bot.send_message(
            chat_id=m.from_user.id,
            text=f'no {m.text} yet'
        )

@router.message(lambda m:m.text=='salad')
async def drinks_handler(m:types.Message,db=AsyncDatabase()):
    datab=await db.execute_query(query=queries.SELECT_FOOD,
                          params=(m.text,),
                          fetch='all')
    print(datab)
    if datab:
        for i in datab:
            photo = FSInputFile(i['photo'])
            await bot.send_photo(
                chat_id=m.from_user.id,
                photo=photo,
                caption=f'name: {i["namee"]}\n'
                        f'price: {i["price"]}\n',
            )
    else:
        await bot.send_message(
            chat_id=m.from_user.id,
            text=f'no {m.text} yet'
        )