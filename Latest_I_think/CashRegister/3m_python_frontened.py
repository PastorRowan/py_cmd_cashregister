import keyboard1

import turtle

def pass_func():
    pass

def str_eg_box_func(length, height):

    # creates 1 row
    constructor_mid_row = ['|']
    for _ in range(length):
        constructor_mid_row.append(' ')
    constructor_mid_row.append('|')
    constructor_mid_row.append('\n')
    mid_row = ''.join(constructor_mid_row)

    # creates middle section
    mid_rows = []
    for _ in range(height):
        mid_rows.append(mid_row)
        mid_rows.append('\n')

    # creates top row
    top_row = []
    for _ in range(length + 2):
        top_row.append('_')
    top_row.append('\n')

    # creates bot row
    bot_row = ['|']
    for _ in range(length):
        bot_row.append('_')
    bot_row.append('|')

    # creates example display box string
    ls_eg_box = top_row + mid_rows + bot_row
    str_eg_box = ''.join(ls_eg_box)

    return str_eg_box


arrow_keys = {'left': [0], 'right': [0], 'up': [0], 'down': [0]}

def handleLeftKey(e):
    global arrow_keys
    key = 'left'
    if keyboard1.is_pressed(key):
        amount_key_pressed = arrow_keys[key]
        amount_key_pressed[0] += 1

def handleRightKey(e):
    global arrow_keys
    if keyboard1.is_pressed('right'):
        amount_key_pressed = arrow_keys['right']
        amount_key_pressed[0] += 1

def handleUpKey(e):
    global arrow_keys
    key = 'up'
    if keyboard1.is_pressed(key):
        amount_key_pressed = arrow_keys[key]
        amount_key_pressed[0] += 1

def handleDownKey(e):
    global arrow_keys
    key = 'down'
    if keyboard1.is_pressed(key):
        amount_key_pressed = arrow_keys[key]
        amount_key_pressed[0] += 1

# Initial setup of key handlers
keyboard1.on_press_key("right", handleRightKey)
keyboard1.on_press_key("left", handleLeftKey)
keyboard1.on_press_key("up", handleUpKey)
keyboard1.on_press_key("down", handleDownKey)



def complete_program_loop(func_num):

    while True:

        # 1ST FUNCTION
        # sets display of function
        if func_num == 1:
            default_box_length = 50
            default_box_height = 25

            new_length = [default_box_length]
            new_height = [default_box_height]

            while True:
                print(f'Welcome!!!\n press the arrow keys to adjust the screen size, the default length is {new_length[0]} characters and the default height is {new_height[0]} characters\ncurrent box looks like this \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n\n')
                str_eg_box = str_eg_box_func(new_length[0], new_height[0])
                print(str_eg_box, end='\r')
                turtle.onkeypress(pass_func)

                if True:
                    if arrow_keys['left'][0] != 0:
                        new_length[0] -= 1
                        arrow_keys['left'][0] = 0
                        print('left arrow key was pressed')

                    elif arrow_keys['right'][0] != 0:
                        new_length[0] += 1
                        arrow_keys['right'][0] = 0

                    elif arrow_keys['up'][0] != 0:
                        new_height[0] +=1
                        arrow_keys['up'][0] = 0

                    elif arrow_keys['down'][0] != 0:
                        new_height[0] -=1
                        arrow_keys['down'][0] = 0

# one idea that oculd be intetesrting is to use the cls function off the main thread like have asynchrnous processign which could work very well but yeah hmmm idk i am gonna try to amke that create display part of
# the application faster i just gpotta find the bottleneck for speed first that coud perahps be just the system cls function which means i probs gotta use another method but lets test it out.
                
# one method could be asyncronous processing another method could be taht we only clear the console after x amount of keys are pressed? i guess could be a good idea

# wait wait if i keep dojg carriage reutrns and just overwrit ethe preivous shit then yeah thats ggs yes i knew we could do it ez common rowan W moment although i mean we are a bit lucky tha osmeone did make code that
# can ahcieve our goal but still i eman its all good





# idk why but i am judging my code so muchy more lately and like before its so werid but like i have never expericned this i generally have such an emotionally neutral persepctive of my code but now i am judging
# everything i do and like its weird??? i feel like idk whats going on. i dont want to go to church honetsly number 1 but also number 2 i guess i am not hhappy i spent so much time talkig to people. but rowan that shits
# normal like it fine to talk to people  i just wish i just stopped a bit earliert and got back to work but the thing is we are basically gonna start our calithstenics journey and thats sick. i guess good things can come out of talking to 
# people just dont have like a trauma resposne where you blame that your codew isnt wokrin on your unhappienss when its clearly not thats not the thing your angr about its the fact that you spent more time talinga'\
# to people than you could handle. tjats its
















        elif func_num == 2:
            return 2
        


















default_start_menu = 1

menu_num = default_start_menu

while True:
    menu_num = complete_program_loop(menu_num)
    if menu_num == 'p':
        break
    elif menu_num == '/':
        menu_num -= 1

        # so once menu_num is returned then what i need to do is basically take that menu num and load the functions that i need into the onpress thing i guess and then get the event handler to do that i mean i could
        # put a keyboard wait function somewhere in roder to prevent stack overflow ebcause i feel like if i put hmm somehow i need o do it beofre but our program kida desnt wallow that i mean i guess
        # we could make it that the thing goes through 2 loop hmmm i guess waht i copudl od is do a for lop

        # idk if this is the best way of doing this i feel lie that what could be a cooler system is perahps to have baically this is the detect keys thing and then say ok we are gonna load these into the
        # detect keys function althoguh that is exacltt what we are doing we woud have to load them again anyways it seems is ther antoehr way of gong about it the only way we could go another wqay about it is
        # instead of loading keyboard functions into the thing make the keyboard functions always loaded and they change certain variables that only detect how much they are pressed
        # thgats good i like hat idea so we are gonna make. yeah otherwise we are gonna import the same module like 20times which is very very very silly because those programs do take long to import