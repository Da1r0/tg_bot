import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text
from aiogram.types import Message

from config import config

API_TOKEN = config.token
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer('Привет!\nЯ бот, которого создал человек из ВКИ НГУ.\nМеня зовут Vik, а тебя как зовут?')


@dp.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer('Меня зовут Vik, и у тебя возникли вопросы, как со мной общаться?\n'
                         'Тогда ты попал именно сюда:)\n'
                         'Потом я тебе расскажу, как можно со мной разговаривать и какие функции у меня ещё есть!')


@dp.message(Text(text='Кто меня создал?'))
async def easter_egg(message: Message):
    await message.answer('Имя моего автора Da1r0')


@dp.message()
async def echo(message: Message):
    await message.answer(message.text)


async def main():
    try:
        print('Bot started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
