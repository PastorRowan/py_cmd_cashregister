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
    str_row = str_row_(length, row_char, -2)

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

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Gui creators
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# titles
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def str_one_column_menu_options(length, height, dic_menu_options, start_pos, int_h_chars_between_titles = None):

    int_titles_amount = len(dic_menu_options)
    float_h_chars_between_titles = height / int_titles_amount


    if int_h_chars_between_titles == None:
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



def str_column_titles(box_length, dic_title_plus_frac_apart_out_of_1_whole, box_start_x, title_start_x, title_start_y):

    available_len = box_length + (title_start_x - box_start_x)
    ls_column_titles = []

    for title, percentage in dic_title_plus_frac_apart_out_of_1_whole.items():

        float_x_offset = percentage * available_len

        int_x_offset = int(float_x_offset)

        curr_title_x = title_start_x + int_x_offset

        curr_title_pos = pos(curr_title_x, title_start_y)
        ls_column_titles.append(curr_title_pos)
        ls_column_titles.append(title)

    str_column_titles = ''.join(ls_column_titles)
    return str_column_titles

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



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

def Main_menu_options_to_strs(Main_menu_options):

    ls_option_title_strs = []
    for option_num,option_name in Main_menu_options.items():
        option_str = str(option_num) + ' ' + option_name
        ls_option_title_strs.append(option_str)

    return ls_option_title_strs




def pos (x,y):
    return '\x1b[' + str(y) + ';' + str(x) + 'H'


# ok we are faced with a choice here so now we can either  store the gui updater functions within the block 1 and block 2 info dicitoanries or we can store them seperatelywhcih makes no sense at all
# ok so we are gonna have to add the gui updater functions within the functionsandthen adjust teh like Main menu function to create the text before hand but what if they need to be overwritten??? idk ok i say
# we store the setup function then updater too or we can keep this function then AHAHAH just change the options that we enter based on the other shit ok thatmakesse

Main_menu_options = {1 : '1. Purchase',
                     2 : '2. Refund',
                     3 : '3. Invoice',
                     4 : '4. Stock',
                     5 : '5. Backup'
                    }



def x_and_y_of_selected_option_within_coloumn(column_start_x, column_start_y, total_options, chars_between_titles, selected_option):
    title_start_y = column_start_y + (chars_between_titles * (selected_option - 1))
    return [column_start_x, title_start_y]


if True:
    if True:
        def GUI_item_searcher_block_updater(start_option, box_info, options):

            # start coords
            peri_start_x = box_info['start_and_end_coords']['start_x']
            peri_start_y = box_info['start_and_end_coords']['start_y']

            # end coords
            peri_end_x = box_info['start_and_end_coords']['end_x']
            peri_end_y = box_info['start_and_end_coords']['end_y']

            # size
            length = box_info['size']['length']
            height = box_info['size']['height']

            # column start coords
            column_start_x = peri_start_x + 1
            column_start_y = peri_start_y + 1

            # colunmn end coords
            column_end_x = peri_end_x + 1
            column_end_y = peri_end_y + 1

            # column start pos
            column_start_pos = pos(column_start_x, column_start_y)

            # column end pos
            column_end_pos = pos(column_end_x, column_end_y)


            sel_option = [start_option]


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

            def handle_left(sel_option, total_options):
                pass
            
            def handle_right(sel_option, total_options):
                pass

            handlers = {
            'up': handle_up,
            'down': handle_down,
            'enter': handle_enter,
            'left' : handle_left,
            'right' : handle_right
            }

            total_options = len(options)

            # creates and prints main menu box
            str_options_column_plus_chars_between_titles = str_one_column_menu_options(length, height, options, column_start_pos, 1)

            str_options_column = str_options_column_plus_chars_between_titles[0]
            chars_between_titles = str_options_column_plus_chars_between_titles[1]

            x_and_y_option_return = x_and_y_of_selected_option_within_coloumn(column_start_x, column_start_y, total_options, chars_between_titles, start_option)

            start_x_option = x_and_y_option_return[0]
            start_y_option = x_and_y_option_return[1]

            start_pos_option = pos(start_x_option,start_y_option)
# ok so we need to find the pos of the selected option then bascially take that pos and then replacew that with column start pos then repalce
            print(column_start_pos + str_options_column + start_pos_option + Fore.MAGENTA + options[start_option])

            print(Style.RESET_ALL)


            first_iteration = True
