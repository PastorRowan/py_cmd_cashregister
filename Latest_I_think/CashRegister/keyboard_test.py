import keyboard1

def handleLeftKey(e):
    if keyboard1.is_pressed("4"):
        print("left arrow was pressed w/ key 4")
        # work your magic

keyboard1.on_press_key("left", handleLeftKey)
keyboard1.wait()
# self-explanitory: when the left key is pressed down then do something

#keyboard1.on_release_key("left", handleLeftKey02)
# also self-explanitory: when the left key is released then do something

# don't use both ...on_release & ...on_press or it will be
# triggered twice per key-use (1 up, 1 down)