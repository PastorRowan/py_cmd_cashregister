import copy
import mmap
from tokenize import endpats
from os import path

def idigit_format_checker(input_str):

    if input_str.startswith('i') and input_str[1:].isdigit():
         return True
    else:
         return False

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


# function 1 's'
def prerequesite_information_collection_and_main_processing_append_item_cart():
    global g_item_list

    while True:
        item_ = input('lets add an item\n ---> ')

        alt_option_press_test_return = alt_option_press_test(item_)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
        alt_option_pressed_func_number_return = alt_option_press_test_return[0]

        if alt_options_pressed_TorF_return:
            return alt_option_pressed_func_number_return
        elif idigit_format_checker(item_):
            print('\nEnter an item that follows the correct idigit format\n')
        elif path.exists('Inventory\i1.txt'):
            print('\nEnter an item in the inventory\n')
        else:
            g_item_list.append(item_)


# function 2 'c'
def prerequesite_input_collection_change_cart():
    func_number = 2
    global g_item_list

    if g_item_list != []:
        while True:
            item_position_cP = input('Enter item position you want to change? e.g 2 is equal to the 2nd item in the list \n ----> ')

            alt_option_press_test_return = alt_option_press_test(item_position_cP)
            alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
            alt_option_pressed_func_number_return = alt_option_press_test_return[0]

            if item_position_cP.isdigit():
                while True:
                    item_replacement_cP = input('Enter the item you want in the item postion \n ----> ')

                    alt_option_press_test_return = alt_option_press_test(item_position_cP)
                    alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
                    alt_option_pressed_func_number_return = alt_option_press_test_return[0]

                    if idigit_format_checker(item_replacement_cP):
                        return alt_option_pressed_func_number_return
                    
                    elif alt_options_pressed_TorF_return:
                        return None, func_number 
                    else:
                        print('Please enter items using the correct idigit format or alternative options only.')
                    
            elif alt_options_pressed_TorF_return:
                return None, func_number
            
            else:
                print('Please enter postive integers or alternative options only.')
    else:
        print('Please enter an item into the item list before using the change cart function.')
    





def main_processing_change_cart(item_postion_cM, item_replacement_cM):
    if item_postion_cM != None:
        global g_item_list
        g_item_list[int(item_postion_cM) - 1] = item_replacement_cM

def prerequesite_input_collection_insert_cart():
    pressed_option = 'i'
    while True:
        item_position_iP = input('Enter item position you want to inesrt your item? e.g 2 is equal to the 2nd item in the list \n ---->')

        alt_option_press_test_return = alt_option_press_test(item_position_iP)
        alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
        alt_option_pressed_func_number_return = alt_option_press_test_return[0]
        
        if item_position_iP.isdigit():
            while True:
                item_addition_iP = input('''Enter the item you want in the item postion \n ---->''')

                alt_option_press_test_return = alt_option_press_test(item_position_iP)
                alt_options_pressed_TorF_return = alt_option_press_test_return[-1]
                alt_option_pressed_func_number_return = alt_option_press_test_return[0]

                if idigit_format_checker(item_addition_iP):
                    return item_position_iP, item_addition_iP, alt_option_pressed_func_number_return
                    
                elif alt_options_pressed_TorF_return(item_addition_iP):
                    return None, alt_option_pressed_func_number_return
                    
        elif alt_options_pressed_TorF_return(item_position_iP):
            return None, alt_option_pressed_func_number_return
    
def main_processing_insert_cart(item_postion_iM, item_addition_iM):
    if item_postion_iM != None:
        global g_item_list
        g_item_list.insert(int(item_postion_iM) - 1, item_addition_iM)

# ok now the real problem is how are we gonna be able to search for item identifiers and like items on the thing so i guess we could make an alternative file that basically just has a list of names of items in the shop and then
# the function isbascially like bruh search for items in the shop then like your like ok imma search for items in the shop then you write down like GTX_1050 then bsaiclly it finds hte file the in the file
# its gonna have i1 in it then its gonna say the file name is equal to read the file and mmap it then write it out in text or whatever then it will say ok this is equal to this bascially yeah
# i feel like that would work pretty ez









