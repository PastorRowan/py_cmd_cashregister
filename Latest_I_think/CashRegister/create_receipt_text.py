import mmap
import copy

def load_inventory_data(l_item_list__):

    l_item_list = copy.deepcopy(l_item_list__)

    global required_inventory_data
    for item in l_item_list:
        if item != None:
            for item_ in l_item_list:
                if item_ == item:
                    l_item_list[l_item_list.index(item_)] = None
            item_address = 'Inventory/' + item + '.txt'
            f =  open(item_address, 'r')
            mmaped_f = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

            file_contents = mmaped_f.read()
            product_info = file_contents.split(b'|')

            decoded_name = product_info[0].decode('utf-8')
            decoded_price = float(product_info[1].decode('utf-8'))
            decoded_stock = int(product_info[2].decode('utf-8'))

            item_data = (decoded_name, decoded_price, decoded_stock)

            required_inventory_data[item] = item_data
    f.close()
    mmaped_f.close()

def sum_total_receipt(s_input_item_list): # i guess this is useful if perahps you just wantto
    # wantto see the total of the shopping cart and you dc about the receipt
    # i guess its a tool worth keeping around
    global required_inventory_data
    print(s_input_item_list)
    item_set = set(s_input_item_list)
    print(item_set)
    input('')
    total = 0
    for item in item_set:
        number_of_item = s_input_item_list.count(item)
        int_number_of_item = int(number_of_item)
        price_of_product = required_inventory_data[item][1]
        total_of_item = int_number_of_item * price_of_product
        total += total_of_item
    return total

required_inventory_data = {}
g_item_list = ['i1', 'i1', 'i2', 'i2', 'i2', 'i3', 'i4']


def create_receipt_text(crt_item_list):
    float_total = 0.
    global required_inventory_data
    receipt_text_list = []
    unique_item_list = []
    for _element in crt_item_list:
        if _element not in unique_item_list:
            unique_item_list.append(_element)

    for item in unique_item_list:

        int_number_of_item = crt_item_list.count(item)
        float_total_item = int_number_of_item * required_inventory_data[item][1]
        str_number_of_item = str(int_number_of_item)
        str_product_name = required_inventory_data[item][0]
        str_total_item = str(float_total_item)

        product_line = str_number_of_item + 'x ' + str_product_name + ' ' + str_total_item + '\n'
        receipt_text_list.append(product_line)
        float_total += float_total_item

    str_total = str(float_total)
    total_line = '\n' + str_total
    receipt_text_list.append(total_line)

    receipt_text = ''.join(str(element_) for element_ in receipt_text_list)
    
    return receipt_text



        

# i guess it would be random like if you have an element now and then but i mean.
# so what order do we want do we want the order of items displayed on the receipt text
# to be related to hte order at which you write them down or you want the order
# to be random. i guess what i could do is make it that they are the order
# at which you entered them which would require you to not use a set and instead idk
# some kind of wank function that removes recurring elements in a lsit


required_inventory_data = {}
g_item_list = ['i1', 'i1', 'i2', 'i2', 'i2', 'i3', 'i4']

load_inventory_data(g_item_list)
print(g_item_list)

receipt_text = create_receipt_text(g_item_list)

print(receipt_text)