from main import bot, dp

from aiogram.types import Message
from config import admin_id

#сообщение при запуске бота
async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='Бот запущен. Приятного пользования')
# сообщение при выключении бота
async def send_to_admin_shutdown(dp):
    await bot.send_message(chat_id=admin_id, text='Бот упал:(')

@dp.message_handler()
async def echo(message: Message):
    text = f"Привет, {message.text}"
    await bot.send_message(chat_id=message.from_user.id, text=text)