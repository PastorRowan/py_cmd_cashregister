import copy
import mmap
from tokenize import endpats
import os

from os import path

# repository functions

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
    elif _str_input == 'f':
        return 6, True
    elif _str_input == 't':
        return 5, True
    elif _str_input == 'k':
        return 4, True
    else:
        return _str_input, False
# function 1
# modifies shopping cart
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


def input_item(question_, return_address_TorF_):

    while True:
        item_id = input(question_)

        alt_option_press_test_return = alt_option_press_test(item_id)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

        item_info_address = 'Inventory/' + item_id + '.txt'

        item_in_invenotry_TorF = os.path.exists(item_info_address)
        idigit_format_TorF = idigit_format_checker(item_id)

        if idigit_format_TorF and item_in_invenotry_TorF:
            if return_address_TorF_:
                return item_id, item_info_address, False
            else:
                return item_id, False
        elif item_in_invenotry_TorF:
            print('Enter an item that exists in the inventory')
        elif idigit_format_TorF:
            print('Enter an item that follows the idigit format and exists')
        elif alt_options_pressed_TorF_return:
            return alt_option_press_test_return
        
def input_non_decimal_number(question, option): # 1st parameter is the question hte input method will ask. 2nd parameter is what option we choosing

    vowels = 'aeiouAEIOU'

    if option[0] in vowels:
        incorrect_input_msg = 'Please enter an' + option
    else:
        incorrect_input_msg = 'Please enter a' + option

    while True:
        number = input(question)

        alt_option_press_test_return = alt_option_press_test(number)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

        if alt_options_pressed_TorF_return:
            return alt_option_press_test_return

        elif option == 'natural_number':

            number_only_contains_digits_and_doesnt_start_with_0_TorF = (not number.startswith('0')) and number.isdigit()
            if number_only_contains_digits_and_doesnt_start_with_0_TorF:
                return number, False
            else:
                print(incorrect_input_msg)

        elif option == 'integer':

            number_negative_TorF = number.startswith('-') and number[1:].isdigit()
            number_postive_and_doesnt_start_with_0_TorF = number.isdigit() and (not number.startswith('0'))
            number_is_0_ToF = number == '0'

            if number_postive_and_doesnt_start_with_0_TorF or number_negative_TorF or number_is_0_ToF:
                return number, False
            else:
                print(incorrect_input_msg)

        elif option == 'whole_number':

            number_postive_and_doesnt_start_with_0_TorF = number.isdigit() and (not number.startswith('0'))
            number_is_0_ToF = (number == '0')

            if number_postive_and_doesnt_start_with_0_TorF or number_is_0_ToF:
                return number, False
            else:
                print(incorrect_input_msg)
        elif option == 'integer_not_including_0':

            number_negative_TorF = number.startswith('-') and number[1:].isdigit()
            number_postive_and_doesnt_start_with_0_TorF = number.isdigit() and (not number.startswith('0'))
            number_is_0_ToF = number == '0'

            if number_postive_and_doesnt_start_with_0_TorF or number_negative_TorF or (not number_is_0_ToF):
                return number, False
            else:
                print(incorrect_input_msg)
        else:
            print('ERROR: an option was not correctly parsed into the input_non_decimal_number function')
            break
        

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


# 4TH FUNCTION 'u'
# creates receipt text of shopping cart
def create_receipt_text_func(_current_cart_): # take reciept_text_memoryies documented item list then ocmapre that to the impt 
    float_sum_total = 0.
    global item_data_in_memory
    global receipt_text_memory

    current_cart_unique_item_tuple = tuple(_current_cart_.keys())

    receipt_text_cart_unique_item_tuple_memory = receipt_text_memory[0]
    receipt_text_in_mem = receipt_text_memory[1]

    if current_cart_unique_item_tuple != receipt_text_cart_unique_item_tuple_memory:
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
        
# 5TH FUNCTION 'l'
# creates file of shopping cart

def creates_receipt_file_func(receipt_str, receipt_address):
    global receipt_text_memory
    global current_cart
    with open (receipt_address, 'w') as receipt_file:
        receipt_file.write(receipt_str)
            
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


