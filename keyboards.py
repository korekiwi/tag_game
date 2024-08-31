from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

moves_list = [
    'Подвинуть верхнюю клавишу',
    'Подвинуть правую клавишу',
    'Подвинуть нижнюю клавишу',
    'Подвинуть левую клавишу'
]

moves = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=moves_list[0])],
    [KeyboardButton(text=moves_list[1])],
    [KeyboardButton(text=moves_list[2])],
    [KeyboardButton(text=moves_list[3])]
])

new_moves = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=moves_list[0], callback_data='1')],
    [InlineKeyboardButton(text=moves_list[1], callback_data='2')],
    [InlineKeyboardButton(text=moves_list[2], callback_data='3')],
    [InlineKeyboardButton(text=moves_list[3], callback_data='4')]
])
