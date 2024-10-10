from aiogram.fsm.state import State, StatesGroup


class RegisterForm(StatesGroup):
    lang = State()
    name = State()
    phone = State()
    company = State()
