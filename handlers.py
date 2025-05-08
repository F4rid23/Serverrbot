from aiogram import Dispatcher, types

async def start_handler(message: types.Message):
    await message.reply("Добро пожаловать в ServerrBot! Здесь вы можете проходить обучение, зарабатывать баллы и тратить их на бонусы.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
