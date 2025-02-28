from aiogram import types, Dispatcher
from config import bot
import buttons

async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Hello {message.from_user.first_name}!\n"
                                f"Твой Telegram ID - {message.from_user.id}\n", reply_markup=buttons.start)

async def bot_info(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Hello {message.from_user.first_name}!\n"
                                f"I am bot where you can explore products of our store.", reply_markup=buttons.start)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler,commands="start")
    dp.register_message_handler(bot_info,commands="info")