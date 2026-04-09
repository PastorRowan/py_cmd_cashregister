
import mmap

def main_processing_item_info_collection(item_identifier, data_type_identifier, close_file_TorF, edit_file_TorF): # True = yes, False = no
    error_TorF = False

    item_relative_address_pathyway = 'Inventory/'+ str(item_identifier) + '.txt'
    if edit_file_TorF:
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




def sum_total_receipt(s_input_item_list):
    for item in s_input_item_list:# True = yes, False = no
        if not item.isdigit(): # we could also use the idiigt format checker if we start experieincing bugs
            if s_input_item_list.count(item) > 1:
               item_info_collection_return = main_processing_item_info_collection(item, 'p', True, False)
               price_of_product = item_info_collection_return[0]
               while True:
                    try:
                        item_index = s_input_item_list.index(item)
                        s_input_item_list[int(item_index)] = price_of_product
                    except ValueError:
                        break
            elif s_input_item_list.count(item) == 1:
               price_of_product = main_processing_item_info_collection(item, 'p', True, False) # True = yes, False = no
               item_index = s_input_item_list.index(item)
               s_input_item_list[int(item_index)] = price_of_product

    total = sum(s_input_item_list)
    return total