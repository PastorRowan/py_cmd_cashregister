import copy
import mmap
from tokenize import endpats
import os

from os import path
from datetime import date

# auto load functions
def auto_load_todays_receipts_path_plus_date():
    global todays_date
    global todays_folder_path
    global todays_receipt_folder_name

    todays_date_ = date.today()
    str_todays_date = todays_date_.strftime("%Y-%m-%d")
    todays_receipt_folder_name = 'Receipts_' + str_todays_date
    todays_folder_path = 'Receipts/' + todays_receipt_folder_name
    todays_date = str_todays_date


def auto_load_create_todays_receipt_folder():
    global todays_folder_path
    if not (os.path.exists(todays_folder_path)):
        os.makedirs(todays_folder_path)

# repository functions

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

def idigit_format_checker(input_str):

    if input_str.startswith('i') and input_str[1:].isdigit():
         return True
    else:
         return False

def input_idigit_item(_question__):
    while True:
        item = input(_question__) # question will be something like input an item that follows the
        # idigit format 

        alt_option_press_test_return = alt_option_press_test(item)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

        if item.startswith('i') and item[1:].isdigit():
         return item, False
        
        elif alt_options_pressed_TorF_return:
            return alt_option_press_test_return
        
        else:
            print('Please enter an item that follows the idigit format')


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
        return 2, True
    elif _str_input == 'l':
        return 3, True
    elif _str_input == 'f':
        return 6, True
    elif _str_input == 't':
        return 5, True
    elif _str_input == 'k':
        return 4, True
    elif _str_input == 'j':
        return 8, True
    else:
        return _str_input, False
# function 1
# modifies shopping cart
def append_item_cart_func():
    global current_cart

    while True:
        item_ = input('Enter an item\n ---> ')

        alt_option_press_test_return = alt_option_press_test(item_)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

        item_info_address = 'Inventory/' + item_ + '.txt'

        if alt_options_pressed_TorF_return:
            return alt_option_press_test_return
        elif not idigit_format_checker(item_):
            print('\nEnter an item that follows the correct idigit format\n')
        elif not os.path.exists(item_info_address):
            print('\nEnter an item in the inventory\n')
        else:
            str_number_of_item = input('Enter the amount you want of this item\n ---> ')

            alt_option_press_test_return = alt_option_press_test(item_)
            alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

            if str_number_of_item == '':
                int_number_of_item = 1
                current_cart[item_] = current_cart.get(item_, 0) + int_number_of_item

            elif (str_number_of_item == ';') and (item_ in current_cart):
                del current_cart[item_]


            elif (str_number_of_item.isdigit()) or (str_number_of_item.startswith('-') and str_number_of_item[1:].isdigit()):
                int_number_of_item = int(str_number_of_item)
                current_cart[item_] = current_cart.get(item_, 0) + int_number_of_item
                if current_cart.get(item_) <= 0:
                    del current_cart[item_]

        print(current_cart)


def input_item(question_, check_if_item_existing_in_inventory_TorF_, return_address_TorF_):

    while True:
        item_id = input(question_)

        alt_option_press_test_return = alt_option_press_test(item_id)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

        item_info_address = 'Inventory/' + item_id + '.txt'

        if alt_options_pressed_TorF_return:
            return alt_option_press_test_return
        elif check_if_item_existing_in_inventory_TorF_:

            item_in_invenotry_TorF = os.path.exists(item_info_address)
            
            idigit_format_TorF = idigit_format_checker(item_id)

            if idigit_format_TorF and item_in_invenotry_TorF:
                if return_address_TorF_:
                    return item_id, item_info_address, False
                else:
                    return item_id, False
            elif (not item_in_invenotry_TorF) and (not idigit_format_TorF):
                print('Enter an item that follows the idigit format and exists')
            elif not item_in_invenotry_TorF:
                print('Enter an item that exists in the inventory')
            elif not idigit_format_TorF:
                print('Enter an item that follows the idigit format')
        elif not check_if_item_existing_in_inventory_TorF_ and return_address_TorF_:
            return item_id, item_info_address, False
        elif not check_if_item_existing_in_inventory_TorF_:
            return item_id, False


