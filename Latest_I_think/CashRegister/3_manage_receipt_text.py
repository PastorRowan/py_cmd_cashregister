
import mmap

def loads_and_removes_current_cart_item_s_data_to_memory(current_cart_):
    global item_data_in_memory

    if current_cart_ != {}:
        current_cart_unique_item_set = set(current_cart_.keys())
        cart_in_memory = item_data_in_memory['cart_in_memory']
        if cart_in_memory != current_cart_unique_item_set:
            item_data_in_memory['cart_in_memory'] = current_cart_unique_item_set
            item_data_in_memory = {key: value for key, value in item_data_in_memory.items() if key in current_cart_unique_item_set or key == 'cart_in_memory'}

            for unique_current_cart_item in current_cart_unique_item_set:
                if not (unique_current_cart_item in item_data_in_memory):
                    # if item is in the current cart but not in memory
                    item_address = 'Inventory/' + unique_current_cart_item + '.txt'
                    f =  open(item_address, 'r')
                    mmaped_f = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                    byte_str_file_contents = mmaped_f.read()
                    byte_str_product_info = byte_str_file_contents.split(b'|')

                    decoded_name = byte_str_product_info[0].decode('utf-8')
                    decoded_price = float(byte_str_product_info[1].decode('utf-8'))
                    decoded_stock = int(byte_str_product_info[2].decode('utf-8'))

                    item_data = (decoded_name, decoded_price, decoded_stock)
                    item_data_in_memory[unique_current_cart_item] = item_data


    else:
        print('Please Enter an item into the cart')
        return 1, True



def create_receipt_text_func(input_cart): # take reciept_text_memoryies documented item list then ocmapre that to the impt 
    float_total = 0.
    global required_inventory_data
    global receipt_text_memory

    receipt_text_in_memory = receipt_text_memory[0]
    receipt_text_cart = receipt_text_memory[1]

    if (input_cart != []) and (input_cart != receipt_text_in_memory):
        receipt_text_list = []
        unique_item_list = [] # could make this a tuple to save memory because we are not actually ediitng the datastruuter so therefore we can like
    # basically

    # ok now basically wat we want to do is basically run hte item set thing. ok we have an item list with only unique elements now basically
    # waht i need to do is basically wait yeah thats it i did it. yeah ok now i want ot return hte receipt text memory baisally when its done
        for _element in input_cart:
            if _element not in unique_item_list:
                unique_item_list.append(_element)

        for item in unique_item_list:
            int_number_of_item = input_cart.count(item)
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

        receipt_text_memory = []
        receipt_text_memory.append(receipt_text)
        receipt_text_memory.append(input_cart)

        return receipt_text
    
    elif input_cart != []:
        receipt_text = receipt_text_in_memory
        print('Your shopping cart is empty, no changes were made to the receipt text in memory')
        return receipt_text

    elif input_cart != receipt_text_memory[1]:
        receipt_text = receipt_text_memory[0]
        print('Your shopping cart is exactly the same, no changes were made to the receipt text in memory')
        return receipt_text



        

# i guess it would be random like if you have an element now and then but i mean.
# so what order do we want do we want the order of items displayed on the receipt text
# to be related to hte order at which you write them down or you want the order
# to be random. i guess what i could do is make it that they are the order
# at which you entered them which would require you to not use a set and instead idk
# some kind of wank function that removes recurring elements in a lsit

# examples:
'''
item_data_in_memory = {'cart_in_memory' : set()}
item_data_in_memory = {'cart_in_memory' : set(), 'i1' : ('GTX1050_2GB', 3000.01, 21), 'i3': ('RX480_8GB', 4500.0, 25), 'i4': ('RX580_8GB', 4500.0, 30)}
current_cart = {'i2' : 3, 'i4' : 4}
'''

item_data_in_memory = {'cart_in_memory' : set()}
current_cart = {'i2' : 3, 'i4' : 4}

loads_and_removes_current_cart_item_s_data_to_memory(current_cart)

receipt_text = create_receipt_text(current_cart)

print(receipt_text)

