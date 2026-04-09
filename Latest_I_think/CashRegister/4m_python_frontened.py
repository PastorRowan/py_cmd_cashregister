import colorama1
import os
import math
import mmap
import keyboard1

colorama1.just_fix_windows_console()
up = colorama1.Cursor.UP
down = colorama1.Cursor.DOWN
forward = colorama1.Cursor.FORWARD
back = colorama1.Cursor.BACK

def main():
    """
    expected output:
    1a2
    aba
    3a4
    """
    colorama1.just_fix_windows_console()
    print("aaa")
    print("aaa")
    print("aaa")
    print(up(5) + down(3) + 'b')



#if __name__ == '__main__':
#    main()









colorama1.Fore
colorama1.just_fix_windows_console()

def pos (x,y):
    return '\x1b[' + str(y) + ';' + str(x) + 'H'

def main():
    print(colorama1.Fore.RED + pos(30,10) + " This string in differentpalc")

    input('')



    input('old pos')

def str_box_(length, height):
    constructor_mid_row = ['|']
    for _ in range(length):
        constructor_mid_row.append(' ')
    constructor_mid_row.append('|')
    constructor_mid_row.append('\n')
    mid_row = ''.join(constructor_mid_row)

    ls_mid_rows = []
    # creates middle section
    for _ in range(height - 2):
        ls_mid_rows.append(mid_row)

    # creates top row
    ls_top_row = []
    for _ in range(length + 2):
        ls_top_row.append('_')
    ls_top_row.append('\n')

    # creates bot row
    ls_bot_row = ['|']
    for _ in range(length):
        ls_bot_row.append('_')
    ls_bot_row.append('|')

    ls_eg_box = ls_top_row + ls_mid_rows + ls_bot_row
    str_eg_box = ''.join(ls_eg_box)

    return str_eg_box







def str_eg_box_(length, height):

    str_welcome = f'Welcome!!!press the arrow keys to adjust the screen size (measured in characters) the default length is {default_l_h_and_min_l_h[0]} the default height is {default_l_h_and_min_l_h[1]}'

    int_welcome_num_chars = len(str_welcome)
    float_welcome_chars_into_length = int_welcome_num_chars / length
    int_full_rows = int(float_welcome_chars_into_length)
    ls_top_welcome_section = []

    int_total_welcome_rows = math.ceil(float_welcome_chars_into_length)

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
    num_spaces = length - remainder_chars
    if remainder_chars > 0:
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

    constructor_mid_row = ['|']
    for _ in range(length):
        constructor_mid_row.append(' ')
    constructor_mid_row.append('|')
    constructor_mid_row.append('\n')
    mid_row = ''.join(constructor_mid_row)

    # creates middle section
    ls_mid_rows = [str_top_welcome]
    for _ in range(height - 2 - int_total_welcome_rows):
        ls_mid_rows.append(mid_row)

    # creates top row
    ls_top_row = []
    for _ in range(length + 2):
        ls_top_row.append('_')
    ls_top_row.append('\n')

    # creates bot row
    ls_bot_row = ['|']
    for _ in range(length):
        ls_bot_row.append('_')
    ls_bot_row.append('|')

    ls_eg_box = ls_top_row + ls_mid_rows + ls_bot_row
    str_eg_box = ''.join(ls_eg_box)

    return str_eg_box

def str_clear_box_(length, height):
    ls_constr_row_clear = [' ']

    for _ in range(length):
        ls_constr_row_clear.append(' ')

    ls_constr_row_clear.append(' ')
    ls_constr_row_clear.append('\n')
    row_clear = ''.join(ls_constr_row_clear)

    ls_constr_clear_box = []
    for _ in range(height):
        ls_constr_clear_box.append(row_clear)

    str_clear_box = ''.join(ls_constr_clear_box)

    return str_clear_box



def load_default_box_dimension():
    with open('settings/default_box_dimensions.txt', 'r+') as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mmapped_f:
            strbyt_dimensions_f_content = mmapped_f.read()
            strbyt_dimensions = strbyt_dimensions_f_content.split(b'\n')

            strbyt_l = strbyt_dimensions[0]
            strbyt_h = strbyt_dimensions[1]
            strbyt_min_l = strbyt_dimensions[2]
            strbyt_min_h = strbyt_dimensions[3]

            str_l = strbyt_l.decode('utf-8')
            str_h = strbyt_h.decode('utf-8')
            str_min_l = strbyt_min_l.decode('utf-8')
            str_min_h = strbyt_min_h.decode('utf-8')

            int_l = int(str_l)
            int_h = int(str_h)
            int_min_l = int(str_min_l)
            int_min_h = int(str_min_h)

            return int_l, int_h, int_min_l, int_min_h