# receipt text and create text file and print receipt text prerequisities
        
# ok we definitely need to change this whole ass thing so bacsially waht i want to do is literally like redo teh whole iventory sysem ebcause currently its like not it chief i dont have toscrap anyhting
# but i think that building a new inventory system from scratch will be easier than trying to modfiy tbis one to try fit our new one yeah deifnitelly 100/100 yes ok well lets get to work. ok lets do like a function
# where we basically memory map a file then read the product data put it into a string then work with that. because i feel like that would be fast enoughf ro mei gues what i could do to be more efficeint is make
# a function that literally mmaps the file i couldltierally just make it. nah lets do somethinga little more speciialized. lets make a whole function that memory maps the file then takes out the specific data in a string
# then returns the string of the sepcific data needed that is actually pretty epic i like that. i say lets do that
        
        # i went back toehce kwaht they were doing and again they were just fucking dancing to their own music now i feel dumb again when wil l my mind learn i ltierally







# now how owuld i ge a stock changer fucntion i guess i eman i have already made one with the wohle input line and i think taht would work with just a mmaped file or whatever yeah. i feel like that like i guess
# what i could do is figure out how to use that into this code and see if that shit works as a stock changer as well like we could input . but nahhh wouldnt you want this as just the info collector ship then
# what i oculd od is make another stock changer function. yeah basically like you ltierally just input an integer representing like the amont you wantto change hte stock by then it
# it changes the stock by that amount. i guess something else i could do is also like soemthing i coudl do is like perhaps make it that i can use this within a function to basically
# collect the desired inframtion then basically usethat in someway then if the customer chosoes to che kout then what we could do is like take that line then subtract the integer form the stock and then ltierally#
# literally jsut repace the whole ass line with that and if thats not possible perhaps just make a new file or whatever. but surely i mean we already tried to change an mmaped file and that didint go so well so i
# say we just do the nuke solution and just fucking take that shit out also lets define the stock change outside of hte function elts just see waht we have already written
        
# ok what we could do is make the info collection functions also actually perform the. we could ombine the info colelciton fuction with the stock ahcnging one if like basically like a certain conditins is true then
# the code runs the extra change stock function which i mean could be cool i could even just make it like a setting you can input like make a parametter = to change_stock_TorF then like basically go like ok
# ok i eman like yeah ok ok ok if we really want to make changes to how the mai nprocessing change stock ivnentory whatvee rfucntion we probably should do that first so i feel like yeah we should probs do that
# first o nvm i found the best solution is to actually basically just jeez its quite simple but to call this main_processing_item_info_colleciton funcion into the other function then like make it return
# the desired data then after that then it goes on and does its own processing basically yeha. ok that makes perfect sense. so basically call this function within the other function then our usgae of storage and our
# usage of memory is efficient yeah i feel like yeah that makes sense. hmmmm i feel like that yeah ok we can do that ok so elts do that now then we could yeah basicalyyeah ok i want to take a break now lets go for a
# walk


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


#7th function 't'
def main_processsing_change_stock_inventory(item_identifier, int_change_of_stock):
    edit_file = True
    close_file_TorF = False
    _item_identifier = item_identifier

    item_info_collection_return = main_processing_item_info_collection(_item_identifier, 's', close_file_TorF, edit_file)

    mmaped_item_info = item_info_collection_return[-1]
    file = item_info_collection_return[1]
    str_current_stock = item_info_collection_return[0]

    if str_current_stock[0] != None:
        str_byte_current_stock = str_current_stock.encode('utf-8')
        int_current_stock = int(str_current_stock)
        int_new_stock = int_current_stock + int_change_of_stock
        str_new_stock = str(int_new_stock)
        str_byte_new_stock = str_new_stock.encode('utf-8')
        byte_current_item_info = mmaped_item_info.read()
        byte_new_item_info = byte_current_item_info.replace(str_byte_current_stock, str_byte_new_stock)
        str_new_item_info = byte_new_item_info.decode('utf-8')
        mmaped_item_info.close()
        new_file_size = len(str_new_item_info)
        file.truncate(new_file_size)
        file.flush()
        mmaped_item_info = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_WRITE)
        mmaped_item_info.write(byte_new_item_info)
        mmaped_item_info.flush()
        file.close()
        mmaped_item_info.close()
        return None
    else:
        return None

