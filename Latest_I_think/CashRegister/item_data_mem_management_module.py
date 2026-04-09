import mmap

def item_data_mem_updater(set_new_item_data, setting):

    if setting == 's':
        global shopping_cart_item_data_mem
        current_items_data_in_mem = shopping_cart_item_data_mem['items_data_in_memory']
        set_old_item_data_mem = shopping_cart_item_data_mem 
    elif setting =='e':
        global extra_items_data_mem
        current_items_data_in_mem = extra_items_data_mem['items_data_in_memory']
        set_old_item_data_mem = extra_items_data_mem
    if item_data_mem != {}:
        if set_old_item_data_mem != set_new_item_data:
            item_data_mem['items_data_in_memory'] = set_new_item_data
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




extra_item_mem = {'items_data_in_memory' : set()}  # shopping_cart_item_data_mem = {'items_data_in_memory' : set(), 'i1' : 1, 'i2' : 4}

set_unique_extra_items_mem = set(extra_item_mem.keys())

item_data_mem_updater(set_unique_extra_items_mem, 's')

shopping_cart_item_data_mem = {'items_data_in_memory' : set()} # shopping_cart_item_data_mem = {'items_data_in_memory' : set(), 'i1' : 1, 'i2' : 4}
shopping_cart_unqiue_item_set = set(shopping_cart_item_data_mem.keys())

item_data_mem_updater(shopping_cart_unqiue_item_set, 's')

print(shopping_cart_item_data_mem)

print(set_unique_extra_items_mem)


# ok now what i ened to add is a statementthat literally just colelct inputs of code or i could make it a function that i will insert into hte code that makes sens. that after all the check IF THEY ARE SUCCESSFUL then
# what will happen is the aoslutel last ting i feel like that what wil
# ok we need to makea fucntion that will teirally just add the input varibles into hte thing and then what i can do is make them none before and and if htey are none then ok so the extra items mset really doesnt need to have like
# a adder thing and the shopping cart too so en i geuss we are finishd then because like basically. oh shit nah ok we could keep track of hte extra items in mem as the first item like we usually did.
# and then if there is any differenc. nah but what if i watn to add one to memi guess i could jsut take the mem and hten tsay ok do this but the thing is we need to limit how many can be added
# ok lets make a limit of like 8 we can only have 8 items in extra item mem just to rpevent mem stack overflow. ok thts a fucign rgeat dea we are gonna limit it to 8 and then the way we are gonna add it is that
# we are gonna take the unique item list in mem then basically waht arwe are gonna d is add another item t it and if the set has the same item then basically wahts gonna happen is nothing will happen and then the memroy
# wont be changed. so basically now what we could do is make a fucntion that adds all the inputted items to the function in a sense??? yeah. i feel like that like wahtweculd od si also make a function that makes the exta
# i got a genius idea. we need to add a function taht tests the input cart for the thing. another htign that culd be cool is make functions be able to use the shopping cart mem and hte extra items mem so baically like
# the first thing that gets tested is the shopping cart mem and then after that the . oh my god i got another idea. ok we gotta do one idea at a time. so first lets make it that there is like a small memory.

# ok i got a sick idea so basically what we could do is yeah make an if satemtent that is like if this item is in this mem then read that or if the item is in this mem then read that and else if its in none then report an
# error. so baiscally yeah that makes sense ltes dothat then after htat we can do the other hting. ok nah lets make a lsit then do it tomorrow

# make if statement that reads memory

# i could also make a function that searches for an item in both memory modules and then if the items data doesnt exit in mdule dont reutnr nayhting i guess yeah and hten that will make. because we are gonna
# be repearitng hte same ass code 20 million times so basically like functions owuld be nice i could go like ok run the memory seracher and then. hmmm i feel le that i gotta rethink this memroy mudle ok so we got a memory module updater that ltierally
# udpates it to the exact set of items and shit then after that then. ok then make one thing ok i got a fucking great idea. just make a funciton taht seraches the meory then if the item doesnt exit in memory then the
# mem is updated. that is a great idea

