import tkinter as tk
from tkinter import *
n=0
while (n!=20):
    print("1.Use Label\n")
    print("2.Use Image in Label\n")
    print("3.Text on image\n")
    print("4.Colorized Labels with fonts\n")
    print("5.Dynamical Content in a Label\n")
    print("6.Message Widget\n")
    print("7.Button\n")
    print("8.Radio Buttons\n")
    print("9.Indicator\n")
    print("10.Simple Checkboxes\n")
    print("11.CheckBox with Button\n")
    print("12.button for checking the state of the checkbox\n")
    print("13.Entry Widgets\n")
    print("14.Canvas Widgets\n")
    print("15.Sliders\n")
    print("16.Text Widgets\n")
    print("17.Dialogues and Message Boxes\n")
    print("18. Menu\n")
    print("19. Event\n")
    print("20.Exit\n")
    
    n=int(input("Enter your choice:"))

    if (n==1):
        print("Using Labels")
        root = tk.Tk()
        w = tk.Label(root, text="Hello Tkinter!")
        w.pack()
        root.mainloop()

    if (n==2):
        print("Using Images in Labels")
        root = tk.Tk()
        logo = tk.PhotoImage(file="python_logo_small.gif")
        w1 = tk.Label(root, image=logo).pack(side="right")

        explanation = """At present, only GIF and PPM/PGM
                    formats are supported, but an interface 
                    exists to allow additional image file
                    formats to be added easily."""

        w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=explanation).pack(side="left")
        root.mainloop()

    if (n==3):
        print("The text drawn on top of the image")
        root = tk.Tk()
        logo = tk.PhotoImage(file="python_logo_small.gif")

        explanation = """At present, only GIF and PPM/PGM
                    formats are supported, but an interface 
                    exists to allow additional image file
                    formats to be added easily."""

        w = tk.Label(root, 
             compound = tk.CENTER,
             text=explanation, 
             image=logo).pack(side="right")

        root.mainloop()

    if (n==4):
        print("Colorized Labels in various fonts")
        root = tk.Tk()
        tk.Label(root, 
		 text="Red Text in Times Font",
		 fg = "red",
		 font = "Times").pack()
        tk.Label(root, 
		 text="Green Text in Helvetica Font",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").pack()
        tk.Label(root, 
		 text="Blue Text in Verdana bold",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 10 bold").pack()

        root.mainloop()
       

    if(n==5):
        print("Dynamical Content in a Label")
        counter = 0 
        def counter_label(label):
            def count():
                global counter
                counter += 1
                label.config(text=str(counter))
                label.after(1000, count)
            count()
 
 
        root = tk.Tk()
        root.title("Counting Seconds")
        label = tk.Label(root, fg="green")
        label.pack()
        counter_label(label)
        button = tk.Button(root, text='Stop', width=25, command=root.destroy)
        button.pack()
        root.mainloop()

    if (n==6):
        print("6.Message Widget\n")
        master = tk.Tk()
        whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
        msg = tk.Message(master, text = whatever_you_do)
        msg.config(bg='lightgreen', font=('times', 24, 'italic'))
        msg.pack()
        tk.mainloop()

    if (n==7):
        print("7.Button\n")
        def write_slogan():
            print("Tkinter is easy to use!")

        root = tk.Tk()
        frame = tk.Frame(root)
        frame.pack()

        button = tk.Button(frame, 
                  text="QUIT", 
                   fg="red",
                   command=quit)
        button.pack(side=tk.LEFT)
        slogan = tk.Button(frame,
                  text="Hello",
                   command=write_slogan)
        slogan.pack(side=tk.LEFT)

        root.mainloop()

    if(n==8):
        print("8.Radio Buttons\n")
        root = tk.Tk()

        v = tk.IntVar()
        v.set(1)  # initializing the choice, i.e. Python

        languages = [
                        ("Python",1),
                        ("Perl",2),
                        ("Java",3),
                        ("C++",4),
                        ("C",5)
                    ]

        def ShowChoice():
            print(v.get())

        tk.Label(root, 
        text="""Choose your favourite 
                programming language:""",
        justify = tk.LEFT,
        padx = 20).pack()

        for val, language in enumerate(languages):
            tk.Radiobutton(root, 
                          text=language,
                          padx = 20, 
                          variable=v, 
                          command=ShowChoice,
                          value=val).pack(anchor=tk.W)


        root.mainloop()

    if (n==9):
        print("9.Indicator\n")
        root = tk.Tk()

        v = tk.IntVar()
        v.set(1)  # initializing the choice, i.e. Python

        languages = [
                        ("Python",1),
                        ("Perl",2),
                        ("Java",3),
                        ("C++",4),
                        ("C",5)
                    ]

        def ShowChoice():
            print(v.get())

        tk.Label(root,text="""Choose your favourite 
                programming language:""",justify = tk.LEFT,
                padx = 20).pack()

        for val, language in enumerate(languages):
            tk.Radiobutton(root, 
                      text=language,
                      indicatoron = 0,
                      width = 20,
                      padx = 20, 
                      variable=v, 
                      command=ShowChoice,
                      value=val).pack(anchor=tk.W)
        root.mainloop()

    if(n==10):
        print("10.Simple Checkboxes\n")
    
        master = Tk()
        var1 = IntVar()
        Checkbutton(master, text="male", variable=var1).grid(row=0, sticky=W)
        var2 = IntVar()
        Checkbutton(master, text="female", variable=var2).grid(row=1, sticky=W)
        mainloop()

    if(n==11):
        print("11.CheckBox with Button\n")
        master = Tk()

        def var_states():
           print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))

        Label(master, text="Your sex:").grid(row=0, sticky=W)
        var1 = IntVar()
        Checkbutton(master, text="male", variable=var1).grid(row=1, sticky=W)
        var2 = IntVar()
        Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=W)
        Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
        Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
        mainloop()

    if (n==12):
        print("button for checking the state of the checkbox")
        class Checkbar(Frame):
            def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
                Frame.__init__(self, parent)
                self.vars = []
                for pick in picks:
                    var = IntVar()
                    chk = Checkbutton(self, text=pick, variable=var)
                    chk.pack(side=side, anchor=anchor, expand=YES)
                    self.vars.append(var)
            def state(self):
                return map((lambda var: var.get()), self.vars)
        if __name__ == '__main__':
            root = Tk()
            lng = Checkbar(root, ['Python', 'Ruby', 'Perl', 'C++'])
            tgl = Checkbar(root, ['English','German'])
            lng.pack(side=TOP,  fill=X)
            tgl.pack(side=LEFT)
            lng.config(relief=GROOVE, bd=2)
        def allstates():
            print(list(lng.state()), list(tgl.state()))
        Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
        Button(root, text='Peek', command=allstates).pack(side=RIGHT)
        root.mainloop()

    if(n==13):
        print("Entry Widgets\n")
        def show_entry_fields():
            print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

        master = Tk()
        Label(master, text="First Name").grid(row=0)
        Label(master, text="Last Name").grid(row=1)

        e1 = Entry(master)
        e2 = Entry(master)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)

        Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
        Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

        mainloop( )

    if(n==14):
        print("Canvas Widgets\n")
        master = Tk()

        w = Canvas(master, width=200, height=100)
        w.pack()

        w.create_rectangle(50, 20, 150, 80, fill="#476042")
        w.create_rectangle(65, 35, 135, 65, fill="yellow")
        w.create_line(0, 0, 50, 20, fill="#476042", width=3)
        w.create_line(0, 100, 50, 80, fill="#476042", width=3)
        w.create_line(150,20, 200, 0, fill="#476042", width=3)
        w.create_line(150, 80, 200, 100, fill="#476042", width=3)

        mainloop()

    if (n==15):
        print("15.Sliders\n")
        def show_values():
            print (w1.get(), w2.get())

        master = Tk()
        w1 = Scale(master, from_=0, to=42)
        w1.set(19)
        w1.pack()
        w2 = Scale(master, from_=0, to=200, orient=HORIZONTAL)
        w2.set(23)
        w2.pack()
        Button(master, text='Show', command=show_values).pack()
        mainloop()

    if(n==16):
        print("Text Widgets\n")
        root = Tk()
        T = Text(root, height=2, width=30)
        T.pack()
        T.insert(END, "Just a text Widget\nin two lines\n")
        mainloop()

    if(n==17):
        print("Dialogues and Message Boxes\n")
        
        from tkinter.messagebox import *
       
        def answer():
            showerror("Answer", "Sorry, no answer available")

        def callback():
            if askyesno('Verify', 'Really quit?'):
                showwarning('Yes', 'Not yet implemented')
            else:
                showinfo('No', 'Quit has been cancelled')

        Button(text='Quit', command=callback).pack(fill=X)
        Button(text='Answer', command=answer).pack(fill=X)
        mainloop()

    if (n==18):
        print("Menu\n")
        from tkinter import filedialog
        
        def NewFile():
            print ("New File!")
            
        def OpenFile():
            root = Tk()
            root.filename =  filedialog.askopenfilename(initialdir = "/", title = "Select file")
            print (root.filename)
                        
        def About():
            print ("This is a simple example of a menu")
    
        root = Tk()
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=NewFile)
        filemenu.add_command(label="Open...", command=OpenFile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)

        helpmenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=About)

        mainloop()

    if (n==19):
        print("Event\n")
        def hello(event):
            print("Single Click, Button-l") 
        def quit(event):                           
            print("Double Click, so let's stop") 
            import sys; sys.exit() 

        widget = Button(None, text='Mouse Clicks')
        widget.pack()
        widget.bind('<Button-1>', hello)
        widget.bind('<Double-1>', quit) 
        widget.mainloop()