def input_number(question, option): # 1st parameter is the question hte input method will ask. 2nd parameter is what option we choosing

    vowels = 'aeiouAEIOU'

    if option[0] in vowels:
        incorrect_input_msg = 'Please enter an' + option
    else:
        incorrect_input_msg = 'Please enter a' + option

    while True:
        number = input(question)

        alt_option_press_test_return = alt_option_press_test(number)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

        if alt_options_pressed_TorF_return:
            return alt_option_press_test_return

        elif option == 'natural_number':

            number_only_contains_digits_and_doesnt_start_with_0_TorF = (not number.startswith('0')) and number.isdigit()
            if number_only_contains_digits_and_doesnt_start_with_0_TorF:
                return number, False
            else:
                print(incorrect_input_msg)

        elif option == 'integer':

            number_negative_TorF = number.startswith('-') and number[1:].isdigit()
            number_postive_and_doesnt_start_with_0_TorF = number.isdigit() and (not number.startswith('0'))
            number_is_0_ToF = number == '0'

            if number_postive_and_doesnt_start_with_0_TorF or number_negative_TorF or number_is_0_ToF:
                return number, False
            else:
                print(incorrect_input_msg)

        elif option == 'whole_number':

            number_postive_and_doesnt_start_with_0_TorF = number.isdigit() and (not number.startswith('0'))
            number_is_0_ToF = (number == '0')

            if number_postive_and_doesnt_start_with_0_TorF or number_is_0_ToF:
                return number, False
            else:
                print(incorrect_input_msg)
        elif option == 'integer_not_including_0':

            number_negative_TorF = number.startswith('-') and number[1:].isdigit()
            number_postive_and_doesnt_start_with_0_TorF = number.isdigit() and (not number.startswith('0'))
            number_is_0_ToF = number == '0'

            if number_postive_and_doesnt_start_with_0_TorF or number_negative_TorF or (not number_is_0_ToF):
                return number, False
            else:
                print(incorrect_input_msg)

        elif option == 'non_negative_float_currency':

            input_string = input_string.replace(',', '.')

            # Check if the string represents a non-empty positive number
            if number.lstrip('+-').replace('.', '', 1).isdigit():
                # Convert the string to float and check if it has 0, 1, or 2 decimals
                number_ = float(input_string)
            if 0 <= number_ == round(number_, 2):
                return True

            input_is_empty_TorF = number != ''
            number_postive_and_doesnt_start_with_0_TorF = number.isdigit() and (not number.startswith('0'))
            number_is_0_ToF = number == '0'

            if number_postive_and_doesnt_start_with_0_TorF or number_negative_TorF or (not number_is_0_ToF):
                return number, False
            else:
                print(incorrect_input_msg)

        else:
            print('ERROR: an option was not correctly parsed into the input_non_decimal_number function')
            break
        

# < 5TH FUNCTION
# inventory data memory gets loaded affter a certain point
# what we are gonna do instead because now it doesnt just brute force load all the data at once only if it has to then im just gonna run this code before every function that needs htis code ok what would happen if we
# ok the thing we input is a diocntary and i ddint know that. so i say we make a whole seperate fuctins that does item data mem mangement for a dicontary and one seperate for a set. because they are very differnt
# but i could make like small indivudal fuctionst hat basically turn th. oh my god wait the dioantry ahs the item idand the list oh my fuckng god ok so we are doing the same tig k then the best thing we can o is say
# ok make a whole ass. fucntion that baiscally ltieraly jsut
        
# ok we are gonna input a set that contains all the item data we need for the update then bsically its gonna crate the dicionatyr and hten we just create seperate functins outsdie that tierally just
# take a dciotnary and turn all the unique item ids into a set. and then what we could do is take the yeah. ok so baically yeah this makes sense. now if we input the new unqiue item set then we can skip.
# yeah ok sp now we shall remove the old set making mechncis type shti and then we are just gonna expect the set to of been created before hand which makes sense. becaue creatinga set out of a dicotiary or a lsit is very differnet
# oh my god that makes sense. or a tuple and then that makes our thing 20x more felxible ok so yeah elts d that

def item_data_mem_management_module(set_new_item_data, setting):

    if setting == 's':
        global shopping_cart_item_data_mem
        current_items_data_in_mem = shopping_cart_item_data_mem['items_in_memory']
        set_old_item_data_mem = shopping_cart_item_data_mem 
    elif setting =='e':
        global extra_items_mem
        current_items_data_in_mem = extra_items_mem['items_in_memory']
        set_old_item_data_mem = extra_items_mem
    if item_data_mem != {}:
        if set_old_item_data_mem != set_new_item_data:
            item_data_mem['items_in_memory'] = set_new_item_data
            item_data_mem = {key: value for key, value in current_items_data_in_mem.items() if key in set_new_item_data or key == 'cart_in_memory'} # removes items in cart but not in memory

            for unique_current_cart_item in set_new_item_data:
                if not (current_items_data_in_mem in current_items_data_in_mem):
                    # if item is in the current cart but not in memory
                    item_address = 'Inventory/' + unique_current_cart_item + '.txt'
                    f =  open(item_address, 'r')
                    mmaped_f = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                    byte_str_file_contents = mmaped_f.read()
                    byte_str_product_info = byte_str_file_contents.split(b'|')

                    decoded_name = byte_str_product_info[0].decode('utf-8')
                    decoded_price = float(byte_str_product_info[1].decode('utf-8'))
                    decoded_stock = int(byte_str_product_info[2].decode('utf-8'))

                    item_data = [decoded_name, decoded_price, decoded_stock]
                    current_items_data_in_mem[unique_current_cart_item] = item_data

    else:
        print('ERROR: item data set was not parsed as an arguement')

# wait i see that i think i fucked up so basically taht shwos the items we need to be added whihc would be ok because what we can do is make it that all the inuts get appended to a list and then fater htey get appended
# to a list then like yeah i guess but hten ialso gotta add the current items in memroy cart at the way end of he inptus so bacsially say like ok have htis nad htis and htis type shti. i feel like that perahps what
# could be nah but this thing does all that i wwanted to make an adder fucntion ahtltierally jsut adds al the items you put in but this thing ahs that functionalyity and also a lot of the functionality will ahve to be
# like added i na sense i guess sometjing i could do is go like ok shopping.AHAHAHAHHHHAHAHAHAAHA FUCKCKCKCKCKCKKC. FUCK MAN lol i feel liek taht like absically hmmm i think what i gotta do is bascialyl. i mean i could
# like go like bef OH MY GOD WAIT somethig w coulddo is take hte current memry cart and hten like. i could try. OK LETS SA WE ARGONNA USE THE SAME NEW ITEM DATA IN MEM MECHNICS  and have hta tas a list and shit so then
# bascially waht we could do istake the item list turn it into a set oj thats a good idea so then we make a set oh shit this thig oly wrk with dicitonaryies??? OH MY OD. thats the probem/ if we want to add invidual
# items ok then what we can do is like say ok if the added list is a diocatyr then do this and then if its a set then do this but should ybe just convert it into a set before hand and make that naother functions fucitonarilit
# oh my god so many decisons i fucking lveo it, but i have no idea what to do now. ok so bascially hm mwaht we could do is lieki ahve no fucking idea o say creat ehes et before hand of al the unqiue tiems then basically waht
# what we are gonna do is like take that set then input that set into the thig but htethign is it still remvoes keys that are in memory but not in cart... i guess fuclk. ok i say lets

