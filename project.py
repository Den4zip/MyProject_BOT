from aiogram import Bot, Dispatcher
from aiogram import Bot, Dispatcher,types, utils
from aiogram.filters import Text, Command
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove,KeyboardButtonPollType)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.methods.send_location import SendLocation
import requests
# lat = 0
# long = 0
# api_url_weather = 'https://api.open-meteo.com/v1/forecast?latitude='+str(lat)+'&longitude='+str(long)+'&hourly=temperature_2m,relativehumidity_2m'
BOT_TOKEN: str = '6288842116:AAGPEaQ4pDE-3-MDuNjsRGL9zSa5XY7nwzw'
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
geo_btn: KeyboardButton = KeyboardButton(
                                text='Отправить геолокацию',
                                request_location=True)
kb_builder.row(geo_btn,width=1)
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
                                    resize_keyboard=True)
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    print(message)
    await message.answer(text='1',reply_markup=keyboard)
@dp.message()
async def d1(message:Message):
    print(message)
    print("Success")
    await message.answer('Ку-ку')
# @dp.message(content_types=['location'])
# async def handle_location(message: types.Message):
#     lat = message.location.latitude
#     lon = message.location.longitude
#     reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
#     await message.answer(reply, reply_markup=types.ReplyKeyboardRemove())
if __name__ == '__main__':
    dp.run_polling(bot)