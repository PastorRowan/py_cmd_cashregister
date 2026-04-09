print('Welcome!!!\nwhat screen size would you like, default is')

import keyboard1

# Initialize a dictionary with a key-value pair where the value is a list
arrow_keys = {'left': [0], 'right': [0], 'up': [0], 'down': [0]}

def handleLeftKey(e): 
    global arrow_keys
    key = 'left'
    if keyboard1.is_pressed(key):
        amount_key_pressed = arrow_keys[key]
        amount_key_pressed[0] += 1

        print(f"{key} arrow was pressed")
        print(f'amount_key_pressed is {amount_key_pressed}')

def handleRightKey(e):
    global arrow_keys
    key = 'right'
    if keyboard1.is_pressed(key):
        amount_key_pressed = arrow_keys[key]
        amount_key_pressed[0] += 1

        print(f"{key} arrow was pressed")
        print(f'amount_key_pressed is {amount_key_pressed}')

def handleUpKey(e):
    global arrow_keys
    key = 'up'
    if keyboard1.is_pressed(key):
        amount_key_pressed = arrow_keys[key]
        amount_key_pressed[0] += 1

        print(f"{key} arrow was pressed")
        print(f'amount_key_pressed is {amount_key_pressed}')

def handleDownKey(e):
    global arrow_keys
    key = 'down'
    if keyboard1.is_pressed("down"):
        amount_key_pressed = arrow_keys[key]
        amount_key_pressed[0] += 1

        print(f"{key} arrow was pressed")
        print(f'amount_key_pressed is {amount_key_pressed}')

keyboard1.on_press_key("left", handleLeftKey)
keyboard1.on_press_key("right", handleRightKey)
keyboard1.on_press_key("up", handleUpKey)
keyboard1.on_press_key("down", handleDownKey)

print('Welcome!!!\nwhat screen size would you like, default is')

default_box_length = 50
default_box_height = 25

minimum_length = 20
minimum_height = 10













keyboard1.wait('esc')

