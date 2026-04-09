# ok so basically we are gonna make the functions access the item information in memory then absically read that stock then like eyah and then in the ANY FUNCTIONS THAT CHAGNES THE STOCK we gotta make sure we adjust
# the stock in memory and in permanent hardrive space accordingly yeah basically do both to minimize operating system I/O operations so then basically we maximise computing power avaialbe ok lwra

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
        return 4, True
    elif _str_input == 'l':
        return 5, True
    elif _str_input == 'r':
        return 6, True
    elif _str_input == 't':
        return 7, True
    else:
        return _str_input, False
    
import mmap

import mmap

def load_inventory_data(input_cart):
    global required_inventory_data
    cart_in_memory_ = required_inventory_data['cart_in_memory']

    if cart_in_memory_ != input_cart:
        required_inventory_data['cart_in_memory'] = input_cart
        unique_input_cart_item_set = set(input_cart)
        for unique_input_cart_item in unique_input_cart_item_set:
            if not (unique_input_cart_item in required_inventory_data):
                item_address = 'Inventory/' + unique_input_cart_item + '.txt'
                f =  open(item_address, 'r')
                mmaped_f = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                byte_str_file_contents = mmaped_f.read()
                byte_str_product_info = byte_str_file_contents.split(b'|')

                decoded_name = byte_str_product_info[0].decode('utf-8')
                decoded_price = float(byte_str_product_info[1].decode('utf-8'))
                decoded_stock = int(byte_str_product_info[2].decode('utf-8'))

                item_data = (decoded_name, decoded_price, decoded_stock)
                required_inventory_data[unique_input_cart_item] = item_data
            elif not (required_inventory_data[unique_input_cart_item] in unique_input_cart_item_set):
                del required_inventory_data[unique_input_cart_item]
    try:
        f.close()
    except UnboundLocalError:
        pass
    try:
        mmaped_f.close()
    except UnboundLocalError:
        pass








def prints_stock_in_inventory():
    global item_data_in_memory

    while True:
        item_identifier = input('\nEnter the item you want to check the stock of.\n ---->')

        alt_option_press_test_return = alt_option_press_test(item_identifier)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
        alt_option_pressed_func_number_return = alt_option_press_test_return[0]

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
            f.close()
            mmaped_file.close()
            print('closing files')
            return alt_option_pressed_func_number_return
        else:
            print('Monkey enter an item that follows the idigit format')

    


# ok now akll we gotta d is tak ehte byte item info then basically check out the last group of the lsiced
# i feel like that if i want this code to have the maximum upgradibility i feell ike using
# the extract desired information funciton would be a tad bit more inefficeint but make hte code
# a lot more readable and more upgradble


















current_cart = {'i2' : 3, 'i4' : 4}


required_inventory_data = {'cart_in_memory' : []}
print(required_inventory_data)
print(current_cart)
load_inventory_data(current_cart)
print(required_inventory_data)

prints_stock_in_inventory()