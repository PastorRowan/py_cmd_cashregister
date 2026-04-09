import colorama1
import os


# constructor functions
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# empty box creators
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
    str_left_column = str_column_(height, left_char, 2)

    # creates right column
    str_right_column = str_column_(height, right_char, 2)

    str_empt_box = start_pos + back(1) + str_top_row + start_pos + str_left_column + str_bot_row + up(height + 2) + str_right_column
    return str_empt_box

def main_same_top_and_bot_empty_str_box(length, height, ls_row_column_chars, start_pos):

    row_char = ls_row_column_chars[0]
    column_char = ls_row_column_chars[1]

    # creates top and bot row
    str_row = str_row_(length, row_char, 2)

    # creates left and right column
    str_column = str_column_(height, column_char, 2)

    str_empt_box = start_pos + back(1) + str_row + row_char + start_pos + str_column + str_row + up(height + 2) + str_column
    # + back(1)

    return str_empt_box

# full box creators
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def pos (x,y):
    return '\x1b[' + str(y) + ';' + str(x) + 'H'
up = colorama1.Cursor.UP
down = colorama1.Cursor.DOWN
forward = colorama1.Cursor.FORWARD
back = colorama1.Cursor.BACK














os.system('cls')
colorama1.just_fix_windows_console()















def str_column_titles(box_length, dic_title_plus_frac_apart_out_of_1_whole, box_start_x, title_start_x, title_start_y):

    available_len = box_length + (title_start_x - box_start_x)

    #print(pos(50,50) + str(available_len))

    #print(pos(50,50)+ str(title_start_x))

# ok wait lets me jsut draw ths 
    ls_column_titles = []

    for title, percentage in dic_title_plus_frac_apart_out_of_1_whole.items():

        float_x_offset = percentage * available_len

        int_x_offset = int(float_x_offset)

        #print(pos(51,51) + str(int_x_offset))

        curr_title_x = title_start_x + int_x_offset

        #print(pos(51,51)+ str(curr_title_x))
        
        curr_title_pos = pos(curr_title_x, title_start_y)
        ls_column_titles.append(curr_title_pos)
        ls_column_titles.append(title)

    str_column_titles = ''.join(ls_column_titles)
    return str_column_titles


box_length = 50
box_height = 25
ls_row_column_chars = ['_', '|']
box_start_x = 1
box_start_pos = pos(1,1)

dic_title_plus_frac_apart_out_of_1_whole =  {'Items': 0, 'Total':0.2, 'peepee':0.8}
title_start_x = 3
title_start_y = 3

str_column_titles_ = str_column_titles(box_length, dic_title_plus_frac_apart_out_of_1_whole, box_start_x, title_start_x, title_start_y)

str_empt_box = main_same_top_and_bot_empty_str_box(box_length, box_height, ls_row_column_chars, box_start_pos)

print(str_empt_box + str_column_titles_)