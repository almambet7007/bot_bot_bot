from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.sql_commands import Database

from config import bot
from config import admin



async def word_for_me(message: types.Message):
    markup = InlineKeyboardMarkup()
    secret_button = InlineKeyboardButton(
        "list of users",
        callback_data="secret_button"
    )
    markup.add(secret_button)
    if message.chat.id != -4007879516:
        await message.reply(f"{message.from_user.first_name} you my master, "
                            f"and i will root you",
                            reply_markup=markup)



async def echo_ban(message: types.Message):
    ban_words = [
        'dog',
        'cat',
        'bird'
    ]
    if message.chat.id == -1001634678741:
        for word in ban_words:
            if word in message.text.lower().replace(" ", ""):
                 await bot.delete_message(chat_id=message.chat.id,
                                          message_id=message.message_id)
                 await bot.send_message(message.chat.id,
                                       text=f"{message.from_user.username} use bad word")

async def ban(message: types.Message):
    ban_words = [
        'dog',
        'cat',
        'bird'
    ]
    if message.chat.id == -1001634678741:
        for word in ban_words:
            if word in message.text.lower().replace(" ", ""):
                if Database().sql_insert_ban_table(message.from_user.id,message.from_user.username,message.chat.id):
                    await bot.delete_message(chat_id=message.chat.id,
                                             message_id=message.message_id)
                    await message.reply(text=f" {message.from_user.username} use ban_words,"
                                             f"admin delete {message.from_user.username}")
                Database().sql_insert_ban_table(message.from_user.id,message.from_user.username, message.chat.id)
                await bot.ban_chat_member(message.chat.id,message.from_user.id)

                break

async def admin(message: types.Message):
    if message.chat.id == -1001634678741:
        admin_ans = await check_user_is_admin(message)
        print(admin_ans)
        if admin_ans and message.reply_to_message:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )
            await bot.delete_message(chat_id=message.chat.id,
                                     message_id=message.message_id)
answer = "yes"
check_user_is_admin = bot


def register_handlers_chat_actions(dp: Dispatcher):
    dp.register_message_handler(word_for_me, lambda word:  'onigiri' in word.text)
    dp.register_message_handler(ban)
    dp.register_message_handler(admin)
    dp.register_message_handler(echo_ban)