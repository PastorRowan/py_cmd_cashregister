

print('Welcome!!!\nwhat screen size would you like, default is')

# we need to make a minimum size function probably yeah

# i feel like that i have no idea what i want because idk what each solutio nis gonna look like
# i mean technically the arrow keys are gonna be the only special function keys
# but the thing is like fuck man idk i feel like that each solution could work. but what
# alteranties do i have to global variables for hte arrow keys i mean i can use the
# read key then chekc if read key pipsresed wartevr event i can always do that and then
# say like ok if this is presed then do this or if this is pressed then do this
# i mean like yeah i guess. fuck idk. idk if i shoudl jsut go all out read key mode
# or use global variables with the onpres thing because i honestly prefer using that
# i mean like idk i feel like that either one coud work the glboal variables or the read keys thig and then
# have a special options function. i mean that could work special option tests and then
# hmm i mean i thinkj using a mix is the best idea have the read key for other options and
# yeah so read key is for the unique options and then arrow keys is for everything and have
# some kind of function that handles the usage of that

import keyboard1

# Initialize a dictionary with a key-value pair where the value is a list
arrow_keys = {'left': [0], 'right': [0], 'up': [0], 'down': [0]}

# Access the value using the key
current_value = arrow_keys['left_k_pressed']
print("Current value:", current_value[0])

# Increment the value in the list
current_value[0] += 1

# Access and print the updated value from the list
print("Updated value:", arrow_keys['left_k_pressed'][0])


def handleLeftKey(e): 
    global arrow_keys
    key = 'left'
    if keyboard1.is_pressed(key):
        amount_key_pressed = arrow_keys[key]
        amount_key_pressed[0] += 1

def handleRightKey(e):
    global arrow_keys
    key = 'right'
    if keyboard1.is_pressed(key):
        amount_key_pressed = arrow_keys[key]
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
    if keyboard1.is_pressed("down"):
        print("down arrow was pressed")
        amount_key_pressed = arrow_keys[key]
        amount_key_pressed[0] += 1




























def print_():
    print('right key was pressed')

#input default values
'''
def arrow_keys_func(left_func, right_func, up_func, down_func, default_box_length, default_box_height, minimum_length, minimum_height):

    length = default_box_length
    height = default_box_height
    while True:
        event = keyboard1.read_event()
        if event.event_type == keyboard1.KEY_DOWN and event.name == 'left':
            length = left_func(length, minimum_length)
        elif event.event_type == keyboard1.KEY_DOWN and event.name == 'right':
            length = right_func(length, minimum_length)
        elif event.event_type == keyboard1.KEY_DOWN and event.name == 'up':
            height = up_func(height)
        elif event.event_type == keyboard1.KEY_DOWN and event.name == 'down':
            height = down_func(height)
        elif event.event_type == keyboard1.KEY_DOWN and event.name == 'enter':
            return length, height
'''


def arrow_keys_func(left_func, right_func, up_func, down_func, default_box_length, default_box_height, minimum_length, minimum_height):

    length = default_box_length
    height = default_box_height
    while True:
        key = keyboard1.read_key()
        if keyboard1.is_pressed(key):
            length = left_func(length, minimum_length)
        elif keyboard1.is_pressed(key):
            length = right_func(length, minimum_length)
        elif keyboard1.is_pressed(key):
            height = up_func(height)
        elif keyboard1.is_pressed(key):
            height = down_func(height)
        elif keyboard1.is_pressed(key):
            return length, height



