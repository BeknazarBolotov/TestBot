from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

cancel_fsm = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('отмена'))


start = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
start_buttons = KeyboardButton('/start')



remove_keyboard = ReplyKeyboardRemove()

submit = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
yes = KeyboardButton('да')
no = KeyboardButton('нет')
submit.add(yes, no)

