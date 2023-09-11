from decouple import config
from aiogram import Bot,Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

open_weather_token = "6811bfe704879690e4b3684e9012c5d7"

admin = (1036061654,
         2110846780)

storage = MemoryStorage()
TOKEN= config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
