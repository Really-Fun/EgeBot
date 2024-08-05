from aiogram import F, Router
from aiogram.types import Message
from database.base import baza
from lexicon_ru.lexicon import commands
from keyboards import *

router = Router()

def check_base(message: Message):
    if baza.get_in_database(message.from_user.id):
        return False
    return True

@router.message(check_base)
async def write(message: Message):
    baza.write_to_database(message.from_user.id)
    await message.answer(commands['/start'], reply_markup=keyboard_start)

@router.message(F.text.lower() == 'а')
async def gaga(message: Message):
    await message.answer(f'<a href="tg://user?id={1082861671}"><u><b>И</b></u></a>')