def change_inventory_stock(item_id, item_info_address, str_change_stock):
    global item_data_in_memory
    default_next_func_num =  5
    f = None
    mmaped_file = None
    int_change_stock = int(str_change_stock)

    if item_id in item_data_in_memory:
        int_current_stock = item_data_in_memory[item_id][2] # oh my god its the fucking memoery ok no i haave made no errors its just that when it reads from memroy it doesnt fucking change the memroy stock oh my god
        # its reading the old memroy stock every time which then causes it to fart and shit ok now it makes sense hten all we need to do is make sure that the changes in this function also chang the memory stoc
        int_new_stock = int_current_stock + int_change_stock
        if int_new_stock < 0:
            print('Stock cannot be negative')
            return default_next_func_num, False
        item_data_in_memory[item_id][2] = int_new_stock
    else:
        f = open(item_info_address, 'r+')
        mmaped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
        bytestr_item_info = mmaped_file.read()
        bytestr_current_stock = bytestr_item_info.rsplit(b'|', 1)[-1]

        str_current_stock = bytestr_current_stock.decode('utf-8')
        int_current_stock = int(str_current_stock)
        print(str_current_stock)

        int_new_stock = int_current_stock + int_change_stock

        if int_new_stock < 0:
            print('Stock cannot be negative')
            return default_next_func_num, False

    if (f != None) and (mmaped_file != None):

        str_new_stock = str(int_new_stock)
        bytestr_new_stock = str_new_stock.encode('utf-8')
        bytestr_updated_item_info = bytestr_item_info.replace(bytestr_current_stock,bytestr_new_stock)

        new_size = len(bytestr_updated_item_info)
        mmaped_file.close()
        f.truncate(new_size)

        mmaped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
        
        mmaped_file.write(bytestr_updated_item_info)
        mmaped_file.flush()
        f.close()
        mmaped_file.close()

    else:
        f = open(item_info_address, 'r+')
        mmaped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE) # ok so somehow its reading hte old values but its still here???
        bytestr_item_info = mmaped_file.read()

        int_change_stock = int(str_change_stock)

        str_current_stock = str(int_current_stock)
        bytestr_current_stock = str_current_stock.encode('utf-8')

        str_new_stock = str(int_new_stock)
        bytestr_new_stock = str_new_stock.encode('utf-8')

        print(bytestr_current_stock)
        input('should be the current stock')

        print(bytestr_new_stock)
        input('should be 1 less than the previous stock stock')  # i1 = 12 should become 11

        bytestr_updated_item_info = bytestr_item_info.replace(bytestr_current_stock,bytestr_new_stock) # error is here upwards
        print(bytestr_updated_item_info)
        input('Should be 1 less than before')

        new_size = len(bytestr_updated_item_info)
        mmaped_file.close()
        f.truncate(new_size)

        mmaped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
        mmaped_file.write(bytestr_updated_item_info)
        mmaped_file.flush()
        input('check if file has changed')
        f.close()
        mmaped_file.close()

def error_occured_checker():
    global current_cart
    global item_data_in_memory

    current_cart_empty_TorF = current_cart == {}
    item_data_cart_mem_emtpy_TorF = item_data_in_memory['cart_in_memory'] == {}
    current_cart_equal_item_data_cart_mem = current_cart == item_data_in_memory['cart_in_memory']

    if current_cart_empty_TorF:
        print('ERROR: SHOPPING CART: shopping cart is empty, cannot perform the function')
        return 1 , True

    elif item_data_cart_mem_emtpy_TorF:
        print('ERROR: ITEM DATA MEMORY MANAGEMENT: cart in memory is emtpy, cannot perform the function')
        return 'p' , True

    elif current_cart_equal_item_data_cart_mem:
        print('ERROR: SHOPPING CART AND CART IN MEMORY EQUIVALENCY: shopping cart is not the same as item data cart in memory, cannot perform this function')
        return 'p', True
    else:
        return False,

