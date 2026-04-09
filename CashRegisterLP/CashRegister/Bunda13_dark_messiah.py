import copy
import mmap
from tokenize import endpats
import os

from os import path
from datetime import date

# auto load functions
def auto_load_todays_receipts_path_plus_date():
    global todays_date
    global todays_folder_path
    global todays_receipt_folder_name

    todays_date_ = date.today()
    str_todays_date = todays_date_.strftime("%Y-%m-%d")
    todays_receipt_folder_name = 'Receipts_' + str_todays_date
    todays_folder_path = 'Receipts/' + todays_receipt_folder_name
    todays_date = str_todays_date


def auto_load_create_todays_receipt_folder():
    global todays_folder_path
    if not (os.path.exists(todays_folder_path)):
        os.makedirs(todays_folder_path)

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

def input_idigit_item(_question__):
    while True:
        item = input(_question__) # question will be something like input an item that follows the
        # idigit format 

        alt_option_press_test_return = alt_option_press_test(item)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

        if item.startswith('i') and item[1:].isdigit():
         return item, False
        
        elif alt_options_pressed_TorF_return:
            return alt_option_press_test_return
        
        else:
            print('Please enter an item that follows the idigit format')


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
    elif _str_input == 'j':
        return 8, True
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


def input_existing_item(question_, existing_TorF, return_address_TorF_):

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
        
def input_number(question, option): # 1st parameter is the question hte input method will ask. 2nd parameter is what option we choosing

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

        elif option == 'non_negative_float_currency':

            input_string = input_string.replace(',', '.')

            # Check if the string represents a non-empty positive number
            if number.lstrip('+-').replace('.', '', 1).isdigit():
                # Convert the string to float and check if it has 0, 1, or 2 decimals
                number_ = float(input_string)
            if 0 <= number_ == round(number_, 2):
                return True

            input_is_empty_TorF = number != ''
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

                    item_data = [decoded_name, decoded_price, decoded_stock]
                    item_data_in_memory[unique_current_cart_item] = item_data
    print(item_data_in_memory)

    #else:
        #print('Please Enter an item into the cart')


# 4TH FUNCTION 'u'
# creates receipt text of shopping cart
def create_receipt_text_func(_current_cart_): # take reciept_text_memoryies documented item list then ocmapre that to the impt 
    float_sum_total = 0.
    global item_data_in_memory # list was inputted
    global receipt_text_memory
    global todays_date

    client_firstname = 'John'
    client_surname = 'Smith'

    client_info_plus_date_line = todays_date +  ' ' + client_firstname + ' ' + client_surname + '\n' + '\n'

    current_cart_unique_item_tuple = tuple(_current_cart_.keys())

    receipt_text_cart_unique_item_tuple_memory = receipt_text_memory[0]
    receipt_text_in_mem = receipt_text_memory[1]

    if current_cart_unique_item_tuple != receipt_text_cart_unique_item_tuple_memory:
        receipt_text_list = [client_info_plus_date_line]

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
        receipt_text = receipt_text_in_mem[1]
        print('Your shopping cart is empty, no changes were made to receipt_text_memory')
        return receipt_text

    elif current_cart_unique_item_tuple == receipt_text_cart_unique_item_tuple_memory:
        receipt_text = receipt_text_memory[1]
        print('Your shopping cart is exactly the same, no changes were made to receipt_text_memory')
        return receipt_text

# 5TH FUNCTION 'l'
# creates file of shopping cart

def creates_and_overwrites_receipt_file_func(receipt_str, receipt_address): # recept str was a list
    with open (receipt_address, 'w') as receipt_file:
        receipt_file.write(receipt_str)

def auto_load_current_receipt_number():
    global current_receipt_number_mem
    if os.path.exists == False:
        with open ('Receipt_number_log/Receipt_num_log.txt', 'a') as f_:
            f_.write('1')
            print('Current receipt number has been made 1')
    else:
        with open('Receipt_number_log/Receipt_num_log.txt', 'r') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mmap_file:
                byte_string_current_receipt_number_hard = mmap_file.read()
                str_current_receipt_number = byte_string_current_receipt_number_hard.decode('utf-8')
                current_receipt_number_mem = str_current_receipt_number


# if option is 'u' then add 1 to file log
# if option is 'i' then just update the number log with the one in mem

