import mmap


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
        return 4, True
    elif _str_input == 'l':
        return 5, True
    elif _str_input == 'r':
        return 6, True
    elif _str_input == 't':
        return 7, True
    else:
        return _str_input, False

def auto_load_current_receipt_number():
    global current_receipt_number

    with open('Receipt_number_log/Receipt_num_log.txt', 'r') as f:
    # Create a memory-mapped view of the file
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mmap_file:
            byte_string_current_receipt_number = mmap_file.read()
            int_current_receipt_number = int.from_bytes(byte_string_current_receipt_number, byteorder='big')
            current_receipt_number = int_current_receipt_number
            print(current_receipt_number)




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
    global str_current_receipt_number_mem

    receipt_number_ = input('What receipt number would you like to select?')

    alt_option_press_test_return = alt_option_press_test(receipt_number_)
    alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
    alt_option_pressed_func_number_return = alt_option_press_test_return[0]

    if (receipt_number_.isdigit()) and (receipt_number_ is not '0'):
        str_current_receipt_number_mem = receipt_number_

    elif alt_options_pressed_TorF_return:
        return alt_option_press_test_return
    
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