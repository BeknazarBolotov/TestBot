from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import buttons
from config import bot, staff


class BuyFSM(StatesGroup):
    product_id = State()
    size = State()
    quantity = State()
    contact = State()
    submit = State()


async def start_fsm_buy(message: types.Message):
    await BuyFSM.product_id.set()
    await message.answer('Артикул товара:')


async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await BuyFSM.next()
    await message.answer('Размер товара:')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await BuyFSM.next()
    await message.answer('Кол-во товара:')


async def load_quantity(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = message.text

    await BuyFSM.next()
    await message.answer('Оставьте свой номер телефона:')


async def load_contact(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact'] = message.text

    await BuyFSM.next()

    # Отправка данных пользователю
    await message.answer('Верные ли данные?', reply_markup=buttons.submit)
    await message.answer(
        f'Размер - {data["size"]}\n'
        f'ID продукта - {data["product_id"]}\n'
        f'Кол-во - {data["quantity"]}\n'
        f'Номер телефона - {data["contact"]}'
    )


async def submit_load(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        data = await state.get_data()
        caption = (
            f'Новая заявка!\n'
            f'Размер - {data["size"]}\n'
            f'ID продукта - {data["product_id"]}\n'
            f'Кол-во - {data["quantity"]}\n'
            f'Номер телефона - {data["contact"]}'
        )

        await message.answer("Ваши данные были отправлены сотрудникам! Ожидайте сообщения! ☺️")
        for admin in staff:
            await bot.send_message(chat_id=admin, text=caption)

    elif message.text.lower() == 'нет':
        await message.answer('Хорошо, отменено!')

    else:
        await message.answer('Выберите "да" или "нет"!')

    await state.finish()


def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(start_fsm_buy, commands="buy")
    dp.register_message_handler(load_product_id, state=BuyFSM.product_id)
    dp.register_message_handler(load_size, state=BuyFSM.size)
    dp.register_message_handler(load_quantity, state=BuyFSM.quantity)
    dp.register_message_handler(load_contact, state=BuyFSM.contact)
    dp.register_message_handler(submit_load, state=BuyFSM.submit)