# ok so as we said we could have like 5 keys that are reserved for items that are being used for a specific function to take place. that would make sense to me. basically like we could have a what we have now
# acurrent cart unique item list or set ok looks like its a set then basically what we could also do is then have another sett that is equivalent to basically uhm the overwritable item data?
# so we have the current cart item data which can be infintely large then we have a set that only is gonna contain 5 item data that will represent like what items are being used in the function which is rpobably
# jsut gonna be like one ok lets geet to work ok htis means that the second item iwthin the 

# oh my god i have an even more genius idea how about with the extra item data memroy band lets do this lets make it that each option or function has like a number that basically represents like
# ok how many items do we need in this allocated part. yes i love that idea ok well that means this idea wont work then? yeah hmmmm i guess like a seperate function is probably best
# one that literally adds extra items into the memory as the thing goes along. hmmm thats a cool idea because that would be also very very simple to implement like super duper simple ok nvm i say lets do that
# lets add an extra function that is basically gonna just deal with the extra items only and store their item data into an inventory so its like. wait.
# why dont we just have a cart memory and then a temporary item memory??? oh eyah that makes sense.
# that would be the easiest sotion by far because then all i gotta do is bascically like use that function to add a few items then afterwards if they are not needed then remove them and replace them.
# ok wait a minute we are literally expalinigne exaclly what our item data management function does. hmmmm ok well then i guess maybe we could adjust our function slightly to basicalyl return a dictionary
# that contains the asked item data i guess? but why should we seperate the cart memory from the extra item memory. simplicity sake but then also yeah idk it just kinda makes sense??? i mean
# hmmmm fuck. i guess it makes sense??? xD idk. having 2 global varialbe extra items dictionary and then a cart items dictionary? and then if the function requires items that might not be in the cart like i dont
# want to add random ass items to cart taht we dont need i guess. yeah. that makes perfect sense right??? hmmm ok okokokokookokookokokookookok. ok we have made a DECISION !!!!!!! yes. we have seeprate
# global variable called extra_item_data_mem then basically literally use the exact same code here item data in memroy then yeah. but what if the item is in the cart memory. ok wait perahps we could make a bit of
# a mix build where we absically go like ok IF THIS KEY EXISTS IN THE CART the we just use that but if it doesnt then. OH MY GOD. absolute perfect fucking efficeincy godly effieicnt. ok that maeks perfect
# sense then if the item is extra then basically make that like a temproary sotarge that basically gets deleted after every usage right??? ok yeah that makes sense. if item is in current cart memory then
# just use that but i its not then look for it in extra item memory then if its not there then add it tempraitliy for removal.
# ok a few checks will take place but ahts ok. so lets rather cal it shopping_cart_item_data_mem and then extra_item_data_mem and then we gotta change the item data memroy amgmenmtn fucntio to basically return
# the completed dictionary. actualyl tbh i do much prefer to use the global varialbes ok then how can we make it swtich between the 2. could we hyypothetically parse a variable then declare whatever it is as the global
# version that will be edited r i could ahve a simple likeif function like OH if option = n then use this global variable and create a relatio. ok we using this option parsing it as a arguemnt then eclaring it
# wait im doing exactly that??? im just parsing a setting. ok moerse W so basically take the setting then have if elif contrl staetn or wahtver the fuck you cal lit then makeit if setting = n then change shopping
# cart mem elif setting = y change whaaver and ten. so we input the extra item needed and then if its the extra item thing then i ugess what we could do is run the exactsam. i could even be like ok if input is
# if input is a shopping cart set then do x or if input is a extar item set but how can the thing tell the difference ok. go lik 

# 4TH FUNCTION 'u'
# creates receipt text of shopping cart
def create_receipt_text_func(_current_cart_): # take reciept_text_memoryies documented item list then ocmapre that to the impt 
    float_sum_total = 0.
    global item_data_in_memory # list was inputted
    global receipt_text_memory
    global todays_date

    client_firstname = 'John'
    client_surname = 'Smith'

    client_info_plus_date_line = todays_date +  ' ' + client_firstname + ' ' + client_surname + '\n' + '\n'

    current_cart_unique_item_tuple = tuple(_current_cart_.keys())

    receipt_text_cart_unique_item_tuple_memory = receipt_text_memory[0]
    receipt_text_in_mem = receipt_text_memory[1]

    if current_cart_unique_item_tuple != receipt_text_cart_unique_item_tuple_memory:
        receipt_text_list = [client_info_plus_date_line]

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
        receipt_text = receipt_text_in_mem[1]
        print('Your shopping cart is empty, no changes were made to receipt_text_memory')
        return receipt_text

    elif current_cart_unique_item_tuple == receipt_text_cart_unique_item_tuple_memory:
        receipt_text = receipt_text_memory[1]
        print('Your shopping cart is exactly the same, no changes were made to receipt_text_memory')
        return receipt_text

# 5TH FUNCTION 'l'
# creates file of shopping cart

