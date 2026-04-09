import mmap
import os

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

def receipt_number_log_and_mem_updater(str_updated_receipt_number, selected_option, update_hardrive_yorn):
    global current_receipt_number_mem

    # updates memory
    if selected_option == 'u': # u is add one which we are gonna add to the end of the function
        int_updated_receipt_number= int(current_receipt_number_mem) + 1
        str_updated_receipt_number_ = str(int_updated_receipt_number)
        current_receipt_number_mem = str_updated_receipt_number_
    elif selected_option == 'i': # i is update
        current_receipt_number_mem = str_updated_receipt_number
    else:
        print("ERROR: variable 'selected_option' WAS NOT PARSED: 'selected_option' was not assigned a compatible value")

    # updates hardrive
    if update_hardrive_yorn == 'y':
        bytestr_updated_receipt_number = str_updated_receipt_number.encode('utf-8')
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


def receipt_number_selection_func():
    global current_receipt_number_mem

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

current_receipt_number_mem = '1'
print(current_receipt_number_mem + ' before change')
auto_load_current_receipt_number()
print(current_receipt_number_mem + ' after change')

if True:
    receipt_number_selection_func()

print(current_receipt_number_mem)
print('mem receipt number')

with open('Receipt_number_log/Receipt_num_log.txt', 'r') as f___:
    current_receipt_number_hard = f___.read()

print(current_receipt_number_hard)
print('harddrive receipt number')