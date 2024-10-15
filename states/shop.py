from aiogram.fsm.state import State, StatesGroup


class Shop(StatesGroup):
    product_type = State() # tabriknomalar/devor uchun qabul qiladi
    event_type = State() # Bayramlar/ Tug'ilgan kun...
    event = State() # Yangi yil, xotira va qadrlash kuni...
    for_who = State() # Erkak/Ayol...
    product = State()
    order_item = State()
    order = State()
