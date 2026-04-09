

import os

default_l_h_and_min_l_h = [50, 25]

def str_eg_box_(length, height): # maybe we should seperate the functins like one is for example bo and one is for clear box but i mean like i gues taht makes sense. i mena 

    # creates 1 row

    str_welcome = f'Welcome!!!press the arrow keys to adjust the screen size (measured in characters) the default length is {default_l_h_and_min_l_h[0]} the default height is {default_l_h_and_min_l_h[1]}'

    int_welcome_num_chars = len(str_welcome)

    # 2.3 always round up then 
    float_welcome_chars_into_length = int_welcome_num_chars / length
    # will be like 3
    int_full_rows = int(float_welcome_chars_into_length)
    # total_needed_rows = math.ceil(float_welcome_chars_into_length)
    ls_top_welcome_section = []


    curr_char_index = [0]
    total_chars = len(str_welcome)


    if int_full_rows > 0:
        for _ in range(int_full_rows):
            ls_top_welcome_row = ['|']
            for _ in range(length):
                ls_top_welcome_row.append(str_welcome[curr_char_index[0]])
                curr_char_index[0] += 1
            ls_top_welcome_row.append('|')
            ls_top_welcome_row.append('\n')

            ls_top_welcome_section += ls_top_welcome_row


    remainder_chars = total_chars - curr_char_index[0]
    num_spaces = length - remainder_chars # num_spaces + remainder_chars must be equal to length

    ls_last_top_welcome_row = ['|']
    for _ in range(remainder_chars):
        ls_last_top_welcome_row.append(str_welcome[curr_char_index[0]])
        curr_char_index[0] += 1
    
    for _ in range(num_spaces):
        ls_last_top_welcome_row.append(' ')


    ls_last_top_welcome_row.append('|')
    ls_last_top_welcome_row.append('\n')

    ls_top_welcome_section += ls_last_top_welcome_row

    str_top_welcome = ''.join(ls_top_welcome_section)
    
    print(str_top_welcome)

    input('\n\n\n\nerjg9iojoigjroe4i')






length = 50
height = 25

os.system('cls')
str_eg_box_(length, height)