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

# temp repalement probs will cause problems

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

def str_clear_box______(int_length, int_height, start_x, start_y):
    ls_constr_row_clear = []

    # single row
    for _ in range(int_length):
        ls_constr_row_clear.append(' ')
    ls_constr_row_clear.append(' ')
    row_clear = ''.join(ls_constr_row_clear)

    # box
    ls_constr_clear_box = []
    for index in range(int_height):
        ls_constr_clear_box.append(pos(start_x, start_y + index))
        ls_constr_clear_box.append(row_clear)

    str_clear_box = ''.join(ls_constr_clear_box)

    return str_clear_box


def str_perfect_clear_box(int_length, int_height, start_x, start_y):

    # row
    str_row = str_row_(int_length, ' ', 0)

    ls_constr_full_box = []
    for index in range(int_height):
        if index != int_height - 1:
            ls_constr_full_box.append(pos(start_x, start_y + index))
            ls_constr_full_box.append(str_row)

    str_full_box =''.join(ls_constr_full_box)
    # + back(1)

    return str_full_box




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


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Gui creators
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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




'''

def str_one_column_menu_options(length, height, dic_menu_options, start_pos, ):

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

'''


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

def x_and_y_of_selected_option_within_coloumn(column_start_x, column_start_y, total_options, chars_between_titles, selected_option):
    title_start_y = column_start_y + (chars_between_titles * (selected_option - 1))
    return [column_start_x, title_start_y]


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

    print(str_main_box + str_sub_boxes)




def block_setup(box_info, options, block_number):

    start_option = 1    
    
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

    total_options = len(options)

    # creates and prints main menu box
    str_options_column_plus_chars_between_titles = str_one_column_menu_options(length, height, options, column_start_pos, 1)


    str_options_column = str_options_column_plus_chars_between_titles[0]
    chars_between_titles = str_options_column_plus_chars_between_titles[1]

# ok so we need to find the pos of the selected option then bascially take that pos and then replacew that with column start pos then repalce

    #print(column_start_pos + str_options_column + Style.RESET_ALL)

    print(str(str_options_column) + Style.RESET_ALL)

    if block_number == 1:
        x_and_y_option_return = x_and_y_of_selected_option_within_coloumn(column_start_x, column_start_y, total_options, chars_between_titles, start_option)

        start_x_option = x_and_y_option_return[0]
        start_y_option = x_and_y_option_return[1]
        start_pos_option = pos(start_x_option,start_y_option)
        print(start_pos_option + Fore.MAGENTA + options[start_option] + Style.RESET_ALL)



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
    '''
    print(column_start_pos + str_options_column + start_pos_option + Fore.MAGENTA + options[start_option])

    print(Style.RESET_ALL)
    '''
    print(start_pos_option + Fore.MAGENTA + options[start_option])
    print(Style.RESET_ALL)


    first_iteration = True
# ok idk what i want to do to contiue to imrpiove this program so now basically it seems like what is happening is that it prints t he same selection again and again which i dont want i would prefer it that it
# prints the GUI once then after that goes through the selection and deselection functions so then what i am gonna do is make it that the printing of the UIs happens once and once only and then also 
# i neede o make sure the deleseciton of a title function happens once after pressing left or right which ioahve a lil funciton for so its fine



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

                    print(str_updated_desel_title + str_updated_sel_title + Style.RESET_ALL)

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
    '''
    print(column_start_pos + str_options_column + start_pos_option + Fore.MAGENTA + options[start_option])

    print(Style.RESET_ALL)
    '''

    print(start_pos_option + Fore.MAGENTA + options[start_option])
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


def rgb_f(ls_rgb):
    ansi_fore_ground_rgb_str = f'\033[38;2;{str(ls_rgb[0])};{str(ls_rgb[1])};{str(ls_rgb[2])}m'
    return ansi_fore_ground_rgb_str



def rgb_b(ls_rgb):
    ansi_background_rgb_str = f'\033[48;2;{ls_rgb[0]};{ls_rgb[1]};{ls_rgb[2]}m'
    return ansi_background_rgb_str

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
                            return 3
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

# MENU 3 - id='purchase_menu'
# main menu that goes into sub menus
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        elif menu_num == 3:

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

            item_searcher_options = {1 : 'GTX 1050',
           2 : 'RX 480',
           3 : 'RX 580',
           4 : 'GTX 1060 3gb',
          }

            blocks = {
                      1 : 'block_1',
                      2 : 'block_2'
                      }

            GUI_loops = {
                         # block 1
                        1 : GUI_item_searcher_block_updater,

                        # block 2
                        2 : GUI_checkout_block_updater
                         }

            current_sel_block = [1]
            last_option = 1
            carry_over_option = []

            sub_boxes_start_and_end_coords = block_coords(peri_menu_length, peri_menu_height, boxes_start_and_end_percentages, peri_start_x, peri_start_y, peri_menu_end_x, peri_menu_end_y)
            sub_boxes_size = boxes_length_and_height(sub_boxes_start_and_end_coords)
            sub_boxes_start_and_end_poses = boxes_start_and_end_poses_(sub_boxes_start_and_end_coords)

            sub_boxes_info = empt_block_info_into_full_block(boxes_info_empt, boxes_start_and_end_percentages, sub_boxes_start_and_end_coords, sub_boxes_start_and_end_poses, sub_boxes_size)




            # printing actual UI
            print(str_perfect_clear_box(peri_menu_length, peri_menu_height, peri_start_x + 1 , peri_start_y + 1) + Style.RESET_ALL)

            for block_num in blocks:

                block_id_str = blocks[block_num]

                box_info_ = sub_boxes_info[block_id_str]

                block_setup(box_info_, item_searcher_options, block_num)







            create_menu_with_main_box_and_subbox(menu_block_info, sub_boxes_info)



            item_searcher_block_info = sub_boxes_info['block_1']

            checkout_block_info = sub_boxes_info['block_2']

            current_sel_block_info = item_searcher_block_info


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

                #else:
                 #   break




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
         'purchase_menu' : 3,
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