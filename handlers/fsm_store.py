
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from db import main_db
import buttons
from config import staff

class StoreFSM(StatesGroup):
    name_product = State()
    category = State()
    size = State()
    price = State()
    product_id = State()
    photo = State()
    submit = State()


async def start_fsm_store(message: types.Message):
    if message.from_user.id not in staff:
        await message.answer('У вас недостаточно прав для выполнения этого действия!⛔')
        return
    await message.answer('Введите название товара:', reply_markup=buttons.cancel_fsm)
    await StoreFSM.name_product.set()

async def name_load (message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_product'] = message.text

    await StoreFSM.next()
    await message.answer('Введите категорию:')


async def category_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category_product'] = message.text


    await StoreFSM.next()
    await message.answer('Введите размер:')


async def size_load (message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size_product'] = message.text

    await StoreFSM.next()
    await message.answer('Введите цену товара:')

async def price_load (message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price_product'] = message.text

    await StoreFSM.next()
    await message.answer('Введите артикул для товара: ')

async def product_id_load (message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await StoreFSM.next()
    await message.answer("Отправьте фото товара:")

async def photo_load (message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id


    await StoreFSM.next()
    await message.answer('Верные ли данные ?', reply_markup=buttons.submit)
    await message.answer_photo(photo=data['photo'],
                                   caption=f'Название товара - {data["name_product"]}\n'
                                           f'Категория - {data["category_product"]}\n'
                                           f'Размер товара - {data["size_product"]}\n'
                                           f'Цена - {data["price_product"]}\n'
                                           f'Артикул - {data["product_id"]}\n')


async def submit_load (message: types.Message, state: FSMContext):
    if message.text == 'да':
        async with state.proxy() as data:
            await main_db.sql_insert_products(
                name_product=data['name_product'],
                category=data['category_product'],
                size=data['size_product'],
                price=data['price_product'],
                product_id=data['product_id'],
                photo=data['photo']
            )

        await message.answer('Ваши данные в базе!', reply_markup=buttons.remove_keyboard)
        await state.finish()

    elif message.text == 'нет':
        await message.answer('Хорошо, отменено!', reply_markup=buttons.remove_keyboard)
        await state.finish()

    else:
        await message.answer('Выберите да или нет')


def register_handlers_store(dp: Dispatcher):
    dp.register_message_handler(start_fsm_store, commands=['store'])
    dp.register_message_handler(name_load, state=StoreFSM.name_product)
    dp.register_message_handler(size_load, state=StoreFSM.size)
    dp.register_message_handler(price_load, state=StoreFSM.price)
    dp.register_message_handler(category_load, state=StoreFSM.category)
    dp.register_message_handler(product_id_load, state=StoreFSM.product_id)
    dp.register_message_handler(photo_load, state=StoreFSM.photo, content_types=['photo'])
    dp.register_message_handler(submit_load, state=StoreFSM.submit)