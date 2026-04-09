import mmap

#so the goal is we input a string e.g i1 then this code is supposed to search in the database for that code ok so basically fucntions are actually more efficient and in fact simplerso waht do we do now... eish i
#idk waht to do with this code hmmm. guess we could just like SIGH fuck ill talk to troy about it


def check_idigit_format(input):
    if input == '':
        input = None
    elif not input_variable.startswith('i'):
        input_variable = None
    elif not input_variable[1:].isdigit():
        input_variable = None
    else:
        idigit_format_correct = True
        test = input('Input variable follows the idigit format')

    if idigit_format_correct:
            test = input('Input variable follows the idigit format')
    return idigit_format_correct
    
def turns_function_to_object


def mmaps_inventory():
    with open('Inventory.txt', 'r+') as file:
        mmap_of_inventory = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
        return mmap_of_inventory


def item_search_selection():
    item_we_searching_for = input('Write down the item we are searching for: ')
    item_search_selection = item_we_searching_for
    return item_search_selection



def product_data_info(mmap_inventory, item_identifier):
    byte_array_data_item_we_searching_for = item_identifier.encode('utf-8')
    input_item_position_in_inventory = mmap_inventory.find(byte_array_data_item_we_searching_for)
    
    if input_item_position_in_inventory != -1:
        #Move the pointer to the beginning of the line
        mmap_inventory.seek(input_item_position_in_inventory)
        line = mmap_inventory.readline().decode('utf-8')
        return line.strip()  # Remove leading/trailing whitespaces
    else:
        return None
    
mmaps_inventory()
#item_search_selection()

idigit_format_checker(item_search_selection_object.input)
product_data_info(mmaps_inventory, item_search_selection())



class ItemSearchSelectionObject:
    def __init__(self):
        self.input = item_search_selection()

def item_search_selection_object():
    return ItemSearchSelectionObject()

# Use the returned object in the same scope
search_object = item_search_selection_object()
idigit_format_checker(search_object.input)