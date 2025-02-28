from aiogram import executor
import logging
from handlers import fsm_store
from config import dp, bot, staff
from handlers import commands
import buttons

if __name__ == '__main__':
    commands.register_handlers(dp)
    fsm_store.register_handlers_store(dp)


    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)