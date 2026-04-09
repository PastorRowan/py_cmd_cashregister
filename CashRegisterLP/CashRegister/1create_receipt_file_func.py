import mmap
from os import path

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

import mmap

def loads_and_removes_current_cart_item_s_data_to_memory(current_cart_):
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

def create_receipt_text_func(_current_cart_): # take reciept_text_memoryies documented item list then ocmapre that to the impt 
    float_sum_total = 0.
    global item_data_in_memory
    global receipt_text_memory

    current_cart_unique_item_tuple = tuple(_current_cart_.keys())

    receipt_text_cart_unique_item_tuple_memory = receipt_text_memory[0]
    receipt_text_in_memory = receipt_text_memory[1]

    if (_current_cart_ != {}) and (current_cart_unique_item_tuple != receipt_text_cart_unique_item_tuple_memory):
        receipt_text_list = [] # rename to product line building blocks

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
        receipt_text = receipt_text_memory
        print('Your shopping cart is empty, no changes were made to receipt_text_memory')
        return receipt_text

    elif current_cart_unique_item_tuple == receipt_text_cart_unique_item_tuple_memory:
        receipt_text = receipt_text_memory
        print('Your shopping cart is exactly the same, no changes were made to receipt_text_memory')
        return receipt_text
    
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

def create_receipt_file_func(receipt_str):
    global item_data_in_memory

    if (receipt_str is not None) and (item_data_in_memory is not {}):
        while True:
            str_receipt_number = input('What receipt number do you want?')

            alt_option_press_test_return = alt_option_press_test(str_receipt_number)
            alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
            alt_option_pressed_func_number_return = alt_option_press_test_return[0]

            if (str_receipt_number.isdigit()) and (str_receipt_number is not '0'):
                receipt_address = 'Receipts/' + 'receipt' + str_receipt_number + '.txt'
                if path.exists(receipt_address):
                    print('receipt does already exist')
                    question = 'enter y to overwrite file or enter n to not overwrite the file and reset the function' # still need to add the back function
                    answer = answer_y_or_n(question)

                    alt_option_press_test_return = alt_option_press_test(answer)
                    alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
                    alt_option_pressed_func_number_return = alt_option_press_test_return[0]

                    if answer == 'y': # said yes
                        # opens and deletes contents of receipt file
                        with open (receipt_address, 'w') as receipt_file:
                        # writes receipt onto receipt file
                            receipt_file.write(receipt_str)
                        return 's'
                    elif answer == 'n': # said no
                        return 's'
                    elif alt_options_pressed_TorF_return:
                        return alt_option_pressed_func_number_return
                else:
                    # creates receipt file
                    with open (receipt_address, 'w') as receipt_file:
                        # writes receipt onto receipt file
                        receipt_file.write(receipt_str)
                        break

            elif alt_options_pressed_TorF_return:
                    return alt_option_pressed_func_number_return

    elif receipt_str is None:
        print('ERROR: receipt string is == None')
    elif item_data_in_memory is {}:
        print('ERROR: no item data loaded into memory')