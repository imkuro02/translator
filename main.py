from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import pyautogui
import pyperclip 
import threading
import gui

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
        print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
        
        if not pressed:
            old_clip = pyperclip.paste()   # copy old clip
            pyautogui.hotkey('ctrl', 'c')  # copy new content
            new_clip = pyperclip.paste()   # put new content in new_clip var
            pyperclip.copy(old_clip)       # set old clip back into clipboard
            self.main_gui.update(new_clip) # set new_clip as text

def main():
    main_gui = gui.Main()
    keylogger = threading.Thread(target=Keylogger, args=(main_gui,), daemon=True)
    keylogger.start() # start logger
    main_gui.start()

if __name__ == '__main__':
    main()
