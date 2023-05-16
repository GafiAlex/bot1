import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ChatMemberAdministrator
from aiogram.dispatcher.filters import Command

API_TOKEN = '6082537301:AAEIO5hwbVnjH8lLqN1bfNoS1cWwo-0zkhg'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN,parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands=["generate"])
async def generate(message: types.Message, command):
    import random
    n = random.randint(0, 2)
    promo = ["16341763T", "65245345", "53415673"]
    print(promo[n])
    await message.answer(promo[n])

@dp.message_handler(commands=["promo"])
async def promo(message: types.Message, command):
    if command.args=="16341763T":
      await bot.promote_chat_member(message.chat.id, message.from_user.id, can_pin_messages=True)
      await bot.set_chat_administrator_custom_title(message.chat.id, message.from_user.id, command.args)
      await message.answer(f"Привет, <b>{message.from_user.full_name}</b>")
    elif command.args=="65245345":
        await message.answer(f"Добрый день, <b>{message.from_user.full_name}/b>")
    elif command.args == "53415673":
        await message.answer(f"Добрый день, <b>{message.from_user.full_name}</b>")
    else:
            await  message.answer("Неверный Промокод")

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ существую для того, чтобы ты изучал Python!\nКак тебя зовут?")

@dp.message_handler(regexp='(^Привет)')
async def cats(message: types.Message):
    with open('hi.jpg', 'rb') as photo:

        await message.reply_photo(photo, caption='Привет.')

@dp.message_handler(regexp='(^Пон)')
async def cats(message: types.Message):
    with open('razmer2-7.jpg', 'rb') as photo:

        await message.reply_photo(photo, caption='Ааааа Omg.')

@dp.message_handler(regexp='(^Важный)')
async def cats(message: types.Message):
    with open('1604310902.jpg', 'rb') as photo:

        await message.reply_photo(photo, caption='Капец Важный.')

@dp.message_handler(regexp='(^Кот)')
async def cats(message: types.Message):
    with open('181729708.jpg', 'rb') as photo:

        await message.reply_photo(photo, caption='Кот с тапком.')

@dp.message_handler(regexp='(^Apple)')
async def cats(message: types.Message):
    with open('020cccc6dfea6b56186878e1c0s1--dlya-doma-i-interera-podstavka-pod-telefon-smeshnye-kotiki.jpg', 'rb') as photo:

        await message.reply_photo(photo, caption='Продукция Эпл ).')

@dp.message_handler(regexp='(^Непон)')
async def cats(message: types.Message):
    with open('maxresdefault.jpg', 'rb') as photo:

        await message.reply_photo(photo, caption='Что непон >:( ).')

@dp.message_handler(regexp='(^Саша)')
async def cats(message: types.Message):
    with open('647198-1.jpg', 'rb') as photo:

        await message.reply_photo(photo, caption=':).')

@dp.message_handler(regexp='(^Можно мне ещё поиграть в компьютер)')
async def Da(message: types.Message):
    await message.reply("Да.")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Очень приятно, "+message.text)

    await message.reply("Хочешь увидеть смешные картинки? А я все равно покажу.")

    await asyncio.sleep(2)

    await types.ChatActions.upload_photo('')

    media = types.MediaGroup()

    media.attach_photo(types.InputFile('гг.jpg'), 'Картинка!')

    media.attach_photo(types.InputFile('AuVu5BW_bQE.jpg'), 'Больше картинок!')

    media.attach_photo(types.InputFile('LJWhSeZnLo4.jpg'), 'Мем.')

    await message.reply_media_group(media=media)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