# ok idk what i want to do to contiue to imrpiove this program so now basically it seems like what is happening is that it prints t he same selection again and again which i dont want i would prefer it that it
# prints the GUI once then after that goes through the selection and deselection functions so then what i am gonna do is make it that the printing of the UIs happens once and once only and then also 
# i neede o make sure the deleseciton of a title function happens once after pressing left or right which ioahve a lil funciton for so its fine


            if True:
                while True:
                    print(pos(50,4) + 'currently in block 1')

                    event_ = keyboard1.read_event()
                    print(pos(50,3) + 'event on block 1')

                    sel_option_before_change = sel_option[0]


                    if event_.event_type == keyboard1.KEY_DOWN:
                        handler_function = handlers.get(event_.name)

                        if handler_function:
                            result = handler_function(sel_option, total_options)

                        # graphic updater
                        # only runs if up arrow or down arrow are pressed
                            if ((event_.name == 'up') or (event_.name == 'down')):

                                foreg_colour = Fore.WHITE
                                str_updated_desel_title = Main_menu_main_str_update_sel_title(sel_option_before_change, column_start_x, column_start_y, options, total_options, chars_between_titles, foreg_colour)

                                foreg_colour = Fore.MAGENTA
                                str_updated_sel_title = Main_menu_main_str_update_sel_title(sel_option[0], column_start_x, column_start_y, options, total_options, chars_between_titles, foreg_colour)

                                print(str_updated_desel_title + str_updated_sel_title)
                                print(Style.RESET_ALL)

                            elif event_.name == 'left':
                                print(pos(50,5) + ' left was pressed in block 1')
                                foreg_colour = Fore.WHITE
                                str_updated_desel_title = Main_menu_main_str_update_sel_title(sel_option_before_change, column_start_x, column_start_y, options, total_options, chars_between_titles, foreg_colour)
                                print(str_updated_desel_title)
                                return ('left', sel_option_before_change)
                    
                            elif (event_.name == 'right'):
                                print(pos(50,5) + 'right was pressed in block 1')
                                foreg_colour = Fore.WHITE
                                str_updated_desel_title = Main_menu_main_str_update_sel_title(sel_option_before_change, column_start_x, column_start_y, options, total_options, chars_between_titles, foreg_colour)
                                print(str_updated_desel_title)
                                return ('right', sel_option_before_change)


                            elif (event_.name == 'enter'): # we gotta create an iterable test solutio nfor this yeah that makes sens 
                        
                                if first_iteration:
                                    first_iteration = False
                                    break
                                # 1. purchase
                                elif sel_option[0] == 1:
                                    print
                                    #Main_menu_main_purchase()
                                # 2. refund. purchase
                                elif sel_option[0] == 2:
                                    print
                                #Main_menu_main_refund()
                                # 3. invoice. purchase
                                elif sel_option[0] == 3:
                                    print
                                #Main_menu_main_invoice()
                                # 4. stock change
                                elif sel_option[0] == 4:
                                    print
                                #Main_menu_main_stock_change()
                                # 5. backup
                                elif sel_option[0] == 5:
                                    print
                                #Main_menu_menu_backup


