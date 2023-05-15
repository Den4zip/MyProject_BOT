from aiogram import Bot, Dispatcher
from aiogram.filters import Text, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
BOT_TOKEN: str = '6288842116:AAGPEaQ4pDE-3-MDuNjsRGL9zSa5XY7nwzw'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()
kb_builder1: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
kb_builder2: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ms_error = "Out of range"
btn_i2s:KeyboardButton = KeyboardButton(text='Перевести число из десятичной системы счисления')
btn_s2i:KeyboardButton = KeyboardButton(text='Перевести число в десятичную систему счисления')
btn_help:KeyboardButton = KeyboardButton(text='Help')
btn2:KeyboardButton = KeyboardButton(text='Двоичная')
btn8:KeyboardButton = KeyboardButton(text='Восьмиричная')
btn16:KeyboardButton = KeyboardButton(text='Десятиричная')
kb_builder1.row(btn_i2s, btn_s2i, btn_help, width=1)
keyboard1: ReplyKeyboardMarkup = kb_builder1.as_markup(
                                    resize_keyboard=True)
kb_builder2.row(btn2,btn8,btn16,width=1)
keyboard2: ReplyKeyboardMarkup = kb_builder2.as_markup(
                                    resize_keyboard=True)
def int2str(n, radix):
    if not (n >= 0):
        return ms_error
    if not (2 <= radix <= len(DIGITS)):
        return ms_error
    s = ''
    while n != 0:
        s += DIGITS[n % radix]
        n //= radix
    return s[::-1]
def str2int(s, radix):
    if not (2 <= radix <= len(DIGITS)):
        return ms_error
    n = 0
    for c in s.upper():
        n *= radix
        d = DIGITS.find(c)  # TODO: not optimal search
        if d == -1 or d >= radix:
            return ms_error
        n += d
    return n
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nЭто бот калькулятор систем счисления.Он может переводить '
                         'из одной системы счисления в другую\n\n'
                         'Чтобы получить список доступных '
                         'команд - отправьте команду /help',reply_markup=keyboard1)
@dp.message(Text(text="Перевести число из десятичной системы счисления"))
async def process1_int2str(message: Message):
    await message.answer('Введите число')
@dp.message(lambda x: x.text and x.text.isdigit())
async def process2_int2str(message: Message):
    current = message.text
    await message.answer("Введите систему счисления",reply_markup=keyboard2)
@dp.message(Text(text="Двоичная"))
async def process3_int2str(message: Message):
    c_с = "2"
    await message.answer("Число" +current +"в" +c_c+ "системе счисления равно "+int2str(int(current), c_c))
@dp.message(Text(text="Восьмиричная"))
async def process3_int2str(message: Message):
    c_с = "8"
    await message.answer("Число" +current +"в" +c_c+ "системе счисления равно "+int2str(int(current), c_c))
@dp.message(Text(text="Шестнадцатиричная"))
async def process3_int2str(message: Message):
    c_с = "16"
    await message.answer("Число" +current +"в" +c_c+ "системе счисления равно "+int2str(int(current), c_c))


@dp.message(Text(text="Перевести число в десятичную систему счисления"))
async def process1_str2int(message: Message):
    await message.answer('Введите число')
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f"")

if __name__ == '__main__':
    dp.run_polling(bot)