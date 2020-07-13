from tkinter import *

class GUI():

    def __init__(self):
        self.root = Tk()
        self.root.title("Tex Analysis")
        self.root.geometry("500x500")
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.mainloop()

GUI()