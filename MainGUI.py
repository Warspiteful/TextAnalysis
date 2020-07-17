from tkinter import *
from tkinter import messagebox
import json
from textAnalysis import textAnalyst, json
from timeAnalysis import timeAnalyst

class GUI():
    root = Tk()
    v = IntVar()
    s = StringVar()
    def __init__(self):
        pass
    
    def compile(self):
        self.root.iconbitmap('Telegram.ico')
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

    def get_users(self, file_name):
        users = []
        with open(file_name, 'r+', encoding='utf-8') as f:
            file = json.load(f)
        for message in file['messages']:
            if message.get('from') not in users:
                users.append(message.get('from'))
        return users

    def get_years(self, file_name):
        years = []
        with open(file_name, 'r+', encoding='utf-8') as f:
            file = json.load(f)
        for message in file['messages']:
            if message.get('date')[:4] not in years:
                years.append(message.get('date')[:4])
        return years

    def createTextAnalyst(self, file):
        self.ta = textAnalyst(file)
    
    def createTimeAnalyst(self, file):
        self.ta = timeAnalyst(file)