def GUI_checkout_block_updater(start_option, box_info, options):
    # start coords
    peri_start_x = box_info['start_and_end_coords']['start_x']
    peri_start_y = box_info['start_and_end_coords']['start_y']

    # end coords
    peri_end_x = box_info['start_and_end_coords']['end_x']
    peri_end_y = box_info['start_and_end_coords']['end_y']

    # size
    length = box_info['size']['length']
    height = box_info['size']['height']

    # column start coords
    column_start_x = peri_start_x + 1
    column_start_y = peri_start_y + 1

    # colunmn end coords
    column_end_x = peri_end_x + 1
    column_end_y = peri_end_y + 1

    # column start pos
    column_start_pos = pos(column_start_x, column_start_y)

    # column end pos
    column_end_pos = pos(column_end_x, column_end_y)


    sel_option = [start_option]


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
    
    def handle_left(sel_option, total_options):
        pass
            
    def handle_right(sel_option, total_options):
        pass

    handlers = {
              'up': handle_up,
              'down': handle_down,
              'enter': handle_enter,
              'left' : handle_left,
              'right' : handle_right
              }


    total_options = len(options)

    # creates and prints main menu box
    str_options_column_plus_chars_between_titles = str_one_column_menu_options(length, height, options, column_start_pos, 1)

    str_options_column = str_options_column_plus_chars_between_titles[0]
    chars_between_titles = str_options_column_plus_chars_between_titles[1]

    x_and_y_option_return = x_and_y_of_selected_option_within_coloumn(column_start_x, column_start_y, total_options, chars_between_titles, start_option)

    start_x_option = x_and_y_option_return[0]
    start_y_option = x_and_y_option_return[1]

    start_pos_option = pos(start_x_option,start_y_option)
    print(column_start_pos + str_options_column + start_pos_option + Fore.MAGENTA + options[start_option])

    print(Style.RESET_ALL)


    first_iteration = True


    if True:
        while True:

            print(pos(50,4) + 'currently in block 2')

            event_ = keyboard1.read_event()
            print(pos(50,3) + 'event on block 2')

            sel_option_before_change = sel_option[0]

            if event_.event_type == keyboard1.KEY_DOWN:
                handler_function = handlers.get(event_.name)

                if handler_function:
                    result = handler_function(sel_option, total_options)
                        # graphic updater
                        # only runs if up arrow or down arrow are pressed
                    if ((event_.name == 'up') or (event_.name == 'down')):

                        foreg_colour = Fore.WHITE
                        str_updated_desel_title = Main_menu_main_str_update_sel_title(sel_option_before_change, column_start_x, column_start_y, options, total_options, chars_between_titles, foreg_colour)

                        foreg_colour = Fore.MAGENTA
                        str_updated_sel_title = Main_menu_main_str_update_sel_title(sel_option[0], column_start_x, column_start_y, options, total_options, chars_between_titles, foreg_colour)

                        print(str_updated_desel_title + str_updated_sel_title)
                        print(Style.RESET_ALL)

                    elif event_.name == 'left':
                        foreg_colour = Fore.WHITE
                        str_updated_desel_title = Main_menu_main_str_update_sel_title(sel_option_before_change, column_start_x, column_start_y, options, total_options, chars_between_titles, foreg_colour)
                        print(str_updated_desel_title)
                        return ('left', sel_option_before_change)
                    
                    elif (event_.name == 'right'):
                        foreg_colour = Fore.WHITE
                        str_updated_desel_title = Main_menu_main_str_update_sel_title(sel_option_before_change, column_start_x, column_start_y, options, total_options, chars_between_titles, foreg_colour)
                        print(str_updated_desel_title)
                        return ('right', sel_option_before_change)


                    elif (event_.name == 'enter'): # we gotta create an iterable test solutio nfor this yeah that makes sens 
                        
                        if first_iteration:
                            first_iteration = False
                            break
                        # 1. purchase
                        elif sel_option[0] == 1:
                            print
                            #Main_menu_main_purchase()
                        # 2. refund. purchase
                        elif sel_option[0] == 2:
                            print
                            #Main_menu_main_refund()
                        # 3. invoice. purchase
                        elif sel_option[0] == 3:
                            print
                            #Main_menu_main_invoice()
                        # 4. stock change
                        elif sel_option[0] == 4:
                            print
                            #Main_menu_main_stock_change()
                        # 5. backup
                        elif sel_option[0] == 5:
                            print
                            #Main_menu_menu_backup













colorama1.just_fix_windows_console()
os.system('cls')

def str_perfect_box_(length, height, ls_row_column_chars, start_pos):

    row_char = ls_row_column_chars[0]
    column_char = ls_row_column_chars[1]

    # creates top and bot row
    str_row = str_row_(length, row_char, 0)

    # creates left and right column
    str_column = str_column_(height, column_char, 0)

    str_empt_box = start_pos + str_row + start_pos + str_column + str_row + up(height) + str_column
    # + back(1)

    return str_empt_box


length = 6
height = 4
ls_row_column_chars = ['_', '|']
start_pos = pos(1,1)
str_perfect_box = str_perfect_box_(length, height, ls_row_column_chars, start_pos)






