# ok o now bascially. the thing we need to do is have a product_line memory dictionary that is gonna basically have item identifiers and their product lines for the receipt text then basically like th values of these
# keys will be lists that repressent the product lines and within hte product lines will just be the amountof the item that was bought and the item float total and then whenver you try to print a new receipt then basiclal
# the receipt_text_shopping_cart_mem will be compared to the new one and if its different then what will happen is the amont of item bought key values will be compared and if they are different then basically
# yeah they will be changed therefore changingthe product line then they will be joined together again??? will that change much computing power though. i mean ig ugess if i store like the float total
# and the amoount of item bought then after that have a 3rd item within hte list that being the actual product line as a string then if the integers are different then the one product line will be changed then the
# strings will be concatonated i think that should work. right??? but cant i perhaps just make one big receipt text thing then. ok make one big one then go like ok replace this old onewith the new one. okk that would
# be the most efficeint way. is actually store the entire receipt text and also store the product lines within variables then when a product line is changed then all that happens is a new product line is produced
# then a replace method is used. # wati we could take this to thenext level and just replace the float item totals and then also just replace the amount hte item was bought and then also obvously replace the
# ok the most efficient solution would be to change just one single line within a file and also be able to locate it say liek replace line 4 with this line rather than look for this string within this massive file
# it wouldbe more efficent to go to line 4 or 5 or 100 first then basically read that entire line then replace the entire line or something like that. that would make sense. so basically yeah. i feel like that
# we could rather have the dictionary. oh i like this idea have a dictionary that is equal to the line number then basically like the dictionary shows like line 1 line 2 line 3 or wahtver then wtihin each line
# will be an item identifier and then after that is gonna be the float total and the amount of the item bought and whatever. i guessthe way we could storethis i mean we could hypothetically make a dicotary within a
# dictioanry??? i mean that makes sense??? nah we dont need taht much info i think a named tuple.no we need to modift. ok nvm we gonna have to make a dictioary with a list that contains the item identifier then the
# amount of the item that was bought then the float total. ok so list with 3 items 


# receipt text blue print almost
# receipt_text_building_blocks = {1 : [item_identifier, amount_of_item_bought, float_total], 2 : [item_identifier, amount_of_item_bought, float_total], 3 : [item_identifier, amount_of_item_bought, float_total]}
# example use:
# receipt_text_building_blocks = {1 : ['i1', 2, 3000,0], 2 : ['i2', 1, 3500,0]}

# now we can use that to create a new receipt text or basically change the old one so then we dont have to make a new one each time their are changes i feel like these types of methods that i am pulling
# are not really useful for a pos sysye but if i were to like work on like a simalair information handling sysetem for MUCH MORE information tehn perhaps these methods wouldbe useful i dont feell ikethey are but i
# enjoy the challenge of making them so i shall continue

receipt_text_instructions = {1 : ['i1', 2, 3000,0], 2 : ['i2', 1, 3500,0]}

# so i say that like we get the manage receipt text func to basically create these which will act as the building blocks for the receipt text. yeah that makes sense to m
# take reciept_text_memoryies documented item list then ocmapre that to the impt i could make it that the reeipt text never actually gets written down or saved because lets say in our hypethical world that this
# code is gonna be used to idk manage chemical reactions at a lab and record the results of each trial and idk.
# couldnt we just store the current receipt text into a file perhaps like if we are gonna deal with really large files then its probably best that we store that large file into a file in a sense??? and then use hte
# file as memory basically and read and write off it as the program is being used althoghui think thats gonna cause too much computing overhead to the point the applcaition is actually becoming less practical for
# small files like it wil beable to handle smaller files but not as efficiently because of the file i/o operationst that are gonna take place.
# ok nah so lets ban this idea for larger data pools its probably better to use different programmingemthods compared to smaller files like for exmaple with lrger file you might want to lean more towards using hardrive
# space as memory over actual memory and then try to use lazy chunk loading operations or chunk loading operations instead of loading all data at once yeah so i feel like that in the contexts of our program.
# lets keep things simple as this is supposed to be for a small business s we will try to make things as simple and efficeint as psosiblethen if we want to scale up this program into like
# idk manages stock for an entire business then perahps we can start to find other means of data mangenemnt so keep in mind what is the prupsoe of your program and who is gonna use it and how big are the projects gonna
# be and who are they designed for i can always perahps sjust make a second versin ofthis program that slighly adjuts its datahandling to be more hardrive dependant so it can be used for muhc larger databases
# but then also the whole theme of the program is gonna change. ok. shall we just redo the writing eahc time for now yes then if we really want to use the receipt isntrucitons tech then we can do it later

def create_receipt_text_func(input_cart):
    float_total = 0.
    global required_inventory_data
    global receipt_text_memory