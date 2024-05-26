from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
from aiogram.fsm.storage.memory import MemoryStorage

load_dotenv()
storage = MemoryStorage()
token = os.getenv("TOKEN")
media_image=os.getenv("MEDIA_IMAGE")
bot = Bot(token=token)
dp=Dispatcher(storage=storage, bot=bot)