print('''
          __-----__
     ..;;;--'~~~`--;;;..
   /;-~IN GOD WE TRUST~-.\
  //      ,;;;;;;;;      \\
.//      ;;;;;    \       \\
||       ;;;;(   /.|       ||
||       ;;;;;;;   _\      ||
||       ';;  ;;;;=        ||
||LIBERTY | ''\;;;;;;      ||
 \\     ,| '\  '|><| 1995 //
  \\   |     |      \  A //
   `;.,|.    |      '\.-'/
     ~~;;;,._|___.,-;;;~'
         ''=--'

Instructions:
1. Enter 'i(item number)' to add the desired item to your receipt e.g i1.
2. Enter 'c' to change an item in the list enter the item postion 
   within the lsit you want to change and then enter the 
   replacement item e.g to change item 2,       enter 2 
3. Enter r to restart.
4. Enter v to view the current list being curated.
5. Enter to sum up the item list
6.

You can perform these commands at any time

warning: do not add quatiotn in examples
''')
item_list = []
int_total = 0
string_total = ''
def make_and_modify_item_list():
    global item_list
    while True:
        item = input('''lets add an item.--->''')
        if item == 'x':
            break
        options_item(item)
        prevent_option_input_item_to_change_list(item)
        #    elif c_item_position != 'c':
#        options()

def options_item(item):
    global item_list
    if item == 'v':
        print(item_list)
    elif item == 'i':
        i_item_position = input('''Enter item position you want to
        insert? e.g 2 is equal to the 2nd item in the list
        --->''')
        i_item_insert = input('Enter the item you want in the item postion')
        item_list.insert(int(i_item_position) - 1, i_item_insert)
    elif item == 'c':
            c_item_position = input('''Enter item position you want to 
            change? e.g 2 is equal to the 2nd item in the list
            --->''')
            c_item_replacement = input('''Enter the item you want in the item postion''')
            item_list[int(c_item_position) - 1] = c_item_replacement


def prevent_option_input_item_to_change_list(item):
    global item_list
    if item == 'i':
        item = None
    elif item == 'v':
        item = None
    elif item == 'c':
        item = None
    else:
        item_list.append(item)
def replace_item_identifiers_with_prices():
    global item_list
    #item list command, checks + repaces with money.
    while True:
    #gtx1050 2gb
        if item_list.count('i1') > 0:
            item_list[item_list.index('i1')] = 3000
    #gtx1060 3gb
        elif item_list.count('i2') > 0:
            item_list[item_list.index('i2')] = 4000
    #RX480 8gb
        elif item_list.count('i3') > 0:
            item_list[item_list.index('i3')] = 4500
    #RX580 8gb
        elif item_list.count('i4') > 0:
            item_list[item_list.index('i4')] = 4500
        else:
            return item_list

def input_validation():
    for item_in_list in item_list:
        String_identifier = isinstance(item_in_list, str)
        if String_identifier == True:
            del item_list[item_list.index(item_in_list)]
            #item_list.pop(item_list.index(items1))
            #item_list[item_list.index(items1)] = None
            #item_list.remove(items1)

def sum_total_item_list():
    global item_list
    global int_total
    global string_total
    int_total = sum(item_list)
    string_total = str(int_total)
    #return int_total we might need this code for the program to work
    return string_total

i1_bought_receipt = None
i2_bought_receipt = None
i3_bought_receipt = None
i4_bought_receipt = None

def terminal_print_receipt():
    global i1_bought_receipt
    global i2_bought_receipt
    global i3_bought_receipt
    global i4_bought_receipt

    if item_list_receipt.count('i1') > 0:
        i1_bought_receipt = str(item_list_receipt.count('i1')) + 'X' + ' GTX 1050 2GB' + ' ' + str(item_list_receipt.count('i1') * 3000)
    if item_list_receipt.count('i2') > 0:
        i2_bought_receipt = str(item_list_receipt.count('i2')) + 'X' + ' GTX 1060 3GB' + ' ' + str(item_list_receipt.count('i2') * 4000)
    if item_list_receipt.count('i3') > 0:
        i3_bought_receipt = str(item_list_receipt.count('i3')) + 'X' + '   RX 480 8GB' + ' ' + str(item_list_receipt.count('i3') * 4500)
    if item_list_receipt.count('i4') > 0:
        i4_bought_receipt = str(item_list_receipt.count('i4')) + 'X' + '   RX 580 8GB' + ' ' + str(item_list_receipt.count('i4') * 4500)
