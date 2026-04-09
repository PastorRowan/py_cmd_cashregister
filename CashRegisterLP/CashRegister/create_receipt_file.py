import mmap
from os import path

def answer_y_or_n(_question):
    while True:
        _answer = input(_question)

        alt_option_press_test_return = alt_option_press_test(_answer)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
        alt_option_pressed_func_number_return = alt_option_press_test_return[0]

        if _answer == 'y':
            return _answer
        elif _answer == 'n':
            return _answer
        elif alt_options_pressed_TorF_return:
            return alt_option_pressed_func_number_return
        else:
            print('\nEnter y or n or a special option\n\n ---->')

def alt_option_press_test(_str_input): # else retrn _str input??? idk
    if _str_input == 'p':
        return 'p', True
    elif _str_input == '/':
        return '/', True
    elif _str_input == 'c':
        return 2, True
    elif _str_input == 'i':
        return 3, True
    elif _str_input == 's':
        return 1, True
    elif _str_input == 'u':
        return 4, True
    elif _str_input == 'l':
        return 5, True
    elif _str_input == 'r':
        return 6, True
    elif _str_input == 't':
        return 7, True
    else:
        return _str_input, False

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

def load_inventory_data(l_item_list):
    global required_inventory_data
    unique_item_set = set(l_item_list)
    for unique_item in unique_item_set:
        item_address = 'Inventory/' + unique_item + '.txt'
        f =  open(item_address, 'r')
        mmaped_f = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        byte_str_file_contents = mmaped_f.read()
        byte_str_product_info = byte_str_file_contents.split(b'|')

        decoded_name = byte_str_product_info[0].decode('utf-8')
        decoded_price = float(byte_str_product_info[1].decode('utf-8'))
        decoded_stock = int(byte_str_product_info[2].decode('utf-8'))

        item_data = (decoded_name, decoded_price, decoded_stock)
        required_inventory_data[unique_item] = item_data

    f.close()
    mmaped_f.close()

def prerequesite_information_collection_and_main_processing_creates_receipt_file(receipt_str):
    global required_inventory_data

    if (receipt_str is not None) and (required_inventory_data is not {}):
        while True:
            str_receipt_number = input('What receipt number do you want?')

            alt_option_press_test_return = alt_option_press_test(str_receipt_number)
            alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
            alt_option_pressed_func_number_return = alt_option_press_test_return[0]

            if (str_receipt_number.isdigit()) and (str_receipt_number is not '0'):
                receipt_address = 'Receipts/' + 'receipt' + str_receipt_number + '.txt'
                if path.exists(receipt_address):
                    print('receipt does already exist')
                    question = 'enter y to overwrite file or enter n to not overwrite the file and reset the function' # still need to add the back function
                    answer = answer_y_or_n(question)

                    alt_option_press_test_return = alt_option_press_test(answer)
                    alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
                    alt_option_pressed_func_number_return = alt_option_press_test_return[0]

                    if answer == 'y': # said yes
                        # opens and deletes contents of receipt file
                        with open (receipt_address, 'w') as receipt_file:
                        # writes receipt onto receipt file
                            receipt_file.write(receipt_str)
                        return 's'
                    elif answer == 'n': # said no
                        return 's'
                    elif alt_options_pressed_TorF_return:
                        return alt_option_pressed_func_number_return
                else:
                    # creates receipt file
                    with open (receipt_address, 'w') as receipt_file:
                        # writes receipt onto receipt file
                        receipt_file.write(receipt_str)
                        break

            elif alt_options_pressed_TorF_return:
                    return alt_option_pressed_func_number_return




# ok we are facing a bit of a problem here basically what we coul do is either have a receipt number database or we could just use the path.exist method to check if a file exists i think hypthetically the receipt
# number database would require less computing power but tbh shit im actually starting to see my quest for effiiecny work holy shit after the program has loaded the necessary information into memory the fucking
# program is blitzvinnig that is the goal. the program must be blitz vinning and very efficeint

    elif receipt_str is None:
        print('ERROR: receipt string is == None')
    elif required_inventory_data is {}:
        print('ERROR: no item data loaded into memory')


required_inventory_data = {}
g_item_list = ['i1', 'i1', 'i2', 'i2', 'i2', 'i3', 'i4']

load_inventory_data(g_item_list)
print(required_inventory_data)
input('')
str_receipt = create_receipt_text(g_item_list)
print(str_receipt)
input('')
creates_receipt_file(str_receipt)

# why am i doubting my passion for coding Rowan just keep coding oyu enjoy it thats all taht matrters who cares whther you are pasisoante about it or not just keep going if you wan tot'
# if you enjoy waht you are oding what is the problem? just ecaues you cant fucking work 24/7 and code and dont feel like doing it all the time is fine your passion and wokr ethic wavers at certain moments
# thats just hte reality Rowan calm down

# ok so i had this old text file that stored the receipt numbers basically but i feel like that like that i have 2 options atm to solve this problem of logging what receipt nubemr we are
# on so basically either we could like

# i have anoher idea for a feature why dont we actually create receipts but store them in date order like basically like store them in files where the current date is accessed
# and then yeah i dont think we need th. yeah i think its agood idea for like filing pruposes becuase yeah i think receipts generally do have like dates on them i guess what i could also do
# is like perhaps have more details on the receipt like for example like the date that the item was bought then i guess also like something else that could be cool
# would perahps be like that you can put on the clients details anually onto hte receipt or you could access a database that has their details then just load their information. dam fucking
# clientel information type shit holy crap. i feel like that like yeah that could be fucking sick. i could even just have hte client database as a text file with delimmiters and shit
# or perahps like do the same thing i did with items is like have the text files have the clients name and surname written exactly like with a specific format then lke basically you can ask them
# BRO what are your detials bruh then you input them into the terminal then it searches if they exist or something like that and then if i really wanna be fancy with it i could like od other
# things like get a c++ file searcher code to basically make it that you dont have to write the exact clients name and surname exactly type shit hmm yeah interesting.
# we shall ahve to see