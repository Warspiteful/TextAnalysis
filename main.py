from MainGUI import GUI
from tkinter import *
from TextAnalysisGUI import Text_Analyst_GUI
from ImageGUI import TimeGUI

class main(GUI):

    def __init__(self):
        self.root.title("Telegram Analysis")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.initialize()
        self.compile()

    def initialize(self):
        self.reset()
        label = Label(self.frame, text = "Select your analyzer.").pack()
        button1 = Radiobutton(self.frame, text="Text Analyzer", variable=self.v, value=1).pack(anchor=W)
        button2 = Radiobutton(self.frame, text="Statistics Analyzer", variable=self.v, value=2).pack(anchor=W)
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Send", width="12", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.select).pack(anchor=W)

            
    def select(self):
        if self.v.get() == 1:
            self.reset()
            Text_Analyst_GUI()
        
        if self.v.get() == 2:
            self.reset()
            TimeGUI()

        else:
            return

main()
