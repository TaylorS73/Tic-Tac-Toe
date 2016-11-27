import tkinter as tk
from random import randint

TITLE_FONT = ("Helvetica", 24, "bold")

class tictactoe_game(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        path = "bg.jpg"
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (menu, singleplayer, multiplayer):# input frame name here
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

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        label = tk.Label(self, text="Tic-Tac-Toe", font=TITLE_FONT, bg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Created by", bg="white").pack()
        label = tk.Label(self, text="Kyle Speke + Taylor Southorn", bg="white").pack()
        label = tk.Label(self, text="Harry Hudson + Ayyub Lindroos", bg="white").pack()
        label = tk.Label(self, text="Faizan Ahmed", bg="white").pack()

        button1 = tk.Button(self, text="Player vs Computer", bg="white", command=lambda: controller.show_frame("singleplayer")).pack(fill="both", expand=True, side="left")
        button2 = tk.Button(self, text="Player vs Player", bg="white", command=lambda: controller.show_frame("multiplayer")).pack(fill="both", expand=True, side="right")

class singleplayer (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        label = tk.Label(self, text="Playing Computer", font=TITLE_FONT, bg="white").grid(row=0, column=0, columnspan=3)
        self._board()
        button1 = tk.Button(self, text="Menu", bg="white", command=lambda: controller.show_frame("menu")).grid(row=2, column=0)
        button2 = tk.Button(self, text="Reset", bg="white", command=self.reset).grid(row=2, column=1)

    def reset (self):
        self.board.delete("all")
        self.board.unbind("<ButtonPress-1>")
        self.j=True
        self._board()

    def _board(self):
        self.board = tk.Canvas(self, width=300, height=300)
        self.board.bind("<ButtonPress-1>")
        self.board.grid(row=1, column=0, columnspan=2)
        self.board.create_rectangle(0,0,300,300, outline="black", fill="white")
        self.board.create_rectangle(100,300,200,0, outline="black")
        self.board.create_rectangle(0,100,300,200, outline="black")
        self.location=[[0,0,0],[0,0,0],[0,0,0]]
        self.i=0
        self.j=False

#player vs player
class multiplayer (tk.Frame):


#creats a frame and initialize it.
    def __init__(self, parent, controller):
        frame=tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        label = tk.Label(self, text="Playing vs Player", font=TITLE_FONT, bg="white", fg="black").grid(row=0, column=0, columnspan=3)
        self.canvas()
        button = tk.Button(self, text="New Game", bg="white", fg="black", command=self.reset).grid(row=3, column=0)
        button = tk.Button(self, text="Menu", bg="white", fg="black", command=lambda: controller.show_frame("menu")).grid(row=3, column=1)

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
        self.board.create_rectangle(0,0,300,300, outline="black", fill="white")
        self.board.create_rectangle(100,300,200,0, outline="black")
        self.board.create_rectangle(0,100,300,200, outline="black")
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
                            self.board.create_oval( X+25, Y+25, X-25, Y-25, width=8, outline="black")
                            self.location[Y1][X1]+=1
                            self.i+=1
                        else:
                            X=(2*k+100)/2
                            Y=(2*j+100)/2
                            X1=int(k/100)
                            Y1=int(j/100)
                            #creats the X on the board
                            self.board.create_line( X+20, Y+20, X-20, Y-20, width=8, fill="black")
                            self.board.create_line( X-20, Y+20, X+20, Y-20, width=8, fill="black")
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

if __name__ == "__main__":
    app = tictactoe_game()
    app.title("Tic-Tac-Toe")
