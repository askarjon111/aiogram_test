import os
from aiohttp import ClientSession
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv

load_dotenv()

SITE_NAME = os.environ.get('SITE_NAME')


async def register_customer(state: FSMContext):
    try:
        async with ClientSession() as session:
            async with session.post(f'{SITE_NAME}/api/customer/create/', json=await state.get_data()) as response:
                print(await response.json(), response.status)
                return await response.json(), response.status==201

    except Exception as e:
        return f'{e}', False


async def get_customer(telegram_id):
    try:
        async with ClientSession() as session:
            async with session.get(f'{SITE_NAME}/api/customer/', params={'telegram_id': telegram_id}) as response:
                data = await response.json()
                return data['customer'], response.status==200

    except Exception as e:
        return f'{e}', False


async def get_categories():
    try:
        async with ClientSession() as session:
            async with session.get(f'{SITE_NAME}/api/products/categories/') as response:
                data = await response.json()
                return data['results']

    except Exception as e:
        return f'{e}'
