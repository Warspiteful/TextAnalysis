from tkinter import *
from tkinter import messagebox
class GUI():
    root = Tk()
    v = IntVar()
    s = StringVar()

    def __init__(self):
        pass

    def compile(self):
        self.root.mainloop()

    def limit_size(self, *args):
        value = self.limit.get()
        if len(value) > 20: self.limit.set(value[:20])

    def on_closing(self):
        if messagebox.askyesnocancel("Quit", "Do you want to quit?"):
            self.root.destroy()
    
    def reset(self):
        if hasattr(self,'frame'):
            self.frame.destroy()
        self.frame = Frame(self.root)
        self.frame.pack()
