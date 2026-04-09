import mmap

def change_stock_inventory(item_identifier, int_change_of_stock):

    item_relative_address_pathyway = 'Inventory/'+ str(item_identifier) + '.txt'
    file = open(item_relative_address_pathyway, 'r+')
    mmaped_item_info = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_WRITE)
    bytes_data_type_identifier = 's'.encode('utf-8')

    # Find the index of data type identifier in mmaped item information file
    index_data_type_identifier = mmaped_item_info.find(bytes_data_type_identifier)

    # Find the index of the first down line after the specified data type identifier
    index_down_line_after_data_type_identifier = mmaped_item_info.find(b'|', index_data_type_identifier)

    # Extract the substring between identifier and the first down line after identifier
    if (index_data_type_identifier != -1) and (index_down_line_after_data_type_identifier != -1):
        byte_current_stock = mmaped_item_info[index_data_type_identifier + 1 : index_down_line_after_data_type_identifier]
        int_current_stock = int(byte_current_stock)
        int_new_stock = int_current_stock + int_change_of_stock
        str_new_stock = str(int_new_stock)
        byte_new_stock = str_new_stock.encode('utf-8')
        byte_current_item_info = mmaped_item_info.read()
        byte_new_item_info = byte_current_item_info.replace(byte_current_stock, byte_new_stock)
        str_new_item_info = byte_new_item_info.decode('utf-8')
        mmaped_item_info.close()
        new_file_size = len(str_new_item_info)
        file.truncate(new_file_size)
        file.flush()
        mmaped_item_info = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_WRITE)
        mmaped_item_info.write(byte_new_item_info)
        mmaped_item_info.flush()
        file.close()
        mmaped_item_info.close()
        return None
    elif index_data_type_identifier == -1:
        print("ERROR: item's data_type_identifier tag is missing error in inventory")
        file.close()
        mmaped_item_info.close()
        return None
    elif index_down_line_after_data_type_identifier == -1:
        print("ERROR: item's '|' after data_type_identifier tag is missing in inventory")
        file.close()
        mmaped_item_info.close()
        return None
    else:
        file.close()
        mmaped_item_info.close()
        return None
    

change_stock_inventory('i1', 1)