import mmap

# there is probably a way to make this method way more efficient with more code basically what
# we could do is like go like ok if it detects mutiple of one item then it runs a for loop
# eliminating all the same items until it returns false then when it returns false then
# all items have been yeah i wanna do that to mtiigate the amoutn of searching of products
# because that is quite a computer taxing resources idkkk its like a very
# taxing event euhehguherugh idk
    
def sum_total_receipt(s_input_item_list):
    global required_inventory_data
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
# imma be honest idk what to do i want to make an as efficient solution as possible
# and i see so many fucking count methods that do the same fucking thing and I want to like basically
# somehow put them all together or some shit it must be possible. i feel like that like yeah
# i feel like that yeah. hmmm idk what the fuck to do but i feel like that like basically i can
# like somehow robably return the counts of items somehow and then use them in the receipt text
# functon i feel like i guess something i could do is whenever you try to create a receipt text
# then what happens is like basically the sum total reciept funtion is called then what happens 
# after that is lie basically the receipt total function reutns the total of the cart but then
# also returns the count of the items that it found idk. but how can i have a for loop basically
# like take the element within the list then like store every single different item ideintifier
# into a different variable the nreutnr hte vairale i could return a tuple or a list xD
# but thats the fucking same thing though i mean i guess like we could create a ok i guess we could
# basically amost like create elements within a dictioary where they have the item and then
# the like amount that the item was bought i feel like that makes sense then basically
# we have a long ass thing that basically jesus ok. so basically we need like basically all
# the data if we want this program to work so basically it seems like in certain instances we
# only need basically the name of hte product but in ceratin other points we only need the
# price and then in other points we only need the stock so then how do we decide when at what
# time do we need certain uhm information well we could always call the information seperealy
# but it does seem that we just simply need basically all the fucking information of all the
# products purchased in the cart i guess maybe what we could do


def receipt_text(p_input_item_list, ):
    input_copy = copy.deepcopy(p_input_item_list)
    receipt_text_list = []

    for p_item in p_input_item_list:
        item_id = p_item

        mmaped_inventory = mmaps_inventory()
        mmaped_inventory.seek(0)

        if p_item != None:
            byte_array_data_item_we_searching_for = p_item.encode('utf-8')
            input_item_position_in_inventory = mmaped_inventory.find(byte_array_data_item_we_searching_for)

            if input_item_position_in_inventory != -1:
                int_number_of_item_in_list = p_input_item_list.count(item_id)
                str_number_of_items_in_list = str(int_number_of_item_in_list)
                current_index_logger_of_element = -1
                for element in p_input_item_list:
                    current_index_logger_of_element += 1
                    if element == item_id:
                        p_input_item_list[current_index_logger_of_element] = None
                        
                line_of_product_info = product_data_info(mmaped_inventory, item_id)
                product_name = takes_out_name(line_of_product_info)
                product_price = takes_out_price(line_of_product_info)

                int_total_product_bought = int_number_of_item_in_list * product_price
                str_total_product_bought = str(int_total_product_bought)
                receipt_text_list.append(str_number_of_items_in_list)
                receipt_text_list.append('x ')
                receipt_text_list.append(product_name)
                receipt_text_list.append(' ')
                receipt_text_list.append(str_total_product_bought)
                receipt_text_list.append('\n')
            
    total = sum_total_receipt(input_copy)
    receipt_text_list.append('\n')
    receipt_text_list.append(total)

    receipt_text_ = ''.join(str(element_) for element_ in receipt_text_list)

    return receipt_text_

