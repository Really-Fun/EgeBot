from aiogram import F, Router
from aiogram.types import FSInputFile, Message

router = Router()


@router.message(F.text == 'Степени и корни')
async def get_sqrt_and_stepeni(message: Message):
    new = FSInputFile('material_ege//f_004.jpg')
    await message.answer_photo(new)


@router.message(F.text == 'Векторы')
async def get_vectors(message: Message):
    new = FSInputFile('material_ege//geometrija_015.jpg')
    await message.answer_photo(new)

@router.message(F.text == 'Площади (планиметрия)')
async def get_vectors(message: Message):
    new = FSInputFile('material_ege//f535907c48291a25845317be10b44759.jpeg')
    await message.answer_photo(new)

@router.message(F.text == 'ФСУ')
async def get_vectors(message: Message):
    new = FSInputFile('material_ege//slide_8.jpg')
    await message.answer_photo(new)

@router.message(F.text == 'Тригонометрическая таблица')
async def get_vectors(message: Message):
    new = FSInputFile('material_ege//aaf0fdf7926b33a67bc0585bde5cf2c2.png')
    await message.answer_photo(new)