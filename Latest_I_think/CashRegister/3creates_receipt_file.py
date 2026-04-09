import os
from os import path
import mmap


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

        elif option == 'natural_numbers':

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
            
        elif option == 'integers_0':

            number_negative_TorF = number.startswith('-') and number[1:].isdigit()
            number_postive_and_doesnt_start_with_0_TorF = number.isdigit() and (not number.startswith('0'))
            number_is_0_ToF = number == '0'

            if number_postive_and_doesnt_start_with_0_TorF or number_negative_TorF or (not number_is_0_ToF):
                return number, False
            else:
                print(incorrect_input_msg)
        else:
            print('ERROR: an option was not correctly parsed into the input_non_decimal function')
            break

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

import mmap

def creates_receipt_file_func(receipt_str, receipt_address):
    global receipt_text_memory
    global current_cart
    with open (receipt_address, 'w') as receipt_file:
        receipt_file.write(receipt_str)

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


def error_occured_checker():
    global current_cart
    global item_data_in_memory

    current_cart_empty_TorF = current_cart == {}
    item_data_cart_mem_emtpy_TorF = item_data_in_memory['cart_in_memory'] == {}
    current_cart_equal_item_data_cart_mem = current_cart == item_data_in_memory['cart_in_memory']

    if current_cart_empty_TorF:
        print('ERROR: SHOPPING CART: shopping cart is empty, cannot perform the function')
        return True

    elif item_data_cart_mem_emtpy_TorF:
        print('ERROR: ITEM DATA MEMORY MANAGEMENT: cart in memory is emtpy, cannot perform the function')
        return True

    elif current_cart_equal_item_data_cart_mem:
        print('ERROR: SHOPPING CART AND CART IN MEMORY EQUIVALENCY: shopping cart is not the same as item data cart in memory, cannot perform this function')
        return True
    else:
        return False








# main program


current_cart = {'i1' : 1, 'i2' : 2}
item_data_in_memory = {'cart_in_memory' : ''}
receipt_text_memory = ['', '']

current_cart_empty_TorF = current_cart == {}
item_data_cart_mem_emtpy_TorF = item_data_in_memory['cart_in_memory'] == {}
current_cart_equal_item_data_cart_mem = current_cart == item_data_in_memory['cart_in_memory']

item_data_memory_management(current_cart)

# error checking
error_occured_TorF = error_occured_checker()

if error_occured_TorF:
    item_data_in_memory[10]
    # return

else:

    input_non_decimal_return = input_non_decimal_number('Enter a receipt receipt number', 'natural_numbers')

    str_receipt_number = input_non_decimal_return[0]
    alt_options_pressed_TorF_return = input_non_decimal_return[-1]

    if alt_options_pressed_TorF_return:
        item_data_in_memory[10]
        # return input_non_decimal_return

    receipt_address = 'Receipts/' + 'receipt' + str_receipt_number + '.txt'

    answer = None

    if path.exists(receipt_address): # make input
        print('receipt does already exist')
        question = 'enter y to overwrite file or enter n to not overwrite the file and reset the function' # still need to add the back function
        answer = answer_y_or_n(question)

        alt_option_press_test_return = alt_option_press_test(answer)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

        if alt_options_pressed_TorF_return:
            item_data_in_memory[10] # might just return function number in complete program function
            # return alt_option_press_test_return
        elif answer == 'n':
            item_data_in_memory[10]
            # return alt_option_press_test_return
        receipt_str = create_receipt_text_func(current_cart)
        creates_receipt_file_func(receipt_str, receipt_address)
    else:
        receipt_str = create_receipt_text_func(current_cart)
        creates_receipt_file_func(receipt_str, receipt_address)

def ask_overwrite_file(receipt_address):
    if path.exists(receipt_address): # make input
        print('receipt does already exist')
        question = 'enter y to overwrite file or enter n to not overwrite the file' # still need to add the back function
        answer = answer_y_or_n(question)

        alt_option_press_test_return = alt_option_press_test(answer)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

        if alt_options_pressed_TorF_return:
            item_data_in_memory[10] # might just return function number in complete program function
            # return alt_option_press_test_return
        elif answer == 'n':
            item_data_in_memory[10]
            # return alt_option_press_test_return