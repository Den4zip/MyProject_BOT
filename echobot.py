from aiogram import Bot, Dispatcher
from aiogram.filters import Command, or_f
from aiogram.types import Message
from aiogram import F
from aiogram.filters import Text


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = '6288842116:AAGPEaQ4pDE-3-MDuNjsRGL9zSa5XY7nwzw'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')
@dp.message(F.audio)
async def send_audio_echo(message: Message):
    await message.reply_audio(message.audio.file_id)
    await message.answer_audio(message.audio.file_id)
@dp.message(F.animation)
async def send_animation_echo(message: Message):
    await message.reply_animation(message.animation.file_id)
    await message.answer_animation(message.animation.file_id)
@dp.message(F.document)
async def send_document_echo(message: Message):
    await message.reply_document(message.document.file_id)
    await message.answer_document(message.document.file_id)
@dp.message(F.voice)
async def send_voice_echo(message: Message):
    await message.reply_voice(message.voice.file_id)
    await message.answer_voice(message.voice.file_id)
@dp.message(F.video)
async def send_video_echo(message: Message):
    await message.reply_video(message.video.file_id)
    await message.answer_video(message.video.file_id)
@dp.message(F.sticker)
async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)
    await message.answer_sticker(message.sticker.file_id)

@dp.message(F.photo)
async def send_photo_echo(message: Message):
     await message.reply_photo(message.photo[0].file_id)
     await message.answer_photo(message.photo[0].file_id)
@dp.message(Text(contains = ['молоко'],ignore_case = True))
@dp.message(Text(contains = ['кефир'],ignore_case = True))
@dp.message(Text(contains = ['йогурт'],ignore_case = True))
async def send_echo_answer(message: Message):
    await message.answer(text='Это очень полезные продукты!')
# @dp.message()
# async def send_echo(message: Message):
#     await message.reply(text=message.text)
#     await message.answer(text=message.text)
if __name__ == '__main__':
    dp.run_polling(bot)