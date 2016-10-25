#   First we are going to import a gui... 
#   we have chosen tkinter so we are going to import
import tkinter as tk

#defines a font to use 
TITLE_FONT = ("", 32, "bold")

#defining what the game is
class app(tk.tk):
  
# *arg allow you to pass multiple arguments through without knowing exactly how many you want to pass through
#**kwargs allows you to select a particular argument ( the stars is just an order based system)
#__init__ function is a constructor  or initializer, and is automatically called when you create a new instance of a class
  def __init__(self, *args, **kwargs):
    tk.Tk.__init(self, *args, **kwargs)
    
# container is a layout manager
# grid_rowconfigure/columnconfigure configures the row/column 
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

#this allows you to select different frames to bring to the top
        self.frames = {}
        for F in (StatPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

#defining what show frame is 
#this raises a frame to the top
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

#this is the menu
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Tic-Tac-Toe", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Computer", bg="black", fg="white", command=lambda: controller.show_frame("PageOne")).pack()
        button2 = tk.Button(self, text="Multiplayer", bg="black", fg="white", command=lambda: controller.show_frame("PageTwo")).pack()

#computer page where you can play against computer
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        label = tk.Label(self, text="Playing Computer", font=TITLE_FONT, bg="black", fg="white").grid(column=1, row=0, columnspan=3) 
        button = tk.Button(self, text="Menu", bg="black", fg="white", command=lambda: controller.show_frame("StartPage")).grid(column=2, row=5) 

        button1 = tk.Button(self, height="10", width="20").grid(column=1, row=1) 
        button2 = tk.Button(self, bg="yellow", height="10", width="20").grid(column=2, row=1) 
        button3 = tk.Button(self, bg="black", height="10", width="20").grid(column=3, row=1) 
        button4 = tk.Button(self, bg="white", height="10", width="20").grid(column=1, row=2) 
        button5 = tk.Button(self, bg="orange", height="10", width="20").grid(column=2, row=2) 
        button6 = tk.Button(self, bg="pink", height="10", width="20").grid(column=3, row=2) 
        button7 = tk.Button(self, bg="blue", height="10", width="20").grid(column=1, row=3) 
        button8 = tk.Button(self, bg="red", height="10", width="20").grid(column=2, row=3) 

#multiplayer page
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        label = tk.Label(self, text="Playing Multiplayer", font=TITLE_FONT, bg="black", fg="white").grid(column=1, row=0, columnspan=3) 
        button = tk.Button(self, text="Menu", bg="black", fg="white", command=lambda: controller.show_frame("StartPage")).grid(column=2, row=5) 
        
        button1 = tk.Button(self, height="10", width="20").grid(column=1, row=1) 
        button2 = tk.Button(self, bg="yellow", height="10", width="20").grid(column=2, row=1) 
        button3 = tk.Button(self, bg="black", height="10", width="20").grid(column=3, row=1) 
        button4 = tk.Button(self, bg="white", height="10", width="20").grid(column=1, row=2) 
        button5 = tk.Button(self, bg="orange", height="10", width="20").grid(column=2, row=2) 
        button6 = tk.Button(self, bg="pink", height="10", width="20").grid(column=3, row=2) 
        button7 = tk.Button(self, bg="blue", height="10", width="20").grid(column=1, row=3) 
        button8 = tk.Button(self, bg="red", height="10", width="20").grid(column=2, row=3) 
        button9 = tk.Button(self, bg="purple", height="10", width="20").grid(column=3, row=3)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


     
