# import requests
# import datetime
# from config import open_weather_token
# from config import dp
# from config import bot
# from aiogram import types
# from aiogram import Dispatcher
#
#
# @dp.message_handler(commands=["start_weather"])
# async def weather_start(message:types.Message):
#     await message.reply(text=f"{message.from_user.first_name} enter city  name:")
#
#
#     # while await message.reply( text=f"{message.from_user.first_name} enter city  name:") == 1:
#     #         if await message.reply( text=f"{message.from_user.first_name} enter city  name:") == 'stop_bot':
#     #              print("bay")
#     #              break
#
#
# @dp.message_handler()
# async def get_weather(message: types.Message):
#     while await message.reply(text=f"{message.from_user.first_name} enter city  name:") != 1:
#         if await message.reply(text=f"{message.from_user.first_name} enter city  name:") == 'stop_bot':
#             print("bay")
#             break
#
#         code_to_smile = {
#                 "Clear": "Ясно \U0001F31E",
#                 "Clouds": "Облачно \U00002601",
#                 "Rain": "Дождь \U00002614",
#                 "Drizzle": "Дождь \U00002614",
#                 "Thunderstorm": "Гроза \U000026A1",
#                 "Show": "Снег \U0001F328",
#                 "Mist": "Туман \U0001F32B",
#             }
#
#         try:
#             r = requests.get(
#                 f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
#             )
#             data = r.json()
#
#
#             city = data['name']
#             cur_weather = data['main']['temp']
#
#             weather_description = data["weather"][0]["main"]
#             if weather_description in code_to_smile:
#                 wd = code_to_smile[weather_description]
#             else:
#                 wd = "Посмотри что там за окном ,я не знаю какая дичь там происходит"
#
#             cur_weather_max = data['main']['temp_max']
#             cur_weather_min = data['main']['temp_min']
#             wind = data['wind']['speed']
#             sunrise_timestamp =datetime.datetime.fromtimestamp(data['sys']['sunrise'])
#             sunset_timestamp =datetime.datetime.fromtimestamp(data['sys']['sunset'])
#             humidity = data['main']['humidity']
#             length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
#                 data['sys']['sunrise'])
#             await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}*** \n"
#                   f"Погода в городе: {city}\n Температура: {cur_weather}°C {wd}\n"
#                   f" Максимальная температура: {cur_weather_max}°C\n"
#                   f" Минимальная температура :{cur_weather_min}°C\n Влажность: {humidity}%\n"
#                   f" Скорость ветра: {wind}m/c\n Рассвет: {sunrise_timestamp}\n Закат: {sunset_timestamp}\n"
#                   f"Продолжительность дня:{length_of_the_day}\n"
#                   f'хорошего дня :)')
#
#
#         except:
#             # if bot.send_message(message.chat.id, text='\U00002621 prover nazvanie goroda \U00002620'):
#             #     while  await message.reply('\U00002621 prover nazvanie goroda \U00002620') == 'stop_bot':
#                     await message.reply('\U00002621 prover nazvanie goroda \U00002620')
#                     # break
#             # while True:
#                 # await message.reply('\U00002621 prover nazvanie goroda \U00002620')
#                 # if message == "('\U00002621 prover nazvanie goroda \U00002620')":
#                 #     break
#                 # await message.reply('\U00002621 prover nazvanie goroda \U00002620')
#
#
#
# def register_castom_weather(dp: Dispatcher):
#         dp.register_message_handler(weather_start, commands=["start_weather"])