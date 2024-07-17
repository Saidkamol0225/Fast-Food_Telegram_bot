from aiogram.dispatcher.filters.state import State, StatesGroup

class RegisterState(StatesGroup):
    name = State()
    phone_number = State()
    location = State()

class OrderState(StatesGroup):
    order = State()