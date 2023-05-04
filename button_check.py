from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = '6288842116:AAGPEaQ4pDE-3-MDuNjsRGL9zSa5XY7nwzw'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
buttons_1: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 1}') for i in range(6)]
buttons_2: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 7}') for i in range(5)]
buttons_3: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 13}') for i in range(4)]
buttons_4: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 19}') for i in range(3)]
buttons_5: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 25}') for i in range(2)]
buttons_6: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 31}') for i in range(1)]
kb_builder.row(*buttons_1, width=6)
kb_builder.row(*buttons_2, width=5)
kb_builder.row(*buttons_3, width=4)
kb_builder.row(*buttons_4, width=3)
kb_builder.row(*buttons_5, width=2)
kb_builder.row(*buttons_6, width=1)
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая получается клавиатура',
                         reply_markup=kb_builder.as_markup(
                                            resize_keyboard=True))
# button_1: KeyboardButton = KeyboardButton(text='Собак 🦮')
# button_2: KeyboardButton = KeyboardButton(text='Огурцов 🥒')
#
# # Создаем объект клавиатуры, добавляя в него кнопки
# keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
#                                     keyboard=[[button_1, button_2]],resize_keyboard=True)
#
#
# # Этот хэндлер будет срабатывать на команду "/start"
# # и отправлять в чат клавиатуру
# @dp.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(text='Чего кошки боятся больше?',
#                          reply_markup=keyboard)
#
#
# # Этот хэндлер будет срабатывать на ответ "Собак 🦮" и удалять клавиатуру
# @dp.message(Text(text='Собак 🦮'))
# async def process_dog_answer(message: Message):
#     await message.answer(text='Да, несомненно, кошки боятся собак. '
#                               'Но вы видели как они боятся огурцов?',
#                          reply_markup=ReplyKeyboardRemove())
#
#
# # Этот хэндлер будет срабатывать на ответ "Огурцов 🥒" и удалять клавиатуру
# @dp.message(Text(text='Огурцов 🥒'))
# async def process_cucumber_answer(message: Message):
#     await message.answer(text='Да, иногда кажется, что огурцов '
#                               'кошки боятся больше',
#                          reply_markup=ReplyKeyboardRemove())


if __name__ == '__main__':
    dp.run_polling(bot)