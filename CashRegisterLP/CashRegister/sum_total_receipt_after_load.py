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


# jesus christ my mind is paralised by choice fuck. ok so we have like 3 ways of solving this
# problem basically we could just take the list then get the count of an elelnt
# then times the amount by
# holy shit ok so basically i got another idea lets create a set that basically takes all the
# item in the list and adds them to the set because sets cant take duplicates then after that
# the program count the occurences of all unique items in the set ist like ok i1 occurs this
# amount of times and i2 this amount of times then after that then it takes the count
# then times it by the price of hte product for each unique thing then basically we add the 
# product (times referenece) to the total and keep doing so until basically yeah we done.
# is this the most efficient solution??? i mean sound efficient to me fuck it im doing it
# i made another mistake bro i misued my enegru i could of spent my energ acuatlly writing code
# not talkinga obutit to soemone that aint gonna help me with whatever i feel like that like yeah.
# i mean i thouht he might also code in python and then like yeah he could help me with some shit but nah
# i feel like that like what are my next goals well basically i can make a sum_total using the data stored in memory
# now i fee like the next step would be to be able to print a receipt which shouldnt be hard but would require a change in the code but tbh i feel like taking
# a break then i am gonna get back to it

def sum_total_receipt(s_input_item_list):
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


def ergonomic_anal_device(ead_item_list):
    global required_inventory_data
    load_inventory_data(g_item_list)
    total = sum_total_receipt(g_item_list)
    print(total)

load_inventory_data(g_item_list)
total = sum_total_receipt(g_item_list)
print(total)