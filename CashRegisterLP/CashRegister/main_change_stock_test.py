
import mmap




def main_processing_item_info_collection(item_identifier, data_type_identifier, close_file_TorF, edit_file):
    error_TorF = False

    item_relative_address_pathyway = 'Inventory/'+ str(item_identifier) + '.txt'
    if edit_file:
        file = open(item_relative_address_pathyway, 'r+')
        mmaped_item_info = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_WRITE)
    else:
        file = open(item_relative_address_pathyway, 'r')
        mmaped_item_info = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)


    bytes_data_type_identifier = data_type_identifier.encode('utf-8')

    # Find the index of data type identifier in mmaped item information file
    index_data_type_identifier = mmaped_item_info.find(bytes_data_type_identifier)

    # Find the index of the first down line after the specified data type identifier
    index_down_line_after_data_type_identifier = mmaped_item_info.find(b'|', index_data_type_identifier)

    # Extract the substring between identifier and the first down line after identifier
    if index_data_type_identifier != -1 and index_down_line_after_data_type_identifier != -1:
        bytes_selected_data = mmaped_item_info[index_data_type_identifier + 1 : index_down_line_after_data_type_identifier]
        str_selected_data = bytes_selected_data.decode('utf-8')
    elif index_data_type_identifier == -1:
        print("ERROR: item's data_type_identifier tag was not identified in inventory, find function returned -1, error in inventory")
        error_TorF = True
    elif index_down_line_after_data_type_identifier == -1:
        print("ERROR: item's '|' after data_type_identifier was not identified in inventory, find function returned -1, error in inventory")
        error_TorF = True
    
    if error_TorF:
        file.close()
        mmaped_item_info.close()
        return (None,)
    elif close_file_TorF:
        file.close()
        mmaped_item_info.close()
        return (str_selected_data,)
    else:
        return str_selected_data, file, mmaped_item_info
    

# so basically i hate writing file.close mmaped item info.clsoe and wthawver i felel ike i jsut need to write it once beause i will always perform that action after these if staetments and shit but hte reutnr 
# staetment is gettig i nthe way because once you return a value then the code below the reutn stamente will not run so basically waht i guess i could do is say ok if this is true make
# error_checker = False else if its not true then yeah then else: reutnr none

#7th function 't'
def main_processsing_change_stock_inventory(item_identifier, int_change_of_stock):
    edit_file = True
    close_file_TorF = False
    _item_identifier = item_identifier

    item_info_collection_return = main_processing_item_info_collection(_item_identifier, 's', close_file_TorF, edit_file)

    mmaped_item_info = item_info_collection_return[-1]
    file = item_info_collection_return[1]
    str_current_stock = item_info_collection_return[0]

    if str_current_stock[0] != None:
        str_byte_current_stock = str_current_stock.encode('utf-8')
        int_current_stock = int(str_current_stock)
        int_new_stock = int_current_stock + int_change_of_stock
        str_new_stock = str(int_new_stock)
        str_byte_new_stock = str_new_stock.encode('utf-8')
        byte_current_item_info = mmaped_item_info.read()
        byte_new_item_info = byte_current_item_info.replace(str_byte_current_stock, str_byte_new_stock)
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
    else:
        return None
    
main_processsing_change_stock_inventory('i1', 1)