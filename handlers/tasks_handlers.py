import random
from keyboards import *
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from aiogram.types import FSInputFile
from services.sdamgia_utils import get_png, get_level, get_answer, get_decision, get_decision_images
from services.tasks import math1, math2, math3, math4, math5, math6, math7, math8, math9, math10, math11, math12
from database.base import baza


router = Router()
all_maths = [math1, math2, math3, math4, math5, math6, math7, math8, math9, math10, math11, math12]


def check_is_int(s: Message) -> bool:
    s = s.text
    if s.count(',') <= 1:
        s = s.replace(',', '.')
        try:
            float(s)
            return True
        except:
            return False
    else:
        return False

def check_in_level(s: Message) -> bool:
    return bool(baza.get_in_task(s.from_user.id))

@router.message(F.text.lower() == 'задания')
async def tasks(message: Message):
    await message.answer('Выберите задание из тестовой части', reply_markup=inline_keyboard)

@router.callback_query(F.data.in_(['/first']))
async def process_buttons_press1(callback: CallbackQuery):
    """_summary_

    Args:
        message (Message): _description_
    Даёт пользователю задание и записывает в базу данных
    """
    razdel = random.choice(list(math1))
    await callback.message.answer(f'Задание N{razdel}')
    baza.add_total(callback.from_user.id)
    baza.write_zadanie(callback.from_user.id, 1)
    baza.in_task(callback.from_user.id, 1, razdel)
    my_level = get_png('math', razdel)
    await callback.message.answer(get_level('math', razdel), reply_markup=keyboard_task)
    for i in my_level:
        with open('your_image.png', 'wb') as file:
            file.write(i)
            my = FSInputFile('your_image.png')
        await callback.message.answer_photo(my)
    await callback.message.answer('Ваш ответ:')
    await callback.answer()

@router.callback_query(F.data.in_(['/second']))
async def process_buttons_press2(callback: CallbackQuery):
    """_summary_

    Args:
        message (Message): _description_
    Даёт пользователю задание и записывает в базу данных
    """
    razdel = random.choice(list(math2))
    await callback.message.answer(f'Задание N{razdel}')
    baza.add_total(callback.from_user.id)
    baza.write_zadanie(callback.from_user.id, 2)
    baza.in_task(callback.from_user.id, 1, razdel)
    my_level = get_png('math', razdel)
    await callback.message.answer(get_level('math', razdel), reply_markup=keyboard_task)
    for i in my_level:
        with open('your_image.png', 'wb') as file:
            file.write(i)
            my = FSInputFile('your_image.png')
        await callback.message.answer_photo(my)
    await callback.message.answer('Ваш ответ:')
    await callback.answer()

@router.callback_query(F.data.in_(['/third']))
async def process_buttons_press2(callback: CallbackQuery):
    """_summary_

    Args:
        message (Message): _description_
    Даёт пользователю задание и записывает в базу данных
    """
    razdel = random.choice(list(math3))
    baza.add_total(callback.from_user.id)
    baza.write_zadanie(callback.from_user.id, 3)
    baza.in_task(callback.from_user.id, 1, razdel)
    my_level = get_png('math', razdel)
    await callback.message.answer(f'Задание N{razdel}')
    await callback.message.answer(get_level('math', razdel), reply_markup=keyboard_task)
    for i in my_level:
        with open('your_image.png', 'wb') as file:
            file.write(i)
            my = FSInputFile('your_image.png')
        await callback.message.answer_photo(my)
    await callback.message.answer('Ваш ответ:')
    await callback.answer()

@router.callback_query(F.data.in_(['/fourth']))
async def process_buttons_press2(callback: CallbackQuery):
    """_summary_

    Args:
        message (Message): _description_
    Даёт пользователю задание и записывает в базу данных
    """
    razdel = random.choice(list(math4))
    await callback.message.answer(f'Задание N{razdel}')
    baza.add_total(callback.from_user.id)
    baza.write_zadanie(callback.from_user.id, 4)
    baza.in_task(callback.from_user.id, 1, razdel)
    my_level = get_png('math', razdel)
    await callback.message.answer(get_level('math', razdel), reply_markup=keyboard_task)
    for i in my_level:
        with open('your_image.png', 'wb') as file:
            file.write(i)
            my = FSInputFile('your_image.png')
        await callback.message.answer_photo(my)
    await callback.message.answer('Ваш ответ:')
    await callback.answer()