def creates_and_overwrites_receipt_file_func(receipt_str, receipt_address): # recept str was a list
    with open (receipt_address, 'w') as receipt_file:
        receipt_file.write(receipt_str)

def auto_load_current_receipt_number():
    global current_receipt_number_mem
    if os.path.exists == False:
        with open ('Receipt_number_log/Receipt_num_log.txt', 'a') as f_:
            f_.write('1')
            print('Current receipt number has been made 1')
    else:
        with open('Receipt_number_log/Receipt_num_log.txt', 'r') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mmap_file:
                byte_string_current_receipt_number_hard = mmap_file.read()
                str_current_receipt_number = byte_string_current_receipt_number_hard.decode('utf-8')
                current_receipt_number_mem = str_current_receipt_number


# if option is 'u' then add 1 to file log
# if option is 'i' then just update the number log with the one in mem

def receipt_number_log_and_mem_updater(current_receipt_number, selected_option, update_hardrive_yorn):
    global current_receipt_number_mem

    # updates memory
    if selected_option == 'u': # u is add one which we are gonna add to the end of the function
        int_updated_receipt_number= int(current_receipt_number_mem) + 1
        str_updated_receipt_number = str(int_updated_receipt_number)
        current_receipt_number_mem = str_updated_receipt_number
        print(current_receipt_number_mem)
        print('new current receipt number in mem')
    elif selected_option == 'i': # i is update
        current_receipt_number_mem = current_receipt_number
        print(current_receipt_number_mem)
        print('new current receipt number in mem')
    else:
        print("ERROR: variable 'selected_option' WAS NOT PARSED: 'selected_option' was not assigned a compatible value")

    # updates hardrive
    if update_hardrive_yorn == 'y':
        bytestr_updated_receipt_number = str_updated_receipt_number.encode('utf-8')
        print(bytestr_updated_receipt_number)
        print('new receipt number in hardrive')
        _f_ = open('Receipt_number_log/Receipt_num_log.txt', 'r+')
        new_size = len(str_updated_receipt_number)
        _f_.truncate(new_size)
        _mmap_f = mmap.mmap(_f_.fileno(), 0, access=mmap.ACCESS_WRITE)
        _mmap_f.write(bytestr_updated_receipt_number)
        _mmap_f.flush()
        _mmap_f.close()
        _f_.close()
    elif update_hardrive_yorn == None:
        print("ERROR: variable 'update_hardrive_yorn' WAS NOT PARSED: 'update_hardrive_yorn' was not assigned a compatible value")

def prints_stock_in_inventory():
    global item_data_in_memory

    f = None
    mmaped_file = None

    while True:
        item_identifier = input('\nEnter the item you want to check the stock of.\n ---->')

        alt_option_press_test_return = alt_option_press_test(item_identifier)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

        if idigit_format_checker(item_identifier):
            if item_identifier in item_data_in_memory:
                # runs if item is present in memory
                current_stock = item_data_in_memory[item_identifier][2]
                print('Reading memory sss...sssss...HHHhhhh...sssss')
                print(current_stock)
            else:
                item_info_address = 'Inventory/' + item_identifier + '.txt'
                f = open(item_info_address, 'r')
                mmaped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                byte_item_info = mmaped_file.read()
                current_stock = byte_item_info.rsplit(b'|', 1)[-1].decode('utf-8')
                print('Reading hardrive inventory sss...sssss...HHHhhhh...sssss')
                print(current_stock)
        elif alt_options_pressed_TorF_return:
            if (f != None) and (mmaped_file != None):
                f.close()
                mmaped_file.close()
                print('closing files')
            else:
                print('Didnt close files because they werent open becaues the function only used the memory')
            return alt_option_press_test_return
        else:
            print('Monkey enter an item that follows the idigit format')


def change_inventory_stock(item_id, item_info_address, str_change_stock):
    global item_data_in_memory
    default_next_func_num =  5
    f = None
    mmaped_file = None
    int_change_stock = int(str_change_stock)

    if item_id in item_data_in_memory:
        int_current_stock = item_data_in_memory[item_id][2]
        int_new_stock = int_current_stock + int_change_stock
        if int_new_stock < 0:
            return default_next_func_num, False
        item_data_in_memory[item_id][2] = int_new_stock
    else:
        f = open(item_info_address, 'r+')
        mmaped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
        bytestr_item_info = mmaped_file.read()
        bytestr_current_stock = bytestr_item_info.rsplit(b'|', 1)[-1]

        str_current_stock = bytestr_current_stock.decode('utf-8')
        int_current_stock = int(str_current_stock)

        int_new_stock = int_current_stock + int_change_stock

        if int_new_stock < 0:
            return default_next_func_num, False

    if (f != None) and (mmaped_file != None):

        str_new_stock = str(int_new_stock)
        bytestr_new_stock = str_new_stock.encode('utf-8')
        bytestr_updated_item_info = bytestr_item_info.replace(bytestr_current_stock,bytestr_new_stock)

        new_size = len(bytestr_updated_item_info)
        mmaped_file.close()
        f.truncate(new_size)

        mmaped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
        
        mmaped_file.write(bytestr_updated_item_info)
        mmaped_file.flush()
        f.close()
        mmaped_file.close()

    else:
        f = open(item_info_address, 'r+')
        mmaped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE) # ok so somehow its reading hte old values but its still here???
        bytestr_item_info = mmaped_file.read()

        int_change_stock = int(str_change_stock)

        str_current_stock = str(int_current_stock)
        bytestr_current_stock = str_current_stock.encode('utf-8')

        str_new_stock = str(int_new_stock)
        bytestr_new_stock = str_new_stock.encode('utf-8')

        bytestr_updated_item_info = bytestr_item_info.replace(bytestr_current_stock,bytestr_new_stock) # error is here upwards

        new_size = len(bytestr_updated_item_info)
        mmaped_file.close()
        f.truncate(new_size)

        mmaped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
        mmaped_file.write(bytestr_updated_item_info)
        mmaped_file.flush()
        f.close()
        mmaped_file.close()

