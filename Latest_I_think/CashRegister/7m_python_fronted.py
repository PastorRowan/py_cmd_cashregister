# IMPORT MODULES
#
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import colorama1
import os
import math
import mmap
import keyboard1 
from colorama1 import Fore, Back, Style

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# DISPLAY
#
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Box Creator
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
    str_row = str_row_(length, row_char, 1)


    #str_row = str_row_(length, row_char, 2)

    # creates left and right column
    str_column = str_column_(height, column_char, -1)

    str_empt_box = start_pos + back(1) + str_row + row_char + start_pos + str_column + str_row + up(height + 2) + str_column
    # + back(1)

    return str_empt_box

# full box creators
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

def str_eg_box_(int_length, int_height):

    str_welcome = f'Welcome!!!press the arrow keys to adjust the screen size (measured in characters) the default length is {str(int_length)} the default height is {str(int_height)}'

    int_welcome_num_chars = len(str_welcome)
    float_welcome_chars_into_length = int_welcome_num_chars / int_length
    int_full_rows = int(float_welcome_chars_into_length)
    ls_top_welcome_section = []

    int_total_welcome_rows = math.ceil(float_welcome_chars_into_length)

    curr_char_index = [0]
    total_chars = len(str_welcome)


    if int_full_rows > 0:
        for _ in range(int_full_rows):
            ls_top_welcome_row = ['|']
            for _ in range(int_length):
                ls_top_welcome_row.append(str_welcome[curr_char_index[0]])
                curr_char_index[0] += 1
            ls_top_welcome_row.append('|')
            ls_top_welcome_row.append('\n')

            ls_top_welcome_section += ls_top_welcome_row


    remainder_chars = total_chars - curr_char_index[0]
    num_spaces = int_length - remainder_chars
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
    for _ in range(int_length):
        constructor_mid_row.append(' ')
    constructor_mid_row.append('|')
    constructor_mid_row.append('\n')
    mid_row = ''.join(constructor_mid_row)

    # creates middle section
    ls_mid_rows = [str_top_welcome]
    for _ in range(int_height - 2 - int_total_welcome_rows):
        ls_mid_rows.append(mid_row)

    # creates top row
    ls_top_row = []
    for _ in range(int_length + 2):
        ls_top_row.append('_')
    ls_top_row.append('\n')

    # creates bot row
    ls_bot_row = ['|']
    for _ in range(int_length):
        ls_bot_row.append('_')
    ls_bot_row.append('|')

    ls_eg_box = ls_top_row + ls_mid_rows + ls_bot_row
    str_eg_box = ''.join(ls_eg_box)

    return str_eg_box

def str_clear_box_(int_length, int_height):
    ls_constr_row_clear = [' ']

    for _ in range(int_length):
        ls_constr_row_clear.append(' ')

    ls_constr_row_clear.append(' ')
    ls_constr_row_clear.append('\n')
    row_clear = ''.join(ls_constr_row_clear)

    ls_constr_clear_box = []
    for _ in range(int_height):
        ls_constr_clear_box.append(row_clear)

    str_clear_box = ''.join(ls_constr_clear_box)

    return str_clear_box

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Gui creators
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def str_one_column_menu_options(length, height, dic_menu_options, start_pos):

    int_titles_amount = len(dic_menu_options)
    float_h_chars_between_titles = height / int_titles_amount
    int_h_chars_between_titles = int(float_h_chars_between_titles)

    ls_one_column_menu_options = [start_pos]
    for title_num in dic_menu_options:
        str_title = dic_menu_options[title_num]
        str_title_chars = len(str_title)
        ls_one_column_menu_options.append(str_title)
        ls_one_column_menu_options.append(back(str_title_chars))
        if title_num != (int_titles_amount):
            ls_one_column_menu_options.append(down(int_h_chars_between_titles))

    str_one_column_menu_options_ = ''.join(ls_one_column_menu_options)
    return [str_one_column_menu_options_, int_h_chars_between_titles]
    



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Gui Manager
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# i want this fucniton to also handle selection and unselection or make this the select function then another the unselect function i guess could be a cool idea. also antoehr cool idea
# nah we are just gonan run 2 of the same fucntio nwtaht will reutnr different srings then bascakly all we are gonna do is shove them all into one big print statement then yeah print that
def Main_menu_main_str_update_sel_title(sel_option, column_start_x, column_start_y, Main_menu_options, total_titles, chars_between_titles, foregr_colour):

    str_new_sel_option = Main_menu_options[sel_option]

    new_sel_option_x = column_start_x
    new_sel_option_y = (column_start_y) + ((sel_option - 1) * chars_between_titles)
    new_pos = pos(new_sel_option_x, new_sel_option_y)

    str_updated_title = new_pos + foregr_colour + str_new_sel_option

    return str_updated_title
    #print(new_pos + foregr_colour + str_new_sel_option)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# COLORAMA SETUP
