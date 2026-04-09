import colorama1
import os
import keyboard1


# constructor functions
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def str_row_(length, char, offset):
    ls_row = []

    for _ in range(length + offset):
        ls_row.append(char)

    str_row = ''.join(ls_row)
    return str_row

def str_column_(height, char, offset):
    ls_column = []
    for _ in range(height + offset):
        ls_column.append(down(1))
        ls_column.append(back(1))
        ls_column.append(char)

    str_column = ''.join(ls_column)
    return str_column

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# empty box creators
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main_custimizable_empty_str_box(length, height, ls_top_right_bot_left_chars, start_pos):

    top_char = ls_top_right_bot_left_chars[0]
    right_char = ls_top_right_bot_left_chars[1]
    bot_char = ls_top_right_bot_left_chars[2]
    left_char = ls_top_right_bot_left_chars[3]

    # creates top row
    str_top_row = str_row_(length, top_char, 2)

    # creates bot row
    str_bot_row = str_row_(length, bot_char, 1)

    # creates left column
    str_left_column = str_column_(height, left_char, 2)

    # creates right column
    str_right_column = str_column_(height, right_char, 2)

    str_empt_box = start_pos + back(1) + str_top_row + start_pos + str_left_column + str_bot_row + up(height + 2) + str_right_column
    return str_empt_box

def main_same_top_and_bot_empty_str_box(length, height, ls_row_column_chars, start_pos):

    row_char = ls_row_column_chars[0]
    column_char = ls_row_column_chars[1]

    # creates top and bot row
    str_row = str_row_(length, row_char, 2)

    # creates left and right column
    str_column = str_column_(height, column_char, 2)

    str_empt_box = start_pos + back(1) + str_row + row_char + start_pos + str_column + str_row + up(height + 2) + str_column
    # + back(1)

    return str_empt_box

# full box creators
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def pos (x,y):
    return '\x1b[' + str(y) + ';' + str(x) + 'H'
up = colorama1.Cursor.UP
down = colorama1.Cursor.DOWN
forward = colorama1.Cursor.FORWARD
back = colorama1.Cursor.BACK














os.system('cls')
colorama1.just_fix_windows_console()



def dic_column_title_coords_and_percentages(box_length, dic_title_plus_frac_apart_out_of_1_whole, box_start_x, title_start_x, title_start_y):

    available_len = box_length + (title_start_x - box_start_x)

    #print(pos(50,50) + str(available_len))

    #print(pos(50,50)+ str(title_start_x))
# i guess one thin we need to make is almost like a title coords list or a dicitoary nah lets make it a dictionary with lists eyah taht makes szense so bascisally like take the x value that represents the title starts
# then bascially waht we can do is take the coords of the title start poses and then do shit with them to see ok where are we gonna place our hmmmm. we could then take the thing then - somethng an get the x coordinate
# for a column or something or watever and then next level i guess wo2qudl be taht what ew could od is take an x coordinate then craet a box within the title box within the menu box and then if we can do that then
# that would be cool yeah i guess yeah. i feel like that yeah then what we have is the x adn y coords for the box within the box and then i can perhapos use those coords to then create another one column title str
# then once i got that then yeah we chilling then after that then create another str_colun title thing that basically just has the price or whatever or create a seperate function to do that
#
# ok wait lets me jsut draw ths
    
    dic_column_title_coords_and_percentages = {}
    ls_column_titles = []

    for title, percentage in dic_title_plus_frac_apart_out_of_1_whole.items():

        float_x_offset = percentage * available_len

        int_x_offset = int(float_x_offset)

        #print(pos(51,51) + str(int_x_offset))

        curr_title_x = title_start_x + int_x_offset

        #print(pos(51,51)+ str(curr_title_x))
        
        curr_title_pos = pos(curr_title_x, title_start_y)
        ls_column_titles.append(curr_title_pos)
        ls_column_titles.append(title)

        str_column_title = ''.join(ls_column_titles)

        dic_column_title_coords_and_percentages[title] = {'str' : str_column_title, 'coords' : [curr_title_x, title_start_y], 'percentage' : percentage}
    

    return dic_column_title_coords_and_percentages

