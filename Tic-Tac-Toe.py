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
    container = tk.Frame(self).pack(side=top", fill="both", expand=true)
                                    
# grid_rowconfigure/columnconfigure configures the row/column
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    
    self.frames = {}
#this allows you to select different frames to bring to the top
    for F in (Menu,Pageone, Pagetwo):
        page_name = F.__name__
        frame = F(parent=container, cpntroller=self)
        self.frames[page_name]

        frame.grid(row=0, column=0, sticky="nsew")

#defining what show frame is 
#this raises a frame to the top
 def show_frame(self, page_name):
    frame = self.frames[page_name]
    frame.tkraise()
