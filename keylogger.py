from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

def on_press(key):
    print(key)
    keyboard_listener.stop()
    mouse_listener.stop()

def on_move(x, y):
    pass
    #print('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    if not pressed:
        pass
        # Stop listener
        # return False

# Collect events until released

keyboard_listener = KeyboardListener(on_press=on_press)
mouse_listener = MouseListener(on_move=on_move, on_click=on_click) 

keyboard_listener.start()
mouse_listener.start()

keyboard_listener.join()
mouse_listener.join()

