import tkinter as tk
import pyautogui as pya

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-topmost", 1)
        self.root.overrideredirect(True)

        self.root.label_src=tk.Label(self.root,text="src")
        self.root.label_origin=tk.Label(self.root,text="origin")
        self.root.label_text=tk.Label(self.root,text="text")

        self.root.label_src.pack(fill=tk.BOTH, expand=True)
        self.root.label_origin.pack(fill=tk.BOTH, expand=True)
        self.root.label_text.pack(fill=tk.BOTH, expand=True)
        # movements
        self.root.bind("<ButtonPress-1>", self.start_move)
        self.root.bind("<ButtonRelease-1>", self.stop_move)
        self.root.bind("<B1-Motion>", self.do_move)
        self.root.bind('<Double-Button-1>', self.hide)
        #self.root.after(2000,self.update)

    def start(self):
        self.root.mainloop()

    def hide(self, event):
        self.root.withdraw()

    def update(self,text):
        self.root.label_src.configure(text=f"{text.src}")
        self.root.label_origin.configure(text=f"{text.origin}")
        self.root.label_text.configure(text=f"{text.text}")
        x, y = pya.position()
        self.root.geometry(f"+{x}+{y}")
        self.root.deiconify()
        
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, _event):
        self.x = None
        self.y = None

    def do_move(self, event):
        delta_x = event.x - self.x
        delta_y = event.y - self.y
        x = self.root.winfo_x() + delta_x
        y = self.root.winfo_y() + delta_y
        self.root.geometry(f"+{x}+{y}")

if __name__ == '__main__':
    Main()
