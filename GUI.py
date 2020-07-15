from tkinter import *
from analysis import textAnalyst
import re
class GUI():

    root = Tk()
    v = IntVar()
    def __init__(self):
        
        self.root.title("Text Analysis")
        self.reset()
        self.start()
        self.compile()


    def compile(self):
        self.root.mainloop()

    def start(self):
        button1 = Radiobutton(self.frame, text="Text", variable=self.v, value=1).pack(anchor=W)
        button2 = Radiobutton(self.frame, text="Multi-Text", variable=self.v, value=2).pack(anchor=W)
        button3 = Radiobutton(self.frame, text="JSON", variable=self.v, value=3).pack(anchor=W)
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Send", width="12", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.send).pack(anchor=W)

    
    def create_path_frame(self):
        self.limiter = StringVar()
        self.limiter.trace('w', self.limit_size)
        label = Label(self.frame, text = "Set Text File").pack()
        self.EntryBox = Entry(self.frame, bd=0, bg="white",width="20", font="Arial", textvariable=self.limiter, )
        self.EntryBox.pack()
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Send", width="12", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.set_path).pack()
    
        self.compile()

    def set_path(self):
        msg = self.EntryBox.get().strip()
        self.EntryBox.delete(0,END)
        try:
            self.ta = textAnalyst(msg)
            self.root.geometry("500x500")
            self.reset()
            self.create_main_screen()
        except Exception:
            return
       

    def create_main_screen(self):
        self.digit_lock = StringVar()
        self.digit_lock.trace('w', self.digit_locker)
        print("Hello")
        self.common_words_display = Text(self.frame, bd=0, bg="white", height="25", width="20", font="Arial")
        self.common_words_display.grid(row = 0, column = 0, rowspan = 25,  padx=10)
        label = Label(self.frame,text = "Common Terms").grid(row = 0, column = 1)
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Send", width="12", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.most_common).grid(row = 2, column = 1)
        self.common_words_entry = Entry(self.frame, bd=0, bg="white", width="10", font="Arial", textvariable = self.digit_lock)
        self.common_words_entry.grid(row = 1, column = 1)
        
        
    
        self.compile()

    def digit_locker(self, *args):
        value = self.digit_lock.get()
        re.sub(r'^[\d]+',"", value)

    def most_common(self):
        self.common_words_display.delete('1.0', END)
        if int(self.common_words_entry.get()) > 0:
            words = self.ta.most_frequent_words(int(self.common_words_entry.get()))
            for num, word in enumerate(words):
                self.common_words_display.insert(END, str(num + 1) + ". " + word[0] + "\n")

    def reset(self):
        if hasattr(self,'frame'):
            self.frame.destroy()
        self.frame = Frame(self.root)
        self.frame.pack()
    
    def send(self):
        if self.v.get() > 0:
            self.reset()
            self.create_path_frame()
        else:
            return
     #   self.root = Tk()
      #  
        #self.limiter = StringVar()
        #self.limiter.trace('w', self.limit_size)
        #self.root.resizable(width=FALSE, height=FALSE)
        #self.label = Label(self.root, text = "Set Text File")
        #self.EntryBox = Entry(self.root, bd=0, bg="white",width="20", font="Arial", textvariable=self.limiter)
        #self.EntryBox.place(x="125",y="50")
        #self.root.mainloop()
    
    def limit_size(self, *args):
        value = self.limiter.get()
        if len(value) > 20: self.limiter.set(value[:20])


GUI()