# and then i had another idea to add chunk loading to my memory mamgenment so basically what i could do is say thtatthe limit for hte shopping items whateve ris like 32 items and then like ok so so then if the memory
# searchr ends up returning false then baiscaly waht happens is the memory gets udpated then the item gets extracted after the update.

def mem_searcher(item_id, setting):
    item_data = None
    if setting == 's':
        global shopping_cart_item_data_mem
        if item_id in shopping_cart_item_data_mem:
            item_data = shopping_cart_item_data_mem[item_id]
    elif setting == 'e':
        global extra_item_mem
        if item_id in extra_item_mem:
            item_data = extra_item_mem[item_id]

    if item_data == None:
        print('item does not exist in mem need to add it to mem')
    return

# i mean it woudl make sense that we could use the cleaner for the. ok nah so bascialyl this other extra memory thing is not gonna need a cleaner thing ecause it is nly gonna contains like 30 item information otherwise
# its just gonna delete them but the problem is once i start to limit the meomry to only a few tiemsdatas whatever then baiscally waht i am gonna have to do then also is bsiaclly to prevent a stac overflow or memory lea
# is to basicallyyeah be able to somehow intitaie chunk aoding like say like ok now we have 30 items in data whatever so then whwat i want i a way to like use the memory as data or something if for some reason the
# computer needs more than like 30 items data to load into memory then what i woud need is that baiscally i coulduse hte ahrdrive space as temporary memory for item data thats a cool idea. ok creating all these systesms
# at once is gonna be super fucign diffcitl so i say what we do is actually break it down into little parts and then after that ok that makes sense yeah. o bascially eyah lets do that then. so we are gonna make
# a whole ass memory amagnement system then try to implent taht into our program

def load_hard_drive_item_into_mem(item_id, setting):
    if setting == 's':
        global shopping_cart_item_data_mem
        item_data_mem = shopping_cart_item_data_mem
    elif setting =='e':
        global extra_item_mem
        item_data_mem = extra_item_mem
    if item_id == None:
        item_address = 'Inventory/' + item_id + '.txt'
        f =  open(item_address, 'r')
        mmaped_f = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        byte_str_file_contents = mmaped_f.read()
        byte_str_product_info = byte_str_file_contents.split(b'|')

        decoded_name = byte_str_product_info[0].decode('utf-8')
        decoded_price = float(byte_str_product_info[1].decode('utf-8'))
        decoded_stock = int(byte_str_product_info[2].decode('utf-8'))

        item_data = [decoded_name, decoded_price, decoded_stock]
        item_data_mem[item_id] = item_data

def cleans_

item_data_mem = {key: value for key, value in current_items_data_in_mem.items() if key in set_new_item_data or key == 'cart_in_memory'}



# ok the ai
# i just thoughtaobut it how about we make afuctionthat ltierally just checks if an item exist sin emory then makes item data= to that data then baiscally eyh so basically now waht i want is a way to literally just add
# one item to memory i can use the big memory amagneemnt software but hoenstlyi feel like that i could make a seperate smaller function that is gonna takeup less memory bascaly so if elel ike yeah. so eiter ica n make a function
# that is smalerand that literally just adds the item to

# so this is bascialyl for the extra items data info shit i feel like that like yeah i guess we coudl then also usethe 




# if i do this i am baiscally gonna be reactirng the top function but with extra steps. yeah so then might as well just use tge ther fucntion yeah but tthe thing is like the problem is that if the item doesnt exit in memory
# at an input point then what we could do is botain the item data via hardrie search so basically that will be like big memory then the other will be like short term memory yeah that makes sense. we could do that oh my god this
# shit is gonna work. ok so baiscally we could go liek if item id = None then do this but we could just do this on the otside