import mmap

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





# we need to create a variable that ltierally jsut stores how many item information that thing has. ok waht we could do is within our global variables waht we can do is take the global variable then make it equal to.
# oh my god i had an isnane idea we could also like put in a global arguemnt as a viarble??? then change wit within the htignah thats not gonna work becaue ig uoiu put in a rugmet of a varible that
# doesnt cange hte orginal vairable tha twas inputted
# i could create a variable called item count then make it an integer then make it that everytime a number gets added then  1 gets added to item count so yeah then basically what is gonna happen when it reaches max items
# so lets make the limit 128 then if the items count itneger reaches 128 then what do we do next. then we start writing it to hardrive then we create a system that basically. like make it that ok write all the item data
# to the text file then after that when ok lets do this ebcause i know how to do this.

# we will probs d the memory add ehck outside ofhte fucntion ebcause i dont want ot add them one by one i want to add them all togethr athte same time
# lets make setting a tuple that can t
        #est for each thing like ok if tupe tes ets do that
# opk so basically i feel like that basicaly like hmmmmmmmmm so i guess what i could do is like make it taht the memory seracher just sends out taht the item does exist in niventyro then it
# returns true then absically i could go like on the otusdie if this is true then take ut the thing i guess syea htah makes senes and also we need to udpate our memory seracehr to do a for loop that checks
# wehther the dictioaries within the dictionary have like the ok so basically i feel like that
def item_in_mem_TorF(item_id, memory_checks_list):
    global memory_module

    for mem_id in memory_checks_list:
        mem_block = memory_module[mem_id]
        if item_id in mem_block:
            return mem_id, True

def item_info_add_to_mem(item_id, memory_add_list):
    global memory_module

    for mem_id in memory_add_list:
        mem_block = memory_module[mem_id]
        if item_id not in mem_block:
            pass
        else:
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

def stack_overflow_checker(int_current_item_data_count, int_items_data_added, setting_):
    if (int_current_item_data_count + int_items_data_added) > 128:
        return False
    else:
        return True

def removes(amount_item_info_to_remove, memory_remove_list):
    global memory_module

# example:
shopping_cart_item_info_mem_OrderedDict = {{'i1' : 0 + offset, 'i2': 2 + offset, 'i3' : 3 + offset}} # where are we gonna store this inforation thoguh
# ok yeah so basically what i could even do is make it that basically ok nah this idea. ok so basically we could keep a recollection of the order the items were inputed but then what if i remove them
# what isgonna happen so an item gets removed from the memory like i1 compleltey .so then the ordered dicitonray item also must be removed too then after that then idk wht is gonna happen next after
# that yeah. i could make all the items . ok wait i got a giga brain plan how about i make all of these items the same variable but its related to each other somehow then when i cahnge 
# the one variable then all the others change. oh thats a great IDEA LIKE AN OFFSET. like almost like offset then eventualy the offest is gonna get to the point where the first item is at front so
# then the max offset is 128 then basically. oh my go hta ts A FUCKING GENIUS IDEA I REALYFUFKING LOVE THAT IDEA  AND SHIT H MY GOD OK YEAH THAT MAKES SENSE. SO THEN YEAH  we can do that i guess
# so i can make it that i might need to make hte other one equal to another varible so basicay make it like 1 + offset then chagne the offest until 1 is at the front then make the offset back = to one
# and thn i also get to mainaitn hte ability of havng like 1 - 128 as like the thig but the thing is everytime. then when the 3rd item gets removed thre is aplus 1 and everything moves up

memory_module = [{'shopping_cart_item_info_mem' : {'i1' : [], 'i2': [], 'i3' : []}, 'esrngiergroei' : {'i1' : [], 'i2': [], 'i3' : []}}]

shopping_cart_mem_module_OrderedDict = {{'i1' : 0 + offset, 'i2': 2 + offset, 'i3' : 3 + offset}}

shopping_cart_mem_module = {'shopping_cart_item_info_mem' : {'i1' : [], 'i2': [], 'i3' : []}, shopping_cart_mem_module_OrderedDict, offset}



