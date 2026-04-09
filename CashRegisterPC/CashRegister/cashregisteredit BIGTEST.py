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
total = None
def make_and_modify_item_list():
    global item_list
    while True:
        item = input('''lets add an item.--->''')
        if item == 'x':
            break
        view_item_list(item)
        change_item_list(item)
        insert_item_into_item_list(item)

        prevent_option_input_item_to_change_list(item)
        
        else:
        item_list.append(item)







def view_item_list(is_input_variable_v):
global item_list
    if is_input_variable_v == 'v':
        print(item_list)

def insert_item_into_item_list(is_input_variable_i):
global item_list
    if is_input_variable_i == 'i':
        insert_item_position = input('''Enter item position you want to
        insert? e.g 2 is equal to the 2nd item in the list
        --->''')
        item_insert = input('Enter the item you want in the item postion')
        item_list.insert(int(insert_item_position) - 1, item_insert)


def change_item_list(is_input_variable_c):
    if is_input_variable_c == 'c':
        item_position_to_change = input('''Enter item position you want to 
        change? e.g 2 is equal to the 2nd item in the list
        --->''')
        item_replacement = input('''Enter the item you want in the item postion''')
        c_item_replacement = item_list[int(item_position_to_change) - 1]

def prevent_option_input_item_to_change_list(is_input_variable_an_option):
    global item_list
    if is_input_variable_an_option == '':
        is_input_variable_an_option = None
    elif not is_input_variable_an_option.startswith('i'):
        is_input_variable_an_option = None
    elif not is_input_variable_an_option[1:].isdigit():
        is_input_variable_an_option = None
    else:
        item_list.append(is_input_variable_an_option)



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
    global total 
    total = sum(item_list)
    total = str(total)
    return total

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
    print(total)

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
    item_list_receipt = copy.deepcopy(item_list)
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

#receipt_number = "1.txt"
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

'''

receipt_number = ''
receipt_suffix = receipt_number + ".txt"
receipt_name = "C:\\Users\\MSI\\Desktop\\CashRegister\\Receipts\\receipt"
receipt_address = receipt_name + receipt_suffix

'''

def place_receipt_on_file():
    global i1_bought_receipt
    global i2_bought_receipt
    global i3_bought_receipt
    global i4_bought_receipt

    receipt_number = input('What receipt number do you want?')

#checks receipt number data base if this receipt number has already been used and therefore might needto overwrite another receipt



#then asks if you wanna overwrite the receipt or if you wanna use another number if the receipt number is in use






#if you say yes or if the receipt nubemr in the receipt databse is not in ue then it will just make a new receipt




#if a new receipt is made then 1 is added to the current_receipt_file_logger file in order to eyah basically do shit

#lets jsut make code to add a number to a the receipt_number_dataabse










    receipt_suffix = receipt_number + ".txt"
    receipt_name = "C:\\Users\\MSI\\Desktop\\CashRegister\\Receipts\\receipt"
    receipt_address = receipt_name + receipt_suffix

    file = open(receipt_address, "a")

#r"C:\Users\MSI\Desktop\CashRegister\Receipts\receipt.txt"

    receipt_wrote_something = 0
    with open(receipt_address, "w") as receipt_write_instance_variable:
        if i1_bought_receipt != None:
           receipt_write_instance_variable.write(i1_bought_receipt + '\n')
           receipt_wrote_something += 1 
        if i2_bought_receipt != None:
           receipt_write_instance_variable.write(i2_bought_receipt + '\n')
           receipt_wrote_something += 1 
        if i3_bought_receipt != None:
            receipt_write_instance_variable.write(i3_bought_receipt + '\n')
            receipt_wrote_something += 1 
        if i4_bought_receipt != None:
            receipt_write_instance_variable.write(i4_bought_receipt + '\n')
            receipt_wrote_something += 1
# ok so something here downwards went wrong \/\/
        if receipt_wrote_something > 0:
            Receipt_number_database_file_object = open('Receipt_number_database.txt', 'r')
            searching_receipt_number_mmap_object = mmap.mmap(Receipt_number_database_file_object.fileno(), 0, access=mmap.ACCESS_READ)
            receipt_number_in_bytes = int(receipt_number).to_bytes(2, byteorder='big')
            if searching_receipt_number_mmap_object.find(receipt_number_in_bytes) != -1:
                print('will not print because function already exists (function still to be made)')
                
                
                
                
                
                #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                #so basically if now it sees ok the receipt number is on the file then what happens??? then its gonna ask ok do you wanna overwrite the file or nah and then if you say yeah i 
                #wanna overwrite the file then yeah it overwrites it and then if you say nah then its gonna ask you to change the receipt number and then contue??? yoh ok thats hectic lets
                #just make a function where it says ok yes receipt number is on here so then do you want to overwrite it then it overwrites it and then if you say no
                #then what it can do is just end the program lets start with that yeah.

            if searching_receipt_number_mmap_object.find(receipt_number_in_bytes) == -1:
                    print('string doesnt exist in the file')
                    test = input('string doesnt exist.')
                    with open('Receipt_number_database.txt','w') as write_receipt_number_object:
                        write_receipt_number_object.write(receipt_number + '\n')
                        receipt_wrote_something = 0

            #if srting doesnt exist then what do we do??? well then we do the thing and then yeah. what we could do is like if it doesnt exist then we add the receipt nubmer onto the database
            #like append it or nah and then after we append it then yeah we then create the receipt file
            #
            #
            #
            #

#b'laptop' use this to turn a string into bytes^^^^^^

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














'''
Receipt
Items:     Price:
GTX 1050 -   3 000
GTX 1060 -   4 000
RX 480   -   5 000
RX 580   -   5 000
sumtotal -  17 000






'''










'''sum_total_item_list(item_list,total)'''

'''
#item list command, checks + repaces with money.

#gtx1050 2gb

if item_list.count('i1') > 0:
    item_list[index('i1')] = 3000
#gtx1060 3gb
elif item_list.count('i2') > 0:
    item_list[index('i2')] = 4000
#RX480 8gb
elif item_list.count('i3') > 0:
    item_list[index('i3')] = 4500
#RX580 8gb
elif item_list.count('i4') > 0:
    item_list[index('i4')] = 4500
'''












'''








print(item_list)





















#taxessssss
VAT_mutliplier = 1.15
if 'nonVATdeductable'



#vat deductable products or nah
nonVATdeductable 

#shop item list
GTX_1050_Ti = [2000, 'nonVATdeductable']
GTX_1060_6gb = [3000, 'nonVATdeductable']
RX_480_8gb = [3000, 'nonVATdeductable']
GTX_1070_8gb = [5000, 'nonVATdeductable']

#customer count. we can try to make the customer count update later on perhaps once we learn how to use frameworks and all that jazz.
Rcustomer1 = 0

#taxessssss
VAT_mutliplier = 1.15
if 'nonVATdeductable'



#date
date = 4/8/2023

#company name
company_name = 'GPUS for days'

#computer parts list

#reciept sum total
total_customer1 += GTX_1050_Ti
total_customer1 += GTX_1070_8gb
total_customer1 = Rcustomer1

#printing out reciept
print(date)
print(companyname)
print(total_customer1)

if 


'''