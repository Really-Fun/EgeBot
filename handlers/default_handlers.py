from aiogram import F, Router
from aiogram.types import Message, FSInputFile
from lexicon_ru import lexicon
from aiogram.filters import Command
from database.base import baza
from keyboards import *

router = Router()


@router.message(Command(commands=["start", "Start"]))
async def get_start(message: Message) -> None:
    await message.answer(lexicon.commands["/start"], reply_markup=keyboard_start)
    result = baza.get_in_database(str(message.from_user.id))
    if result:
        pass
    else:
        baza.write_to_database(str(message.from_user.id))



@router.message(Command(commands=["stats", "Stats"]))
async def get_stats(message: Message):
    wins_total = baza.get_total_and_wins(message.from_user.id)
    await message.answer(
        f"<b>Всего задач: {wins_total[0]}</b>\n<b>Правильно решено: {wins_total[1]}</b>"
    )


@router.message(Command(commands=["help", "Help"]))
async def get_help(message: Message) -> None:
    await message.answer(lexicon.commands["/help"], reply_markup=keyboard_start)


@router.message(Command(commands=["material"]))
async def get_material(message: Message) -> None:
    await message.answer("Успешно", reply_markup=keyboard_material)


@router.message(Command(commands=["leave"]))
async def leave(message: Message):
    await message.answer("Успешно", reply_markup=keyboard_start)