# one thing i could do just to make this code more readable is store all my pos functions in like different foldres and then import them when i need to use them. i feel like thats a good idea so that we dont end up
# with one long ass python script with everything on one page i mean yeah that could be a good idea i acutally would liek to get started on that and then also perahps like an options bar or something
# like a uhm yeah i woukd rpobably need that like something that shows current options at the bottom of the screen. i mean that makes sense but i think first lets make the options well the thing is
# after func 1 thats where we are gonna get to the main menu

#os.terminal_size

os.system('cls')
#keyboard1.press('f11')

default_l_h_and_min_l_h = load_default_box_dimension()

globals = {'size' : {'length' : [], 'height' : []}, 'mem' : 0}

def complete_program_loop(func_num):
    global globals

    colorama1.just_fix_windows_console()

    # ok we are gonna have to make a font selection screen so yeah i guess we coudl create an asci art generatore that adjusts to font size

    while True:

        # 1ST FUNCTION
        # sets display of function
        if func_num == 1:

            new_l = [default_l_h_and_min_l_h[0]]
            new_h = [default_l_h_and_min_l_h[1]]

            min_l = default_l_h_and_min_l_h[2]
            min_h = default_l_h_and_min_l_h[3]

            reduce_min_l_attempt = False
            reduce_min_h_attempt = False

            above_max_l_attempt = False
            above_max_h_attempt = False

            box_curs_pos = pos(1, 1)
            str_eg_box = str_eg_box_(new_l[0], new_h[0])
            print(pos(1, 1) + str_eg_box)

            while True:

                event = keyboard1.read_event()

                if event.event_type == keyboard1.KEY_DOWN:
                    if event.name == 'left':
                        if (new_l[0] - 1) > min_l:
                            str_clear_box = str_clear_box_(new_l[0], new_h[0])
                            print(box_curs_pos  + str_clear_box)
                            new_l[0] -= 1
                            str_eg_box = str_eg_box_(new_l[0], new_h[0])
                            print(box_curs_pos  + str_eg_box)
                        else:
                            reduce_min_l_attempt = True

                    elif event.name == 'right':
                        new_l[0] += 1
                        str_eg_box = str_eg_box_(new_l[0], new_h[0])
                        print(box_curs_pos  + str_eg_box)
                    elif  event.name == 'up':
                        if (new_h[0] - 1) > min_h:
                            str_clear_box = str_clear_box_(new_l[0], new_h[0])
                            print(box_curs_pos  + str_clear_box)
                            new_h[0] -= 1
                            str_eg_box = str_eg_box_(new_l[0], new_h[0])
                            print(box_curs_pos  + str_eg_box)
                        else:
                            reduce_min_h_attempt = True
                    elif event.name == 'down':
                        new_h[0] += 1
                        str_eg_box = str_eg_box_(new_l[0], new_h[0])
                        print(box_curs_pos  + str_eg_box)
                    elif event.name == 'enter':
                        str_box = str_eg_box
                        size = globals['size']
                        size['length'] = [new_l[0]]
                        size['height'] = [new_h[0]]
                        return 2
                    elif event.name == '/':
                        os.system('cls')
                        str_eg_box = str_eg_box_(new_l[0], new_h[0])
                        print(pos(1, 1) + str_eg_box)

                    # str_eg_box = str_eg_box_(new_l[0], new_h[0])
                    # print(box_og_curs_pos  + str_eg_box)

                    if reduce_min_l_attempt:
                        print(pos(4, 10) + f"Length can't be lower than {min_l} characters")
                        reduce_min_l_attempt = False
                    elif reduce_min_h_attempt:
                        print(pos(4, 10) + f"Height can't be lower than {min_h} characters")
                        reduce_min_h_attempt = False

        # main menu
        elif func_num == 2:
            lenth = globals['size']['length'][0]
            height = globals['size']['length'][0]
            str_box = str_box_(lenth, height)
            print(str_box)

            handlers = {
            'left': handle_left,
            'right': handle_right,
            'up': handle_up,
            'down': handle_down,
            'enter': handle_enter,
            '/': handle_slash
            }

            while True:
                event = keyboard1.read_event()

                if event.event_type == keyboard1.KEY_DOWN:



        

# lets make the main menu very simaliar to hte shops 
# honestlyu i dont feel like how could i set a max height ok i can do that but then also how
# can i more importtantly set a max height thatmatches teh screen and then also perhaps if i
# do set a screen size preaps what i coudldo is soemhow lke 


# wait i just had a genius idea ok how about wat we do is take the szie variable and store that as a dictionary
# within a list that is like globals or something. idk like have a whole bunch of like here 












default_start_menu = 1

menu_num = default_start_menu

while True:
    menu_num = complete_program_loop(menu_num)
    if menu_num == 'p':
        break
    elif menu_num == '/':
        menu_num -= 1