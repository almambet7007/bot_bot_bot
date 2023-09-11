from config import bot
from aiogram import types, Dispatcher
from database.sql_commands import Database
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup






async def list_of_users(call: types.CallbackQuery):
    users = Database().sql_select_users()
    print(users)
    print(str(users))
    data = []
    for user in users:
        if not user["username"]:
            data.append("None Username")
        else:
            data.append(user["username"])

    data = "\n".join(data)
    await call.message.reply(data)

def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(list_of_users, lambda call: call.data == 'secret_button')
