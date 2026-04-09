'''
import mmap

def extract_product_info():

    f =  open(file_path, 'r')
    mmaped_f = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    file_contents = mmaped_f.read()
    product_info = file_contents.split(b'|')

    decoded_name = product_info[0].decode('utf-8')
    decoded_price = product_info[1].decode('utf-8')
    decoded_stock = product_info[2].decode('utf-8')
'''

# what is my goal now ok a certain amoount of functions within our code baically need to use
# inventory data so basically wha ti wanted to do is for them to call open the current inventory
# data and then basically like use that to perform its function so basically ok i seewhat i want
# ok i see so basically we need ceratin data from theivnentory and we retrieve that through item
# info collection and basically like we need them to instead basically call upon someting else?
# yeah basically they just need to call upon the key in the diciotary to find the value instead
# of using the other thing ok that makes sense to me 
import mmap

def load_inventory_data(input_cart):
    global required_inventory_data
    try:
        cart_in_memory_ = required_inventory_data['cart_in_memory']
    except:
        required_inventory_data['cart_in_memory'] = input_cart
    unique_input_cart_item_set = set(input_cart)
    if cart_in_memory_ != input_cart:
        required_inventory_data['cart_in_memory'] = input_cart
        for unique_input_cart_item in unique_input_cart_item_set:
            if not (unique_input_cart_item in required_inventory_data):
                item_address = 'Inventory/' + unique_input_cart_item + '.txt'
                f =  open(item_address, 'r')
                mmaped_f = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                byte_str_file_contents = mmaped_f.read()
                byte_str_product_info = byte_str_file_contents.split(b'|')

                decoded_name = byte_str_product_info[0].decode('utf-8')
                decoded_price = float(byte_str_product_info[1].decode('utf-8'))
                decoded_stock = int(byte_str_product_info[2].decode('utf-8'))

                item_data = (decoded_name, decoded_price, decoded_stock)
                required_inventory_data[unique_input_cart_item] = item_data
            elif not (required_inventory_data[unique_input_cart_item] in unique_input_cart_item_set): # what do we want to check ok so we want to check if specific item_info is in cart memory but not in the cart then
                del required_inventory_data[unique_input_cart_item]

# idk if this has the feature to basically be like ok bro like 

            # we remove the item information form item_information_memory
# i think the code is now has maximum effiency ok is if the cart in memory is the same as the input_cart then nothing happens ez common rowan W then if a unqie input cart item is not in memory but in the input cart then
# obivsuly we add it to memro then if the unqiue input cart item is in memory then yeah hte code doenst run then if the input cart item is in memory but not in the input cart then we del the item from memory
# im gnna re read this tomorow iwith a fresh brain because honetly idk whats goig on but i think it makes sense

    f.close()
    mmaped_f.close()




required_inventory_data = {}
g_item_list = ['i1','i1', 'i2', 'i2', 'i2', 'i3', 'i4']
load_inventory_data(g_item_list)
print(required_inventory_data)

# o so now we wanted to eid ttis load invetory data program bascallt we wanted to make it run more efficent how did we want to achieve that. i need to now start now makingjournal entires of how i wanna change my code
# like i cant remeber fckigna ll of them basically this one changes the memory but i also want it to have the feature of basically going like ok if the item list ok then it oone way we could preven like file penign funtions
# is checking if the unique item in input unique item list already exists in memory nad then if it does then do nothing and then if it doesn . then we can just do the reverse like if unqiue item in unque item list
# does not exist then run all these checks