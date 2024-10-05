import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from utils import get_age
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton

TOKEN = "6812297282:AAEn2dlfpk6kK-vxuSzZiKkQJuIMVG9Ylys"


dp = Dispatcher()


# handler
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

# handler
@dp.message(F.text=="test")
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def name_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Test")]], resize_keyboard=True)
    
    age = await get_age(message.text)
    await message.answer(age, reply_markup=keyboard)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())