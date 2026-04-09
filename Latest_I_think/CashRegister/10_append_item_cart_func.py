import os

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
    
def idigit_format_checker(input_str):

    if input_str.startswith('i') and input_str[1:].isdigit():
         return True
    else:
         return False


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

# ok basically  iwant to make a function that allwos you to add or subtract the number of items
# from the 
# should i add a replace function??? hmmm i mean like i guess i could but what would be the use
# of that if i can just delete an item from the shopping cart then just add another one
# nah im not making a replace function just make it that you delete it then add a new one then also
# do you want to be able to print the current receipt??? i mean yeah why not but we already have
# a function like that so yeah we just need it to be compatible with this funtion now
# but the thing is that basically the other functions after 5 basically are literally
# just use the loaded_memory so the if they use the loaded_inventory_memroy and dont even use the
# the current cart then i guess what we could do is just like basicallychange tha 



current_cart = {}
append_item_cart_func()
