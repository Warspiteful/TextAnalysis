from tkinter import *
from analysis import textAnalyst
class GUI():

    root = Tk()
    v = IntVar()
    def __init__(self):
        
        self.root.title("Tex Analysis")
        self.create_frame()
        self.start()
        self.compile()


    def create_frame(self):
        self.frame = Frame(self.root)
        self.frame.pack()

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
        self.frame.destroy()
       
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