#
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def pos (x,y):
    return '\x1b[' + str(y) + ';' + str(x) + 'H'

up = colorama1.Cursor.UP
down = colorama1.Cursor.DOWN
forward = colorama1.Cursor.FORWARD
back = colorama1.Cursor.BACK

FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
STYLES = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]

# saved code:
# colorama1.just_fix_windows_console()


# LOADING SETTINGS
#
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def load_default_box_dimension():
    with open('settings/default_box_dimensions.txt', 'r+') as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mmapped_f:
            strbyt_dimensions_f_content = mmapped_f.read()
            strbyt_dimensions = strbyt_dimensions_f_content.split(b'\n')

            strbyt_l_index = strbyt_dimensions[0].strip(b'\r')     # b'l 50'
            strbyt_h_index = strbyt_dimensions[1].strip(b'\r')     # b'h 25'
            strbyt_min_l_index = strbyt_dimensions[2].strip(b'\r') # b'minl 50'
            strbyt_min_h_index = strbyt_dimensions[3].strip(b'\r') # b'minh 50'

            print(strbyt_l_index)
            print(strbyt_h_index)
            print(strbyt_min_l_index)
            print(strbyt_min_h_index)

            strbyt_l_index_list = strbyt_l_index.split(b'|')
            strbyt_h_index_list = strbyt_h_index.split(b'|')
            strbyt_min_l_index_list = strbyt_min_l_index.split(b'|')
            strbyt_min_h_index_list = strbyt_min_h_index.split(b'|')

            strbyt_l = strbyt_l_index_list[1]
            strbyt_h = strbyt_h_index_list[1]
            strbyt_min_l = strbyt_min_l_index_list[1]
            strbyt_min_h = strbyt_min_h_index_list[1]

            print(strbyt_l)
            print(strbyt_h)
            print(strbyt_min_l)
            print(strbyt_min_h)

            str_l = strbyt_l.decode('utf-8')
            str_h = strbyt_h.decode('utf-8')
            str_min_l = strbyt_min_l.decode('utf-8')
            str_min_h = strbyt_min_h.decode('utf-8')

            int_l = int(str_l)
            int_h = int(str_h)
            int_min_l = int(str_min_l)
            int_min_h = int(str_min_h)

            size = {'l' : [int_l], 'h' : [int_h], 'min_l' : [int_min_l], 'min_h' : [int_min_h]}

            return size

def Main_menu_options_to_strs(Main_menu_options):

    ls_option_title_strs = []
    for option_num,option_name in Main_menu_options.items():
        option_str = str(option_num) + ' ' + option_name
        ls_option_title_strs.append(option_str)

    return ls_option_title_strs


# MENU LOOP
#
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def complete_program_loop(Main_menu_options, menu_num, size):

    new_l = size['l']
    min_l = size['min_l']
    new_h = size['h']
    min_h = size['min_h']

    while True:


