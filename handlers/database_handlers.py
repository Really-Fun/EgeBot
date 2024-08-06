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