def dic_column_title_coords_and_percentages(box_length, dic_title_plus_frac_apart_out_of_1_whole, box_start_x, title_start_x, title_start_y):

    available_len = box_length + (title_start_x - box_start_x)

    
    dic_column_title_coords_and_percentages = {}
    ls_column_titles = []

    for title, percentage in dic_title_plus_frac_apart_out_of_1_whole.items():

        float_x_offset = percentage * available_len

        int_x_offset = int(float_x_offset)

        curr_title_x = title_start_x + int_x_offset
        
        curr_title_pos = pos(curr_title_x, title_start_y)
        ls_column_titles.append(curr_title_pos)
        ls_column_titles.append(title)

        str_column_title = ''.join(ls_column_titles)

        dic_column_title_coords_and_percentages[title] = {'str' : str_column_title, 'coords' : [curr_title_x, title_start_y], 'percentage' : percentage}
    

    return dic_column_title_coords_and_percentages










boxes_start_and_end_percentages = {'block_1' : {'percentage_start_x' : 0, 'percentage_start_y' : 0, 'percentage_end_x' : 0.5, 'percentage_end_y' : 0.5},
                              
                             'block_2' : {'percentage_start_x' : 0.5, 'percentage_start_y' : 0, 'percentage_end_x' : 1, 'percentage_end_y' : 0.5}
                             }




def block_coords(menu_length, menu_height, boxes_start_and_end_percentages, menu_start_x, menu_start_y, menu_end_x, menu_end_y):


    boxes_start_and_end_coords = {}

    for box in boxes_start_and_end_percentages:
        curr_box = boxes_start_and_end_percentages[box]
        curr_box_start_and_end_coords = {}

        # start x
        percentage_start_x = curr_box['percentage_start_x']
        float_x_offset = percentage_start_x * menu_length
        int_x_offset = int(float_x_offset)
        curr_box_start_x = menu_start_x + int_x_offset
        curr_box_start_and_end_coords['start_x'] = curr_box_start_x

        # start y
        percentage_start_y = curr_box['percentage_start_y']
        float_start_y_offset = percentage_start_y * menu_height
        int_start_y_offset = int(float_start_y_offset)
        curr_box_start_y = menu_start_y + int_start_y_offset
        curr_box_start_and_end_coords['start_y'] = curr_box_start_y

        # end x
        percentage_end_x = curr_box['percentage_end_x']
        float_end_x_offset = percentage_end_x * menu_length
        int_end_x_offset = int(float_end_x_offset)
        curr_box_end_x = menu_start_x + int_end_x_offset
        curr_box_start_and_end_coords['end_x'] = curr_box_end_x + 1

        # end y
        percentage_end_y = curr_box['percentage_end_y']
        float_end_y_offset = percentage_end_y * menu_height
        int_end_y_offset = int(float_end_y_offset)
        curr_title_end_y = menu_start_y + int_end_y_offset
        curr_box_start_and_end_coords['end_y'] = curr_title_end_y


        boxes_start_and_end_coords[box] = curr_box_start_and_end_coords


    return boxes_start_and_end_coords


def boxes_length_and_height(boxes_start_and_end_coords):




    boxes_length_and_height = {}
    for box in boxes_start_and_end_coords:
        curr_box = boxes_start_and_end_coords[box]

        box_length_and_height = {}

        # l
        start_x = curr_box['start_x']
        end_x = curr_box['end_x']
        box_length = end_x - start_x
        box_length_and_height['length'] = box_length

        # w
        start_y = curr_box['start_y']
        end_y = curr_box['end_y']
        box_height = end_y - start_y
        box_length_and_height['height'] = box_height

        boxes_length_and_height[box] = box_length_and_height

    return boxes_length_and_height



boxes_start_and_end_coords___ = {'block_1': {'start_x': 2, 'start_y': 2, 'end_x': 27, 'end_y': 14}, 
                                 'block_2': {'start_x': 27, 'start_y': 2, 'end_x': 52, 'end_y': 14}
                                 }


def boxes_start_and_end_poses_(boxes_start_and_end_coords):

    boxes_start_and_end_poses = {}
    for curr_box in boxes_start_and_end_coords:
        curr_box_start_and_end_coords = boxes_start_and_end_coords[curr_box]

        # start_pos
        curr_box_start_pos = pos(curr_box_start_and_end_coords['start_x'],curr_box_start_and_end_coords['start_y'])
        # end_pos
        curr_box_end_pos = pos(curr_box_start_and_end_coords['end_x'],curr_box_start_and_end_coords['end_y'])


        boxes_start_and_end_poses[curr_box] = {'start_pos' : curr_box_start_pos, 'end_pos' : curr_box_end_pos}

    return boxes_start_and_end_poses
    









