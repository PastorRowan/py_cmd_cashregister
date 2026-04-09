import copy
import mmap
from tokenize import endpats
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
        return 4, True
    elif _str_input == 'l':
        return 5, True
    elif _str_input == 'r':
        return 6, True
    elif _str_input == 't':
        return 7, True
    else:
        return _str_input, False

def append_item_cart_func():
    global current_cart

    while True:
        item_ = input('lets add an item\n ---> ')

        alt_option_press_test_return = alt_option_press_test(item_)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
        alt_option_pressed_func_number_return = alt_option_press_test_return[0]

        item_info_address = 'Inventory/' + item_ + '.txt'

        if alt_options_pressed_TorF_return:
            return alt_option_press_test_return
        elif not idigit_format_checker(item_):
            print('\nEnter an item that follows the correct idigit format\n')
        elif not path.exists(item_info_address):
            print('\nEnter an item in the inventory\n')
        else:
            current_cart.append(item_)


def change_cart_func():
    alt_option_pressed_func_number_return = 2
    global current_cart

    if current_cart != []:
        while True:
            item_position_cP = input('Enter item position you want to change? e.g 2 is equal to the 2nd item in the list \n ----> ')

            alt_option_press_test_return = alt_option_press_test(item_position_cP)
            alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
            alt_option_pressed_func_number_return = alt_option_press_test_return[0]

            if (item_position_cP.isdigit) and (0 <= (item_position_cP - 1) < len(current_cart)):
                while True:
                    item_replacement_cP = input('Enter the item you want in the item postion \n ----> ')

                    alt_option_press_test_return = alt_option_press_test(item_replacement_cP)
                    alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
                    alt_option_pressed_func_number_return = alt_option_press_test_return[0]

                    if idigit_format_checker(item_replacement_cP):
                        current_cart[int(item_position_cP) - 1] = item_replacement_cP
                        return alt_option_press_test_return
                    
                    elif alt_options_pressed_TorF_return:
                        return alt_option_press_test_return 
                    else:
                        print('Please enter items using the correct idigit format or alternative options only.')
                    
            elif alt_options_pressed_TorF_return:
                return alt_option_press_test_return
            
            else:
                print('Please enter postive integers or alternative options only.')
    else:
        print('Please enter an item into the item list before using the change cart function.')
        alt_option_press_test_return = (1, True)
        return alt_option_press_test_return

def insert_cart_func():
    alt_option_pressed_func_number_return = 3

    while True:
        item_position_iP = input('Enter item position you want to inesrt your item? e.g 2 is equal to the 2nd item in the list \n ---->')

        alt_option_press_test_return = alt_option_press_test(item_position_iP)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
        alt_option_pressed_func_number_return = alt_option_press_test_return[0]
        
        if item_position_iP.isdigit():
            while True:
                item_addition_iP = input('''Enter the item you want in the item postion \n ---->''')

                alt_option_press_test_return = alt_option_press_test(item_position_iP)
                alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
                alt_option_pressed_func_number_return = alt_option_press_test_return[0]

                if idigit_format_checker(item_addition_iP):
                    g_item_list.insert(int(item_position_iP) - 1, item_addition_iP)
                    return alt_option_pressed_func_number_return

                elif alt_options_pressed_TorF_return(item_addition_iP):
                    return alt_option_pressed_func_number_return

        elif alt_options_pressed_TorF_return(item_position_iP):
            return alt_option_pressed_func_number_return
        

# < 5TH FUNCTION
# inventory data memory gets loaded affter a certain point

def load_inventory_data(l_item_list):
    global required_inventory_data
    unique_item_set = set(l_item_list)
    for unique_item in unique_item_set:
        item_address = 'Inventory/' + unique_item + '.txt'
        f =  open(item_address, 'r')
        mmaped_f = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        byte_str_file_contents = mmaped_f.read()
        byte_str_product_info = byte_str_file_contents.split(b'|')

        decoded_name = byte_str_product_info[0].decode('utf-8')
        decoded_price = float(byte_str_product_info[1].decode('utf-8'))
        decoded_stock = int(byte_str_product_info[2].decode('utf-8'))

        item_data = (decoded_name, decoded_price, decoded_stock)
        required_inventory_data[unique_item] = item_data

    f.close()
    mmaped_f.close()


# 4TH FUNCTION 'u'
# prints current receipt of shopping cart
        
# 5TH FUNCTION 'l'
# creates file of shopping cart

