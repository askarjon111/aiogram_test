import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from utils import calculate, get_age
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram import Router

register_router = Router()


@register_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Tabriknomalar")]], resize_keyboard=True)

    await message.answer(f"Assalomu alaykum.\nQuyidagi kerakli bo'limni tanlang!", reply_markup=keyboard)

