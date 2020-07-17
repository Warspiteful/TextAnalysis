from tkinter import *
from tkinter import messagebox
import re, ntpath
from MainGUI import GUI

class Text_Analyst_GUI(GUI):


    def __init__(self): 
        self.root.title("Text Analysis")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.start()
        self.compile()


    def start(self):
        self.reset()
        button1 = Radiobutton(self.frame, text="Single File (.txt,.json)", variable=self.v, value=1).pack(anchor=W)
        button2 = Radiobutton(self.frame, text="Multi-File (.txt)", variable=self.v, value=2).pack(anchor=W)
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Send", width="12", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.send).pack(anchor=W)
    def send(self):
        if self.v.get() > 0:
            self.create_path_frame(self.v.get())
        else:
            messagebox.showerror("Error", "Select an option")
            return
   
    def create_path_frame(self, selection):
        self.reset()
        self.EntryBoxes = []
    
        if selection == 1:
            label = Label(self.frame, text = "Set .txt/.json File Path").pack()
            limit = StringVar()
            limit.trace('w', self.limit_size)    
            self.limiters.append(limit)
            self.EntryBoxes.append(Entry(self.frame, bd=0, bg="white",width="20", font="Arial", textvariable=self.limiters[0], ))
        elif selection == 2:
            label = Label(self.frame, text = "Set File Paths").pack()
            for i in range(3):
                limit = StringVar()
                limit.trace('w', self.limit_size)    
                self.limiters.append(limit)
                self.EntryBoxes.append(Entry(self.frame, bd=0, bg="white",width="20", font="Arial", textvariable=self.limiters[i], borderwidth=5 ))
        for box in self.EntryBoxes:
            box.pack()
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Send", width="12", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.set_path).pack()

        self.compile()

    def set_path(self):
        msg = []
        self.files = []
        for box in self.EntryBoxes:
            if box.get().strip()[-4:] != "":
                msg.append(box.get().strip()) 
            box.delete(0,END)
        try:
         
            for file in msg:
                self.files.append(ntpath.basename(file))
            if msg[0][-4:] == 'json':
              
                if len(msg) < 2: 
                    print("".join(msg))
                    self.json_user_select("".join(msg))
                    return
                else:
                    raise Exception
        
            self.createTextAnalyst(msg)
            self.root.geometry("")
            self.create_main_screen()
        except Exception:
            messagebox.showerror("Error", "Can not parse provided file path")
            return
    
    def json_user_select(self, json_path):
        self.reset()
        self.json = json_path
        self.users = self.get_users(json_path)
        
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
            if msg[-3:] != ".txt" and msg[-3:] != "":
                msg += ".txt"
            self.text_path.delete(0,END)
            self.createTextAnalyst([self.json, self.users[self.v.get()-1], msg])
            self.reset()
            self.create_main_screen()

    def create_main_screen(self):
        self.reset()
        pos = {"NN":"Noun","VB":"Verb","JJ":"Adjective"}
        pos_word = []
        num = 0
        for tag in pos.keys():
            label =  Label(self.frame,text = pos[tag], padx = 20).grid(row = 0, column = num, columnspan = 2)
            word = Text(self.frame, width = 10, height = 1, padx = 20, state = NORMAL)
            word.grid(row = 1, column = num, columnspan = 2)
            num += 2
            word.insert(END, self.ta.find_favorite_pos(tag)[0])
            word.config(state=DISABLED)

        vcmd = (self.root.register(self.digit_locker))
        self.common_words_display = Text(self.frame, bd=0, bg="white", height="10", width="10", font="Arial")
        self.common_words_display.grid(row = 5, column = 0, rowspan = 10,  padx=10)
        label = Label(self.frame,text = "Common Terms").grid(row = 2, column = 0, columnspan = 2)
        self.common_words_entry = Entry(self.frame, bd=0, bg="white", width="10", font="Arial", validate = "all", validatecommand = (vcmd,'%P'))
        self.common_words_entry.grid(row = 3, column = 0, columnspan = 2)
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Send", width="8", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.most_common).grid(row = 4, column = 0, columnspan = 2)
        self.common_words_display.config(state = DISABLED)

        label = Label(self.frame, text = "Files in Model").grid(row = 2, column = 2, columnspan = 2)
        text_files_display = Text(self.frame, width = 10, height = 5, state = NORMAL)
        text_files_display.grid(row = 3, column = 2, rowspan = 3, columnspan = 2)
        for file in self.files:
            text_files_display.insert(END,file + "\n")
        text_files_display.config(state = NORMAL)

        main_screen = Button(self.frame, font=("Verdana",12,'bold'), text="Return", width="12", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.start).grid(row = 7, column = 2, columnspan = 2)

        similar_word_label = Label(self.frame, text ="Word").grid(row = 2, column = 4)
        similar_word_num_label = Label(self.frame, text ="# Of Similar").grid(row = 2, column = 5)
        self.similar_word_entry = Entry(self.frame, width = 10)
        self.similar_word_entry.grid(row = 3, column = 4)
        self.similar_word_num_entry = Entry(self.frame, width = 2, validate = "all", validatecommand = (vcmd,'%P'))
        self.similar_word_num_entry.grid(row = 3, column = 5)
        button = Button(self.frame, font=("Verdana",12,'bold'), text="Send", width="12", height=1,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.find_similar).grid(row = 4, column = 4, columnspan = 2)
        self.similar_word_display = Text(self.frame, bd=0, bg="white", height="10", width="15", font="Arial")
        self.similar_word_display.grid(row = 5, column = 4, rowspan = 10, columnspan = 2,)
        self.similar_word_display.config(state = DISABLED)
        self.compile()
    def find_similar(self):
        self.similar_word_display.config(state = NORMAL)
        self.similar_word_display.delete('1.0', END)
        if self.similar_word_entry.get() == '':
            messagebox.showerror("Error", "Cannot search for empty word")
            return
        elif self.similar_word_num_entry.get() == '':
            messagebox.showerror("Error", "Cannot display 0 terms")
            return
        try:
            if int(self.similar_word_num_entry.get()) > 0 and self.similar_word_entry.get() != '':
                words = self.ta.return_most_similar(self.similar_word_entry.get(),int(self.similar_word_num_entry.get()))
                for num, word in enumerate(words):
                    self.similar_word_display.insert(END, str(num + 1) + ". " + word[0] + "\n")
            self.similar_word_display.config(state = DISABLED)
        except Exception:
            messagebox.showerror("Error", "Word Not Present in Vocabulary")
            return
        
    def digit_locker(self, P):
        if str.isdigit(P) or P == '':
            return True
        else:
            return False

    def most_common(self):
        self.common_words_display.config(state = NORMAL)
        self.common_words_display.delete('1.0', END)
        try:
            if int(self.common_words_entry.get()) > 0:
                words = self.ta.most_frequent_words(int(self.common_words_entry.get()))
                for num, word in enumerate(words):
                    self.common_words_display.insert(END, str(num + 1) + ". " + word[0] + "\n")
        except:
            messagebox.showerror("Error", "Cannot display 0 terms")
        self.common_words_display.config(state = DISABLED)
    