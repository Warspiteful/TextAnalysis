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
        msg = []
        for box in self.EntryBoxes:
            if box.get().strip()[-4:] == ".txt":
                msg.append(box.get().strip()) 
            box.delete(0,END)
        try:
            if msg[0][-4:] == 'json':
                self.json_user_select("".join(msg))
            self.ta = gf.textAnalyst(msg)
            self.root.geometry("")
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
            self.reset()
            self.create_main_screen()




    def create_main_screen(self):
        
        pos = {"NN":"Noun","VB":"Verb","JJ":"Adjective"}
        pos_word = []
        for num, tag in enumerate(pos.keys()):
            label =  Label(self.frame,text = pos[tag], padx = 20).grid(row = 0, column = num)
            word = Text(self.frame, width = 10, height = 1, padx = 20, state = NORMAL)
            word.grid(row = 1, column = num)
            word.insert(END, self.ta.find_favorite_pos(tag)[0])
            word.config(state=DISABLED)

        vcmd = (self.root.register(self.digit_locker))
        self.common_words_display = Text(self.frame, bd=0, bg="white", height="10", width="10", font="Arial")
        self.common_words_display.grid(row = 5, column = 0, rowspan = 10,  padx=10)
        label = Label(self.frame,text = "Common Terms").grid(row = 2, column = 0)
        self.common_words_entry = Entry(self.frame, bd=0, bg="white", width="10", font="Arial", validate = "all", validatecommand = (vcmd,'%P'))
        self.common_words_entry.grid(row = 3, column = 0)
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Send", width="8", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.most_common).grid(row = 4, column = 0)
        self.common_words_display.config(state = DISABLED)
     


          
        
       

        
        
    
        self.compile()

    def digit_locker(self, P):
        if str.isdigit(P) or P == '':
            return True
        else:
            return False

    def most_common(self):
        self.common_words_display.config(state = NORMAL)
        self.common_words_display.delete('1.0', END)
        if int(self.common_words_entry.get()) > 0:
            words = self.ta.most_frequent_words(int(self.common_words_entry.get()))
            for num, word in enumerate(words):
                self.common_words_display.insert(END, str(num + 1) + ". " + word[0] + "\n")
        self.common_words_display.config(state = DISABLED)

    def reset(self):
        if hasattr(self,'frame'):
            self.frame.destroy()
        self.frame = Frame(self.root)
        self.frame.pack()
    
   
GUI()