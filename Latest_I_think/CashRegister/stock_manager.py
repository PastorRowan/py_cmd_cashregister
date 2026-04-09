import mmap



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

# we could make this stock more efficient and resble if perhaps what we do is like kinda do a prerequieiste stock ting where likethi sis a change stock functions and then you collect the ifnormation
# to change hte stock in another functions i feel like then i could reuse this function more in a sense like yeah this funciton would then become a lot more reusable

def stock_manager_func():
    global item_data_in_memory
    global str_current_receipt_number_mem
    global current_cart

    int_current_stock = None
    byte_item_info = None
    f = None
    mmaped_file = None


    while True:
        item_id = input('\nEnter the item you want to change the stock of.\n ---->')

        alt_option_press_test_return = alt_option_press_test(item_id)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
        alt_option_pressed_func_number_return = alt_option_press_test_return[0]

        if idigit_format_checker(item_id):


            if item_id in item_data_in_memory:
                int_current_stock = item_data_in_memory[item_id][2]
                print('Reading memory sss...sssss...HHHhhhh...sssss')
                print(int_current_stock)
            else:
                item_info_address = 'Inventory/' + item_id + '.txt'
                f = open(item_info_address, 'r+')
                mmaped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
                byte_item_info = mmaped_file.read()
                byte_current_stock = byte_item_info.rsplit(b'|', 1)[-1]
                print('Reading hardrive inventory sss...sssss...HHHhhhh...sssss')
                print(byte_current_stock)

            while True:
                str_change_stock = input('Enter the amount you want to change stock by')
                if (str_change_stock.isdigit() or (str_change_stock.startswith('-') and str_change_stock[1:].isdigit())) and (str_change_stock != '0'):
                    if byte_item_info != None:
                        byte_updated_item_info = byte_item_info.replace(,)
                    elif int_current_stock != None:
                        item_info_address = 'Inventory/' + item_id + '.txt'
                        f = open(item_info_address, 'r+')
                        mmaped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
                        byte_item_info = mmaped_file.read()

                        int_change_stock = int(str_change_stock)

                        str_current_stock = str(int_current_stock)
                        bytestr_current_stock = str_current_stock.encode('utf-8')

                        int_new_stock = int_current_stock + int_change_stock
                        str_new_stock = str(int_new_stock)

                        byte_updated_item_info = byte_item_info.replace(bytestr_current_stock,)






# ok lets just break this down so its easier for us to make ok so we want to now read the
# item text file then take out the stock then turn it into a string then an integer then
# we want to add or subtract from it then we want to take the item info then replace the old
# stock with the new stock then truncate the file to new size then flush changes of the mmap
# then yeah we do something else after that but first lets do this ok we alreadt git the whole
# mmaped file then all we acutally nee to do is take ot the old stock then replace it with the
# new stokc

                else:
                    print('Please enter a negative or postive integer')




        elif alt_options_pressed_TorF_return:
            f.close()
            mmaped_file.close()
            print('closing files')
            return alt_option_pressed_func_number_return
        else:
            print('Monkey enter an item that follows the idigit format')

def change_hardrive_stock(item_id, str_change_stock):

    if item_id in item_data_in_memory:
                int_current_stock = item_data_in_memory[item_id][2]
                print('Reading memory sss...sssss...HHHhhhh...sssss')
                print(int_current_stock)
    else:
        item_info_address = 'Inventory/' + item_id + '.txt'
        f = open(item_info_address, 'r+')
        mmaped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
        byte_item_info = mmaped_file.read()
        byte_current_stock = byte_item_info.rsplit(b'|', 1)[-1]
        print('Reading hardrive inventory sss...sssss...HHHhhhh...sssss')
        print(byte_current_stock)


    if byte_item_info != None:
        byte_updated_item_info = byte_item_info.replace(,)
    elif int_current_stock != None:
        item_info_address = 'Inventory/' + item_id + '.txt'
        f = open(item_info_address, 'r+')
        mmaped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
        byte_item_info = mmaped_file.read()

        int_change_stock = int(str_change_stock)

        str_current_stock = str(int_current_stock)
        bytestr_current_stock = str_current_stock.encode('utf-8')

        int_new_stock = int_current_stock + int_change_stock
        str_new_stock = str(int_new_stock)

        byte_updated_item_info = byte_item_info.replace(bytestr_current_stock,)