# i guess one thing i could do is like basically make it that uhm the global left and right pressed vaibles like manipu;ate tem on hte outside
# i feel like that could be a good idea? then store the output of the left and right pressed varianbles. i think taht oculd be a good idea but honestly i have no idea. i feel like that i dont likethe idea of using
# global variables but i mean yeah we could then have different fucntiosn taht proces the global key press variabnles that amkes sense. yeah then litreally make it that the arrow pressed variables are the onl;y thing
# that changes that makes sense. i feel like ayeah. hmmmmm ok so lobal left and right pressd variables that have limits of how high or low they can be i guess could be a good idea just to prevent stack overflow or
# gettig to max intreger wvalue i guess. i feel like yeah that makes sense. ohoenstly hte oly reason i want to do that is because it would make it that i get to use the same hahandle lefyt eky and handle right key fucntions
# they will all do the same thing and ten all i do is manipu;ate hte arrow key pressed variables. i guess the other thig i dot really like is like ok now i thin. ah theri is a solution to that problem 
# so if i want to use the variable within a loop then basically i could jsut use the keyboard wait variable or the read_event . ahhh so i could use the read event or read key funciton rather event because
# i want it. idk/. i mean i can sit here argueing iwath myself all day but honestly idk wat to

# ok finaly decision we gonna use the read_key event or the on press global varible thing both can work
# just ogtta use read key to stop the program like a while true loop i guess it could work
# i fel lik teht it would result in less code in the long run i guess? and i am gonna use on press
# for basically everythjing just gotta change what they do like i assume the arrow keyts are
# gonna be a key part of the program that absicalyl like thats gonna be the main way of navigating it
# except when in ceratin psecific scenarios but then i can just use the other stuff.










        '''
        global default_box_length
        global minimum_length
        print('Left arrow key was pressed')
        print(default_box_length)
        print(minimum_length)
        '''
        length -= 1
        if length < minimum_length:
            print(f'the minimum length is {minimum_length}')
        print(f'new width is {length}')

#arrow_keys_func(left_press, right_press, up_press, down_press, default_box_length, default_box_height, minimum_length, minimum_height)
#keyboard1.on_press_key("left", lambda e: handleLeftKey(e, default_box_length, minimum_length))












def handleLeftKey(length_container, height_container):
    # Your logic here
    print("Left key pressed")

    # Subtract 1 from the length
    length_container[0] -= 1

    # Print the modified length
    print("Modified length:", length_container[0])

# Similar functions for other keys...

# Example usage
default_box_length = 50
default_box_height = 25

new_length = [default_box_length]
new_height = [default_box_height]

while True:
    keyboard1.on_press_key("left", lambda e: handleLeftKey(new_length, new_height))
    # Similar lines for other keys...

    keyboard1.wait('esc')








def right_press(length, minimum_length):
    length += 1
    if length < minimum_length:
        print(f'the minimum length is {minimum_length}')
        return minimum_length
    print(f'new width is {length}')
    return length
def up_press(height):
    height += 1
    print(f'new height is {height}')
    return height
def down_press(height):
    height -= 1
    print(f'new height is {height}')
    return height

default_box_length = 50
default_box_height = 25

minimum_length = 20
minimum_height = 10

new_length = [default_box_length]
new_height = [default_box_height]

while True:

    keyboard1.on_press_key("left", handleLeftKey)
    keyboard1.on_press_key("right", handleRightKey)
    keyboard1.on_press_key("up", handleUpKey)
    keyboard1.on_press_key("down", handleDownKey)

    keyboard1.wait('esc')






input('you pressed esc')


def handleLeftKey(e):
    if keyboard1.is_pressed("left"):
        print("left arrow was pressed sergsres")



keyboard1.on_press_key("left", handleLeftKey)






box_length = input('iejfiej')
box_height = input('jgirgji')

def min_integer_input(int_min_integer):
    str_min_integer = str(int_min_integer)
    while True:
        str_input = input(f'Please input a postive integer that is equal to or greater than {str_min_integer}')

        # special options pressed test

        int_input = int(str_input)
        if (str_input.isdigit()) and (int_input >= int_min_integer):
            return int_input

def box_dimensions_program_loop(min_length, min_height):
    while True:
        box_length = min_integer_input(50)
        box_height = min_integer_input(25)

        if (box_length != None) and (box_height != None):
            return box_length, box_height


# default screen size
print('''
_______________________________________________________________________________________________________________________________________________________________
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
|_____________________________________________________________________________________________________________________________________________________________|''')

input('wefe')


tup_box_legnth_plus_height = box_dimensions_program_loop()
