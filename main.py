from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import threading
import gui
from time import sleep
import subprocess
import shlex

def copy():
    sleep(.1) # a little delay helps prevent selecting previously selecting text
    sselected_text = subprocess.check_output((shlex.split('xclip -i /dev/null'))) # empty it
    selected_text = subprocess.check_output((shlex.split('xclip -out -selection')))
    print('copied : ', selected_text)
    return(selected_text)

class Keylogger:
    def __init__(self,main_gui):
        self.main_gui = main_gui
        self.keyboard_listener = KeyboardListener(on_press=self.on_press)
        self.mouse_listener = MouseListener(on_move=self.on_move, on_click=self.on_click) 

        self.keyboard_listener.start()
        self.mouse_listener.start()

        self.keyboard_listener.join()
        self.mouse_listener.join()

    def on_press(self,key):
        pass
        #print(key)
        #self.keyboard_listener.stop()
        #self.mouse_listener.stop()

    def on_move(self, x, y):
        pass
        #print('Pointer moved to {0}'.format((x, y)))

    def on_click(self, x, y, button, pressed):
        #print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
        
        if not pressed:
            text = copy().decode('utf-8')
            self.main_gui.update(text) # set new_clip as hext

def main():
    main_gui = gui.Main()
    keylogger = threading.Thread(target=Keylogger, args=(main_gui,), daemon=True)
    keylogger.start() # start logger
    main_gui.start()

if __name__ == '__main__':
    main()
