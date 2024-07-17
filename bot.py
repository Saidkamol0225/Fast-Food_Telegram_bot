from aiogram.dispatcher.filters import Text
from aiogram import Dispatcher, Bot, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import logging

logging.basicConfig(level=logging.INFO)

from state import *
from default_btn import *
from database import DatabaseManager
from inline_btn import *

TOKEN = "7087349542:AAFGo_n13L2XDJ8IFgEvuwrGdSUtS4LqkGU"

PROXY_URL = "http://proxy.server:3128"

bot = Bot(TOKEN, parse_mode="HTML", proxy=PROXY_URL)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
database = DatabaseManager("fast_food.db")


async def on_startup(dp):
    database.create_tables()
    await bot.send_message(chat_id=6702034677, text="Bot has started")

async def on_shutdown(dp):
    await bot.send_message(chat_id=6702034677, text="Bot has stopped")


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    user = database.get_user_by_id(chat_id=chat_id)
    if user:
        await message.answer(f"Hello {user[2]}. Welcome to Shashlik-NonKabob center. Hammasi chotkimi", reply_markup=main_menu)
    else:
        await state.update_data(chat_id=chat_id)
        await message.answer(f"Welcome to Shashlik-NonKabob center \nPlease enter <b>Your name</b>:")
        await RegisterState.name.set()


@dp.message_handler(state=RegisterState.name)
async def name_handler(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer(f"Click button to share your phone number", reply_markup=phone_number)
    await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.phone_number, content_types=types.ContentType.CONTACT)
async def phone_number_handler(message: types.Message, state: FSMContext):
    contact = message.contact.phone_number
    await state.update_data(phone_number=contact)
    await message.answer("You can use this bot", reply_markup=main_menu)
    data = await state.get_data()
    database.add_user(data=data)
    await state.finish()

@dp.message_handler(text="Order")
async def menu_handler(message: types.Message):
    await message.answer("""
1. Shashlik mol go'shti
2. Shashlik tovuq go'shti
3. Non Kabob mol go'shti
4. Non Kabob tovuq go'shti
    """, reply_markup=kebab_menu)

# @dp.callback_query_handler(Text(startswith="btn_"))
# async def order_handler(call: types.CallbackQuery):
#     btn_number = call.data
#     if btn_number == "btn_1":
#         await call.message.answer_photo(photo="https://dostavo4ka.uz/upload-file/2021/07/05/6229/ffa8810e-46c4-4102-b141-00642a7285e4.jpg",
#                                         caption="Shashlik mol go'shti, 20000 so'm",
#                                         reply_markup=count_kebab)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
