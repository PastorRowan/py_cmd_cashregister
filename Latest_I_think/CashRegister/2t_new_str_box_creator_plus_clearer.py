import colorama1
import os

# back(2)


up = colorama1.Cursor.UP
down = colorama1.Cursor.DOWN
forward = colorama1.Cursor.FORWARD
back = colorama1.Cursor.BACK

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




def main_custimizable_empty_str_box(length, height, ls_top_right_bot_left_chars, start_pos):

    top_char = ls_top_right_bot_left_chars[0]
    right_char = ls_top_right_bot_left_chars[1]
    bot_char = ls_top_right_bot_left_chars[2]
    left_char = ls_top_right_bot_left_chars[3]

    # creates top row
    str_top_row = str_row_(length, top_char, 2)

    # creates bot row
    str_bot_row = str_row_(length, bot_char, 1)

    # creates left column
    str_left_column = str_column_(height, left_char, 0)

    # creates right column
    str_right_column = str_column_(height, right_char, 0)

    str_empt_box = start_pos + back(1) + str_top_row + start_pos + str_left_column + str_bot_row + up(height) + str_right_column
    return str_empt_box

def main_same_top_and_bot_empty_str_box(length, height, ls_row_column_chars, start_pos):

    row_char = ls_row_column_chars[0]
    column_char = ls_row_column_chars[1]

    # creates top and bot row
    str_row = str_row_(length, row_char, 0)

    # creates left and right column
    str_column = str_column_(height, column_char, 0)

    str_empt_box = start_pos + back(1) + str_row + row_char + start_pos + str_column + str_row + up(height) + str_column
    # + back(1)

    return str_empt_box

os.system('cls')
colorama1.just_fix_windows_console()

# main_custimizable_empty_str_box test:


length = 5
height = 4

ls_menu_box_top_right_bot_left_chars = ['_', '|', '_', '|']

ls_clear_menu_box_top_right_bot_left_chars = [' ', ' ', ' ', ' ']


# menu box
str_menu_box = main_custimizable_empty_str_box(length, height, ls_menu_box_top_right_bot_left_chars, pos(16, 8))

# clear menu box
str_clear_menu_box = main_custimizable_empty_str_box(length, height, ls_clear_menu_box_top_right_bot_left_chars, pos(16, 8))

# prints menu box
print(str_menu_box)

# clear menu box
#print(str_clear_menu_box)

# can print them on top of each other like this but it seems pretty useless to me
# print(str_menu_box + str_clear_menu_box)


'''

# main_same_top_and_bot_empty_str_box test:

length = 5
height = 4

ls_menu_box_top_right_bot_left_chars = ['_', '|', '_', '|']

ls_clear_menu_box_top_right_bot_left_chars = [' ', ' ', ' ', ' ']

# menu box
str_menu_box = main_same_top_and_bot_empty_str_box(length, height, ls_menu_box_top_right_bot_left_chars, pos(16, 8))

# clear menu box
str_clear_menu_box = main_same_top_and_bot_empty_str_box(length, height, ls_clear_menu_box_top_right_bot_left_chars, pos(16, 8))

# prints menu box
print(str_clear_menu_box)

# clear menu box
#print(str_clear_menu_box)
'''




















# can print them on top of each other like this but it seems pretty useless to me
# print(str_menu_box + str_clear_menu_box)





# ok we can make a few other functions that act as more efficeint versions than this one i guess? i feel like that, thats a good idea i guess?
# i mean do we really need more efficeiny because i mean all of these functions are gonna be stored in memory anyways so then if they are stored in mem anyways then the performance increase of calling smaller
# functions is just gonna be negligible i guess one thing i could do is like make there like settings likeoh make top and side row same i guess and then the processing becomes different instead of creating more
# of exact same functionsi mean yeah but i could also create a function that literally only creates a top and bot row and then it creates the string ez??> i guess i feel like yaeh that makes sense hmmm i guess it
# will increase effieicny of frontend but i mean like is it really worht hte extra mem overhead? fuck it lets do it