def error_occured_checker():
    global current_cart
    global item_data_in_memory

    current_cart_empty_TorF = current_cart == {}
    item_data_cart_mem_emtpy_TorF = item_data_in_memory['cart_in_memory'] == {}
    current_cart_equal_item_data_cart_mem = current_cart == item_data_in_memory['cart_in_memory']

    if current_cart_empty_TorF:
        print('ERROR: SHOPPING CART: shopping cart is empty, cannot perform the function')
        return 1 , True

    elif item_data_cart_mem_emtpy_TorF:
        print('ERROR: ITEM DATA MEMORY MANAGEMENT: cart in memory is emtpy, cannot perform the function')
        return 'p' , True

    elif current_cart_equal_item_data_cart_mem:
        print('ERROR: SHOPPING CART AND CART IN MEMORY EQUIVALENCY: shopping cart is not the same as item data cart in memory, cannot perform this function')
        return 'p', True
    else:
        return False,

def ask_overwrite_file(receipt_address):
    if path.exists(receipt_address): # make input
        print('receipt does already exist')
        question = 'enter y to overwrite file or enter n to not overwrite the file' # still need to add the back function
        answer = answer_y_or_n(question)

        alt_option_press_test_return = alt_option_press_test(answer)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]

        if alt_options_pressed_TorF_return:
            return alt_option_press_test_return
        elif answer == 'n':
            return alt_option_press_test_return
        else:
            return alt_option_press_test_return
    else:
        return None, False# ok if the file doesnt exist then we 

def question_and_answer(str_question, set_str_answers):

    while True:
        _answer = input(str_question)

        alt_option_press_test_return = alt_option_press_test(_answer)
        alt_options_pressed_TorF = alt_option_press_test_return[-1]
        alt_option_pressed_test_return = alt_option_press_test_return

        if _answer in set_str_answers:
            return _answer
        elif alt_options_pressed_TorF:
            return alt_option_pressed_test_return
        else:
            print('\nEnter y or n or a special option\n\n ---->')







def complete_program_loop(func_option): # selected 's' by default
    global current_cart
    global item_data_in_memory
    global current_receipt_number_mem
    global todays_folder_path

    while True:

# 1ST FUNCTION 's'
# shopping cart management
        if func_option == 1:
            input('we are currentky on function 1')
            append_item_cart_return = append_item_cart_func()

            append_item_cart_alt_option_pressed_TorF = append_item_cart_return[-1]
            append_item_cart_alt_option_pressed_func_number = append_item_cart_return[0]

            if append_item_cart_alt_option_pressed_TorF:
                return append_item_cart_alt_option_pressed_func_number

# 2ND FUNCTION 'u'
# prints current receipt of shopping cart
        elif func_option == 2:
            input('we are currentky on function 2')
            item_data_memory_management(current_cart)
            receipt_text = create_receipt_text_func(current_cart)
            print(receipt_text)
            return 1

# 3RD FUNCTION 'l'
# creates file of shopping cart
        elif func_option == 3:
            input('we are currentky on function 3')
            item_data_memory_management(current_cart)
            receipt_text = create_receipt_text_func(current_cart)
# c:\Users\MSI\Desktop\CashRegister\Receipts\Receipts_2024-01-01
            receipt_address_ = todays_folder_path + '\Receipt' + current_receipt_number_mem + '.txt'

            creates_and_overwrites_receipt_file_func(receipt_text, receipt_address_)
            return 1


# 4TH FUNCTION 'k'
# prints stock of items in inventory
# reads memory of inventory and if it isnt available reads harddrive inventory
        elif func_option == 4:
            input('we are currentky on function 4')
            item_data_memory_management(current_cart)
            prints_stock_in_inventory_return = prints_stock_in_inventory()

            alt_option_pressed_TorF = prints_stock_in_inventory_return[-1]
            alt_option_pressed_func_number = prints_stock_in_inventory_return[0]

            if alt_option_pressed_TorF:
                return alt_option_pressed_func_number
            else:
                return 1


# 5TH FUNCTION 't'
# changes stock in inventory
        elif func_option == 5:
            input('we are currentky on function 5')

            question_ = '\nEnter the item you want to change the stock of.\n ---->'
            return_address_TorF = True

            input_item_return = input_item(question_, return_address_TorF)

            alt_option_pressed_TorF = input_item_return[-1]
            alt_option_pressed_func_number = input_item_return[0]

            if alt_option_pressed_TorF:
                return alt_option_pressed_func_number
            
            question_ = '\nEnter an integer that is not 0.\n ---->'

            input_integer_return = input_non_decimal_number(question_, 'integer_not_including_0')

            alt_option_pressed_TorF = input_integer_return[-1]
            alt_option_pressed_func_number = input_integer_return[0]

            if alt_option_pressed_TorF:
                return alt_option_pressed_func_number
            
            item_id = input_item_return[0]
            item_info_address = input_item_return[1]
            str_change_stock = input_integer_return[0]
            
            change_inventory_stock(item_id, item_info_address, str_change_stock)

            return 5
        

