<<<<<<< HEAD
import tkinter as tk
import importlib, sys

TITLE_FONT = ("Helvetica", 24, "bold")

class tictactoe_game(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (menu, roll_credits, multiplayer, Online_Multiplayer, close):# input frame name here
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("menu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class menu(tk.Frame):

    menuCount1 = 0
    menuCount2 = 0
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        label = tk.Label(self, text=" ", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Tic-Tac-Toe", font=TITLE_FONT, bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text=" ", bg="black", fg="white").pack(fill="both", expand=True)
        button1 = tk.Button(self, text="Player vs Computer", bg="black", fg="white", command=self.singleplayer).pack(fill="both", expand=True)
        button2 = tk.Button(self, text="Offline Multiplayer", bg="black", fg="white", command=lambda: controller.show_frame("multiplayer")).pack(fill="both", expand=True)
        button3 = tk.Button(self, text="Online Multiplayer", bg="black", fg="white", command=lambda: controller.show_frame("Online_Multiplayer")).pack(fill="both", expand=True)
        button4 = tk.Button(self, text="Credits", bg="black", fg="white", command=lambda: controller.show_frame("roll_credits")).pack(fill="both", expand=True)
        button5 = tk.Button(self, text="Close", bg="black", fg="white", command=lambda: controller.show_frame("close")).pack(fill="both", expand=True)

    def singleplayer(self):
        if self.menuCount1 == 0:
            self.menuCount1 = 1
            import singleplayer
        elif self.menuCount1 == 1:
            import singleplayer
            importlib.reload(module=singleplayer)

class Online_Multiplayer(tk.Frame):

    menuCount3 = 0
    menuCount4 = 0
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        button = tk.Button(self, text="Return to Menu", bg="black", fg="white", command=lambda: controller.show_frame("menu")).pack(fill="both", expand=True)
        

class roll_credits(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        label = tk.Label(self, text=" ", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Credits", font=TITLE_FONT, bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text=" ", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Created by", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text=" ", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Kyle Speke", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Taylor Southorn", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Harry Hudson", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Ayyub Lindroos", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Faizan Ahmed", bg="black", fg="white").pack(fill="both", expand=True)
        button = tk.Button(self, text="Return to Menu", bg="black", fg="white", command=lambda: controller.show_frame("menu")).pack(fill="both", expand=True)

#player vs player
class multiplayer (tk.Frame):

#creats a frame and initialize it.
    def __init__(self, parent, controller):
        frame=tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        label = tk.Label(self, text="Playing vs Player", font=TITLE_FONT, bg="black", fg="white").grid(row=0, column=0, columnspan=3)
        self.canvas()
        button = tk.Button(self, text="New Game", bg="black", fg="white", command=self.reset).grid(row=3, column=0)
        button = tk.Button(self, text="Return to Menu", bg="black", fg="white", command=lambda: controller.show_frame("menu")).grid(row=3, column=1)

    def reset (self):
        #resets the board
        self.board.delete("all")
        self.board.unbind("<ButtonPress-1>")
        self.j=True
        self.canvas()

    def canvas(self):
        self.board = tk.Canvas(self, width=300, height=300)
        # allows me to make the canvas clickerble
        self.board.bind("<ButtonPress-1>", self.sgplayer)
        self.board.grid(row=2, column=0, columnspan=2)
        self.board.create_rectangle(0,0,300,300, outline="white", fill="black")
        self.board.create_rectangle(100,300,200,0, outline="white")
        self.board.create_rectangle(0,100,300,200, outline="white")
        #allows me to store a number in each square which is relevant to ( O, X )
        self.location=[[0,0,0],[0,0,0],[0,0,0]]
        self.i=0
        self.j=False

    def sgplayer(self, event):
        # k is the x coords
        for k in range(0,300,100):
            # j is the y coords
            for j in range(0,300,100):
                if event.x in range(k,k+100) and event.y in range(j,j+100):
                    if self.board.find_enclosed(k,j,k+100,j+100)==():
                        if self.i%2==0:
                            X=(2*k+100)/2
                            Y=(2*j+100)/2
                            X1=int(k/100)
                            Y1=int(j/100)
                            #creats the O on the board
                            self.board.create_oval( X+25, Y+25, X-25, Y-25, width=8, outline="white")
                            self.location[Y1][X1]+=1
                            self.i+=1
                        else:
                            X=(2*k+100)/2
                            Y=(2*j+100)/2
                            X1=int(k/100)
                            Y1=int(j/100)
                            #creats the X on the board
                            self.board.create_line( X+20, Y+20, X-20, Y-20, width=8, fill="white")
                            self.board.create_line( X-20, Y+20, X+20, Y-20, width=8, fill="white")
                            self.location[Y1][X1]+=9
                            self.i+=1
        self.check()
#cirlce wins
    def circle(self):
        tk.messagebox.showinfo("Congratulations!", "O won the game!")
        self.reset()
#crosses win
    def cross(self):
        tk.messagebox.showinfo("Congratulations!", "X won the game!")
        self.reset()
#draw
    def draw(self):
        tk.messagebox.showinfo("It is a tie", "Better Luck Next Time!")
        self.reset()
#checks who wins
    def check(self):
        #horizontal check
        #below transposes self.location so that it could use the sum fucntion again
        self.location=[[row[i] for row in self.location] for i in range(3)]
        for i in range(0,3):
            if sum(self.location[i])==27:
                self.cross()
            if sum(self.location[i])==3:
                self.circle()
        #vertical check
        #below transposes self.location so that it could use the sum fucntion again
        self.location=[[row[i] for row in self.location] for i in range(3)]
        for i in range(0,3):
            if sum(self.location[i])==27:
                self.cross()
            if sum(self.location[i])==3:
                self.circle()
        #check for diagonal wins
        if self.location[1][1]==9:
            if self.location[0][0]==self.location[1][1] and self.location[2][2]==self.location[1][1] :
                self.cross()
            elif self.location[0][2]==self.location[1][1] and self.location[2][0]==self.location[1][1] :
                self.cross()
        if self.location[1][1]==1:
            if self.location[0][0]==self.location[1][1] and self.location[2][2]==self.location[1][1] :
                self.circle()
            elif self.location[0][2]==self.location[1][1] and self.location[2][0]==self.location[1][1] :
                self.circle()
        #check for draws
        if self.j==False:
            a=0
            for i in range(0,3):
                a+= sum(self.location[i])
            if a==41:
                self.draw()

class close(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        label = tk.Label(self, text="Closing", bg="black", fg="white").pack(fill="both", expand=True)

if __name__ == "__main__":
    app = tictactoe_game()
    app.title("Tic-Tac-Toe")
=======
import tkinter as tk
import importlib

TITLE_FONT = ("Helvetica", 24, "bold")

class tictactoe_game(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (menu, roll_credits, multiplayer, close):# input frame name here
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("menu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class menu(tk.Frame):

    menuCount1 = 0
    menuCount2 = 0
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        label = tk.Label(self, text=" ", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Tic-Tac-Toe", font=TITLE_FONT, bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text=" ", bg="black", fg="white").pack(fill="both", expand=True)
        button1 = tk.Button(self, text="Player vs Computer", bg="black", fg="white", command=self.singleplayer).pack(fill="both", expand=True)
        button2 = tk.Button(self, text="Offline Multiplayer", bg="black", fg="white", command=lambda: controller.show_frame("multiplayer")).pack(fill="both", expand=True)
        button3 = tk.Button(self, text="Online Multiplayer", bg="black", fg="white", command=self.Online_Multiplayer).pack(fill="both", expand=True)
        button4 = tk.Button(self, text="Credits", bg="black", fg="white", command=lambda: controller.show_frame("roll_credits")).pack(fill="both", expand=True)
        button5 = tk.Button(self, text="Close", bg="black", fg="white", command=lambda: controller.show_frame("close")).pack(fill="both", expand=True)

    def singleplayer(self):
        '''runs text based singleplayer client(with ai)'''
        if self.menuCount1 == 0:
            self.menuCount1 = 1
            import singleplayer
        elif self.menuCount1 == 1:
            import singleplayer
            importlib.reload(module=singleplayer)

    def Online_Multiplayer(self):
        '''runs text based online multiplayer client'''
        if self.menuCount2 == 0:
            self.menuCount2 = 1
            import Game_Client
        elif self.menuCount2 == 1:
            import Game_Client
            importlib.reload(module=Game_Client)

class roll_credits(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        label = tk.Label(self, text=" ", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Credits", font=TITLE_FONT, bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text=" ", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Created by", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text=" ", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Kyle Speke", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Taylor Southorn", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Harry Hudson", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Ayyub Lindroos", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Faizan Ahmed", bg="black", fg="white").pack(fill="both", expand=True)
        button = tk.Button(self, text="Menu", bg="black", fg="white", command=lambda: controller.show_frame("menu")).pack(fill="both", expand=True)

#player vs player
class multiplayer (tk.Frame):
#creats a frame and initialize it.
    def __init__(self, parent, controller):
        frame=tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        label = tk.Label(self, text="Playing vs Player", font=TITLE_FONT, bg="black", fg="white").grid(row=0, column=0, columnspan=3)
        self.canvas()
        button = tk.Button(self, text="New Game", bg="black", fg="white", command=self.reset).grid(row=3, column=0)
        button = tk.Button(self, text="Menu", bg="black", fg="white", command=lambda: controller.show_frame("menu")).grid(row=3, column=1)

    def reset (self):
        #resets the board
        self.board.delete("all")
        self.board.unbind("<ButtonPress-1>")
        self.j=True
        self.canvas()

    def canvas(self):
        self.board = tk.Canvas(self, width=300, height=300)
        # allows me to make the canvas clickerble
        self.board.bind("<ButtonPress-1>", self.sgplayer)
        self.board.grid(row=2, column=0, columnspan=2)
        self.board.create_rectangle(0,0,300,300, outline="white", fill="black")
        self.board.create_rectangle(100,300,200,0, outline="white")
        self.board.create_rectangle(0,100,300,200, outline="white")
        #allows me to store a number in each square which is relevant to ( O, X )
        self.location=[[0,0,0],[0,0,0],[0,0,0]]
        self.i=0
        self.j=False

    def sgplayer(self, event):
        # k is the x coords
        for k in range(0,300,100):
            # j is the y coords
            for j in range(0,300,100):
                if event.x in range(k,k+100) and event.y in range(j,j+100):
                    if self.board.find_enclosed(k,j,k+100,j+100)==():
                        if self.i%2==0:
                            X=(2*k+100)/2
                            Y=(2*j+100)/2
                            X1=int(k/100)
                            Y1=int(j/100)
                            #creats the O on the board
                            self.board.create_oval( X+25, Y+25, X-25, Y-25, width=8, outline="white")
                            self.location[Y1][X1]+=1
                            self.i+=1
                        else:
                            X=(2*k+100)/2
                            Y=(2*j+100)/2
                            X1=int(k/100)
                            Y1=int(j/100)
                            #creats the X on the board
                            self.board.create_line( X+20, Y+20, X-20, Y-20, width=8, fill="white")
                            self.board.create_line( X-20, Y+20, X+20, Y-20, width=8, fill="white")
                            self.location[Y1][X1]+=9
                            self.i+=1
        self.check()
#cirlce wins
    def circle(self):
        tk.messagebox.showinfo("Congratulations!", "O won the game!")
        self.reset()
#crosses win
    def cross(self):
        tk.messagebox.showinfo("Congratulations!", "X won the game!")
        self.reset()
#draw
    def draw(self):
        tk.messagebox.showinfo("It is a tie", "Better Luck Next Time!")
        self.reset()
#checks who wins
    def check(self):
        #horizontal check
        #below transposes self.location so that it could use the sum fucntion again
        self.location=[[row[i] for row in self.location] for i in range(3)]
        for i in range(0,3):
            if sum(self.location[i])==27:
                self.cross()
            if sum(self.location[i])==3:
                self.circle()
        #vertical check
        #below transposes self.location so that it could use the sum fucntion again
        self.location=[[row[i] for row in self.location] for i in range(3)]
        for i in range(0,3):
            if sum(self.location[i])==27:
                self.cross()
            if sum(self.location[i])==3:
                self.circle()
        #check for diagonal wins
        if self.location[1][1]==9:
            if self.location[0][0]==self.location[1][1] and self.location[2][2]==self.location[1][1] :
                self.cross()
            elif self.location[0][2]==self.location[1][1] and self.location[2][0]==self.location[1][1] :
                self.cross()
        if self.location[1][1]==1:
            if self.location[0][0]==self.location[1][1] and self.location[2][2]==self.location[1][1] :
                self.circle()
            elif self.location[0][2]==self.location[1][1] and self.location[2][0]==self.location[1][1] :
                self.circle()
        #check for draws
        if self.j==False:
            a=0
            for i in range(0,3):
                a+= sum(self.location[i])
            if a==41:
                self.draw()

class close(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        label = tk.Label(self, text="Closing", bg="black", fg="white").pack(fill="both", expand=True)

if __name__ == "__main__":
    app = tictactoe_game()
    app.title("Tic-Tac-Toe")
>>>>>>> origin/master