def empt_block_info_into_full_block(boxes_info, boxes_start_and_end_percentages, boxes_start_and_end_coords, boxes_start_and_end_poses, boxes_size):


    for box in boxes_info:

        curr_box = boxes_info[box]
        curr_box['boxes_start_and_end_percentages'] = boxes_start_and_end_percentages[box]
        curr_box['start_and_end_coords'] = boxes_start_and_end_coords[box]
        curr_box['start_and_end_poses'] = boxes_start_and_end_poses[box]
        curr_box['size'] = boxes_size[box]

    return boxes_info

boxes_info_empt = {'block_1' : {'boxes_start_and_end_percentages' : {}, 'start_and_end_coords' : {}, 'start_and_end_poses' : {}, 'size' : {} },
              
              'block_2' : { 'boxes_start_and_end_percentages' : {}, 'start_and_end_coords' : {}, 'start_and_end_poses' : {}, 'size' : {} }
              }

boxes_start_and_end_percentages = {'block_1' : {'percentage_start_x' : 0, 'percentage_start_y' : 0, 'percentage_end_x' : 0.5, 'percentage_end_y' : 0.5},
                              
                             'block_2' : {'percentage_start_x' : 0.5, 'percentage_start_y' : 0, 'percentage_end_x' : 1, 'percentage_end_y' : 0.5}
                             }




def create_menu_with_main_box_and_subbox(menu_block_info, sub_boxes_info):

    main_length = menu_block_info['size']['length']
    main_height = menu_block_info['size']['height']

    ls_main_row_column_chars = ['_', '|']
    main_start_pos = menu_block_info['start_and_end_poses']['start_pos']

    str_main_box = main_same_top_and_bot_empty_str_box(main_length, main_height, ls_main_row_column_chars, main_start_pos)

    ls_str_sub_boxes = []
    for sub_box in sub_boxes_info:
        sub_box_info = sub_boxes_info[sub_box]
        sub_length = sub_box_info['size']['length']
        sub_height = sub_box_info['size']['height']
        ls_sub_row_column_chars = ['_', '|']
        sub_start_pos = sub_box_info['start_and_end_poses']['start_pos']

        str_sub_box = main_same_top_and_bot_empty_str_box(sub_length, sub_height, ls_sub_row_column_chars, sub_start_pos)

        ls_str_sub_boxes.append(str_sub_box)

    str_sub_boxes = ''.join(ls_str_sub_boxes)

    os.system('cls')
    colorama1.just_fix_windows_console()

    print(str_main_box + str_sub_boxes)




def option_select(start_option):
    while True:
        print



GUI_functions = {'block_1' : {option_select},
                 'block_2' : {}
                 
                 
                 }


def gui_manager(GUI_functions):
    print















peri_menu_length = 50
peri_menu_height = 35
peri_start_x = 1
peri_start_y = 1
peri_menu_end_x = 52
peri_menu_end_y = 27


menu_block_info = {'start_and_end_coords' : {'start_x': 1, 'start_y': 1, 'end_x' : 51, 'end_y': 26},
                   'start_and_end_poses' : {'start_pos' : pos(1,1), 'end_pos' : pos(51,26)}, 
                   'size' : {'length' : peri_menu_length, 'height' : peri_menu_height}}

boxes_start_and_end_percentages = {'block_1' : {'percentage_start_x' : 0, 'percentage_start_y' : 0, 'percentage_end_x' : 0.5, 'percentage_end_y' : 0.5},
                              
                             'block_2' : {'percentage_start_x' : 0.5, 'percentage_start_y' : 0, 'percentage_end_x' : 1, 'percentage_end_y' : 0.5}
                             }


boxes_info_empt = {'block_1' : {'boxes_start_and_end_percentages' : {}, 'start_and_end_coords' : {}, 'start_and_end_poses' : {}, 'size' : {} },
              
              'block_2' : { 'boxes_start_and_end_percentages' : {}, 'start_and_end_coords' : {}, 'start_and_end_poses' : {}, 'size' : {} }
              }