# 6TH FUNCTION 'f'
# Does a full checkout, changes inventory according to the cart (and saves receipts and inventory to an online database)
        elif func_option == 6:
            input('we are currentky on function 6')

            # loads shopping cart item data
            item_data_memory_management(current_cart)

            # error checker
            errr_occured_return = error_occured_checker() # i1 = 15 ||| i2 = 21
            errr_occured_TorF = errr_occured_return[-1]
            error_occured_next_action= errr_occured_return[0]
            if errr_occured_TorF:
                return error_occured_next_action
            
            # creates and prints receipt str
            receipt_str = create_receipt_text_func(current_cart)
            print(receipt_str)

            # creates receipt file
            receipt_address = 'Receipts/' + 'receipt' + current_receipt_number_mem + '.txt'

            print(receipt_address)

            ask_overwrite_file_return = ask_overwrite_file(receipt_address)

            answer = ask_overwrite_file_return[0]
            alt_option_pressed_TorF = ask_overwrite_file_return[-1]
            alt_option_pressed_func_number = ask_overwrite_file_return[0]

            if alt_option_pressed_TorF:
                return alt_option_pressed_func_number
            elif (answer == 'y') or (answer == None):
                creates_and_overwrites_receipt_file_func(receipt_str, receipt_address) # a list was inputted =

            # Removes sold stock inventory
            for item_id_ in current_cart:
                int_amount_bought = current_cart[item_id_]
                int_change_stock = -int_amount_bought
                str_change_stock_ = str(int_change_stock)

                item_info_address_ = 'Inventory/' + item_id_ + '.txt'
                change_inventory_stock(item_id_, item_info_address_, str_change_stock_)

            receipt_number_log_and_mem_updater(current_receipt_number_mem, 'u', 'y')
            print(current_receipt_number_mem)
            current_cart = {}
            print('checkout was successful and shopping cart was emptied')
            return 1




# 7TH FUNCTION 'q'
# changes current receipt number and receipt number in hardrive
        elif func_option == 7:
            input('we are currentky on function 7')

            question = 'Enter the new current receipt number'

            input_non_decimal_number_return = input_non_decimal_number(question, 'natural_number')

            receipt_number_ = input_non_decimal_number_return[0]
            alt_options_pressed_return = input_non_decimal_number_return
            alt_options_pressed_TorF = input_non_decimal_number_return[-1]

            if alt_options_pressed_TorF:
                return alt_options_pressed_return

            question = 'Enter y if you want to save the selected receipt_number into hardrive or enter n if you dont want to'
            answer_y_or_n_return = answer_y_or_n(question)

            answer = answer_y_or_n_return[0]
            alt_options_pressed_return = answer_y_or_n_return
            alt_options_pressed_TorF = answer_y_or_n_return[-1]

            if answer == 'y':
                receipt_number_log_and_mem_updater(receipt_number_, 'i', answer)
            elif answer == 'n':
                receipt_number_log_and_mem_updater(receipt_number_, 'i', answer)
                print('Hardrive receipt number was not updated')
            elif alt_options_pressed_TorF:
                return alt_options_pressed_return
            
# 8TH FUNCTION 'j'
# adds or overwrites inventory item and item data
        elif func_option == 8:
            input('we are currentky on function 8')
            question = 'Enter an item'
            input_idigit_item_return = input_idigit_item(question)

            item_id = input_idigit_item_return[0]
            alt_option_pressed_func_number = input_idigit_item_return[0]
            alt_options_pressed_TorF = input_idigit_item_return[-1]

            if alt_options_pressed_TorF:
                return alt_option_pressed_func_number

            item_info_address = 'Inventory/' + item_id + '.txt'
            ask_overwrite_file_return = ask_overwrite_file(item_info_address)

            answer = ask_overwrite_file_return[0]
            alt_option_pressed_func_number = ask_overwrite_file_return[0]
            alt_options_pressed_TorF = ask_overwrite_file_return[-1]

            
            if answer == 'n':
                return 1
            elif alt_options_pressed_TorF:
                return alt_option_pressed_func_number
            
            item_name = input('Enter an item name, you can enter whatever name you want but please follow the correct format. for more details please enter nothing')

            item_price = input_number('Enter an item price', 'non_negative_float_currency')

            item_stock = input_number('Enter an item stock', 'whole_number')

# ok now lets construct a string that has all of this ifnormation
            
            item_data_line = item_name + '|' + item_price + '|' + item_stock

            creates_and_overwrites_receipt_file_func(item_data_line, item_info_address)

# ok so we are gnna keep the roignal receipt but what i could do is put a refunded tag over it and then show like ok this and this was refunded or something yeah
# i think that makes sense. so basically like the way we could remember a receipt got refunded in some way idk. so baiscally we could put the refunded tag like above the receipt or something idk like at the top next
# to the name is like a refuneded tag then perhaps we could move hte receipt file to a refunded category??? idk i say we keep the original receipt then basically create anoher receipt with the same receipt number that
# is basically like receipt6 refund and then is within the same date folder or whatever should i put the days date into the receipt file nae because i feel like that is very important and provides very very
# easy searchability of the receipt and the refund if we were to create some kind of search enginge or just use the windows search engine or linux search engine or whatever. i say what we could do is like
# ok yeah that makes sense to me so that will be the next feature of our program and then i am gonna finish the changing what ever now lets create the inventory item

