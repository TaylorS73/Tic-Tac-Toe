from tkinter import * #imports Python's GUI from the database

B_FONT = ("Helvetica",42)
root = Tk()
root.title("Tic Tac Toe") #Creates the title of the Window and labels it to something relevant

bclick = True

def tictactoe(buttons): #  a function used to define the buttons used to in the game
    
    global bclick
    
    if buttons ["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
    elif buttons ["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True

# This is the method we used in order to check if the buttons have been pressed and therefore display either
# player 1 or 2, represented by an "X" and "O". This is better because we dont need to create each player as a
# profile.

    if(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
         button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
         button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
         button3["text"] == "X" and button4["text"] == "X" and button5["text"] == "X" or
         button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
         button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
         button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
         button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" ):
        messagebox.showinfo("Congratulations!", "Player X won the game!")

    elif(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
         button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
         button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
         button3["text"] == "O" and button4["text"] == "O" and button5["text"] == "O" or
         button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
         button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
         button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
         button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" ):
        messagebox.showinfo("Congratulations!", "Player O won the game!")

buttons=StringVar()

button1=Button(root, text=" ",font=B_FONT,height=3,width=7,bg="cyan",fg="white",command=lambda:tictactoe(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)

button2=Button(root, text=" ",font=B_FONT,height=3,width=7,bg="cyan",fg="white",command=lambda:tictactoe(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)

button3=Button(root, text=" ",font=B_FONT,height=3,width=7,bg="cyan",fg="white",command=lambda:tictactoe(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)
    
button4=Button(root, text=" ",font=B_FONT,height=3,width=7,bg="cyan",fg="white",command=lambda:tictactoe(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)

button5=Button(root, text=" ",font=B_FONT,height=3,width=7,bg="cyan",fg="white",command=lambda:tictactoe(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)

button6=Button(root, text=" ",font=B_FONT,height=3,width=7,bg="cyan",fg="white",command=lambda:tictactoe(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)

button7=Button(root, text=" ",font=B_FONT,height=3,width=7,bg="cyan",fg="white",command=lambda:tictactoe(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)

button8=Button(root, text=" ",font=B_FONT,height=3,width=7,bg="cyan",fg="white",command=lambda:tictactoe(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)

button9=Button(root, text=" ",font=B_FONT,height=3,width=7,bg="cyan",fg="white",command=lambda:tictactoe(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)

root.mainloop()
