from aiogram import executor
import logging
from config import dp, bot, staff
from handlers import commands, send_products, fsm_store,fsm_buy
from db import main_db
import buttons

async def on_startup(_):
    for admin in staff:
        await bot.send_message(chat_id=admin, text='Бот включен!', reply_markup=buttons.start)
        await main_db.create_tables()

async def on_shutdown(_):
    for admin in staff:
        await bot.send_message(chat_id=admin, text='Бот выключен!')


if __name__ == '__main__':
    commands.register_handlers(dp)
    fsm_store.register_handlers_store(dp)
    send_products.register_handlers(dp)
    fsm_buy.register_handlers_fsm(dp)


    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)