def receipt_number_log_and_mem_updater(current_receipt_number, selected_option, update_hardrive_yorn):
    global current_receipt_number_mem

    # updates memory
    if selected_option == 'u': # u is add one which we are gonna add to the end of the function
        int_updated_receipt_number= int(current_receipt_number_mem) + 1
        str_updated_receipt_number = str(int_updated_receipt_number)
        current_receipt_number_mem = str_updated_receipt_number
        print(current_receipt_number_mem)
        print('new current receipt number in mem')
    elif selected_option == 'i': # i is update
        current_receipt_number_mem = current_receipt_number
        print(current_receipt_number_mem)
        print('new current receipt number in mem')
    else:
        print("ERROR: variable 'selected_option' WAS NOT PARSED: 'selected_option' was not assigned a compatible value")

    # updates hardrive
    if update_hardrive_yorn == 'y':
        bytestr_updated_receipt_number = str_updated_receipt_number.encode('utf-8')
        print(bytestr_updated_receipt_number)
        print('new receipt number in hardrive')
        _f_ = open('Receipt_number_log/Receipt_num_log.txt', 'r+')
        new_size = len(str_updated_receipt_number)
        _f_.truncate(new_size)
        _mmap_f = mmap.mmap(_f_.fileno(), 0, access=mmap.ACCESS_WRITE)
        _mmap_f.write(bytestr_updated_receipt_number)
        _mmap_f.flush()
        _mmap_f.close()
        _f_.close()
    elif update_hardrive_yorn == None:
        print("ERROR: variable 'update_hardrive_yorn' WAS NOT PARSED: 'update_hardrive_yorn' was not assigned a compatible value")

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
        int_current_stock = item_data_in_memory[item_id][2]
        int_new_stock = int_current_stock + int_change_stock
        if int_new_stock < 0:
            return default_next_func_num, False
        item_data_in_memory[item_id][2] = int_new_stock
    else:
        f = open(item_info_address, 'r+')
        mmaped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
        bytestr_item_info = mmaped_file.read()
        bytestr_current_stock = bytestr_item_info.rsplit(b'|', 1)[-1]

        str_current_stock = bytestr_current_stock.decode('utf-8')
        int_current_stock = int(str_current_stock)

        int_new_stock = int_current_stock + int_change_stock

        if int_new_stock < 0:
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

        bytestr_updated_item_info = bytestr_item_info.replace(bytestr_current_stock,bytestr_new_stock) # error is here upwards

        new_size = len(bytestr_updated_item_info)
        mmaped_file.close()
        f.truncate(new_size)

        mmaped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
        mmaped_file.write(bytestr_updated_item_info)
        mmaped_file.flush()
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
    else:
        return None, False# ok if the file doesnt exist then we 

def question_and_answer(str_question, set_str_answers):

    while True:
        _answer = input(str_question)

        alt_option_press_test_return = alt_option_press_test(_answer)
        alt_options_pressed_TorF = alt_option_press_test_return[-1]
        alt_option_pressed_test_return = alt_option_press_test_return

        if _answer in set_str_answers:
            return _answer
        elif alt_options_pressed_TorF:
            return alt_option_pressed_test_return
        else:
            print('\nEnter y or n or a special option\n\n ---->')







def complete_program_loop(func_option): # selected 's' by default
    global current_cart
    global item_data_in_memory
    global current_receipt_number_mem
    global todays_folder_path

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
# c:\Users\MSI\Desktop\CashRegister\Receipts\Receipts_2024-01-01
            receipt_address_ = todays_folder_path + '\Receipt' + current_receipt_number_mem + '.txt'

            creates_and_overwrites_receipt_file_func(receipt_text, receipt_address_)
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
            errr_occured_return = error_occured_checker() # i1 = 15 ||| i2 = 21
            errr_occured_TorF = errr_occured_return[-1]
            error_occured_next_action= errr_occured_return[0]
            if errr_occured_TorF:
                return error_occured_next_action
            
            # creates and prints receipt str
            receipt_str = create_receipt_text_func(current_cart)
            print(receipt_str)

            # creates receipt file
            receipt_address = 'Receipts/' + 'receipt' + current_receipt_number_mem + '.txt'

            print(receipt_address)

            ask_overwrite_file_return = ask_overwrite_file(receipt_address)

            answer = ask_overwrite_file_return[0]
            alt_option_pressed_TorF = ask_overwrite_file_return[-1]
            alt_option_pressed_func_number = ask_overwrite_file_return[0]

            if alt_option_pressed_TorF:
                return alt_option_pressed_func_number
            elif (answer == 'y') or (answer == None):
                creates_and_overwrites_receipt_file_func(receipt_str, receipt_address) # a list was inputted =

            # Removes sold stock inventory
            for item_id_ in current_cart:
                int_amount_bought = current_cart[item_id_]
                int_change_stock = -int_amount_bought
                str_change_stock_ = str(int_change_stock)

                item_info_address_ = 'Inventory/' + item_id_ + '.txt'
                change_inventory_stock(item_id_, item_info_address_, str_change_stock_)

            receipt_number_log_and_mem_updater(current_receipt_number_mem, 'u', 'y')
            print(current_receipt_number_mem)
            current_cart = {}
            print('checkout was successful and shopping cart was emptied')
            return 1




