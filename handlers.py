from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import keyboards as kb
from tag_functions import (create_field, draw_field, is_win, find_empty_y, find_empty_x,
                           is_message_correct, is_move_possible, move_empty_cell)

from text import start_text, help_text

router = Router()


class Game(StatesGroup):
    lst = State()
    move = State()


@router.message(Command('start'))
async def start_bot(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(start_text)


@router.message(Command('help'))
async def help_bot(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(help_text)


@router.message(Command('play'))
async def play(message: Message, state: FSMContext):
    await state.clear()
    tag_lst = create_field()
    tag_message = draw_field(tag_lst)
    await state.set_state(Game.lst)
    await state.update_data(lst=tag_lst)
    await state.set_state(Game.move)
    await message.answer(tag_message, reply_markup=kb.moves)


@router.message(Game.move)
async def move(message: Message, state: FSMContext):

    if not is_message_correct(kb.moves_list, message.text):
        await message.answer('Неверный ввод, попробуйте еще раз')
        return

    await state.update_data(move=message.text)
    data = await state.get_data()

    for i in range(len(data['lst'])):
        if data['lst'][i] == '*':
            empty_cell = i

    empty_y = find_empty_y(empty_cell)
    empty_x = find_empty_x(empty_cell, empty_y)

    if not is_move_possible(kb.moves_list, data['move'], empty_y, empty_x):
        await state.clear()
        await state.set_state(Game.lst)
        await state.update_data(lst=data['lst'])
        await state.set_state(Game.move)
        await message.answer('Такой клавиши не существует, попробуйте передвинуть другую')
        return

    current_cell = move_empty_cell(kb.moves_list, data['move'], empty_y, empty_x)
    data['lst'][current_cell], data['lst'][empty_cell] = data['lst'][empty_cell], data['lst'][current_cell]
    tag_message = draw_field(data['lst'])

    if is_win(data['lst']):
        await state.clear()
        win_message = tag_message + '\n' + 'Поздравляю!!!'
        await message.answer(win_message)

    await state.set_state(Game.lst)
    await state.update_data(lst=data['lst'])
    await state.set_state(Game.move)
    await message.answer(tag_message, reply_markup=kb.moves)