def print_receipt(_receipt_text):
    print(_receipt_text)

def answer_y_or_n(question):
    while True:
        _answer = input(question)
        if _answer == 'y':
            return _answer
        elif _answer == 'n':
            return _answer
        elif special_option_press_test(_answer):
                pressed_option = _answer
                return pressed_option
        else:
            print()

# you know what would be a cool idea to save ocmputing power perhps like baiscally store
# ok 2 ideas lets sart with one though so what we could do is stor ehte receipt text into a global
# varialbe this is used to save memory basically what i could do is make the global vairalbe
# this and then after storing the reeipt
# ok wait genius ok so lets make an empty list call it:
# receipt_text_memory = [receipt_text, item_list_used_to_make_receipt_text] ok we can change the
# names later but look here its perfect so then basically what happens is that basically
# when the checkout funciton is used or whatever then basically yeah the checkout funciton
# is gonna check ok this is the current shopping cart and this was the shopping cart used to
# create the receipt text ok so now if the shopping cart used to create the receipt text is
# the same yeah if its the same then ok it just uses hta treciept text but if it isnt the same
# then what happens is the program will then run the receipt text function again to then
# create a new receipt that reflects the items in the shopping cart
# another idea how about fuck ust do htis idea how about even with the receipt text has this functio
# basically like it checks ok is the current shopping cart the same as the one that was used
# to 
# oh my god i could use this same method for memory amagement ok if the shopping cart is the
# same as before then dont reload items then if its different then reload items then even when
# it reloads items then it does chekcs like ok if this item already in the diciotnary if it is
# then dont add it if it doesnt exist then add it and if there is one that is in the diocntary
# but not in the g_item_list then remove it oh my goddd ok thats perfect
            
# i feel more scared to program??? its weird like i genuinely feel less like i want to
# and i literall think its justbecause i didnt go for a walk before this work? so weird???
# wow i dont feel like programming right now and its weird. imma be honest.
# i havent felt this way in the past 2 weeks and for all those days all i did was take a long ass
# walk bfeore i programmed ok TOMOORW WE WILL DO THAT IDC THE COSTS

def creates_receipt_file(receipt_str):

        str_receipt_number = input('What receipt number do you want?')
        if str_receipt_number.isdigit():
            # opens receipt_number_database.txt file
            with open('Receipt_number_database.txt', 'r') as receipt_number_database_file:
                mmaped_receipt_file = mmap.mmap(receipt_number_database_file.fileno(), 0, access=mmap.ACCESS_READ)
                str_receipt_number_in_bytes = str_receipt_number.encode('utf-8')
                receipt_number_postion = mmaped_receipt_file.find(str_receipt_number_in_bytes)

            if receipt_number_postion != -1: # code will ask to overwrite or cancel thingy then if you choose to cancel it will go back to creates receipt
                # receipt does exist
                print('receipt does already exist')
                question = 'enter y to overwrite file or enter n to not overwrite the file and reset the function' # still need to add the back function
                answer = answer_y_or_n(question)
                if answer == 'y': # said yes
                    # opens and deletes contents of receipt file
                    with open (receipt_address, 'w') as receipt_file:
                    # writes receipt onto receipt file
                        receipt_file.write(receipt_str)
                elif answer == 'n': # said no
                    return 's'
                elif special_option_press_test(answer):
                    pressed_option = answer
                    return None, None, pressed_option

            elif receipt_number_postion == -1:
                # receipt doesnt exists
                with open('Receipt_number_database.txt', 'a') as receipt_number_database_file:
                # creating receipt address (not relative will make relative)
                    receipt_suffix = str_receipt_number + ".txt"
                    receipt_file_path = "C:\\Users\\MSI\\Desktop\\CashRegister\\Receipts\\receipt"
                    receipt_address = receipt_file_path + receipt_suffix
                    receipt_number_database_file.write(str_receipt_number)
                    receipt_number_database_file.write('\n')

                # creates receipt file
                with open (receipt_address, 'w') as receipt_file:
                    # writes receipt onto receipt file
                    receipt_file.write(receipt_str)