@router.callback_query(F.data.in_(['/fifth']))
async def process_buttons_press2(callback: CallbackQuery):
    """_summary_

    Args:
        message (Message): _description_
    Даёт пользователю задание и записывает в базу данных
    """
    razdel = random.choice(list(math5))
    await callback.message.answer(f'Задание N{razdel}')
    baza.add_total(callback.from_user.id)
    baza.write_zadanie(callback.from_user.id, 5)
    baza.in_task(callback.from_user.id, 1, razdel)
    my_level = get_png('math', razdel)
    await callback.message.answer(get_level('math', razdel), reply_markup=keyboard_task)
    for i in my_level:
        with open('your_image.png', 'wb') as file:
            file.write(i)
            my = FSInputFile('your_image.png')
        await callback.message.answer_photo(my)
    await callback.message.answer('Ваш ответ:')
    await callback.answer()

@router.callback_query(F.data.in_(['/sixth']))
async def process_buttons_press2(callback: CallbackQuery):
    """_summary_

    Args:
        message (Message): _description_
    Даёт пользователю задание и записывает в базу данных
    """
    razdel = random.choice(list(math6))
    await callback.message.answer(f'Задание N{razdel}')
    baza.add_total(callback.from_user.id)
    baza.write_zadanie(callback.from_user.id, 6)
    baza.in_task(callback.from_user.id, 1, razdel)
    my_level = get_png('math', razdel)
    await callback.message.answer(get_level('math', razdel), reply_markup=keyboard_task)
    for i in my_level:
        with open('your_image.png', 'wb') as file:
            file.write(i)
            my = FSInputFile('your_image.png')
        await callback.message.answer_photo(my)
    await callback.message.answer('Ваш ответ:')
    await callback.answer()

@router.callback_query(F.data.in_(['/seventh']))
async def process_buttons_press2(callback: CallbackQuery):
    """_summary_

    Args:
        message (Message): _description_
    Даёт пользователю задание и записывает в базу данных
    """
    razdel = random.choice(list(math7))
    await callback.message.answer(f'Задание N{razdel}')
    baza.add_total(callback.from_user.id)
    baza.write_zadanie(callback.from_user.id, 7)
    baza.in_task(callback.from_user.id, 1, razdel)
    my_level = get_png('math', razdel)
    await callback.message.answer(get_level('math', razdel), reply_markup=keyboard_task)
    for i in my_level:
        with open('your_image.png', 'wb') as file:
            file.write(i)
            my = FSInputFile('your_image.png')
        await callback.message.answer_photo(my)
    await callback.message.answer('Ваш ответ:')
    await callback.answer()

@router.callback_query(F.data.in_(['/eighth']))
async def process_buttons_press2(callback: CallbackQuery):
    """_summary_

    Args:
        message (Message): _description_
    Даёт пользователю задание и записывает в базу данных
    """
    razdel = random.choice(list(math8))
    await callback.message.answer(f'Задание N{razdel}')
    baza.add_total(callback.from_user.id)
    baza.write_zadanie(callback.from_user.id, 8)
    baza.in_task(callback.from_user.id, 1, razdel)
    my_level = get_png('math', razdel)
    await callback.message.answer(get_level('math', razdel), reply_markup=keyboard_task)
    for i in my_level:
        with open('your_image.png', 'wb') as file:
            file.write(i)
            my = FSInputFile('your_image.png')
        await callback.message.answer_photo(my)
    await callback.message.answer('Ваш ответ:')
    await callback.answer()

@router.callback_query(F.data.in_(['/ninth']))
async def process_buttons_press2(callback: CallbackQuery):
    """_summary_

    Args:
        message (Message): _description_
    Даёт пользователю задание и записывает в базу данных
    """
    razdel = random.choice(list(math9))
    await callback.message.answer(f'Задание N{razdel}')
    baza.add_total(callback.from_user.id)
    baza.write_zadanie(callback.from_user.id, 9)
    baza.in_task(callback.from_user.id, 1, razdel)
    my_level = get_png('math', razdel)
    await callback.message.answer(get_level('math', razdel), reply_markup=keyboard_task)
    for i in my_level:
        with open('your_image.png', 'wb') as file:
            file.write(i)
            my = FSInputFile('your_image.png')
        await callback.message.answer_photo(my)
    await callback.message.answer('Ваш ответ:')
    await callback.answer()

@router.callback_query(F.data.in_(['/tenth']))
async def process_buttons_press2(callback: CallbackQuery):
    """_summary_

    Args:
        message (Message): _description_
    Даёт пользователю задание и записывает в базу данных
    """
    razdel = random.choice(list(math10))
    await callback.message.answer(f'Задание N{razdel}')
    baza.add_total(callback.from_user.id)
    baza.write_zadanie(callback.from_user.id, 10)
    baza.in_task(callback.from_user.id, 1, razdel)
    my_level = get_png('math', razdel)
    await callback.message.answer(get_level('math', razdel), reply_markup=keyboard_task)
    for i in my_level:
        with open('your_image.png', 'wb') as file:
            file.write(i)
            my = FSInputFile('your_image.png')
        await callback.message.answer_photo(my)
    await callback.message.answer('Ваш ответ:')
    await callback.answer()

