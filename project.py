from aiogram import Bot, Dispatcher
from aiogram.filters import Text, Command, or_f
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from random import randint

BOT_TOKEN: str = '6288842116:AAGPEaQ4pDE-3-MDuNjsRGL9zSa5XY7nwzw'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()
kb_builder1: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
kb_builder2: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ms_error = "Out of range"
kittens_stickers = ['CAACAgIAAxkBAAEJF61kbigthOn6NrOzEJRtIpxTg_Mg2AACoxgAArvwwEuKzMnbs96XFy8E',
                    'CAACAgIAAxkBAAEJF69kbigxXy0UJoQcyUIvDh2nHDpFfQACzRQAAj_oyEsAAdDBEYT0LHwvBA',
                    'CAACAgIAAxkBAAEJF7Fkbig4Ezs48cDCoHq_J5bf94fATAACixQAAtMncEjDbeKmKcIRGC8E',
                    'CAACAgIAAxkBAAEJF7Nkbig8yjylxic1JmQVj1r3S3IQYAACbRQAApLAcUiYAAFRicjxcvkvBA',
                    'CAACAgIAAxkBAAEJF7VkbihA6wlFWFLE34DVsRQ-rw_vOwACjhcAAgzYaUjbXjCV4aGCOy8E',
                    'CAACAgIAAxkBAAEJF9hkbiwhLR1fsIgJTDTLF0fH4_4MDwACWRcAAtSJ6UgInxcFXrXpEy8E',
                    'CAACAgIAAxkBAAEJF-BkbixMH3nafHGJqB57DRQyac8d_gAC_BcAAnq-yUugX_MausOeZS8E']
current = ''
c_c = ''
flag1 = False
flag2 = False
btn_i2s:KeyboardButton = KeyboardButton(text='Перевести число из десятичной системы счисления')
btn_s2i:KeyboardButton = KeyboardButton(text='Перевести число в десятичную систему счисления')
btn_help:KeyboardButton = KeyboardButton(text='Help')
btn_secret:KeyboardButton = KeyboardButton(text='Котики')
kb_builder1.row(btn_i2s, btn_s2i, btn_help,btn_secret, width=1)
keyboard1: ReplyKeyboardMarkup = kb_builder1.as_markup(
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
    global flag1
    flag1= True
    await message.answer('Введите число')
@dp.message(Text(text="Перевести число в десятичную систему счисления"))
async def process1_str2int(message: Message):
    global flag1,flag2
    flag1 = True
    flag2 = True
    await message.answer('Введите число')
@dp.message(lambda x: x.text and x.text.isdigit() and flag1)
async def process2_int2str(message: Message):
    global current,flag1,flag2
    current = message.text
    flag1 = False
    await message.answer("Введите систему счисления")
@dp.message(lambda x: x.text and x.text.isdigit())
async def process2_int2str(message: Message):
    global current,c_c,flag2
    c_c = message.text
    if(not flag2):
        await message.answer("Число " + current +" в " + c_c + " системе счисления равно " +
                             int2str(int(current),int(c_c)))
    else:
        await message.answer("Число " + current + " в " + c_c + " системе счисления равно " +
                             str(str2int(current, int(c_c))))

@dp.message(or_f(Command(commands=['help']),Text(text="Help")))
async def process_help_command(message: Message):
    await message.answer('Объясняю:\n\n'
                         'Команда "Перевести число из десятичной системы счисления" переводить десятичное число'
                         'в другую систему счисления.\nДля этого нужно ввести число и основание системы счисления'
                         ',в которую нужно перевести число.\n\n'
                         'Команда "Перевести число в десятичную систему счисления" переводит число из любой(не десятичной)'
                         'системы в десятичную.\nДля этого нужно ввести число и основание системы счисления введённого числа.\n\n')
@dp.message(Text(text="Котики"))
async def secret_def(message: Message):
        await bot.send_sticker(chat_id=message.from_user.id,
                               sticker=kittens_stickers[randint(0,6)])
@dp.message()
async def unknown_message_process(message: Message):
    await message.answer(f"Неизвестная команда",reply_markup=keyboard1)


if __name__ == '__main__':
    dp.run_polling(bot)