# lets first start ok change item in inventory so basically what we are gonna do is somehow changing one item iwthin hte inventory so whawt we could do is read the entire file and get all the data then
# we can subsitiute in bytes the price data ohh hi got a cool idea so basically we came up with this idea ok ok t=this is a fucking great idea we came up with this one idea to take out information out of a funciton
# no in fact we still use that its called item loading function so we can use that to number 1 take out the information then basically we could read the item information in memory and say like ok encode it into bytes
# then replace that code with this code. that is one option or we can take out hte inforaton a gian nah that sounds like the most mid idea ever i say lets make it a bit more spicy and then like basically replace
# the original product line with hte informato in memoery or even better just to make things a bit more spicy we have the entire product line in memoru so lets recreate the product line using the data in memor
# to avoid file i/o operations then basically jsut instnatly pput it all gotehtet then take hte old info and replace it with the new info then yeah take that then open the file and then truncate the fie to hte new size
# then overwrite the data with mmap. perfect
        


# 9TH FUNCTION 'd'
# refunds a receipt
        elif func_option == 9:
            input('we are currentky on function 9')


# 10TH FUNCTION 's'
# Saves receipts and inventory to an online database
        elif func_option == 10:
            input('we are currentky on function 10')


# 11th FUNCTION 'g'
# changes item data of item in inventory
        elif func_option == 11:
            input('we are currentky on function 11')
            question = 'Enter an item that you want to change or add'
            input_item_in_inventory_TorF = False
            return_address_TorF = True
            input_item_return = input_item(question, input_item_in_inventory_TorF, return_address_TorF)

            item_id = input_item_return[0]
            item_info_address = input_item_return[1]

            alt_option_pressed_func_number = input_item_return[0]
            alt_options_pressed_TorF = input_item_return[-1]

            if alt_options_pressed_TorF:
                return alt_option_pressed_func_number
            elif os.path.exists(item_info_address):
                set_inputted_answers = set('n','e', 't')
            else:
                set_inputted_answers = set()

            set_all_valid_settings = set('n','e', 't')
            question = 'Enter n to change the name, enter e to change the price, enter t to change the stock, enter h to coninue'

            while True:
                if set_inputted_answers == set_all_valid_settings:
                    break
                elif answer == 'h':
                    break

                answer = question_and_answer(question, set_all_valid_settings)
                set_inputted_answers.add(answer)


            if item_id in item_data_in_memory:
                # runs if item is present in memory
                current_stock = item_data_in_memory[item_id][2]
                str_current_item_name = item_data_in_memory[item_id][0]
                str_current_price = str(item_data_in_memory[item_id][1])
                str_current_stock = str(item_data_in_memory[item_id][2])
            else:
                item_info_address = 'Inventory/' + item_identifier + '.txt'
                f = open(item_info_address, 'r')
                mmaped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                byte_item_info = mmaped_file.read()
                current_stock = byte_item_info.rsplit(b'|', 1)[-1].decode('utf-8')
                print('Reading hardrive inventory sss...sssss...HHHhhhh...sssss')
                print(current_stock)

            str_current_item_name = item_data_in_memory[item_id][0]
            str_current_price = str(item_data_in_memory[item_id][1])
            str_current_stock = str(item_data_in_memory[item_id][2])

# only problem i can see is that the item might not be loaded into memroy so hterefore we would have
# to copy the code from the print stock function basically yeah or we could adjust the memory management
# function to also be able to insert items into memory like perhaps insert an individual item into memory
# somehow or create a seperate function based on that i mean yeah i guess but i am only gonna use
# the information once so basically yeah ok nvm we just gonna copy the code from the other function
# ok so if we were to add a whole ass new item to the inventory then i feel like what we could
# could do is basicall take the item id then search if the file path already exists
# if it doesnt then some settings for all our next code changes where we now have to
# add all the information tehn change all the informatio which is acutally very easy to do
# ok nah this code makes no sense i am not happy wit hthis ok look here we are about to
# take this code ok we gonna take this file ok listen here listen here boeta listen listen
# ok we are gonna now take this the data already in meroy then create a string outof it cool iwth hte item data
# that is massive W respect love epic but now ok this shit make no sense now if the item
# is not in memory we are now gonna search throough hte files and try to fucking find
# the item??? wait hold up up why dont we just add the item to hte inventory manager function
# like basically take the current cart then like basically add this item too into their
# into memory or holup what we could just do is edit the load item mangement sysetm
# to now be able to add items of choosing into memory like for example add this item into
# memoey with all the item data i feel like that makes 20x more sense to me because I HATE
# COPYING AND PASTING THE SAME CODE 3000 times it is literally evident of bad code that is
# a bad programmers job im sorry. if you take code and have 300 lines of repeated code
# then idk how else to tell you but you dont understand how to use functions i feel like that
# what would be a better practise for us is to either load tis information into memroy
# yeah because if you do a full checkout anyways you are just gonna end up creating a
# new fucking shopping cart literally so i say what we do is literally just
# make the load item data into memroy function or functions if we want VERY GOOD and resposnbile for all
# item data memroy managemnet and then we never EVER EVER rewrite code tat is like read
# shit off hardrive then put it into memroy??? then why not just put it into memory in the
# first place because its not like the computing resoeurces holding the item data
# is any less than when its in the item data memory i feel like yeah. but i feel like
# then if we want the most efficient solution we need to find the abosutel best way
# to handle item data in memory then role with that and add a few more functionalities
# to the function so that we can just also add items at will type shit. yeah i like that
# i think yeah that makes sense make item data memroy mangement super efficeint then just
# use that function all the time to call item data from the hardrive into memory yeah.
# that makes perfect sense make it that we can easily add items to the item_data_in_
# memroy or should we call items_data_mem. and then like make a set that contains
# all the items that are necessary. i say we could also try make it more eficent by
# like trying to limit the amount of items in memory that are equal to the shopping cart
# plus 3 or something like that. yeah that makes sense. so that basiaclly ok if we do ever
# come accross functions taht need an items item data to change it most likely the
# function is just gonna need like at most 4 extra item data slots in memroy it wont fucking
# need any more and then if the function starts needing more we can take the
# item data that is not preesnt in the shopping cart and then remove one of them from memory
# but what if the function needs multiple... oof... idk what to do then i guess we
# could even make a 2nd list that respersents ok this item needs 2 slots in memory
# so these 2 slots are taken then the other slots will be left as overwritable
# yeah that makes sense to me i like that idea yeah that makes sense shoh this is gonna
# be an intricute system but i feel like that literally ok if i am able to pull this off then
# ez W. i feel like that basically then i dont have to recall this retarded reading hardrive
# functio nthat much or it will be more automated than before. basically yeah that makes
# sense. eyah i like that find a way to automate all memroy amangement and all you need
# to do is literally like yeah

