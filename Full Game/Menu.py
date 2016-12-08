import tkinter as tk
import AI

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
        for F in (menu, roll_credits):# input frame name here
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
        label = tk.Label(self, bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Tic-Tac-Toe", font=TITLE_FONT, bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, bg="black", fg="white").pack(fill="both", expand=True)
        button1 = tk.Button(self, text="Single Player Mode", bg="black", fg="white").pack(fill="both", expand=True)
        button2 = tk.Button(self, text="Multi-Player Mode", bg="black", fg="white").pack(fill="both", expand=True)
        button3 = tk.Button(self, text="Online Multi-Player Mode", bg="black", fg="white").pack(fill="both", expand=True)
        button4 = tk.Button(self, text="Credits", bg="black", fg="white", command=lambda: controller.show_frame("roll_credits")).pack(fill="both", expand=True)
        button5 = tk.Button(self, text="Exit Game", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, bg="black", fg="white").pack(fill="both", expand=True)

class roll_credits (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        label = tk.Label(self, bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Credits", font=TITLE_FONT, bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Created by", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Kyle Speke + Taylor Southorn", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Harry Hudson + Ayyub Lindroos", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, text="Faizan Ahmed", bg="black", fg="white").pack(fill="both", expand=True)
        label = tk.Label(self, bg="black", fg="white").pack(fill="both", expand=True)
        button1 = tk.Button(self, text="Return", bg="black", fg="white", command=lambda: controller.show_frame("menu")).pack(fill="both", expand=True)

if __name__ == "__main__":
    app = tictactoe_game()
    app.title("Tic-Tac-Toe")