sub_boxes_start_and_end_coords = block_coords(peri_menu_length, peri_menu_height, boxes_start_and_end_percentages, peri_start_x, peri_start_y, peri_menu_end_x, peri_menu_end_y)

sub_boxes_start_and_end_poses = boxes_start_and_end_poses_(sub_boxes_start_and_end_coords)

sub_boxes_size = boxes_length_and_height(sub_boxes_start_and_end_coords)



sub_boxes_info = empt_block_info_into_full_block(boxes_info_empt, boxes_start_and_end_percentages, sub_boxes_start_and_end_coords, sub_boxes_start_and_end_poses, sub_boxes_size)




create_menu_with_main_box_and_subbox(menu_block_info, sub_boxes_info)

item_searcher_block_info = sub_boxes_info['block_1']

checkout_block_info = sub_boxes_info['block_2']



item_searcher_options = {1 : 'GTX 1050',
           2 : 'RX 480',
           3 : 'RX 580',
           4 : 'GTX 1060 3gb',
          }

carry_over_option = []




GUI_loops = {

             # block 1
             1 : GUI_item_searcher_block_updater,

             # block 2
             2 : GUI_checkout_block_updater


             }


blocks = {
          1 : 'block_1',
          2 : 'block_2'
          }

blocks__ = {
          1 : {'block_1' : 'block ionof'},
          2 : {'block_2' : 'block_info'}
          }

# or i coudl just replace block 1 and bock 2 wih integers istead repsetning block 1 and block 2 i think lowkey maybe a future update coukd just do that

# start block \/\/\/\/\/


# ok we have a tiny problem that is that we need to basically be able to know like are we on block 1 or block 2 so basically we gotta create some kind of like block 1 to block 2 ditoanry taht basicallyidentifeis
# ok are we on block 1 or block 2. i feel like that yeah but i am quite tired perahps we shoudl taea rbeak and watch someyoutube tghen get back to coding or we can work on the maths paper 2 now we dont have to
# worry about the nbts yeah. i feel like that sounds like a good idea. yeah nice ok lets start with defining our blocks GUI loops then basically creating a function that takes the GUI loops then. nah just store 
# the gui loops in the dictioanries then i coudl create a function that lists all the blocks and there block numbers and then there corresponding gui loop so then i could go like block 1 = ok there are millions of
# ways to oranise it lets jsut make it homogenous thoghout so ltes take this and shove it into the sub_box_info funcs then create a function that just takes out the gui loops nah but hten i might as well just
# definte them seperaetley like bro you get what i am saying mmm myeah i get that but like yeah i have no idea. hmmmm. bruh thes poeple must also people say random things there isnt aynthing we can do about it
# same iwth poep;le talkigna about us. yeah
# ok so then what we are gonna do is make the block info seperate then. nmah lets put the gui loops
# ok final decison we are gonna take hte gui looops and pout them into their correwspdonig blks then create a for loop that creatse antoher dciotranr that ltierally ust takes the block names and then creates value pairs
# lke block 1 = this gui loop and etc then after that i am gonna have another function that is gonna assign the gui loops numbers based on there position relative to the 


current_sel_block_info = item_searcher_block_info

# start block
current_sel_block = [1]

# first selected in starting block
last_option = 1

while True:

    GUI_loop = GUI_loops.get(current_sel_block[0])

    if GUI_loop:
        GUI_return = GUI_loop(last_option, current_sel_block_info, item_searcher_options)

        last_key_stroke = GUI_return[0]
        last_option = GUI_return[1]

        if ((last_key_stroke == 'left') or (last_key_stroke == 'right')) and (current_sel_block[0] == 1):
            current_sel_block[0] += 1
            new_sel_current_block_str_id = blocks.get(current_sel_block[0])
            current_sel_block_info = sub_boxes_info[new_sel_current_block_str_id]

        elif ((last_key_stroke == 'left') or (last_key_stroke == 'right')) and (current_sel_block[0] == 2):
            current_sel_block[0] -= 1

            new_sel_current_block_str_id = blocks.get(current_sel_block[0])
            current_sel_block_info = sub_boxes_info[new_sel_current_block_str_id]


    else:
        break