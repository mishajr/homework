from aiogram.filters import CommandStart,Command
from aiogram import types, Router

user_private = Router()

@user_private.message(CommandStart())

async def start_cmd(message: types.Message):
    await message.answer('Hello! I am a your personal bot☺ !')

@user_private.message(Command('menu'))


async def menu_cmd(message: types.Message):
    await message.answer('menu:\n 1. /menu - menu\n 2. /help - help\n 3. /echo - echo')


@user_private.message(Command('help'))
    
async def help_cmd(message: types.Message):
    await message.answer('Цей телеграм БОТ був створений 07.02.2024 Михайлом Віталієвичем\n Телеграм БОТ бут написаний на мові програмування Python\n Для створення телеграм БОТа була використана бібліотека aiogram\n Для зберігання конфіденційної інформації була використана бібліотека python-dotenv\n Для зберігання конфіденційної інформації була використана бібліотека python-dotenv\n Для зберігання конфіденційної інформації була використана бібліотека python-dotenv\n Для зберігання конфіденційної інформації була використана бібліотека python-dotenv\n Для зберігання конфіденційної інформації була використана бібліотека python-dotenv\n Для зберігання конфіденційної інформації була використана бібліотека python-dotenv\n Для зберігання конфіденційної інформації була використана бібліотека python-dotenv\n Для зберігання конфіденційної інформації була використана бібліотека python-dotenv\n Для зберігання конфіденційної інформації була використана бібліотека python-dotenv\n Для зберігання конфід')


@user_private.message(Command('echo'))

async def echo(message: types.Message):
    await message.answer(message.text)



@user_private.message()
async def voice(message: types.Message):
    text = message.text.lower()
    if text in ['hello', 'hi']:
        await message.answer('Hello! I am a your personal bot☺ !')
    elif text in ['bye', 'goodbye']:
        await message.answer('Goodbye! Have a nice day!')
    else:
        await message.answer("я тебе не зрозумів")
    # await message.answer(message.text)
    # await message.reply(message.text)


    
    