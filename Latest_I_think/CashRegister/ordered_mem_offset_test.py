import mmap
from collections import OrderedDict


def item_info_extraction(item_id, mem_item_info_extract_list):
    global memory_module

    for mem_id in mem_item_info_extract_list:
        mem_block = memory_module[mem_id]
        if item_id not in mem_block:
            return
        else:
            item_address = 'Inventory/' + item_id + '.txt'
            f =  open(item_address, 'r')
            mmaped_f = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            byte_str_file_contents = mmaped_f.read()
            byte_str_product_info = byte_str_file_contents.split(b'|')

            decoded_name = byte_str_product_info[0].decode('utf-8')
            decoded_price = float(byte_str_product_info[1].decode('utf-8'))
            decoded_stock = int(byte_str_product_info[2].decode('utf-8'))

            item_data = [decoded_name, decoded_price, decoded_stock]
            return item_data


def adds_item_data_to_mem(item_id, item_data, memory_add_list):

    for mem_id in memory_add_list:
        mem_block = global_mem_mods[mem_id]
        mem_block[item_id] = item_data





def removes_item_s_from_mem(int_amount_items_remove, memory_remove_list): # this is gonna change
    global global_mem_mods

    for mem_id in memory_remove_list:
        mem_block = memory_module[mem_id]

        keys_to_remove = list(mem_block.keys())[:int_amount_items_remove]
        for key in keys_to_remove:
            del mem_block[key]











def item_info_count(memory_current_item_count_list):
    global global_mem_mods

    dic_stack_count = {}

    for mem_id in memory_current_item_count_list:
        mem_mod = global_mem_mods[mem_id]
        int_item_info_slot_count = mem_mod['int_items_data_mem']
        dic_stack_count[mem_id] = int_item_info_slot_count

    return dic_stack_count


def stack_overflow_checker(dic_stack_count, int_item_info_add):

    maximum_mem_threshhold = 128
    dic_mem_id_plus_overflow_int = {}

    for key in dic_stack_count:
        int_item_info_slot_count = dic_stack_count[key]
        if (int_item_info_slot_count + int_item_info_add) > maximum_mem_threshhold:
            return dic_mem_id_plus_overflow_int, True
        else:
            return dic_mem_id_plus_overflow_int, False
    return


cart_item_info_mem_mod = {'cart_item_info_mem' : {'i1' : [], 'i2': [], 'i3' : []}, 'int_items_data_mem' : 3}

extra_item_info_mem_mod = {'extra_item_info_mem' : {'i1' : [], 'i2': [], 'i3' : []}, 'int_items_data_mem' : 3}

global_mem_mods = {'cart_items_mem_mod' : cart_item_info_mem_mod, 'extra_items_mem_mod' : extra_item_info_mem_mod}

# OK lets get started on the i guess virtual memory device ok so lets get it conceptually down.
# so basically we are gonna have a virtually memory folder that will contain virtual memory for different mem_mods ok and the mem_mod ids will or mem_ids will dwefeitely be useful to figure out which is which andwhatver so
# basicaly waht my plan is tomorrow is see how we can store virutal memroy but also see ok when will virtual memory be arpobe,so what stutions could arrise that require irtual memroy ok if the mem item info coutn si over 128
# so the real question is when would it be over 128 so if we have a MASSIVE shopping cart. i guess perahps maybe we would want to check the stock of mutiple items perahps like lets say we want to chek cthe stock of
# 160 items at ocne then virtual memory could come in handy and then we could even introducesome kind of chunk loading as well which would be genius that the printer like basically prints the things in chunks WHEN ONLY WHEN
# dealing with virtual memory that makes sense. so basically it doesnt load eveyting into memory at once just one item at a time it will read and extract info or we could even have a setting that checks the files size
# because that would be stored on the operating systesm and then say ok if its above a certain size like lets say 1kb idk just so wecan test it xD then chunk loading will be used to extract info
# otherwise then we will just extract it all at once which would make perfect sense. i feel like yeah. thats quite crazyok s then absically we would need to take x the amount of stack overflow then basicaly
# say ok we open a text file that repressents the virutal memory 