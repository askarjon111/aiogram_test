from aiogram.fsm.state import State, StatesGroup


class Shop(StatesGroup):
    category = State()
    event = State()
    for_who = State()
    product = State()
    order_item = State()
    order = State()
