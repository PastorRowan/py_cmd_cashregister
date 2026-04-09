import keyboard1

while True:

    event = keyboard1.read_event()

    if (event.event_type == keyboard1.KEY_DOWN):
        print(f'{event.name} was pressed down')