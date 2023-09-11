import sqlite3

import const
from config import bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ParseMode, PollAnswer
from database.sql_commands import Database
from keyboards import start_keyboard

async def start_button(message: types.Message):
    telegram_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    try:
        Database().sql_insert_user_query(telegram_id=telegram_id,
                                    username=username,
                                   first_name=first_name,
                                   last_name=last_name)
    except sqlite3.IntegrityError:
        pass
    await message.reply(text=f'Hi {message.from_user.username} ',
                        reply_markup=start_keyboard.start_markup)


async def help_button(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=const.HELP_TEXT)


quiz_id = None
async def quiz_1(message: types.Message):
    global quiz_id
    quiz_id = "quiz_1"
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "Next victory, you ready,go!!!",
        callback_data="button_call_23"
    )
    markup.add(button_call_1)
    quations = "Who invented mazeraty?"
    oprion = [
        "alma",
        "ars",
        "dava",
        "baha"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=quations,
        options=oprion,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        explanation=f"{message.from_user.first_name} ioyy bro it's only luky",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

async def quiz_2(call: types.CallbackQuery):
    global quiz_id
    quiz_id = "quiz_2"
    quations = "Who invented honda?"
    oprion = [
        "alma",
        "ars",
        "dava",
        "baha"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=quations,
        options=oprion,
        is_anonymous=False,
        type="quiz",
        correct_option_id=1,
        explanation=f"{call.message.from_user.first_name} ioyy bro it's only luky",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )

async def answer_poll(poll_answer : types.PollAnswer):
    Database().sql_insert_answer_query(id_user = poll_answer.user.id,
                                        username = poll_answer.user.username,
                                        first_name = poll_answer.user.first_name,
                                        quiz = quiz_id,
                                       quiz_option=poll_answer.option_ids[0])


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=["start"])
    dp.register_message_handler(help_button, commands=["help"])
    dp.register_message_handler(quiz_1,commands=["quiz"])
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_23")
    dp.register_poll_answer_handler(answer_poll)