def str_culumn_titles(dic_column_title_coords_and_percentages_):

    ls_column_titles = []
    for title in dic_column_title_coords_and_percentages_:
        dic_title_info = dic_column_title_coords_and_percentages_[title]
        str_title = dic_title_info['str']
        ls_column_titles.append(str_title)

    str_column_titles = ''.join(ls_column_titles)
    return str_column_titles

def get_coords(dic_column_title_coords_and_percentages_):

    coords = {}
    for title in dic_column_title_coords_and_percentages_:
        dic_title_info = dic_column_title_coords_and_percentages_[title]
        coords[title] = dic_title_info['coords']

    return coords




# ok now i got the coords so now wat but also i just dont really lie this oprgansitaion system liek it feels very ewwy hoenstly is the onyl wor di have to describe it its just eww its very complcaited but i mean at the saqme
# time lets say we are dealing with fucking idk 50 titles in one line then i wuld say this is as simple as it gets like i canty imagine it getting much more simpler you search for the coords of a given part of
# the row by looking searching up its title  that makes sense to me eyah so this solution is not simple for like 2 titles within a row but for 50 yes this is probably as simple as it gets so yeah
# i guess that is fine then i mean yeah ok then its fine ill keep doing it this way 

# idk whether we put this ifnormation intp the funciton or outisde the function io feel like that yeah i just so the like basically we could print everythng before we enter the main loop[ or
# we print everything when we enter the main loop i feel like that a better idewa would be too print everthng isndie the main loop as like a ok we are no here type of function idk hmmmm yeah but hten i have
# to input all this dogshit into the function which is ultra lame and makes my code harder to read we are bacialyl going from a while true loop into antoehr so it makes sense. fuck it just shove them into the
# fucti weait nah we have to input these thigs becaue what f we have a clear funciton that clears the temrinal where is the loop supposed to know were the str for these thigns are it ahs to have some kind of
# access to it yeah so then yeah lets just nput them 

# ok so then basically what we can do is take the coords of the titles now and then modify them to do shit idk like say ok the x coordinate for this is gona be this and this and this and then
# make it that yeah basically we can print a columm now that is equal to the height of the menu container ez so thats cool but now we should definte like ok this is gonna be the box for this and use the empty box
# creator tool for that and then after that then record those coords as like the menu_box coords and then the i gues we can call it cart box coords and then create something with that like for example yeah i really
# like that idea beauce then basically we will have organised every single box into like rows and columns and shit and then basically

# yeah i like these ideas i love htat idea of trying to divide the ok tomoorw we are definitely gonna do that we are gonna divide the whole ass page into this block and this block with this height and this width
# and create functions that work on this block logic and hten if i keep doing that then yeah we could even store these coords into a dicitoanry like boxes then have hte title of the titeboes and then the box_info diionaryies with specific things like 
# the string or the perimeter coords and the internal box coords and then use the itnerna;l box coord and then the legnth and height and then yeah use that to do shit ebcause we arleady have some fucntiosnt that can
# do shit. i guess one problem i am gonna face is defining the boxes. hmmm i think yeah it should work. so rather maybe instead. ok lets first defint ehdimensions of this box and see what i can do with that info
# ok i gues this is gona b e a differnt thing tha ti am gonna have to write down like boxes

def Main_menu_main_purchase(dic_column_title_coords_and_percentages_, box_peri_x, box_peri_y):

    str_column_titles_ = str_culumn_titles(dic_column_title_coords_and_percentages_) # row strings and there starting coords? as simple as it gets i guess? i mean idk how it can get much more simpler

    print(str_column_titles_)
    coords = get_coords(dic_column_title_coords_and_percentages_)

    str_empt_box = main_same_top_and_bot_empty_str_box(box_length, box_height, ls_row_column_chars, box_start_pos)

    print(str_empt_box, str_column_titles_)



    while True:
        break




box_length = 110
box_height = 25
ls_row_column_chars = ['_', '|']
box_start_x = 1
box_start_y = 1
box_start_pos = pos(1,1)

dic_title_plus_frac_apart_out_of_1_whole =  {'Items': 0, 'Total':0.8}
title_start_x = 3
title_start_y = 3





dic_column_title_coords_and_percentages_ = dic_column_title_coords_and_percentages(box_length, dic_title_plus_frac_apart_out_of_1_whole, box_start_x, title_start_x, title_start_y)

Main_menu_main_purchase(dic_column_title_coords_and_percentages_, box_start_x, box_start_y)