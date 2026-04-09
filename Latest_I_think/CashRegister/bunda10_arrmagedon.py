import copy
import mmap
from tokenize import endpats
import os

from os import path

def idigit_format_checker(input_str):

    if input_str.startswith('i') and input_str[1:].isdigit():
         return True
    else:
         return False

def alt_option_press_test(_str_input): # else retrn _str input??? idk
    if _str_input == 'p':
        return 'p', True
    elif _str_input == '/':
        return '/', True
    elif _str_input == 'c':
        return 2, True
    elif _str_input == 'i':
        return 3, True
    elif _str_input == 's':
        return 1, True
    elif _str_input == 'u':
        return 2, True
    elif _str_input == 'l':
        return 3, True
    elif _str_input == 'r':
        return 6, True
    elif _str_input == 't':
        return 7, True
    elif _str_input == 'k':
        return 4, True
    else:
        return _str_input, False

def append_item_cart_func():
    global current_cart

    while True:
        item_ = input('Enter an item\n ---> ')

        alt_option_press_test_return = alt_option_press_test(item_)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

        item_info_address = 'Inventory/' + item_ + '.txt'

        if alt_options_pressed_TorF_return:
            return alt_option_press_test_return
        elif not idigit_format_checker(item_):
            print('\nEnter an item that follows the correct idigit format\n')
        elif not os.path.exists(item_info_address):
            print('\nEnter an item in the inventory\n')
        else:
            str_number_of_item = input('Enter the amount you want of this item\n ---> ')

            alt_option_press_test_return = alt_option_press_test(item_)
            alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

            if str_number_of_item == '':
                int_number_of_item = 1
                current_cart[item_] = current_cart.get(item_, 0) + int_number_of_item

            elif (str_number_of_item == ';') and (item_ in current_cart):
                del current_cart[item_]


            elif (str_number_of_item.isdigit()) or (str_number_of_item.startswith('-') and str_number_of_item[1:].isdigit()):
                int_number_of_item = int(str_number_of_item)
                current_cart[item_] = current_cart.get(item_, 0) + int_number_of_item
                if current_cart.get(item_) <= 0:
                    del current_cart[item_]

        print(current_cart)
        

# < 5TH FUNCTION
# inventory data memory gets loaded affter a certain point
# what we are gonna do instead because now it doesnt just brute force load all the data at once only if it has to then im just gonna run this code before every function that needs htis code

def item_data_memory_management(current_cart_):
    global item_data_in_memory

    if current_cart_ != {}:
        current_cart_unique_item_set = set(current_cart_.keys())
        cart_in_memory = item_data_in_memory['cart_in_memory']
        if cart_in_memory != current_cart_unique_item_set:
            item_data_in_memory['cart_in_memory'] = current_cart_unique_item_set
            item_data_in_memory = {key: value for key, value in item_data_in_memory.items() if key in current_cart_unique_item_set or key == 'cart_in_memory'}

            for unique_current_cart_item in current_cart_unique_item_set:
                if not (unique_current_cart_item in item_data_in_memory):
                    # if item is in the current cart but not in memory
                    item_address = 'Inventory/' + unique_current_cart_item + '.txt'
                    f =  open(item_address, 'r')
                    mmaped_f = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                    byte_str_file_contents = mmaped_f.read()
                    byte_str_product_info = byte_str_file_contents.split(b'|')

                    decoded_name = byte_str_product_info[0].decode('utf-8')
                    decoded_price = float(byte_str_product_info[1].decode('utf-8'))
                    decoded_stock = int(byte_str_product_info[2].decode('utf-8'))

                    item_data = (decoded_name, decoded_price, decoded_stock)
                    item_data_in_memory[unique_current_cart_item] = item_data


    else:
        print('Please Enter an item into the cart')
        return 1, True


# 4TH FUNCTION 'u'
# prints current receipt of shopping cart
        
# 5TH FUNCTION 'l'
# creates file of shopping cart