@router.callback_query(F.data.in_(['/eleventh']))
async def process_buttons_press2(callback: CallbackQuery):
    """_summary_

    Args:
        message (Message): _description_
    Даёт пользователю задание и записывает в базу данных
    """
    razdel = random.choice(list(math11))
    await callback.message.answer(f'Задание N{razdel}')
    baza.add_total(callback.from_user.id)
    baza.write_zadanie(callback.from_user.id, 11)
    baza.in_task(callback.from_user.id, 1, razdel)
    my_level = get_png('math', razdel)
    await callback.message.answer(get_level('math', razdel), reply_markup=keyboard_task)
    for i in my_level:
        with open('your_image.png', 'wb') as file:
            file.write(i)
            my = FSInputFile('your_image.png')
        await callback.message.answer_photo(my)
    await callback.message.answer('Ваш ответ:')
    await callback.answer()

@router.callback_query(F.data.in_(['/twelfth']))
async def process_buttons_press2(callback: CallbackQuery):
    """_summary_

    Args:
        message (Message): _description_
    Даёт пользователю задание и записывает в базу данных
    """
    razdel = random.choice(list(math12))
    await callback.message.answer(f'Задание N{razdel}')
    baza.add_total(callback.from_user.id)
    baza.write_zadanie(callback.from_user.id, 12)
    baza.in_task(callback.from_user.id, 1, razdel)
    my_level = get_png('math', razdel)
    await callback.message.answer(get_level('math', razdel), reply_markup=keyboard_task)
    for i in my_level:
        with open('your_image.png', 'wb') as file:
            file.write(i)
            my = FSInputFile('your_image.png')
        await callback.message.answer_photo(my)
    await callback.message.answer('Ваш ответ:')
    await callback.answer()

@router.message(F.text.lower() == 'следующий')
async def next_task(message: Message):
    razdel = random.choice(list(all_maths[baza.get_zadanie(message.from_user.id) - 1]))
    await message.answer(f'Задание N{razdel}')
    baza.add_total(message.from_user.id)
    baza.write_zadanie(message.from_user.id, baza.get_zadanie(message.from_user.id))
    baza.in_task(message.from_user.id, 1, razdel)
    my_level = get_png('math', razdel)
    await message.answer(get_level('math', razdel), reply_markup=keyboard_task)
    for i in my_level:
        with open('your_image.png', 'wb') as file:
            file.write(i)
            my = FSInputFile('your_image.png')
        await message.answer_photo(my)
    await message.answer('Ваш ответ:')

@router.message(F.text.lower() == 'ответ')
async def otvet(message: Message):
    id_user_task = baza.get_id_user_task(message.from_user.id)[0]
    baza.in_task(message.from_user.id, in_level=0, level=id_user_task)
    await message.answer(get_answer('math', id=id_user_task))
    
@router.message(F.text.lower() == 'решение')
async def decision(message: Message):
    id_user_task = baza.get_id_user_task(message.from_user.id)[0]
    await message.answer(get_decision(subject='math', id=id_user_task))
    all_images = get_decision_images('math', id=id_user_task)
    baza.in_task(message.from_user.id, in_level=0, level=id_user_task)
    for i in all_images:
        with open('your_image.png', 'wb') as file:
            file.write(i)
            my = FSInputFile('your_image.png')
        await message.answer_photo(my)

@router.message(check_in_level, check_is_int)
async def check_answer(message: Message):
    id_user_task = baza.get_id_user_task(message.from_user.id)[0]
    try:
        if message.text.find('/') != -1 or message.text.find('*') != -1:
            num = eval(message.text)
            if num == float(get_answer('math', id_user_task).replace(',', '.').replace(' ', '').replace('−', '-')):
                await message.answer('Прaвильно')
                baza.add_win(message.from_user.id)
                baza.in_task(message.from_user.id, in_level=0, level=id_user_task)
        elif float(message.text.replace(',', '.')) == float(get_answer('math', id_user_task).replace(',', '.').replace(' ', '').replace('−', '-')):
            await message.answer('Прaвильно')
            baza.add_win(message.from_user.id)
            baza.in_task(message.from_user.id, in_level=0, level=id_user_task)
        else:
            await message.answer('Подумай ещё')
    except:
        await message.answer('К сожалению, у этого задания нет ответа. Однако вы можете посмотреть решение.')