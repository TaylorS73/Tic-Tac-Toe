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

                                    
                                    
# This code will add the background image
from PIL import ImageTk,Image
root=Tk()
canvasWidth=600
canvasHeight=400
self.canvas=Canvas(root,width=canvasWidth,height=canvasHeight)
backgroundImage=root.PhotoImage("D:\Documents\Background.png")
backgroundLabel=root.Label(parent,image=backgroundImage)
backgroundLabel.place(x=0,y=0,relWidth=1,relHeight=1)
self.canvas.pack()
root.mainloop()
#http://stackoverflow.com/questions/13637028/adding-a-background-image-in-python
                                    
# This code will make the background images loop
import PIL
import Image
import glob

for filename in glob.glob("*.tif"):
    im=Image.open(filename)
    box=(50, 50, 200, 200)
    im_crop=im.crop(box)
    im_crop.show()
#  http://stackoverflow.com/questions/6997419/how-to-create-a-loop-to-read-several-images-in-a-python-script                                 
