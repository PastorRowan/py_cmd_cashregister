
import os
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

        elif option == 'natural numbers':

            number_is_digits_and_doesnt_start_with_0_TorF = 
            if (number.isdigit()) and not (number.startswith(0)):
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

        elif option == 'Whole number':

            number_postive_and_doesnt_start_with_0_TorF = number.isdigit() and (not number.startswith('0'))
            number_is_0_ToF = (number == '0')

            if number_postive_and_doesnt_start_with_0_TorF or number_is_0:
                return number, False
            else:
                print(incorrect_input_msg)








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
            print('Stock cannot be negative')
            return default_next_func_num, False
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
        mmaped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
        bytestr_item_info = mmaped_file.read()

        int_change_stock = int(str_change_stock)

        str_current_stock = str(int_current_stock)
        bytestr_current_stock = str_current_stock.encode('utf-8')

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









item_data_in_memory = {}


question_ = '\nEnter the item you want to change the stock of.\n ---->'

_question_ = 'Enter an integer that is not 0'


input_item_return = input_item(question_, True)

item_id = input_item_return[0]
item_info_address = input_item_return[1]
alt_option_whatever = input_item_return[-1]

input_integer_return = input_non_float_number(_question_, False)

int_change_stock = input_integer_return[0]
str_change_stock = str(int_change_stock)

change_inventory_stock(item_id, item_info_address, str_change_stock)