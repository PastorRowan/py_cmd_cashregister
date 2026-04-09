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
#print(str_menu_box)

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
























# length means length of empty spaces of box within box
# height = height of empty spaces of box within box

# ok each line is gonna take one block so lets divide the height into like ok thisline is for this thing an this line is for this thig and so on but they must be equidistant apart
# so le st say we have 50 height blocks and we have 5 items to work with then every 10 blocks we can have an item
# ok now so baiscally we gotta print this hsit eveyr 2 lines ok we use the down varible

def str_one_column_menu_options(length, height, ls_str_menu_options, start_pos):

    int_titles_amount = len(ls_str_menu_options)
    float_h_chars_between_titles = height / int_titles_amount
    int_h_chars_between_titles = int(float_h_chars_between_titles)


    ls_one_column_menu_options = [start_pos]
    for title_index in range(int_titles_amount):

        str_title = ls_str_menu_options[title_index]

        str_title_chars = len(str_title)

        ls_one_column_menu_options.append(str_title)

        ls_one_column_menu_options.append(back(str_title_chars))
        
        if title_index != (int_titles_amount - 1):
            ls_one_column_menu_options.append(down(int_h_chars_between_titles))




    str_one_column_menu_options_ = ''.join(ls_one_column_menu_options)
    return str_one_column_menu_options_










Main_menu_options = {1 : 'Purchase',
                     2 : 'Refund',
                     3 : 'Invoice',
                     4: 'Stock',
                     5 : 'backup'
                    }

ls_option_titles = ['1. Purchase', '2. Refund', '3. Invoice', '4. Stock', '5. Backup', ]

length = 50
height = 15

ls_row_column_chars = ['_', '|']

box_perimeter_x = 2
box_perimeter_y = 2

box_permiter_top_left = pos(box_perimeter_x, box_perimeter_y)
box_inside_top_left = pos(box_perimeter_x + 1, box_perimeter_y + 1)

str_menu_box = main_same_top_and_bot_empty_str_box(length, height, ls_row_column_chars, box_permiter_top_left)
str_menu_options = str_one_column_menu_options(length, height, ls_option_titles, box_inside_top_left)


print(box_permiter_top_left + str_menu_box + box_inside_top_left + str_menu_options)