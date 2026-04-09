



def dic_column_title_coords_and_percentages(box_length, dic_title_plus_frac_apart_out_of_1_whole, box_start_x, title_start_x, title_start_y):

    available_len = box_length + (title_start_x - box_start_x)

    
    dic_column_title_coords_and_percentages = {}
    ls_column_titles = []

    for title, percentage in dic_title_plus_frac_apart_out_of_1_whole.items():

        float_x_offset = percentage * available_len

        int_x_offset = int(float_x_offset)

        curr_title_x = title_start_x + int_x_offset
        
        curr_title_pos = pos(curr_title_x, title_start_y)
        ls_column_titles.append(curr_title_pos)
        ls_column_titles.append(title)

        str_column_title = ''.join(ls_column_titles)

        dic_column_title_coords_and_percentages[title] = {'str' : str_column_title, 'coords' : [curr_title_x, title_start_y], 'percentage' : percentage}
    

    return dic_column_title_coords_and_percentages










block_1_start_and_end_ratios = {'percentage_start_x' : 0, 'percentage_start_y' : 0, 'percentage_end_x' : 0.5, 'percentage_end_y' : 0.5}

block_2_start_and_end_ratios = {'percentage_start_x' : 0.5, 'percentage_start_y' : 0.5, 'percentage_end_x' : 1, 'percentage_end_y' : 1}





def block_coords(menu_length, menu_height, block_start_and_end_ratios, menu_start_x, menu_start_y, menu_end_x, menu_end_y):

    box_start_and_end_coords = {}

    # start x
    percentage_start_x = block_start_and_end_ratios['percentage_start_x']
    float_x_offset = percentage_start_x * menu_length
    int_x_offset = int(float_x_offset)
    curr_box_start_x = menu_start_x + int_x_offset
    box_start_and_end_coords['start_x'] = curr_box_start_x

    # start y
    percentage_start_y = block_start_and_end_ratios['percentage_start_y']
    float_start_y_offset = percentage_start_y * menu_height
    int_start_y_offset = int(float_start_y_offset)
    curr_box_start_y = menu_start_y + int_start_y_offset
    box_start_and_end_coords['start_y'] = curr_box_start_y

    # end x
    percentage_end_x = block_start_and_end_ratios['percentage_end_x']
    float_end_x_offset = percentage_end_x * menu_length
    int_end_x_offset = int(float_end_x_offset)
    curr_box_end_x = menu_start_x + int_end_x_offset
    box_start_and_end_coords['end_x'] = curr_box_end_x

    # end y
    percentage_end_y = block_start_and_end_ratios['percentage_end_x']
    float_end_y_offset = percentage_end_y * menu_height
    int_end_y_offset = int(float_end_y_offset)
    curr_box_end_y = menu_start_y + int_end_y_offset
    box_start_and_end_coords['end_y'] = curr_box_end_y

    return box_start_and_end_coords





def boxes_length_and_height(box_start_and_end_coords):
        
    # l
    start_x = box_start_and_end_coords['start_x']
    end_x = box_start_and_end_coords['end_x']
    box_length = end_x - start_x

    # w
    start_y = box_start_and_end_coords['start_y']
    end_y = box_start_and_end_coords['end_y']
    box_height = end_y - start_y

    return box_length, box_height



menu_length = 50
menu_height = 25
menu_start_x = 2
menu_start_y = 2
menu_end_x = 52
menu_end_y = 27

box_1_start_and_end_coords = block_coords(menu_length, menu_height, block_2_start_and_end_ratios, menu_start_x, menu_start_y, menu_end_x, menu_end_y)

print(box_1_start_and_end_coords)

box_1_l_andh_h = boxes_length_and_height(box_1_start_and_end_coords)

print(box_1_l_andh_h)

# see the problem i ahve ow ehre is that basically if I output all of these varuibesl then basically yeah I will be able to have some kind of what do youi call it i wil be able to control the amoutn of blocks i ahve
# but i will ltiearlyl have to like do a whole bunhc of shit to be able to have multiple blocs lie i will ahve to say block 1 is this block 2 is this an lock t3 s this which is coo land all but the thing is that means
# every time  iwant to cerate a blok i cant just add a whole bunch of shit to a dictionary instead i gotta basicaly create a whole new set of varibels and i woud oenstly prefer to work with adding information
# to data stcutuers to create shit rather htan that althogh this would mean that i would need to create almost lieka diovcnaty manager or does it. i eman like idk. i feel like that i gotta actualyl create my system then baicsally
# be like ok is this the best sokuton or this one the onyl way we are gonna figure out which one is the best for htis thing is to actualyl do it. i feel like yeah. so bascialky eyaqh i guess one thing we can do is
# reat one bgi dicojtqary which hoenstly seems to be the siplest sokution in my brain but also i guess something else that i can do is manually creeathese vairbels but the thing is why cant i just create the varible
# wtihin hte dictioanry if eel iek taht makes mroe sense ot me in a sense. like if i create the block within the data stcuturte then tahts equivalent to creating it in there the only thng ican imagine is havin
# basically be like ok this function will create the coords for all the functiosn this funciton will do this for all the fucntiosn then this will do this for all the fucntiosn and i mean like thats cool and all
# but that requires next level roghanstionbut tbh i do prefer having thigts together i mean like. ok fuck it lets find some kind of middle gorund and put al this shit together ok so i feel euie the bets spltion
# for me would be to make the dicitoanries create dicitoanries bascially and then have some kind of dicitoanry nmagager that says ok this dicionary that is like perentage coords is gonna be here in this global
# dicitoaryu and this one will be here in this glboal thing like, basically having a glboal block data dicitoanryu is probably gonna be the simplest and then within the fucntiuon then seperating like
# ok this is this block and ok this is this block and so on or whatever. i feel like yeah . hmmm i feel lke that yeah ok fuck it rowan lets do the solution that we like that is creating the blocks and then
# the block manager and hten basically having the whole process automated i guess could be fuckig cool like yeah i feell ike that having the whole process is lke you defint he function. ok wait lets think ehre
# imagine how simple this would be we have hte block system then bascially all we ahve to do to add another block is. ok here is the issue we3 are gonna end up like this is block 1s info and all the varibles for
# that and here are block 2s vairbel and al lteh ifno for that so why not just go with that system form the start??? rather if you are gonna go the dictionaruy route then stick with that to the end
# but if you are gonna go the bvartible roputre then stick wit htaht to the end like that makes sense to me then if you want ot add any you just copy paste code and functions and then yeah i gues si eman we could 
# do some shti like ok lets make this tuple like this

# see and ehre wee arabck at hte issue now we want an arbritray amount of blocks so then we have to use a dta stucutue and thre return thign must reutnr osmethng that is gonna resemble a data strucutuer
# so basically we HAVE TO USE DATA STRUCTURES AT THE END ANYWAYS so why not just use them at the begging and then deassemble them at the end wehne we wanna sue the sdata duhuheriuhgr euiinfo 