def ask_overwrite_file(receipt_address):
    if path.exists(receipt_address): # make input
        print('receipt does already exist')
        question = 'enter y to overwrite file or enter n to not overwrite the file' # still need to add the back function
        answer = answer_y_or_n(question)

        alt_option_press_test_return = alt_option_press_test(answer)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

        if alt_options_pressed_TorF_return:
            return alt_option_press_test_return
        elif answer == 'n':
            return alt_option_press_test_return
        else:
            return alt_option_press_test_return







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

            alt_option_pressed_TorF = prints_stock_in_inventory_return[-1]
            alt_option_pressed_func_number = prints_stock_in_inventory_return[0]

            if alt_option_pressed_TorF:
                return alt_option_pressed_func_number
            else:
                return 1


# 5TH FUNCTION 't'
# changes stock in inventory
        elif func_option == 5:
            input('we are currentky on function 5')

            question_ = '\nEnter the item you want to change the stock of.\n ---->'
            return_address_TorF = True

            input_item_return = input_item(question_, return_address_TorF)

            alt_option_pressed_TorF = input_item_return[-1]
            alt_option_pressed_func_number = input_item_return[0]

            if alt_option_pressed_TorF:
                return alt_option_pressed_func_number
            
            question_ = '\nEnter an integer that is not 0.\n ---->'

            input_integer_return = input_non_decimal_number(question_, 'integer_not_including_0')

            alt_option_pressed_TorF = input_integer_return[-1]
            alt_option_pressed_func_number = input_integer_return[0]

            if alt_option_pressed_TorF:
                return alt_option_pressed_func_number
            
            item_id = input_item_return[0]
            item_info_address = input_item_return[1]
            str_change_stock = input_integer_return[0]
            
            change_inventory_stock(item_id, item_info_address, str_change_stock)

            return 5
        

# 6TH FUNCTION 'f'
# Does a full checkout, changes inventory according to the cart (and saves receipts and inventory to an online database)
        elif func_option == 6:
            input('we are currentky on function 6')

            # loads shopping cart item data
            item_data_memory_management(current_cart)

            # error checker
            errr_occured_return = error_occured_checker()
            errr_occured_TorF = errr_occured_return[-1]
            error_occured_next_action= errr_occured_return[0]
            if errr_occured_TorF:
                return error_occured_next_action
            
            # creates and prints receipt str
            receipt_str = create_receipt_text_func(current_cart)
            print(receipt_str)

            # creates receipt file
            str_receipt_number = input('enter receipt number you want TEST, THERE IS NO CHECKS')

            receipt_address = 'Receipts/' + 'receipt' + str_receipt_number + '.txt'

            ask_overwrite_file_return = ask_overwrite_file(receipt_address)

            answer = ask_overwrite_file_return[0]
            alt_option_pressed_TorF = ask_overwrite_file_return[-1]
            alt_option_pressed_func_number = ask_overwrite_file_return[0]

            if alt_option_pressed_TorF:
                return alt_option_pressed_func_number
            elif answer == 'n':
                creates_receipt_file_func(receipt_str, receipt_address)

            # Removes sold stock inventory
            for item_id_ in current_cart:
                int_amount_bought = current_cart[item_id_]
                int_change_stock = -int_amount_bought
                str_change_stock_ = str(int_change_stock)


                item_info_address_ = 'Inventory/' + item_id_ + '.txt'

                print(item_id_)
                print(type(item_id_))
                print(item_info_address_)
                print(str_change_stock_)

                change_inventory_stock(item_id_, item_info_address_, str_change_stock_)
# i1 = 16
            current_cart = {}
            print('checkout was successful and shopping cart was emptied')
            return 1

# ok so basicalyl what we want is for each item in the current cart we want to take a key out ok take the key out and its value pair and plug them both into the change hardrive stock function and then create a
# create item_info_address code

# 6TH FUNCTION 's'
# Saves receipts and inventory to an online database
        elif func_option == 7:
            input('we are currentky on function 7')
















current_cart = {}
item_data_in_memory = {'cart_in_memory' : set()}
receipt_text_memory = [(' '), '']
default_start_selected_option = 1

selected_option = default_start_selected_option

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