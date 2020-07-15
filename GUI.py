from tkinter import *
import guiFunctions as gf
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
    def send(self):
        if self.v.get() > 0:
            self.reset()
            self.create_path_frame(self.v.get())
        else:
            return
 
    def limit_size(self, *args):
        for limiter in self.limiters:
            value = limiter.get()
            if len(value) > 20: limiter.set(value[:20])
   
    def create_path_frame(self, selection):
       
        self.EntryBoxes = []
        self.limiters = []
        if selection == 1:
            label = Label(self.frame, text = "Set Text File Path").pack()
            limit = StringVar()
            limit.trace('w', self.limit_size)    
            self.limiters.append(limit)
            self.EntryBoxes.append(Entry(self.frame, bd=0, bg="white",width="20", font="Arial", textvariable=self.limiters[0], ))
        elif selection == 2:
            label = Label(self.frame, text = "Set Text File Paths").pack()
            for i in range(3):
                limit = StringVar()
                limit.trace('w', self.limit_size)    
                self.limiters.append(limit)
                self.EntryBoxes.append(Entry(self.frame, bd=0, bg="white",width="20", font="Arial", textvariable=self.limiters[i], borderwidth=5 ))
        elif selection == 3:
                label = Label(self.frame, text = "Set JSON file Path").pack()
                limit = StringVar()
                limit.trace('w', self.limit_size)    
                self.limiters.append(limit)
                self.EntryBoxes.append(Entry(self.frame, bd=0, bg="white",width="20", font="Arial", textvariable=self.limiters[0], borderwidth=5 ))
        for box in self.EntryBoxes:
            box.pack()
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Send", width="12", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.set_path).pack()

        self.compile()

    def set_path(self):
        for box in self.EntryBoxes:
            msg = [box.get().strip()] 
            box.delete(0,END)
        try:
            if msg[0][-4:] == 'json':
                self.json_user_select("".join(msg))
            self.ta = gf.textAnalyst(msg)
            self.root.geometry("500x500")
            self.reset()
            self.create_main_screen()
        except Exception:
            return
    
    def json_user_select(self, json_path):
        self.reset()
        self.json = json_path
        self.users = gf.get_users(json_path)
        
        limit = StringVar()
        limit.trace('w', self.limit_size) 
        self.limiters = [limit]
        label1 = Label(self.frame, text = "Choose User to Pull Data From").pack()
        button1 = Radiobutton(self.frame, text=self.users[0], variable=self.v, value=1)
        button1.pack(anchor=W)
        button2 = Radiobutton(self.frame, text=self.users[1], variable=self.v, value=2)
        button2.pack(anchor=W)
        label2 = Label(self.frame, text = "(Optional) Set text file path ").pack()
        self.text_path = Entry(self.frame, bd=0, bg="white",width="20", font="Arial", textvariable=self.limiters[0], borderwidth=5 )
        self.text_path.pack()
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Send", width="12", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.set_user).pack(anchor=W)
        self.compile()

    def set_user(self):
        if self.v.get() > 0:
            msg = self.text_path.get().strip()
            if msg[-3:] != ".txt":
                msg += ".txt"
            self.text_path.delete(0,END)
            self.ta = gf.textAnalyst([self.json, self.users[self.v.get()-1], msg])
            self.root.geometry("500x500")
            self.reset()
            self.create_main_screen()




    def create_main_screen(self):
      
        vcmd = (self.root.register(self.digit_locker))
        self.common_words_display = Text(self.frame, bd=0, bg="white", height="25", width="20", font="Arial")
        self.common_words_display.grid(row = 0, column = 0, rowspan = 25,  padx=10)
        label = Label(self.frame,text = "Common Terms").grid(row = 0, column = 1)
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Send", width="12", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.most_common).grid(row = 2, column = 1)
        self.common_words_entry = Entry(self.frame, bd=0, bg="white", width="10", font="Arial", validate = "all", validatecommand = (vcmd,'%P'))
        self.common_words_entry.grid(row = 1, column = 1)
        
        
    
        self.compile()

    def digit_locker(self, P):
        if str.isdigit(P):
            return True
        else:
            return False

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
    
   
GUI()