def create_receipt_text_func(_current_cart_): # take reciept_text_memoryies documented item list then ocmapre that to the impt 
    float_sum_total = 0.
    global item_data_in_memory
    global receipt_text_memory

    current_cart_unique_item_tuple = tuple(_current_cart_.keys())

    receipt_text_cart_unique_item_tuple_memory = receipt_text_memory[0]
    receipt_text_in_mem = receipt_text_memory[1]

    if (_current_cart_ != {}) and (current_cart_unique_item_tuple != receipt_text_cart_unique_item_tuple_memory):
        receipt_text_list = []

        for item in current_cart_unique_item_tuple:
            int_number_of_item = _current_cart_[item]
            float_total_item = int_number_of_item * item_data_in_memory[item][1]
            str_number_of_item = str(int_number_of_item)
            str_product_name = item_data_in_memory[item][0]
            str_total_item = str(float_total_item)

            product_line = str_number_of_item + 'x ' + str_product_name + ' ' + str_total_item + '\n'
            receipt_text_list.append(product_line)
            float_sum_total += float_total_item

        str_total = str(float_sum_total)
        total_line = '\n' + str_total
        receipt_text_list.append(total_line)

        receipt_text = ''.join(element_ for element_ in receipt_text_list)

        receipt_text_memory[0] = current_cart_unique_item_tuple
        receipt_text_memory[1] = receipt_text

        return receipt_text
    
    elif _current_cart_ == {}:
        receipt_text = receipt_text_in_mem
        print('Your shopping cart is empty, no changes were made to receipt_text_memory')
        return receipt_text

    elif current_cart_unique_item_tuple == receipt_text_cart_unique_item_tuple_memory:
        receipt_text = receipt_text_memory
        print('Your shopping cart is exactly the same, no changes were made to receipt_text_memory')
        return receipt_text

def answer_y_or_n(_question):
    while True:
        _answer = input(_question)

        alt_option_press_test_return = alt_option_press_test(_answer)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
        alt_option_pressed_func_number_return = alt_option_press_test_return[0]

        if _answer == 'y':
            return _answer
        elif _answer == 'n':
            return _answer
        elif alt_options_pressed_TorF_return:
            return alt_option_pressed_func_number_return
        else:
            print('\nEnter y or n or a special option\n\n ---->')

def creates_receipt_file_func(receipt_str):
    global item_data_in_memory
    global receipt_text_memory

    if (receipt_str != None) and (item_data_in_memory != {}):
        while True:
            str_receipt_number = input('What receipt number do you want?')

            alt_option_press_test_return = alt_option_press_test(str_receipt_number)
            alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

            if (str_receipt_number.isdigit()) and (str_receipt_number != '0'):
                receipt_address = 'Receipts/' + 'receipt' + str_receipt_number + '.txt'
                if path.exists(receipt_address):
                    print('receipt does already exist')
                    question = 'enter y to overwrite file or enter n to not overwrite the file and reset the function' # still need to add the back function
                    answer = answer_y_or_n(question)

                    alt_option_press_test_return = alt_option_press_test(answer)
                    alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

                    if answer == 'y': # said yes
                        # opens and deletes contents of receipt file
                        with open (receipt_address, 'w') as receipt_file:
                        # writes receipt onto receipt file
                            receipt_file.write(receipt_str)
                        return alt_option_press_test_return
                    elif answer == 'n': # said no
                        return alt_option_press_test_return
                    elif alt_options_pressed_TorF_return:
                        return alt_option_press_test_return



                else:
                    # creates receipt file
                    with open (receipt_address, 'w') as receipt_file:
                        # writes receipt onto receipt file
                        receipt_file.write(receipt_str)
                        return alt_option_press_test_return

            elif alt_options_pressed_TorF_return:
                    return alt_option_press_test_return
            
