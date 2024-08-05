from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


button1_1 = KeyboardButton(text='/help')
button1_2 = KeyboardButton(text='задания')
button1_3 = KeyboardButton(text='/material')

button2_1 = KeyboardButton(text='ответ')
button2_2 = KeyboardButton(text='решение')
button2_3 = KeyboardButton(text='следующий')
button2_4 = KeyboardButton(text='/leave')

button3_1 = KeyboardButton(text='Степени и корни')
button3_2 = KeyboardButton(text='/leave')
button3_3 = KeyboardButton(text='Векторы')
button3_4 = KeyboardButton(text='Площади (планиметрия)')
button3_5 = KeyboardButton(text='ФСУ')
button3_6 = KeyboardButton(text='Тригонометрическая таблица')

keyboard_start = ReplyKeyboardMarkup(
    keyboard=[[button1_1], [button1_2], [button1_3]], resize_keyboard=True)
keyboard_task = ReplyKeyboardMarkup(keyboard=[[button2_1], [button2_2], [
                                    button2_3], [button2_4]], resize_keyboard=True)
keyboard_material = ReplyKeyboardMarkup(keyboard=[[button3_4, button3_5], [
                                        button3_3, button3_6], [button3_1, button3_2]], resize_keyboard=True)


inline_1 = InlineKeyboardButton(text='Перовое\nзадание', callback_data='/first')
inline_2 = InlineKeyboardButton(text='Второе\nзадание', callback_data='/second')
inline_3 = InlineKeyboardButton(text='Третье\nзадание', callback_data='/third')
inline_4 = InlineKeyboardButton(text='Четвертое\nзадание', callback_data='/fourth')
inline_5 = InlineKeyboardButton(text='Пятое\nзадание', callback_data='/fifth')
inline_6 = InlineKeyboardButton(text='Шестое\nзадание', callback_data='/sixth')
inline_7 = InlineKeyboardButton(text='Седьмое\nзадание', callback_data='/seventh')
inline_8 = InlineKeyboardButton(text='Восьмое\nзадание', callback_data='/eighth')
inline_9 = InlineKeyboardButton(text='Девятое\nзадание', callback_data='/ninth')
inline_10 = InlineKeyboardButton(text='Десятое\nзадание', callback_data='/tenth')
inline_11 = InlineKeyboardButton(text='Одиннадцатое\nзадание', callback_data='/eleventh')
inline_12 = InlineKeyboardButton(text='Двенадцатое\nзадание', callback_data='/twelfth')

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[inline_1, inline_2, inline_3], [inline_4, inline_5, inline_6], [inline_7, inline_8, inline_9], [inline_10, inline_11, inline_12]])