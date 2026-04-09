
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
    


item_data_in_memory = {'cart_in_memory' : set(), 'i1' : ('GTX1050_2GB', 3000.01, 21), 'i3': ('RX480_8GB', 4500.0, 25), 'i4': ('RX580_8GB', 4500.0, 30)}

current_cart = {'i2' : 3, 'i4' : 4}

receipt_text_memory = [tuple(), '']

item_data_memory_management(current_cart)

_receipt_text_ = create_receipt_text_func(current_cart)

print(_receipt_text_)





























# filled example: receipt_text_memory = [('i2', 'i4'), 
#'''
#2x GTX1050_2GB 6000.02
#3x GTX1060_3GB 12000.0
#1x RX480_8GB 4500.0
#1x RX580_8GB 4500.0
#
#27000.02
#'''
# not written in accordance with shopping cart

# ok now the next level is to make it that whenever there are changes in the current cart compared to hte previous cart that their is a specific program that can basically instead of creating a whole knew receipt
# text would just make adjustments based on the changes of the current cart that would be fuckign awesome i really honesly right now dont feel like it but i think a project for a lter time would be cool
# i mean all i need to do is really just record all the product lines as item info or whatever in dicionaryies then compare then take that dictioanry then run all that info through this program. wait hten yu doing the
# exact same thing. oh no but you can make minor adjustment to the ok i am gonna tjink abut htis later but i hoenstly think that the program is gonna have about hte same functionality if you do
# what i do like i nterms f computing efficieny o nah. yeah. hmm yeah nah. i mean i guess what i could do is like then make it that the changes are then tested for and then... but is this really like gonna save\
# memory having this wait no ok its worth it because with very very very very very very large receipts yes it could save A LOT of memroy if you think about it??? yeah it could if the receipt is very large
# ok well if we want our program to be more scalable then lets do it ok so we gonna have a dicitonary that has keys that have item identifiers with values that are tuples that contain 1 number of item bought
# wait thats all i need because the rest of the information is in memroy i guess i could also record the item float total??? ok we record number of item bought and float total then basically we
# compare first ok with this new cart ok are the keys the exact same. then if the keys are exactly the same then what? then check ok are the numbe rof items bought the same and then if they are different
# then its like ok they are different. if they are different then we - them from each other so elts say the difference is 1 then we take the items price then subtract 1 times the product price from the float total
# then we make that the new float total of that dictionary key then once we have done that then lets say thats the only difference then we take all the lists (values are gonna change often) of the keys of the dictionary
# then we add them all together to form one big list then we will use the join function again basically 
# ok that sounds like it could work and it seems that eh create receipt_file_func is gonna change quite a bit. yeah. for the first receipt text creation though i think ill have to use this method then after that
# then i can use this dictionary method or i can just add the item inforation to the dictioanry that is probably a way better method. ok this is deifnitely qutiea  big challege but its definitely possible
# and would save resources if this application is used for larger corpaions or needs or whatever. eyah basically eah. ok thats makes sense