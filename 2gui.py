import tkinter as tk

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-topmost", 1)
        self.root.overrideredirect(True)
        self.root.label=tk.Label(self.root,text="before")
        self.root.label.pack(fill=tk.BOTH, expand=True) # I changed this   
        # movements
        self.root.bind("<ButtonPress-1>", self.start_move)
        self.root.bind("<ButtonRelease-1>", self.stop_move)
        self.root.bind("<B1-Motion>", self.do_move)
        self.root.after(2000,self.update)
        self.root.mainloop()

    def update(self):
        self.root.label.configure(text="text\na\n\n\n This is very long")
        
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