def create_receipt_text_func(input_cart): # take reciept_text_memoryies documented item list then ocmapre that to the impt 
    float_total = 0.
    global required_inventory_data
    global receipt_text_memory

    receipt_text_in_memory = receipt_text_memory[0]
    receipt_text_cart = receipt_text_memory[1]

    if (input_cart != []) and (input_cart != receipt_text_in_memory):
        receipt_text_list = []
        unique_item_list = [] # could make this a tuple to save memory because we are not actually ediitng the datastruuter so therefore we can like
    # basically

    # ok now basically wat we want to do is basically run hte item set thing. ok we have an item list with only unique elements now basically
    # waht i need to do is basically wait yeah thats it i did it. yeah ok now i want ot return hte receipt text memory baisally when its done
        for _element in input_cart:
            if _element not in unique_item_list:
                unique_item_list.append(_element)

        for item in unique_item_list:
            int_number_of_item = input_cart.count(item)
            float_total_item = int_number_of_item * required_inventory_data[item][1]
            str_number_of_item = str(int_number_of_item)
            str_product_name = required_inventory_data[item][0]
            str_total_item = str(float_total_item)

            product_line = str_number_of_item + 'x ' + str_product_name + ' ' + str_total_item + '\n'
            receipt_text_list.append(product_line)
            float_total += float_total_item

        str_total = str(float_total)
        total_line = '\n' + str_total
        receipt_text_list.append(total_line)

        receipt_text = ''.join(str(element_) for element_ in receipt_text_list)

        receipt_text_memory = []
        receipt_text_memory.append(receipt_text)
        receipt_text_memory.append(input_cart)

        return receipt_text
    
    elif input_cart != []:
        receipt_text = receipt_text_in_memory
        print('Your shopping cart is empty, no changes were made to the receipt text in memory')
        return receipt_text

    elif input_cart != receipt_text_memory[1]:
        receipt_text = receipt_text_memory[0]
        print('Your shopping cart is exactly the same, no changes were made to the receipt text in memory')
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
    global required_inventory_data
    global receipt_text_memory

    if (receipt_str is not None) and (required_inventory_data is not {}):
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
                        return 1
                    elif answer == 'n': # said no
                        return alt_option_pressed_func_number_return
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

def complete_program_loop(func_option): # selected 's' by default
    global current_cart

    while True:
# 1ST FUNCTION 's'
# appends item to shopping cart
        if func_option == 1:
            input('we are currentky on function 1')
            append_item_cart_return = append_item_cart_func()

            append_item_cart_alt_option_pressed_TorF = append_item_cart_return[-1]
            append_item_cart_alt_option_pressed_func_number = append_item_cart_return[0]

            if append_item_cart_alt_option_pressed_TorF:
                return append_item_cart_alt_option_pressed_func_number



# 2ND FUNCTION 'c'
# change item in shopping cart
        elif func_option == 2:
            input('we are currentky on function 2')
            change_cart_return = change_cart_func() # ok if i want to degu agin instead of using input ommands just forcean error thats genius

            change_cart_alt_option_pressed_TorF = change_cart_return[-1]
            change_cart_alt_option_pressed_func_number = change_cart_return[0]

            if change_cart_alt_option_pressed_TorF:
                return change_cart_alt_option_pressed_func_number
            change_cart_func(20)

# 3RD FUNCTION 'i'
# inserts item into shopping cart
        elif func_option == 3:
            input('we are currentky on function 3')
            insert_cart_return = insert_cart_func()

            insert_cart_alt_option_pressed_TorF = insert_cart_return[-1]
            insert_cart_alt_option_pressed_func_number = insert_cart_return[0]

            if insert_cart_alt_option_pressed_TorF:
                return insert_cart_alt_option_pressed_func_number
            



# 4TH FUNCTION 'u'
# prints current receipt of shopping cart
        elif func_option == 4:
            input('we are currentky on function 4')
            receipt_text = create_receipt_text_func(g_item_list)
            print(receipt_text)
            return 1

# 5TH FUNCTION 'l'
# creates file of shopping cart
        elif func_option == 5:
            input('we are currentky on function 5')
            creates_receipt_file_return = creates_receipt_file_func(receipt_text) # [0]= str_receipt_number, [1] = pressed_option, [2]=mmpaed_receipt_number_database

            creates_receipt_alt_option_pressed_TorF = creates_receipt_file_return[-1]
            creates_receipt_alt_option_pressed_func_number = creates_receipt_file_return[0]

            if creates_receipt_alt_option_pressed_TorF:
                return creates_receipt_alt_option_pressed_func_number
                

# 6TH FUNCTION ''
# prints stock of items in inventory
# reads memory of inventory and if it isnt available reads harddrive inventory
        elif func_option == 6:
            input('we are currentky on function 6')


# 7TH FUNCTION 't'
# changes stock in inventory
        elif func_option == 7:
            input('we are currentky on function 7')
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






























current_cart = []
required_inventory_data = {}
receipt_text_memory = []
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