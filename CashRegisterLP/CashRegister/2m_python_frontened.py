#erhgiuerhgui8rehgu89
import keyboard1

def handleRightKey(_):
    pass


def handleLeftKey(_):
    pass


def handleUpKey(_):
    pass

def handleDownKey(_):
    pass

default_box_length = 50
default_box_height = 25

new_length = [default_box_length]
new_height = [default_box_height]




# Set up event handlers outside the loop
keyboard1.on_press_key("right", lambda e: handleRightKey(e, new_length))
keyboard1.on_press_key("left", lambda e: handleLeftKey(e, new_length))
keyboard1.on_press_key("up", lambda e: handleUpKey(e, new_height))
keyboard1.on_press_key("down", lambda e: handleDownKey(e, new_height))
# Similar lines for other keys...


def complete_program_loop():

    while True:

# 1ST FUNCTION
# sets display of function
        if func_num == 1:
            def handleRightKey(e, length_container):
                length_container[0] += 1


            def handleLeftKey(e, length_container):
                length_container[0] -= 1


            def handleUpKey(e, height_container):
                height_container[0] += 1


            def handleDownKey(e, height_container):
                 height_container[0] -= 1


            default_box_length = 50
            default_box_height = 25

            new_length = [default_box_length]
            new_height = [default_box_height]










            return 1

# 2ND FUNCTION
        elif func_num == 2:
            return 1

# 3RD FUNCTION 
        elif func_num == 3:
            return 1


complete_program_loop()