# function will check item data ad use the new memory amagement system accordingly
def test():
    if True:
        if True:
            if True:
                question = "Enter an item you want to check the stock of"
                input_item_return = input_item(question, True)

                item_id = input_item_return[0]
                alt_option_pressed_TorF = input_item_return[-1]
                alt_option_pressed_func_number = input_item_return[0]

                if alt_option_pressed_TorF:
                    return alt_option_pressed_func_number

                item_exists_in_memTorF = mem_searcher(item_id, ('s', 'es'))

                if item_exists_in_memTorF:
                    item_id = 

                elif load hardrive things

                alt_option_pressed_TorF = prints_stock_in_inventory_return[-1]
                alt_option_pressed_func_number = prints_stock_in_inventory_return[0]

                if alt_option_pressed_TorF:
                    return alt_option_pressed_func_number
                else:
                    return 1


# ok i thin what i no want ot do is create a hpthetical sitatuion whee we are gonna use this system and then see what happens ok so i say lets use the
# so i say what we do is definte like this is the amount of items we are adding then like ok so i say lets do something like with the wath we oculd do is like do the chec on the otusdie then like yeah. that makes sense.
# i feel like that like yeah ok so for the mem seracheri guess we cold go like if item is not in there then
    
# ok so bascially i think like what i am gona do is like import like an input sitauon and then see how this program can handle it

































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
    return item_data

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

def cleans

item_data_mem = {key: value for key, value in current_items_data_in_mem.items() if key in set_new_item_data or key == 'cart_in_memory'}



# ok the ai
# i just thoughtaobut it how about we make afuctionthat ltierally just checks if an item exist sin emory then makes item data= to that data then baiscally eyh so basically now waht i want is a way to literally just add
# one item to memory i can use the big memory amagneemnt software but hoenstlyi feel like that i could make a seperate smaller function that is gonna takeup less memory bascaly so if elel ike yeah. so eiter ica n make a function
# that is smalerand that literally just adds the item to

# so this is bascialyl for the extra items data info shit i feel like that like yeah i guess we coudl then also usethe 




# if i do this i am baiscally gonna be reactirng the top function but with extra steps. yeah so then might as well just use tge ther fucntion yeah but tthe thing is like the problem is that if the item doesnt exit in memory
# at an input point then what we could do is botain the item data via hardrie search so basically that will be like big memory then the other will be like short term memory yeah that makes sense. we could do that oh my god this
# shit is gonna work. ok so baiscally we could go liek if item id = None then do this but we could just do this on the otside

# i feel like what could be a super fucking sick idea is that i use the terminal to create my UI i feel like that i saw an applcaiotn at work that does that the only problem i guess ill have is that i cant use the
# coputer mouse to help me do thigns whichi  guess is quite a big disadvantage but then i get to create my own unique original code and dont have to create my own graphical UI yeah  feel ikethat thaose pros are pretty
# cool i like to keep thigns orignal althoghu it has been done before bu also i odnt like the idea of using someone elses code although all code is made of other peoples code unless you working with raw assembly.
# i fee llike though that like basically i mean like ok what application do i wat. lets try do the full on terminal vibe then try something else from there. ok well lets get going ok elts design the menu first
# hmm i want to make this solution scalable and not have problabl  i feel liekthoguhthat like hmmmmm i feel likethat likehmmmm i guess like i couldlike somehowkeep the left side aslikeok
# this is the options and then go likeok theright side is the??? idk therightsideis the hmmmtherightside is the information. i guesstahtmkindamakessense

#waiti gotareallygooideai oudlcreateasepeartewinfdowwhere basicallylikewhathappensisthhatthereare like 3 different presetns for absiacll uhm screen sizes or perahps nbah i gotan even greater idea lets makeit that youcan makeyou
# screen sizeinfiniteamoutnfosiezsyou justgottachange an itnegervaribletaht definesth defines a block andthen the question will be likedoesthis block align with your thingthen ifitsays yesthen that isthe sizeofeach linetaht will beused
# and then thewhole program thereafterwill adjust accordingly.
# thatis a veryy good idea honeestl/ i feel like tahgt abscially yeah that-ideacouldwortk outi feel ike ayeh thatmaekssense. hmmmmm ok so thatscreen has gottapopup first andthen basicallybe likeok do thisthen onlyifthe 
# defaultwidth isntselect.. so the wholethingwill represent like basicalllythe entireareaused forthe application so tehn what is gonna happen is thatyeah.. howdo i makepython.

# ok well atel;astthatisnicei can clear a whole cmd on windwosok butnowthethingis how could i now... hmmm howcouldi removealinefrom aprompt so basicallyremov