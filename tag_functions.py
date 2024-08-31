import random


def create_field() -> list:
    tag_lst = [
        '1', '2', '3', '4',
        '5', '6', '7', '8',
        '9', '10', '11', '12',
        '13', '14', '15'
    ]
    random.shuffle(tag_lst)
    tag_lst.append('*')
    return tag_lst


def draw_field(tag_lst: list) -> str:
    tag_message = ''

    for i in range(0, len(tag_lst)):

        if i % 4 == 0:
            tag_message += '|'

        if len(tag_lst[i]) == 2:
            tag_message += f"  {tag_lst[i]}  |"
        else:
            tag_message += f"   {tag_lst[i]}   |"

        if (i + 1) % 4 == 0:
            tag_message += '\n'
    # tag_message = (f"| {tag_lst[0]} | {tag_lst[1]} | {tag_lst[2]} | {tag_lst[3]} | \n"
    #                f"| {tag_lst[4]} | {tag_lst[5]} | {tag_lst[6]} | {tag_lst[7]} | \n"
    #                f"| {tag_lst[8]} | {tag_lst[9]} | {tag_lst[10]} | {tag_lst[11]} | \n"
    #                f"| {tag_lst[12]} | {tag_lst[13]} | {tag_lst[14]} | {tag_lst[15]} |"
    #                )
    return tag_message


def is_win(field: list) -> bool:
    win_field = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '*']
    if field == win_field:
        return True


def find_empty_y(empty_cell: int) -> int:
    empty_y = 0
    if 0 <= empty_cell <= 3:
        empty_y = 1
    elif 4 <= empty_cell <= 7:
        empty_y = 2
    elif 8 <= empty_cell <= 11:
        empty_y = 3
    elif 12 <= empty_cell <= 15:
        empty_y = 4
    return empty_y


def find_empty_x(empty_cell: int, empty_y: int) -> int:
    empty_x = empty_cell - (empty_y - 1) * 4 + 1
    return empty_x


def is_message_correct(moves_list: list, move: str) -> bool:
    if move in moves_list:
        return True


def is_move_possible(moves_list: list, move: str,
                     empty_y: int, empty_x: int) -> bool:
    if empty_y == 1 and move == moves_list[0]:
        return False
    if empty_y == 4 and move == moves_list[2]:
        return False
    if empty_x == 1 and move == moves_list[3]:
        return False
    if empty_x == 4 and move == moves_list[1]:
        return False
    return True


def move_empty_cell(moves_list: list, move: str, empty_y, empty_x) -> int:
    if move == moves_list[0]:
        new_x = empty_x
        new_y = empty_y - 1
    elif move == moves_list[1]:
        new_x = empty_x + 1
        new_y = empty_y
    elif move == moves_list[2]:
        new_x = empty_x
        new_y = empty_y + 1
    elif move == moves_list[3]:
        new_x = empty_x - 1
        new_y = empty_y
    return (new_y - 1) * 4 + new_x - 1
