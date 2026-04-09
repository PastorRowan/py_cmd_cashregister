import mmap

def loads_and_removes_current_cart_item_s_data_to_memory(input_cart): # what are we gonna call this we could call this unique items input becuase the current_cart is now a dioctioanry but i dont want
    # to load unnecesusray information because hte amoutn of each product doesnt matter so i guess what we could do is create a set of all the keys in the current_cart dicitonary then input that
    global item_data_in_memory

    cart_in_memory = item_data_in_memory['cart_in_memory']
    if input_cart != []:
        if cart_in_memory != input_cart:
            unique_input_cart_item_set = set(input_cart)
            item_data_in_memory['cart_in_memory'] = input_cart
            item_data_in_memory = {key: value for key, value in item_data_in_memory.items() if key in unique_input_cart_item_set or key == 'cart_in_memory'}

            print(item_data_in_memory)
            input('item was memory but not in current cart and therefore was removed')

            for unique_input_cart_item in unique_input_cart_item_set:
                if not (unique_input_cart_item in item_data_in_memory):
                    # if item is in the current cart but not in memory
                    item_address = 'Inventory/' + unique_input_cart_item + '.txt'
                    f =  open(item_address, 'r')
                    mmaped_f = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                    byte_str_file_contents = mmaped_f.read()
                    byte_str_product_info = byte_str_file_contents.split(b'|')

                    decoded_name = byte_str_product_info[0].decode('utf-8')
                    decoded_price = float(byte_str_product_info[1].decode('utf-8'))
                    decoded_stock = int(byte_str_product_info[2].decode('utf-8'))

                    item_data = (decoded_name, decoded_price, decoded_stock)
                    item_data_in_memory[unique_input_cart_item] = item_data

                    print('unique item was in current cart but was not in memory therefore it was added')
                
                elif unique_input_cart_item in item_data_in_memory:
                    print('unique item was in current cart and in memory therefore nothing was done')
      
    else:
        print('Please Enter an item into the cart')
        return 1, True






item_data_in_memory = {'cart_in_memory' : [], 'i1' : ('GTX1050_2GB', 3000.01, 21), 'i3': ('RX480_8GB', 4500.0, 25), 'i4': ('RX580_8GB', 4500.0, 30)}

current_cart = ['i2']

loads_and_removes_current_cart_item_s_data_to_memory(current_cart)
print(item_data_in_memory)


#, 'i1' : ('GTX1050_2GB', 3000.01, 21), 'i3': ('RX480_8GB', 4500.0, 25), 'i4': ('RX580_8GB', 4500.0, 30)

    # something we could do is like have a list of all the items in the current cart and then take that list and say ok if its in. oh wait this would be perfect because like basically if
    # the items data is in the current shopping cart but not in memory then add it but if a key is in the item data memory but not in the current cart then you can get rid of it i guess???
    # so yeah idk. i have no fucking idea i guess i could take all the unqiue items absicall hte unqiue input car titme set whatever then basically go like ok ifits in hte set but not in the keys memory??? then yeah
    # so what i could do is take the set of unique items and be like ok all of these unqiue items in the current shopping cart then take all the unique items then remove them from hte list of all keys??? then
    # then basically remove all of the keys in hte same elemtns??? yes this makes sense because like the current shopping cart items are the only items we want in memro. but then i guess
    # another approach could be lets remove all of the shit in cart before hand???? then just ad new shit everytime i mean this would be a good general soltuon but i want max efficieny and i think ax efficieny
    # means waht we must do is avoid all read functions basically yeah. i feel like that maeks sense
    
    # somethingi could do is take all the keys in a dicitonary then say ok lets remove all of the keys that are the say as the elemntes in teh set then basically 
    
    
    
    
    
    
    






# imma behoenst idk wha i wrote why does this always fucking happen i think i gotta actually
# write much better docemntaiton ebcaue holy shit i dont understad what is happenign
# ok so basically if