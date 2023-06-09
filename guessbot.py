import random

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command, or_f
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN: str = '6288842116:AAGPEaQ4pDE-3-MDuNjsRGL9zSa5XY7nwzw'


# Создаем объекты бота и диспетчера
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()
button_1: KeyboardButton = KeyboardButton(text='Давай')
button_2: KeyboardButton = KeyboardButton(text='Нет')
button_3: KeyboardButton = KeyboardButton(text='stat')
button_4: KeyboardButton = KeyboardButton(text='cancel')
button_5: KeyboardButton = KeyboardButton(text='назад')

keyboard1: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2,button_3]],resize_keyboard=True)
keyboard2: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_4]],resize_keyboard=True)
keyboard3: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2]],resize_keyboard=True)
keyboard4:ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_5]],resize_keyboard=True)
# Количество попыток, доступных пользователю в игре
ATTEMPTS: int = 10

# Словарь, в котором будут храниться данные пользователя
user: dict = {'in_game': False,
              'secret_number': None,
              'attempts': None,
              'total_games': 0,
              'wins': 0}


# Функция возвращающая случайное целое число от 1 до 100
def get_random_number() -> int:
    return random.randint(1, 100)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(or_f(Command(commands=['start']),Text(text='назад')))
async def process_start_command(message: Message):
    await message.answer(text='Привет!\nДавай сыграем в игру "Угадай число"?\n\n'
                         'Чтобы получить правила игры и список доступных '
                         'команд - отправьте команду /help',reply_markup=keyboard1)


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
                         f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
                         f'попыток\n\nДоступные команды:\n/help - правила '
                         f'игры и список команд\n/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\nДавай сыграем?',reply_markup=keyboard1)


# Этот хэндлер будет срабатывать на команду "/stat"
@dp.message(Text(text='stat'))
async def process_stat_command(message: Message):
    await message.answer(f'Всего игр сыграно: {user["total_games"]}\n'
                         f'Игр выиграно: {user["wins"]}',reply_markup=keyboard4)


# Этот хэндлер будет срабатывать на команду "/cancel"
@dp.message(Text(text='cancel'))
async def process_cancel_command(message: Message):
    if user['in_game']:
        await message.answer('Вы вышли из игры. Если захотите сыграть '
                             'снова - напишите об этом',reply_markup=ReplyKeyboardRemove())
        user['in_game'] = False
    else:
        await message.answer('А мы итак с вами не играем. '
                             'Может, сыграем разок?',reply_markup=keyboard3)


# Этот хэндлер будет срабатывать на согласие пользователя сыграть в игру
@dp.message(Text(text=['Да', 'Давай', 'Сыграем', 'Игра',
                       'Играть', 'Хочу играть'], ignore_case=True))
async def process_positive_answer(message: Message):
    if not user['in_game']:
        await message.answer('Ура!\n\nЯ загадал число от 1 до 100, '
                             'попробуй угадать!',reply_markup=keyboard2)
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = ATTEMPTS
    else:
        await message.answer('Пока мы играем в игру я могу '
                             'реагировать только на числа от 1 до 100 '
                             'и команды /cancel и /stat')


# Этот хэндлер будет срабатывать на отказ пользователя сыграть в игру
@dp.message(Text(text=['Нет', 'Не', 'Не хочу', 'Не буду'], ignore_case=True))
async def process_negative_answer(message: Message):
    if not user['in_game']:
        await message.answer('Жаль :(\n\nЕсли захотите поиграть - просто '
                             'напишите об этом',reply_markup=keyboard1)
    else:
        await message.answer('Мы же сейчас с вами играем. Присылайте, '
                             'пожалуйста, числа от 1 до 100')


# Этот хэндлер будет срабатывать на отправку пользователем чисел от 1 до 100
@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_numbers_answer(message: Message):
    if user['in_game']:
        if int(message.text) == user['secret_number']:
            await message.answer('Ура!!! Вы угадали число!\n\n'
                                 'Может, сыграем еще?',reply_markup=keyboard3)
            user['in_game'] = False
            user['total_games'] += 1
            user['wins'] += 1
        elif int(message.text) > user['secret_number']:
            await message.answer('Мое число меньше')
            user['attempts'] -= 1
        elif int(message.text) < user['secret_number']:
            await message.answer('Мое число больше')
            user['attempts'] -= 1

        if user['attempts'] == 0:
            await message.answer(f'К сожалению, у вас больше не осталось '
                                 f'попыток. Вы проиграли :(\n\nМое число '
                                 f'было {user["secret_number"]}\n\nДавайте '
                                 f'сыграем еще?',reply_markup=keyboard3)
            user['in_game'] = False
            user['total_games'] += 1
    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')


# Этот хэндлер будет срабатывать на остальные любые сообщения
@dp.message()
async def process_other_text_answers(message: Message):
    if user['in_game']:
        await message.answer('Мы же сейчас с вами играем. '
                             'Присылайте, пожалуйста, числа от 1 до 100')
    else:
        await message.answer('Я довольно ограниченный бот, давайте '
                             'просто сыграем в игру?')

if __name__ == '__main__':
    dp.run_polling(bot)