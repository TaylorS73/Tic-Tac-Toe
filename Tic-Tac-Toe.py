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

  def tictactoe(buttons):
    
      global bclick
    
      if buttons ["text"] == " "and bclick == True:
          buttons["text"] = "X"
          bclick = False
      elif buttons ["text"] == " "and bclick == False:
         buttons["text"] = "O"
         bclick = True
        
      elif(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
           button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
           button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
           button3["text"] == "X" and button4["text"] == "X" and button5["text"] == "X" or
           button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
           button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
           button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
           button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" ):
          messagebox.showinfo("Winner is X", "Player X won the game!")

      else:
          (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
           button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
           button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
           button3["text"] == "O" and button4["text"] == "O" and button5["text"] == "O" or
           button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
           button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
           button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
           button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" )
          messagebox.showinfo("Winner is O", "Player O won the game!")

  buttons=StringVar()

  button1=Button(root, text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button1)).grid(row=1,column=0,sticky=S+N+E+W)

  button2=Button(root, text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button2)).grid(row=1,column=1,sticky=S+N+E+W)

  button3=Button(root, text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button3)).grid(row=1,column=2,sticky=S+N+E+W)

  button4=Button(root, text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button4)).grid(row=2,column=0,sticky=S+N+E+W)

  button5=Button(root, text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button5)).grid(row=2,column=1,sticky=S+N+E+W)

  button6=Button(root, text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button6)).grid(row=2,column=2,sticky=S+N+E+W)

  button7=Button(root, text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button7)).grid(row=3,column=0,sticky=S+N+E+W)

  button8=Button(root, text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button8)).grid(row=3,column=1,sticky=S+N+E+W)

  button9=Button(root, text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button9)).grid(row=3,column=2,sticky=S+N+E+W)

#multiplayer page
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        label = tk.Label(self, text="Playing Multiplayer", font=TITLE_FONT, bg="black", fg="white").grid(column=1, row=0, columnspan=3) 
        button = tk.Button(self, text="Menu", bg="black", fg="white", command=lambda: controller.show_frame("StartPage")).grid(column=2, row=5) 

  def tictactoe(buttons):
    
      global bclick
    
      if buttons ["text"] == " "and bclick == True:
          buttons["text"] = "X"
          bclick = False
      elif buttons ["text"] == " "and bclick == False:
         buttons["text"] = "O"
         bclick = True
        
      elif(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
           button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
           button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
           button3["text"] == "X" and button4["text"] == "X" and button5["text"] == "X" or
           button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
           button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
           button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
           button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" ):
          messagebox.showinfo("Winner is X", "Player X won the game!")

      else:
          (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
           button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
           button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
           button3["text"] == "O" and button4["text"] == "O" and button5["text"] == "O" or
           button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
           button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
           button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
           button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" )
          messagebox.showinfo("Winner is O", "Player O won the game!")

  buttons=StringVar()

  button1=Button(root, text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button1)).grid(row=1,column=0,sticky=S+N+E+W)

  button2=Button(root, text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button2)).grid(row=1,column=1,sticky=S+N+E+W)

  button3=Button(root, text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button3)).grid(row=1,column=2,sticky=S+N+E+W)

  button4=Button(root, text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button4)).grid(row=2,column=0,sticky=S+N+E+W)

  button5=Button(root, text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button5)).grid(row=2,column=1,sticky=S+N+E+W)

  button6=Button(root, text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button6)).grid(row=2,column=2,sticky=S+N+E+W)

  button7=Button(root, text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button7)).grid(row=3,column=0,sticky=S+N+E+W)

  button8=Button(root, text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button8)).grid(row=3,column=1,sticky=S+N+E+W)

  button9=Button(root, text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button9)).grid(row=3,column=2,sticky=S+N+E+W)        

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


     