def prerequesite_input_collection_creates_receipt_file():
    pressed_option = 'l' # might need to be s so that when function is run through hte program reutnrs to function 1 becuase like why print 2 of the same receipt file

    while True:
        str_receipt_number = input('What receipt number do you want?')
        if special_option_press_test(str_receipt_number):
            pressed_option = str_receipt_number
            return pressed_option
        elif str_receipt_number.isdigit():
            with open('Receipt_number_database.txt', 'r') as receipt_number_database_file:
                mmaped_receipt_number_database = mmap.mmap(receipt_number_database_file.fileno(), 0, access=mmap.ACCESS_READ)
                str_receipt_number_in_bytes = str_receipt_number.encode('utf-8')
                receipt_number_postion = mmaped_receipt_number_database.find(str_receipt_number_in_bytes)
            if receipt_number_postion != -1:
                print('receipt does already exist')
                question = 'enter y to overwrite file or enter n to not overwrite the file and reset the function' # still need to add the back function
                answer = answer_y_or_n(question)
                if answer == 'y': # said yes
                    pressed_option = answer
                    return str_receipt_number, pressed_option, mmaped_receipt_number_database
                elif answer == 'n': # said no
                    pressed_option = answer
                    return None, pressed_option
                elif special_option_press_test(answer):
                    pressed_option = answer
                    return str_receipt_number, pressed_option, mmaped_receipt_number_database
            elif receipt_number_postion == -1:
                print('your file doesnt exist now will create file')
                return str_receipt_number, pressed_option, mmaped_receipt_number_database
                

def main_processing_creates_receipt_file(receipt_number , _receipt, _mmaped_receipt_number_database, answer_slash_input): # str_receipt_number, answer
    if (_receipt != None) and (answer_slash_input != None) and (receipt_number != None) and (_mmaped_receipt_number_database != None):
        mmaped_receipt_number_database = _mmaped_receipt_number_database
        receipt_suffix = receipt_number + ".txt"
        receipt_file_path = "C:\\Users\\MSI\\Desktop\\CashRegister\\Receipts\\receipt"
        _receipt_address = receipt_file_path + receipt_suffix

    if answer_slash_input == 'y':
        with open (_receipt_address, 'w') as receipt_file:
            # writes receipt onto receipt file
            receipt_file.write(_receipt)
            return 'i'
        
    elif answer_slash_input == 'u':
        # receipt doesnt exists
        with open('Receipt_number_database.txt', 'a') as receipt_number_database_file:
        # creating receipt address (not relative will make relative)
            mmaped_receipt_number_database.write(receipt_number)
            receipt_number_database_file.write('\n')
        # creates receipt file
        with open (_receipt_address, 'w') as receipt_file:
            # writes receipt onto receipt file
            receipt_file.write(_receipt)
            return 'i'


















def complete_program_loop(func_option): # selected s by default
    global g_item_list

    while True:
# 1ST FUNCTION
        if func_option == 1:
            input('we are currentky on function 1')
            add_item_list_c = prerequesite_information_collection_append_item_cart()
            main_processing_append_item_cart(add_item_list_c[0])

            selected_option = special_option_return(add_item_list_c[-1])
            if selected_option[-1]: # here uowards i problem soeting is causing this to be none
                return selected_option[0]
            else:
                print('Input an item into the list before proceeding')
                return 1
            

    

# 2ND FUNCTION
        elif func_option == 2:
            input('we are currentky on function 2')
            input_change_cart = prerequesite_input_collection_change_cart() # ok if i want to degu agin instead of using input ommands just forcean error thats genius
            main_processing_change_cart(input_change_cart[0], input_change_cart[1])
            selected_option = special_option_return(input_change_cart[-1])
            if selected_option[-1]:
                return selected_option[0]


