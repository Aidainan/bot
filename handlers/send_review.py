from config import bot,media_image
import sqlite3
from aiogram import Router, types
from aiogram.filters import Command
import os
import random
from aiogram.types import FSInputFile, CallbackQuery
from keyboards.start import start_markup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from database.a_db import AsyncDatabase
from database import queries
router = Router()

class Review(StatesGroup):
    name=State()
    text=State()

@router.callback_query(lambda call: call.data=='send_review')
async def send_review(call: CallbackQuery, state: FSMContext):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='write ur name',
    )
    await state.set_state(Review.name)

@router.message(Review.name)
async def name_process(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await bot.send_message(
        chat_id=message.from_user.id,
        text='write ur review',
    )
    await state.set_state(Review.text)

@router.message(Review.text)
async def text_process(message: types.Message, state: FSMContext,db=AsyncDatabase()):
    await state.update_data(text=message.text)
    await bot.send_message(
        chat_id=message.from_user.id,
        text='thank u for review',
    )

    data=await state.get_data()
    await db.execute_query(query=queries.INSERT_REVIEW,
                           params=(None,
                                   message.from_user.id,
                                   data['name'],
                                   data['text'],))
