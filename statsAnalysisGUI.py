from tkinter import *
from tkinter import messagebox
import re, ntpath
from baseGUI import GUI


class statsAnalysisGUI(GUI):

    def __init__(self):  
        self.root.title("Statistics Analysis")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.start()
        self.compile()

    def start(self):
        self.reset()
        label = Label(self.frame, text = "Set .json File Path").pack()
        
        self.box = Entry(self.frame, bd=0, bg="white",width="20", font="Arial", )
        self.box.pack()
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Send", width="12", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.set_path).pack()

        
    def set_path(self):
        self.files = []
        try:
            self.json = self.box.get().strip()
            self.files.append(ntpath.basename(self.json))
            self.createStatAnalyst(self.json)
            self.root.geometry("")
           
            self.create_main_screen()
        except Exception:
            messagebox.showerror("Error", "Can not parse provided file path")
            return

    def create_main_screen(self):
        self.reset()
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Count Messages", width="18", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.ta.count_messages).pack()
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Monthly Breakdown", width="18", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.year_entry).pack()
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Season Breakdown", width="18", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.ta.season_breakdown).pack()
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Day Breakdown", width="18", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.month_entry).pack()
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Return", width="18", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.start).pack()
        self.compile()

    def year_entry(self):
        self.reset()
        label = Label(self.frame,text = "Select year").pack()
        self.v.set(self.get_years(self.json)[0])
        popupMenu = OptionMenu(self.frame, self.v, *self.get_years(self.json)).pack()
        
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Submit", width="12", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.year_set).pack()
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Go back", width="12", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.create_main_screen).pack()
        

    def year_set(self):
        try:
            self.ta.monthly_breakdown(self.v.get())
        except:
            messagebox.showerror("Error", "Please select a year")
            return
        

    def month_entry(self):
        self.reset()
        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        label = Label(self.frame,text = "Select Month").pack()
        self.s.set(self.months[0])
        popupMenu = OptionMenu(self.frame, self.s, *self.months).pack()
   
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Submit", width="12", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.month_set).pack()
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Go back", width="12", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.create_main_screen).pack()
    def month_set(self):
        try:
            self.ta.day_breakdown(self.months.index(self.s.get()))
        except:
            messagebox.showerror("Error", "Please select a month")
            return


