
from config import dp
from aiogram import executor
from handlers import start, chat_actions,callback
from database import sql_commands
from castom_things import weather


start.register_handlers_start(dp=dp)
callback.register_callback_handlers(dp=dp)
chat_actions.register_handlers_chat_actions(dp=dp)

# weather.register_castom_weather(dp=dp)


async def on_startup(_):
    db = sql_commands.Database()
    db.create_database()
    print("Bot is ready to work:)")


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)


