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



current_cart = {'i1' : 1}
item_id_ = 'i1'
item_data_in_memory = {'cart_in_memory' : set()}

item_data_memory_management(current_cart)
item_info_address_ = 'Inventory/' + item_id_ + '.txt'
change_inventory_stock(item_id_, item_info_address_, '-1')