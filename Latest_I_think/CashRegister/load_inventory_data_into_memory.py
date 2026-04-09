import mmap
import re

def load_inventory_data(l_item_list):
    global required_inventory_data
    for item in l_item_list:
        if item != None:

            for item_ in l_item_list:
                if item_ == item:
                    l_item_list[l_item_list.index(item_)] = None

            item_relative_address_pathyway = 'Inventory/' + item + '.txt'
            file = open(item_relative_address_pathyway, 'r')
            mmaped_item_info = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
            byte_item_info = mmaped_item_info.read()

            print(byte_item_info)

            pattern = b'\|n(.*?)\|p(\d+)\|s(\d+)\|'

            match = re.search(pattern, byte_item_info) # issue is here right here

            print(match)
            if match:
            # Extracted information from groups
                product_name_data = match.group(1).decode('utf-8')  # Assuming the product name is in UTF-8 encoding
                price_data = float(match.group(2).replace(b',', b'').decode('utf-8'))  # Remove commas and convert to float
                stock_data = match.group(3).decode('utf-8')  # Assuming the stock is in UTF-8 encoding

                item_data = (product_name_data, price_data, stock_data)

                required_inventory_data[item] = item_data
                print(required_inventory_data)
                input('')
    file.close()
    mmaped_item_info.close()

required_inventory_data = {}
g_item_list = ['i1','i1', 'i2', 'i3']
load_inventory_data(g_item_list)
print(required_inventory_data)

# ok what i now want to do is basically ask a question like do you want to load items
# into memory bascally like if you say yes then it creates this dictionary effectively
# lodng items into memro then if you say no does it now contiue with the operation or
# does it go back to the start i guess what i would want is for the program to 
# just take you back to start if you loaded the wrong items but hten like
# if you cant go further without answering yes then you might as well make it automati
# yeah might as well make it autatic ok lets make it automatic for now and then like
# basically yeah. i feel like that yeah that makes sense. i feel like
# less anxious now which isgreat. ok now my mind i getting used to him being here or 
# i am just suppressing hte eotion more i have no idea.
# anyways ok so back to work. yeah lets make itautmatic then now we
# need to basically make the rest of our fucnions comaptibl with this i mean
# we could still use theitem info colleciton feature right??? i guess actually
# yeah we could use that i would just like to rather use reuglar expressions
# next compared to our current way of takig out the data from the file like i













# bro its so much fucking harder to engage with higher order thinking in an envirment where i feel unsafe. yeah basically like i feel like super unsafe so like now i am super scared that my shit is gonna get jackd so m
# so my mind is hyper focusedon that because those thoughts also produce fear in me and like yeah
# ok now what we can do is we gotta now get rid of the repeats because atm we just basically going like ok if there is a repeat then 
# should i perahps just go and check like ok is this guy still there yah just pretend lie you grabbinga book ok he is still there on his phone he probably isnt aregular though like i havent ever sen him there before
# ok someting we can do is take hte produtname price and stock and then shit we need the identifier as well to be the name of the tuple fuckckckc. ok whatever its fine. then what we can do is basically add all
# if this information into one big tuples then after that then make another for loop that basically takes the first 4 elements and created a named tuple. i could also just create a set but i really do feel like that
# that a named tuple would be the absolutely best like way to store and call upon this inforation i feel like that yeah that makes sense. i feel like that, that makes sense. yeah fuck man. ok but how the fuck
# do we do that. like xD i have no fucking idea lol... AHAHAHAH shit. sisssshshgshhsgsiudsiuddshudshisdihsdhdsiuhsdiu fuck bro what do i do... ok chat gpt has gotta help me xd lol. i say we literally just store
# all this infomraiton into a tuple then run some kind of for loop that turns tuples into named tupples. ohhhh i could just take all this information AHAHAHA. wait I TAKE ALL THIS INFORMATION THEN ADD THEM TO A TUPPLE
# OH Y GO DI GURE DIT OUT THEN TAKE THE ITEM WHICH WILL BE THE STRING THEN MAKE THAT THE NAME OF THE TUPLE OH MY GODDD that idea is fucking perfect ltierally then after that process its gonna delete all the repeat
# items oh my lord that makes perfect sense. oh my godddd i feel like yeah. oh my godddd oh my GODDDD that makes sense. ok then ltieally, ltierlaly thats perfect code. take all of these new items then add them
# all to one big tuple with a specific order then take the item then make that the name of hte tuple i could literally do that now one idea is acutally to perahps have hte laod inventory data iwthin a for loop
# where the elemts in the item list are taken out and indiivudally inputted into the function but hten after that then how do we create a hypothetically infinite amount of variables??? still like ok now its reuntin
# the information we need from a function ok thats cool. so we just keep puttng shit in but then we encounter the exact same problem now it returns named tuples with all the data we need but now how do we store
# infinite uhhmmmmm how do we store hypethically infinte vairle i bascially need a for loop that creates varialbe ok chat gpt time
# we could even add another function that adds a whole bunch of efficieny oh my god YESYSYSYSYSYSWE ARE DOING THIS 100% OK SO BASICALLY WAHT I WANT TO DO IS MAKE A SCRIPT THAT BEFORE ADDING ITEMS TO THE INVENTORY
# MEMORY WHAT IT LITEARLLY DOES is like check if th

# so i guess what could be a strat is next time just be aware of who enters the room when you chilling at the library. yeah. also worst comes to wrost we can always go to a coffee shop and pay R10 for like a coffee
# or a cookie just to rent their for the day and work on our projects ok yeah so if worst ocmes to wrost we have a backup plan idk what to do now i guess just be aware of our envirment

# ok rowan so we were probably over reacting he is still ther at the same spot for lkeltierally 2hrs about just sittting their on his phone it doesntook like he has the intetion to try and steal shit so yeah i feel
# like that he is actually fine just dont ever offer him any of your stuff so it doesnt get snuffed

# i feel like now its so much harder to work because ow i am triyng to make suremy stuff doesnt get stolen but then also trying to work on my project which i maena i can do because i am a God and i am Rowan but 
# my godly mind is only so powerful. sigh i guess it is what it is