#prints receipt

    if i1_bought_receipt != None:
        print(i1_bought_receipt)
    if i2_bought_receipt != None:
        print(i2_bought_receipt)
    if i3_bought_receipt != None:
        print(i3_bought_receipt)
    if i4_bought_receipt != None:
        print(i4_bought_receipt)
    print(int_total)

#counts amount of specific items in item list to be added to receipt

def receipt_check():
    receipt_check = None
    while receipt_check not in ("y", "n"):
        receipt_check = input('Are your items correct? Answer y or n')
        if receipt_check == 'y':
            break
        elif receipt_check == 'n':
            redo_shop()
        else:
            print('Please enter y or n')

def redo_shop():
    make_and_modify_item_list()
    item_list_receipt = copy.deepcopy(item_list) #this code in the redoshop i believe probably doesnt work??? or maybe it does idk
    replace_item_identifiers_with_prices()
    input_validation()
    sum_total_item_list()
    terminal_print_receipt()

#note \/\/\/\/\/\/\/
"""
so basically i thought a fucking great idea would be to basically take ALL THE VAIRALBES and make them all = to None at the start function in
yeah bsacilyl to number 1 establsih all the vairlabes but nubmer 2 if i ever redo the shop there will be no bugginesss activity because all of the viarables that were used would be set to none again for second
use althouh i could just do that as an extra feature??? like as in make another function that does that that only activiates when you do the redo shop which yeah both would work i am gonna do the second
function option because i feel like it is gonna use hte east ocmptuing power

"""

receipt_number = '1'
receipt_suffix = receipt_number + ".txt"
receipt_name = "C:\\Users\\MSI\\Desktop\\CashRegister\\Receipts\\receipt"
receipt_address = receipt_name + receipt_suffix

def place_receipt_on_file_question():
    place_receipt_on_file_yorn = None
    while place_receipt_on_file_yorn not in ("y", "n"):
        place_receipt_on_file_yorn = input('Do you want receipt to print on receipt file? answer y or n --->')
        if place_receipt_on_file_yorn == 'y':
            place_receipt_on_file()
        elif place_receipt_on_file_yorn == 'n':
            break
        else:
            print('Please enter y or n')



    #file = open(receipt_address, "a")
def place_receipt_on_file():

    if int_total > 0:
        receipt_number = input('What receipt number do you want?')

        byte_receipt_number = receipt_number.encode('utf-8')
        with open('Receipt_number_database.txt', 'rb', 0) as file:
            s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
            if s.find(byte_receipt_number) != -1:
                print(f'String {byte_receipt_number} exists in the file.')
                print('will not append receipt number to database because receipt file already exists and is detected in the receipt number database (function still to be made)')
                #so basically after this i think what i want is for the person to then be asked the question ok do you want to change the uhm receipt number and then if they answer yes then yeah
            else:
            #open_test = open(r"C:\\Users\\MSI\Desktop\\CashRegister\\Receipt_number_database.txt", 'w')#idk uwah
                with open(r"C:\\Users\\MSI\Desktop\\CashRegister\\Receipt_number_database.txt",'a') as write_receipt_number_object:
                    write_receipt_number_object.write(receipt_number + '\n')
            #this adds the receit number to the receipt nubmer dayabse file ^^^^^^^^^^^^^^^
                    receipt_suffix = receipt_number + ".txt"
                    receipt_name = "C:\\Users\\MSI\\Desktop\\CashRegister\\Receipts\\receipt"
                    receipt_address = receipt_name + receipt_suffix
                    #file = open(receipt_address, "a")
                    with open(receipt_address, "w") as receipt_write_instance_variable:
                        if i1_bought_receipt != None:
                            receipt_write_instance_variable.write(i1_bought_receipt + '\n')
                        if i2_bought_receipt != None:
                            receipt_write_instance_variable.write(i2_bought_receipt + '\n')
                        if i3_bought_receipt != None:
                            receipt_write_instance_variable.write(i3_bought_receipt + '\n')
                        if i4_bought_receipt != None:
                            receipt_write_instance_variable.write(i4_bought_receipt + '\n')
                        #I assume what this code does is like basically basically writes the receipt i think??? yes yes yes yes i think that is exactly what it does

from ast import While
import copy
from tkinter import N
import mmap
make_and_modify_item_list()
item_list_receipt = copy.deepcopy(item_list)
replace_item_identifiers_with_prices()
input_validation()
sum_total_item_list()
terminal_print_receipt()
receipt_check()
place_receipt_on_file_question()