# 7TH FUNCTION 'q'
# changes current receipt number and receipt number in hardrive
        elif func_option == 7:
            input('we are currentky on function 7')

            question = 'Enter the new current receipt number'

            input_non_decimal_number_return = input_non_decimal_number(question, 'natural_number')

            receipt_number_ = input_non_decimal_number_return[0]
            alt_options_pressed_return = input_non_decimal_number_return
            alt_options_pressed_TorF = input_non_decimal_number_return[-1]

            if alt_options_pressed_TorF:
                return alt_options_pressed_return

            question = 'Enter y if you want to save the selected receipt_number into hardrive or enter n if you dont want to'
            answer_y_or_n_return = answer_y_or_n(question)

            answer = answer_y_or_n_return[0]
            alt_options_pressed_return = answer_y_or_n_return
            alt_options_pressed_TorF = answer_y_or_n_return[-1]

            if answer == 'y':
                receipt_number_log_and_mem_updater(receipt_number_, 'i', answer)
            elif answer == 'n':
                receipt_number_log_and_mem_updater(receipt_number_, 'i', answer)
                print('Hardrive receipt number was not updated')
            elif alt_options_pressed_TorF:
                return alt_options_pressed_return
            
# 8TH FUNCTION 'j'
# adds or overwrites inventory item and item data
        elif func_option == 8:
            input('we are currentky on function 8')
            question = 'Enter an item'
            input_idigit_item_return = input_idigit_item(question)

            item_id = input_idigit_item_return[0]
            alt_option_pressed_func_number = input_idigit_item_return[0]
            alt_options_pressed_TorF = input_idigit_item_return[-1]

            if alt_options_pressed_TorF:
                return alt_option_pressed_func_number

            item_info_address = 'Inventory/' + item_id + '.txt'
            ask_overwrite_file_return = ask_overwrite_file(item_info_address)

            answer = ask_overwrite_file_return[0]
            alt_option_pressed_func_number = ask_overwrite_file_return[0]
            alt_options_pressed_TorF = ask_overwrite_file_return[-1]

            
            if answer == 'n':
                return 1
            elif alt_options_pressed_TorF:
                return alt_option_pressed_func_number
            
            item_name = input('Enter an item name, you can enter whatever name you want but please follow the correct format. for more details please enter nothing')

            item_price = input_number('Enter an item price', 'non_negative_float_currency')

            item_stock = input_number('Enter an item stock', 'whole_number')

# ok now lets construct a string that has all of this ifnormation
            
            item_data_line = item_name + '|' + item_price + '|' + item_stock

            creates_and_overwrites_receipt_file_func(item_data_line, item_info_address)

# ok so we are gnna keep the roignal receipt but what i could do is put a refunded tag over it and then show like ok this and this was refunded or something yeah
# i think that makes sense. so basically like the way we could remember a receipt got refunded in some way idk. so baiscally we could put the refunded tag like above the receipt or something idk like at the top next
# to the name is like a refuneded tag then perhaps we could move hte receipt file to a refunded category??? idk i say we keep the original receipt then basically create anoher receipt with the same receipt number that
# is basically like receipt6 refund and then is within the same date folder or whatever should i put the days date into the receipt file nae because i feel like that is very important and provides very very
# easy searchability of the receipt and the refund if we were to create some kind of search enginge or just use the windows search engine or linux search engine or whatever. i say what we could do is like
# ok yeah that makes sense to me so that will be the next feature of our program and then i am gonna finish the changing what ever now lets create the inventory item

