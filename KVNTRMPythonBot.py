import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6082537301:AAEIO5hwbVnjH8lLqN1bfNoS1cWwo-0zkhg'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ существую для того, чтобы ты изучал Python!\nКак тебя зовут?")

@dp.message_handler(regexp='(^Привет)')
async def cats(message: types.Message):
    with open('hi.jpg', 'rb') as photo:

        await message.reply_photo(photo, caption='Привет.')

@dp.message_handler(regexp='(^Лев)')
async def cats(message: types.Message):
    with open('1573511281_0_299_2048_1451_1920x0_80_0_0_339e3316d7ec8095ca3a49d76f9e063c.jpg', 'rb') as photo:

        await message.reply_photo(photo, caption='Думаю ты понял ).')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Очень приятно, "+message.text)

    await message.reply("Хочешь увидеть смешные картинки? А я все равно покажу.")

    await asyncio.sleep(2)

    await types.ChatActions.upload_photo()

    media = types.MediaGroup()

    media.attach_photo(types.InputFile('гг.jpg'), 'Картинка!')

    media.attach_photo(types.InputFile('pic2.jpg'), 'Больше картинок!')

    media.attach_photo(types.InputFile('pic3.jpg'), 'Мем.')

    await message.reply_media_group(media=media)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