# ok so first i am gonna work on the easier fucntions or ideas to implement then after that
# i shall move to the harder ones so basically i feel like that like i mean. lets just focus on
# learning c++ i guess because i feel like that. thats really all i really have like an energy bar for?
# i feel like my energy bar to work on tis is lower

            str_new_item_name = str_current_item_name
            str_new_price = str_current_price
            str_new_stock = str_current_stock

            if 'n' in set_inputted_answers:
                input_name_return = input('Enter an item name, you can make it anything but please follow the format')
                str_new_item_name = input_name_return[0]

                alt_option_pressed_func_number = input_name_return[0]
                alt_options_pressed_TorF = input_name_return[-1]

                if alt_options_pressed_TorF:
                    return alt_option_pressed_func_number


            elif 'e'in set_inputted_answers:
                question = 'Enter a valid price'
                input_number_return =  input_number(question, 'non_negative_float_currency')
                str_new_price = input_number_return[0]

                alt_option_pressed_func_number = input_number_return[0]
                alt_options_pressed_TorF = input_number_return[-1]

                if alt_options_pressed_TorF:
                    return alt_option_pressed_func_number

            elif 't' in set_inputted_answers:
                question = 'Enter a valid amount of stock'
                input_new_stock_return = input_number(question, 'whole_number')

                str_new_stock = input_new_stock_return[0]
                alt_option_pressed_func_number = input_new_stock_return[0]
                alt_options_pressed_TorF = input_new_stock_return[-1]

                if alt_options_pressed_TorF:
                    return alt_option_pressed_func_number
                
            elif (str_new_item_name != str_current_item_name) or (str_new_price != str_current_price) or (str_new_stock != str_current_stock):
    
                str_new_item_data = str_new_item_name + '|' + str_new_price + '|' + str_new_stock
                with open


# ok we could imrpove this by using this function for adding and overwritng an item and then also
# replacing old items i feel like that, that would be a spectacular idea i feel like that i am
# definitely gonna do that 100% then also what we could do on top of that is combine the print
# receipt function with this one by printing the item info after selecting the item

            





            
            
            










# example item data in memory (dictionary) = {'cart_in_memory': {'i1'}, 'i1': ['GTX1050_2GB', 3000.01, 198]}
# ok lets build the product line

# shit now we gotta use the hidden jiujitsu the infinite list thig because what if they want
# to change everything yeah i feel like that basically like that could be a thing like
# that they acutally want to change all things and i dont want to have like 6 things to choos
# from i say lets make a set and theok lets make antoehr set and another while true loop then like
# basically like yeah figure this shit out i feel like yeah




# i also wanted to add another feature which its gonna be very hard to add now but its a really cool feature that i feel like is very important but to actually organise the receipts in date order so basically
# the receipts are organised in number order based on the receipt that they are made orwhatveer but then also what i would like is that they are stored in date order so bsaiclly today is idk x date and then
# what i would like is that i could somehow tell the file system to create a file thats name is just the date that the file is created


# ALSO THIS TIME REMEBER T UPDAT ETHE MEMROY UNLIKE LAST TIME YEAH REMEMBER THAT so whatever changes we gotta
# also refelct that in the memory
# ok now they can choose whwat to change the stock the name or the price









current_cart = {}
item_data_in_memory = {'cart_in_memory' : set(), 'extra_items' : set()}
receipt_text_memory = [(' '), '']
default_start_selected_option = 1
current_receipt_number_mem = 1

selected_option = default_start_selected_option

todays_date = 0
todays_folder_path = 0
todays_receipt_folder_name = 0


# loading prerequestite information
auto_load_current_receipt_number()
auto_load_todays_receipts_path_plus_date()
auto_load_create_todays_receipt_folder()

print(current_receipt_number_mem)

while True:

    selected_option = complete_program_loop(selected_option)

    print(selected_option)
    
    input('selected option has been printed. should be the button pressed')
    if selected_option == 'p':
       break
    elif selected_option == '/':
        print('bruh function no work right now')
        break
        # will repeat the complete program loop
    elif selected_option == '/':
        print('bruh function no work right now')
        break
    elif selected_option == 2:
        print('function 2 should be operational')
    elif selected_option == 3:
        print('function 3 should be operational')
    elif selected_option == None:
        print('program is repeated')