# MENU 1 - id='display_menu'
# sets display of function     
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        if menu_num == 1:

            def handle_left(new_l, min_l, new_h, min_h, box_curs_pos):
                if (new_l[0] - 1) > min_l[0]:
                    str_clear_box = str_clear_box_(new_l[0], new_h[0])
                    print(box_curs_pos  + str_clear_box)
                    new_l[0] -= 1
                    str_eg_box = str_eg_box_(new_l[0], new_h[0])
                    print(box_curs_pos  + str_eg_box)
                    print(pos(4, 10) + f"Length can't be lower than {min_l[0]} characters")
                    return {'l_or_h_change' : 'l','reduce_min_l_attempt' : False, 'menu' : 'display_menu'}
                else:
                    return {'l_or_h_change' : 'l','reduce_min_l_attempt' : True, 'menu' : 'display_menu'}

            def handle_right(new_l, min_l, new_h, min_h, box_curs_pos):
                new_l[0] += 1
                str_eg_box = str_eg_box_(new_l[0], new_h[0])
                print(box_curs_pos  + str_eg_box)
                return {'l_or_h_change' : 'l','reduce_min_l_attempt' : False, 'menu' : 'display_menu'}

            def handle_up(new_l, min_l, new_h, min_h, box_curs_pos):
                if (new_h[0] - 1) > min_h[0]:
                    str_clear_box = str_clear_box_(new_l[0], new_h[0])
                    print(box_curs_pos  + str_clear_box)
                    new_h[0] -= 1
                    str_eg_box = str_eg_box_(new_l[0], new_h[0])
                    print(box_curs_pos  + str_eg_box)
                    print(pos(4, 10) + f"Height can't be lower than {min_h[0]} characters")
                    return {'l_or_h_change' : 'h','reduce_min_h_attempt' : False, 'menu' : 'display_menu'}
                else:
                    return {'l_or_h_change' : 'h','reduce_min_h_attempt' : True, 'menu' : 'display_menu'}

            def handle_down(new_l, min_l, new_h, min_h, box_curs_pos):
                new_h[0] += 1
                str_eg_box = str_eg_box_(new_l[0], new_h[0])
                print(box_curs_pos  + str_eg_box)
                return {'l_or_h_change' : 'h', 'above_max_h_attempt' : False, 'menu' : 'display_menu'}

            def handle_enter(new_l, min_l, new_h, min_h, box_curs_pos):
                return {'menu' : 'main_menu'}

            def handle_slash(new_l, min_l, new_h, min_h, box_curs_pos):
                os.system('cls')
                str_eg_box = str_eg_box_(new_l[0], new_h[0])
                print(pos(1, 1) + str_eg_box)
                return {'menu' : 'display_menu'}

            handlers = {
            'left': handle_left,
            'right': handle_right,
            'up': handle_up,
            'down': handle_down,
            'enter': handle_enter,
            '/': handle_slash
            }

            box_curs_pos = pos(1, 1)
            str_eg_box = str_eg_box_(new_l[0], new_h[0])
            print(pos(1, 1) + str_eg_box)

            while True: # 6m_python_Frotntend_new_hope lol ok our new aneis gonna be this ok so now next i guess could be like a ok in the new iteratio of ou code i say what we are gonna do is take these if statments
                # and somehow break them up into smaller pieces yeah thats a good idea

                event = keyboard1.read_event()

                if event.event_type == keyboard1.KEY_DOWN:
                    handler_function = handlers.get(event.name)

                    if handler_function:
                        result = handler_function(new_l, min_l, new_h, min_h, box_curs_pos)

                        if result['menu'] == 'display_menu':

# there is definitely a better way to organise this code it looks so fucking messy and i dont like this i think im gonna think righ tnow of better ways to organiseths but also i would liek to know what are industyr
# stanadard ways of organising this type of code because holey shit this shit is confusing and i dont like this ok so lets serach what is indisuyr standard or just ask chat gpt what are indsirry standards andthen
# ask chat gpt to apply those indstry standards to my code because i am not enjoying reading this. at all. this shit looks shit i mean like something i coulddo is like make the ocntrol flow a bit simpler and dont use nested
# if statemtnes so basicallylike going like ok if menu is display menu then make menu variable = to menu i could even use another dicitoary that searches the avlue of the menu and goes ok if ths is make func number
# ok lets think aboutit like this if our code is ALWAYS GONNA HAVE THE EXACT SAME 5 ARGS ALWAYS or so whatevre then we use eopxlicity yped args if however our funitn can take in an arbritrary amoutn of args then
# consider using kwargs or args it really dpeends on the functions purpose and needs and future palnsof the proram 

                            if result['l_or_h_change'] == 'l':
                                if 'reduce_min_l_attempt' in result:
                                    if result['reduce_min_l_attempt']:
                                      print(pos(4, 10) + f"Length can't be lower than {min_l} characters")
                                elif 'above_max_l_attempt' in result:
                                    if result['above_max_l_attempt']:
                                        print(pos(4, 10) + f"Length can't be lower than {min_l} characters")


                            elif result['l_or_h_change'] == 'h':
                                if 'reduce_min_h_attempt' in result:
                                    if result['reduce_min_h_attempt']:
                                        print(pos(4, 10) + f"Height can't be lower than {min_h} characters")
                                elif 'above_max_h_attempt' in result:
                                    if result['above_max_h_attempt']:
                                        print(pos(4, 10) + f"Height can't be lower than {min_h} characters")

                        elif result['menu'] == 'main_menu':
                            str_clear_box = str_clear_box_(new_l[0], new_h[0])
                            print(box_curs_pos + str_clear_box)
                            size['length'] = new_l
                            size['height'] = new_h
                            return 2

