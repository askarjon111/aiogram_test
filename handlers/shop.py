from aiogram import Bot, Dispatcher, html, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram import Router
from aiogram.fsm.context import FSMContext
from sessions import get_customer, register_customer
from states.shop import Shop
from utils import get_word

shop_router = Router()


@shop_router.message(F.text.in_(['Tabriknomalar', 'Открытки', 'Devor uchun', 'Для стены']))
async def company_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(Shop.product_type)
    customer, _ = await get_customer(message.from_user.id)
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=await get_word('bayram', customer['lang'])),
                   KeyboardButton(text=await get_word('toy', customer['lang']))],
                  [KeyboardButton(text=await get_word('yubiley', customer['lang'])),
                   KeyboardButton(text=await get_word('tugilgan', customer['lang'])),]],
        resize_keyboard=True)

    await message.answer(await get_word('choose-event', customer['lang']), reply_markup=keyboard)