def auto_load_current_receipt_number():
    global str_current_receipt_number_mem

    if os.path.getsize('Receipt_number_log/Receipt_num_log.txt') == 0:
        str_current_receipt_number_mem = '1'
        with open ('Receipt_number_log/Receipt_num_log.txt', 'r+') as f_:
            f_.write('1')
            print('Current receipt number has been made 1')
    else:
        with open('Receipt_number_log/Receipt_num_log.txt', 'r') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mmap_file:
                byte_string_current_receipt_number_hard = mmap_file.read()
                str_current_receipt_number = byte_string_current_receipt_number_hard.decode('utf-8')
                str_current_receipt_number_mem = str_current_receipt_number


# if option is 'u' then add 1 to file log
# if option is 'i' then just update the number log with the one in mem

def receipt_number_log_and_mem_updater(selected_option):
    global str_current_receipt_number_mem

    if selected_option == 'u':
        int_receipt_number= int(str_current_receipt_number_mem) + 1
        str_updated_receipt_number = str(int_receipt_number)
        str_current_receipt_number_mem = str_updated_receipt_number
    elif selected_option == 'i':
        str_updated_receipt_number = str_current_receipt_number_mem

    bytestr_receipt_number = str_updated_receipt_number.encode('utf-8')
    _f_ = open('Receipt_number_log/Receipt_num_log.txt', 'r+')
    new_size = len(str_updated_receipt_number)
    _f_.truncate(new_size)
    _mmap_f = mmap.mmap(_f_.fileno(), 0, access=mmap.ACCESS_WRITE)
    _mmap_f.write(bytestr_receipt_number)
    _mmap_f.flush()
    _mmap_f.close()
    _f_.close()

def receipt_number_selection_func():
    global str_current_receipt_number_mem

    receipt_number_ = input('What receipt number would you like to select?')

    alt_option_press_test_return = alt_option_press_test(receipt_number_)
    alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

    if (receipt_number_.isdigit()) and (receipt_number_ != '0'):
        str_current_receipt_number_mem = receipt_number_

        question = 'Enter y if you want to save the selected receipt_number into hardrive or enter n if you dont want to'
        answer = answer_y_or_n(question)

        alt_option_press_test_return = alt_option_press_test(answer)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

        if answer == 'y':
            receipt_number_log_updater('i')
        elif answer == 'n':
            print('Hardrive receipt number was not updated')
        elif alt_options_pressed_TorF_return:
            return alt_option_press_test_return

    elif alt_options_pressed_TorF_return:
        return alt_option_press_test_return

def prints_stock_in_inventory():
    global item_data_in_memory

    f = None
    mmaped_file = None

    while True:
        item_identifier = input('\nEnter the item you want to check the stock of.\n ---->')

        alt_option_press_test_return = alt_option_press_test(item_identifier)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

        if idigit_format_checker(item_identifier):
            if item_identifier in item_data_in_memory:
                # runs if item is present in memory
                current_stock = item_data_in_memory[item_identifier][2]
                print('Reading memory sss...sssss...HHHhhhh...sssss')
                print(current_stock)
            else:
                item_info_address = 'Inventory/' + item_identifier + '.txt'
                f = open(item_info_address, 'r')
                mmaped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                byte_item_info = mmaped_file.read()
                current_stock = byte_item_info.rsplit(b'|', 1)[-1].decode('utf-8')
                print('Reading hardrive inventory sss...sssss...HHHhhhh...sssss')
                print(current_stock)
        elif alt_options_pressed_TorF_return:
            if (f != None) and (mmaped_file != None):
                f.close()
                mmaped_file.close()
                print('closing files')
            else:
                print('Didnt close files because they werent open becaues the function only used the memory')
            return alt_option_press_test_return
        else:
            print('Monkey enter an item that follows the idigit format')












def complete_program_loop(func_option): # selected 's' by default
    global current_cart
    global item_data_in_memory
    global str_current_receipt_number_mem

    while True:

# 1ST FUNCTION 's'
# shopping cart management
        if func_option == 1:
            input('we are currentky on function 1')
            append_item_cart_return = append_item_cart_func()

            append_item_cart_alt_option_pressed_TorF = append_item_cart_return[-1]
            append_item_cart_alt_option_pressed_func_number = append_item_cart_return[0]

            if append_item_cart_alt_option_pressed_TorF:
                return append_item_cart_alt_option_pressed_func_number

# 2ND FUNCTION 'u'
# prints current receipt of shopping cart
        elif func_option == 2:
            input('we are currentky on function 2')
            item_data_memory_management(current_cart)
            receipt_text = create_receipt_text_func(current_cart)
            print(receipt_text)
            return 1

# 3RD FUNCTION 'l'
# creates file of shopping cart
        elif func_option == 3:
            input('we are currentky on function 3')
            item_data_memory_management(current_cart)
            receipt_text = create_receipt_text_func(current_cart)
            creates_receipt_file_return = creates_receipt_file_func(receipt_text)

            creates_receipt_alt_option_pressed_TorF = creates_receipt_file_return[-1]
            creates_receipt_alt_option_pressed_func_number = creates_receipt_file_return[0]

            if creates_receipt_alt_option_pressed_TorF:
                return creates_receipt_alt_option_pressed_func_number

            else:
                return 1


# 4TH FUNCTION 'k'
# prints stock of items in inventory
# reads memory of inventory and if it isnt available reads harddrive inventory
        elif func_option == 4:
            input('we are currentky on function 4')
            item_data_memory_management(current_cart)
            prints_stock_in_inventory_return = prints_stock_in_inventory()

            prints_stock_in_inventory_alt_option_pressed_TorF = prints_stock_in_inventory_return[-1]
            prints_stock_in_inventory_alt_option_pressed_func_number = prints_stock_in_inventory_return[0]

            if prints_stock_in_inventory_alt_option_pressed_TorF:
                return prints_stock_in_inventory_alt_option_pressed_func_number
            else:
                return 1


# 5TH FUNCTION 't'
# changes stock in inventory
        elif func_option == 5:
            input('we are currentky on function 5')
            input_change_inventory = prerequesite_information_collection_change_inventory()

            int_change_stock = input_change_inventory[0]
            product_data_line = input_change_inventory[2]
            line_start_position = input_change_inventory[3]
            length_to_truncate = input_change_inventory[4]
            mmaped_inventory_return = input_change_inventory[-2]
            pressed_option = input_change_inventory[-1]
            str_old_stock = input_change_inventory[1]

            selected_option = special_option_return(input_change_inventory[-1]) 
            print(input_change_inventory)
            print(str_old_stock)
            print(int_change_stock)
            print(product_data_line)
            print(line_start_position)
            print(length_to_truncate)
            print(mmaped_inventory_return)
            print(pressed_option)
            print(type(str_old_stock))
            input('jerog')
            main_processing_change_inventory(int_change_stock, str_old_stock, product_data_line, line_start_position, mmaped_inventory_return, length_to_truncate)
            # int_change_stock = amount we will change stock by (- or +)
            # selected_product_data_info[1] = product data line,
            # selected_product_data_info[2] = line position within inventory
            # mmaped inventory = memory map of inventory 
            # pressed option so you can cycle through functions
            if selected_option[-1]:
                return selected_option[0]
            
        elif True:
            append_item_cart_return[-10]






























current_cart = {}
item_data_in_memory = {'cart_in_memory' : set()}
receipt_text_memory = [(' '), '']
selected_option = 1

while True:

    selected_option = complete_program_loop(selected_option)

    print(selected_option)
    
    input('selected option has been printed. should be the button pressed')
    if selected_option == 'p':
       break
    elif selected_option == '/':
        print('bruh function no work right now')
        break
        # will repeat the complete program loop
    elif selected_option == '/':
        print('bruh function no work right now')
        break
    elif selected_option == 2:
        print('function 2 should be operational')
    elif selected_option == 3:
        print('function 3 should be operational')
    elif selected_option == None:
        print('program is repeated')