# ok then do we return it as a tuplei mean we oculdalso do thethingwhere we could do somethingliekabsically a global vaibletaht is a glboal varileon the outside that

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# MENU 2 - id='main_menu'
# main menu that goes into submenus
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#{'navigation_to_non_existent' : True} seems not necesary


        elif menu_num == 2:
            #main_main_menu()

            length = size['length']
            height = size['height']

            sel_option = [1]
            total_options = len(menus)


            def handle_up(sel_option, total_options):
                sel_option[0] -= 1
                if sel_option[0] == 0:
                    sel_option[0] = total_options

            def handle_down(sel_option, total_options):
                sel_option[0] += 1
                if sel_option[0] == (total_options + 1):
                    sel_option[0] = 1

            def handle_enter(sel_option, total_options):
                return sel_option

            handlers = {
            'up': handle_up,
            'down': handle_down,
            'enter': handle_enter,
            }


            # main menu options
            Main_menu_options = {1 : '1. Purchase',
                     2 : '2. Refund',
                     3 : '3. Invoice',
                     4 : '4. Stock',
                     5 : '5. Backup'
                    }

            total_options = len(Main_menu_options)

            # row + column chars:
            ls_row_column_chars = ['_', '|']

            # menu box start pos
            box_peri_x_origin = 1
            box_peri_y_origin = 1


            box_peri_start_pos = pos(box_peri_x_origin,box_peri_y_origin)

            # options column start pos
            options_column_x_origin = box_peri_x_origin + 3
            options_column_y_origin = box_peri_y_origin + 3

            # options column start pos
            options_column_start_pos = pos(options_column_x_origin,options_column_y_origin)

            # creates and prints main menu box

            print(length[0])
            print(height[0])
            str_empt_main_menu_box = main_same_top_and_bot_empty_str_box(length[0], height[0], ls_row_column_chars, box_peri_start_pos)
            str_options_column_plus_chars_between_titles = str_one_column_menu_options(length[0], height[0] - 2, Main_menu_options, options_column_start_pos)

            str_options_column = str_options_column_plus_chars_between_titles[0]
            chars_between_titles = str_options_column_plus_chars_between_titles[1]

            print(str_empt_main_menu_box + options_column_start_pos + str_options_column + options_column_start_pos + Fore.MAGENTA + Main_menu_options[1])

            print(Style.RESET_ALL)


            first_iteration = True



            for _ in range(2):
                while True:

                    event_ = keyboard1.read_event()

                    sel_option_before_change = sel_option[0]

                    if event_.event_type == keyboard1.KEY_DOWN:
                        handler_function = handlers.get(event_.name)

                        if handler_function:
                            result = handler_function(sel_option, total_options)

                    # graphic updater
                    # only runs if up arrow or down arrow are pressed
                    if (event_.name == 'up') or (event_.name == 'down'):

                        foreg_colour = Fore.WHITE
                        str_updated_desel_title = Main_menu_main_str_update_sel_title(sel_option_before_change, options_column_x_origin, options_column_y_origin, Main_menu_options, total_options, chars_between_titles, foreg_colour)

                        foreg_colour = Fore.MAGENTA
                        str_updated_sel_title = Main_menu_main_str_update_sel_title(sel_option[0], options_column_x_origin, options_column_y_origin, Main_menu_options, total_options, chars_between_titles, foreg_colour)

                        print(str_updated_desel_title + str_updated_sel_title)
                        print(Style.RESET_ALL)


                    elif event_.name == 'enter': # we gotta create an iterable test solutio nfor this yeah that makes sens 
                        
                        if first_iteration:
                            first_iteration = False
                            break
                        # 1. purchase
                        elif sel_option[0] == 1:
                            print(pos(20,20) + 'You pressed enter')
                            #Main_menu_main_purchase()
                        # 2. refund. purchase
                        elif sel_option[0] == 2:
                            print(pos(20,20) + 'You pressed enter')
                            #Main_menu_main_refund()
                       # 3. invoice. purchase
                        elif sel_option[0] == 3:
                            print(pos(20,20) + 'You pressed enter')
                            #Main_menu_main_invoice()
                        # 4. stock change
                        elif sel_option[0] == 4:
                            print(pos(20,20) + 'You pressed enter')
                            #Main_menu_main_stock_change()
                        # 5. backup
                        elif sel_option[0] == 5:
                            print(pos(20,20) + 'You pressed enter')
                            #Main_menu_menu_backup




#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






# FRONTEND LOOP
#
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


default_start_menu = 1

menus = {'display_menu' : 1,
         'main_menu' : 2,
         }

size = load_default_box_dimension()

default_start_menu = 1

menu_num = default_start_menu


Main_menu_options = {1 : '1. Purchase',
                     2 : '2. Refund',
                     3 : '3. Invoice',
                     4 : '4. Stock',
                     5 : '5. Backup'
                     }

os.system('cls')
colorama1.just_fix_windows_console()

while True:
    menu_num = complete_program_loop(Main_menu_options, menu_num, size)
    if menu_num == 'p':
        break
    elif menu_num == '/':
        menu_num -= 1


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------