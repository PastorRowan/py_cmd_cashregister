import colorama1
import os

# back(2)


up = colorama1.Cursor.UP
down = colorama1.Cursor.DOWN
forward = colorama1.Cursor.FORWARD
back = colorama1.Cursor.BACK

colorama1.Cursor.

def str_row_(length, char, offset):
    ls_row = []

    for _ in range(length + offset):
        ls_row.append(char)

    str_row = ''.join(ls_row)
    return str_row

def str_column_(height, char, offset):
    ls_column = []
    for _ in range(height + offset):
        ls_column.append(down(1))
        ls_column.append(back(1))
        ls_column.append(char)

    str_column = ''.join(ls_column)
    return str_column

def pos (x,y):
    return '\x1b[' + str(y) + ';' + str(x) + 'H'




def main_print_empty_str_box(length, height, ls_top_right_bot_left_chars, start_pos): # i could make top and bototm the same or i can make them all the same i guess idk watver you want idk i guess let jsut do all 
    # then figre it out form there i guess eyah 
    top_char = ls_top_right_bot_left_chars[0]
    right_char = ls_top_right_bot_left_chars[1]
    bot_char = ls_top_right_bot_left_chars[2]
    left_char = ls_top_right_bot_left_chars[3]

    # creates top row
    str_top_row = str_row_(length, top_char, 2)

    # creates bot row
    str_bot_row = str_row_(length, bot_char, 1)

    # creates left column
    str_left_column = str_column_(height, left_char, 2)

    # creates right column
    str_right_column = str_column_(height, right_char, 2)

    str_empt_box = start_pos + str_top_row + back(length + 2) + str_left_column + str_bot_row + up(height + 2) + str_right_column
    return str_empt_box

    #print(str_top_row + back(length + 2) + str_left_column + str_bot_row + up(height + 2) + str_right_column)


length = 20
height = 20

ls_top_right_bot_left_chars = ['_', '|', '_', '|']


colorama1.just_fix_windows_console()
os.system('cls')
str_menu_box = main_print_empty_str_box(length, height, ls_top_right_bot_left_chars, pos(2, 2))
print(pos(3, 3) + 'text')
print(str_menu_box)

# how can i print a str box in any positionnow i would need a start position like 1 1 or something then mark the corenrs ofour creation  because we can
# this should wor