# 3RD FUNCTION
        elif func_option == 3:
            input('we are currentky on function 3')
            input_insert_cart = prerequesite_input_collection_insert_cart() # add_item_list_c[-1] has to be i right???
            input('we are currentky on function 3')
            main_processing_insert_cart(input_insert_cart[0], input_insert_cart[1])

            selected_option = special_option_return(input_insert_cart[-1])
            if selected_option[-1]:
                return selected_option[0]
            

# 4TH FUNCTION
        elif func_option == 4:
            input('we are currentky on function 4')
            if g_item_list != []:
                _receipt_text = receipt_text(g_item_list)
                print_receipt(_receipt_text)
                return 1
            else: # no input therefore no selected option
                print('monkey you havent entered anything into item list now you go back to begining')
                return 1
       

# 5TH FUNCTION
        elif func_option == 5:
            input('we are currentky on function 5')
            if g_item_list != []:
                input_creates_receipt = prerequesite_input_collection_creates_receipt_file() # [0]= str_receipt_number, [1] = pressed_option, [2]=mmpaed_receipt_number_database
                selected_option = special_option_return(input_creates_receipt)
                _receipt_text = receipt_text(g_item_list)
                main_processing_creates_receipt_file(input_creates_receipt[0], _receipt_text, input_creates_receipt[2], input_creates_receipt[1])
                if selected_option[-1]:
                    return selected_option
                

# 6TH FUNCTION
        elif func_option == 6:
            input('we are currentky on function 6')
            g_item_list = []


# 7TH FUNCTION 't' (changes stock of product line)
        elif func_option == 7:
            input('we are currentky on function 7')
            input_change_inventory = prerequesite_information_collection_change_inventory()

            int_change_stock = input_change_inventory[0]
            product_data_line = input_change_inventory[2]
            line_start_position = input_change_inventory[3]
            length_to_truncate = input_change_inventory[4]
            mmaped_inventory_return = input_change_inventory[-2]
            pressed_option = input_change_inventory[-1]
            str_old_stock = input_change_inventory[1]

            selected_option = special_option_return(input_change_inventory[-1]) 
            print(input_change_inventory)
            print(str_old_stock)
            print(int_change_stock)
            print(product_data_line)
            print(line_start_position)
            print(length_to_truncate)
            print(mmaped_inventory_return)
            print(pressed_option)
            print(type(str_old_stock))
            input('jerog')
            main_processing_change_inventory(int_change_stock, str_old_stock, product_data_line, line_start_position, mmaped_inventory_return, length_to_truncate)
            # int_change_stock = amount we will change stock by (- or +)
            # selected_product_data_info[1] = product data line,
            # selected_product_data_info[2] = line position within inventory
            # mmaped inventory = memory map of inventory 
            # pressed option so you can cycle through functions
            if selected_option[-1]:
                return selected_option[0]

# ok so i wana figre out how we are gonna change stock. so basically waht we could do is after you checkout the shopping cart which literally does every thing yeah makes sense
# then basically what i could do is like take the counts of each item that i did in receipt text return them then basically take stocks of the inventory data then like






            






# i want this function to basically just be able to change the stock ammount in the iventory so 
# bascially i guess what we could do is jus search for a specific item identifeir within the invnotry database
# then when we find it we bascically take all the product information then dispplay it and hten display the stock seperatley and say
# this is your item then we say this x stock, enter the amount you want to change
# then basically yeah you write own hte ammontoy want to hacnegthen it taes the product informatinon
# line then finds the poinnt of the stock and then stores the stock as an integer value
# then it adds the ammount you wrote down to the stock value then it takes the new stock and then
# deletes the old stock value and then replaces it with the new stock value then it replaces the product line
# in the inventory database ok so thats quite a few steps but very very doable we basically have
# done quite similar things before so its definitely possible we just gotta try

        








g_item_list = []

selected_option = 1
# ok now what solution should i introduce to the fuction logger problem??? idk tbh. i feell ikeayeh i have no idea


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












# ok so bsaiclly eyah i can see that the reaosn they are laguihng isbecuas they quite 