# lets first start ok change item in inventory so basically what we are gonna do is somehow changing one item iwthin hte inventory so whawt we could do is read the entire file and get all the data then
# we can subsitiute in bytes the price data ohh hi got a cool idea so basically we came up with this idea ok ok t=this is a fucking great idea we came up with this one idea to take out information out of a funciton
# no in fact we still use that its called item loading function so we can use that to number 1 take out the information then basically we could read the item information in memory and say like ok encode it into bytes
# then replace that code with this code. that is one option or we can take out hte inforaton a gian nah that sounds like the most mid idea ever i say lets make it a bit more spicy and then like basically replace
# the original product line with hte informato in memoery or even better just to make things a bit more spicy we have the entire product line in memoru so lets recreate the product line using the data in memor
# to avoid file i/o operations then basically jsut instnatly pput it all gotehtet then take hte old info and replace it with the new info then yeah take that then open the file and then truncate the fie to hte new size
# then overwrite the data with mmap. perfect
        


# 9TH FUNCTION 'd'
# refunds a receipt
        elif func_option == 9:
            input('we are currentky on function 9')
# 

# 10TH FUNCTION 's'
# Saves receipts and inventory to an online database
        elif func_option == 10:
            input('we are currentky on function 10')


# 11th FUNCTION 'g'
# changes item data of item in inventory
        elif func_option == 11:
            input('we are currentky on function 11')
            input_item_return = input_existing_item()

            item_id = input_item_return[0]
            alt_option_pressed_func_number = input_item_return[0]
            alt_options_pressed_TorF = input_item_return[-1]

            if alt_options_pressed_TorF:
                return alt_option_pressed_func_number
            
            set_inputted_answers = set()
            set_all_valid_settings = set('n','e', 't')
            question = 'Enter n to change the name, enter e to change the price, enter t to change the stock, enter h to coninue'

            while True:
                answer = question_and_answer(question, set_all_valid_settings)

                set_inputted_answers.add(answer)

                if set_inputted_answers == set_all_valid_settings:
                    break
                elif answer == 'h':
                    break

            str_item_data = item_data_in_memory[item_id][0] + '|'+ str(item_data_in_memory[item_id][1]) + '|' + str(item_data_in_memory[item_id][2])

            if 'n' in set_inputted_answers:
                new_item_name = input_existing_item(False)
            elif 'e'in set_inputted_answers:
                print()
            elif 't' in set_inputted_answers:
                print()
            
            
            
            
            










# example item data in memory (dictionary) = {'cart_in_memory': {'i1'}, 'i1': ['GTX1050_2GB', 3000.01, 198]}
# ok lets build the product line

# shit now we gotta use the hidden jiujitsu the infinite list thig because what if they want
# to change everything yeah i feel like that basically like that could be a thing like
# that they acutally want to change all things and i dont want to have like 6 things to choos
# from i say lets make a set and theok lets make antoehr set and another while true loop then like
# basically like yeah figure this shit out i feel like yeah




# i also wanted to add another feature which its gonna be very hard to add now but its a really cool feature that i feel like is very important but to actually organise the receipts in date order so basically
# the receipts are organised in number order based on the receipt that they are made orwhatveer but then also what i would like is that they are stored in date order so bsaiclly today is idk x date and then
# what i would like is that i could somehow tell the file system to create a file thats name is just the date that the file is created


# ALSO THIS TIME REMEBER T UPDAT ETHE MEMROY UNLIKE LAST TIME YEAH REMEMBER THAT so whatever changes we gotta
# also refelct that in the memory
# ok now they can choose whwat to change the stock the name or the price









current_cart = {}
item_data_in_memory = {'cart_in_memory' : set()}
receipt_text_memory = [(' '), '']
default_start_selected_option = 1
current_receipt_number_mem = 1

selected_option = default_start_selected_option

todays_date = 0
todays_folder_path = 0
todays_receipt_folder_name = 0


# loading prerequestite information
auto_load_current_receipt_number()
auto_load_todays_receipts_path_plus_date()
auto_load_create_todays_receipt_folder()

print(current_receipt_number_mem)

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