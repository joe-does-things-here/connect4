import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
import random
#todo: get the board array fixed, get scan functin working, modularise?

root = tk.Tk()
root.title("Connect 4")
game = ttk.Frame(root)
splashScreen = ttk.Frame(root)
colour = ["red","yellow"]
nextColour = "red"
global P1Colour,P2Colour #made global for use in functions

X0Ylevel = 0 #used to know the correct Y level to "drop" the counter on the grid
X1Ylevel = 0
X2Ylevel = 0
X3Ylevel = 0
X4Ylevel = 0
X5Ylevel = 0
X6Ylevel = 0

board = ["x","x","x","x","x","x","x",
         "x","x","x","x","x","x","x",
         "x","x","x","x","x","x","x",
         "x","x","x","x","x","x","x",
         "x","x","x","x","x","x","x",
         "x","x","x","x","x","x","x",]
P1name = tk.StringVar()
P2name = tk.StringVar() 
def drawSplashScreen():
    text = ttk.Label(splashScreen,text="Player 1 enter your name: ")
    text.grid(row=1,column=0,sticky="W")
    text1 = ttk.Label(splashScreen,text="Player 2 enter your name: ")
    text1.grid(row=2,column=0,sticky="W")

    textbox = ttk.Entry(splashScreen, textvariable=P1name) 
    textbox.grid(row=1,column=1,sticky="W") 
    textbox1 = ttk.Entry(splashScreen, textvariable=P2name)
    textbox1.grid(row=2,column=1,sticky="W")

    button = ttk.Button(splashScreen, text="Submit and play", command=lambda: play(P1name.get(),P2name.get())) #using lambda so the functions don't run automatically
    button.grid(row=3,column=1,sticky="E") 
    splashScreen.pack()

def play(user,user2):
    if user == "" or user2 =="": 
        messagebox.showerror('Input fields cannot be left blank')
    else:
        login()

def login():
    global P1Colour, P2Colour
    P1Colour =random.choice(colour)
    colour.remove(P1Colour)
    P2Colour = colour
    splashScreen.pack_forget()
    game.pack()

X0Y0 = tk.Canvas(game, bg="gray", height=50, width=50)
X0Y0.grid(row=0, column=0)
X1Y0 = tk.Canvas(game, bg="gray", height=50, width=50)
X1Y0.grid(row=0, column=1)
X2Y0 = tk.Canvas(game, bg="gray", height=50, width=50)
X2Y0.grid(row=0, column=2)
X3Y0 = tk.Canvas(game, bg="gray", height=50, width=50)
X3Y0.grid(row=0, column=3)
X4Y0 = tk.Canvas(game, bg="gray", height=50, width=50)
X4Y0.grid(row=0, column=4)
X5Y0 = tk.Canvas(game, bg="gray", height=50, width=50)
X5Y0.grid(row=0, column=5)
X6Y0 = tk.Canvas(game, bg="gray", height=50, width=50)
X6Y0.grid(row=0, column=6)

X0Y1 = tk.Canvas(game, bg="gray", height=50, width=50)
X0Y1.grid(row=1, column=0)
X1Y1 = tk.Canvas(game, bg="gray", height=50, width=50)
X1Y1.grid(row=1, column=1)
X2Y1 = tk.Canvas(game, bg="gray", height=50, width=50)
X2Y1.grid(row=1, column=2)
X3Y1 = tk.Canvas(game, bg="gray", height=50, width=50)
X3Y1.grid(row=1, column=3)
X4Y1 = tk.Canvas(game, bg="gray", height=50, width=50)
X4Y1.grid(row=1, column=4)
X5Y1 = tk.Canvas(game, bg="gray", height=50, width=50)
X5Y1.grid(row=1, column=5)
X6Y1 = tk.Canvas(game, bg="gray", height=50, width=50)
X6Y1.grid(row=1, column=6)

X0Y2 = tk.Canvas(game, bg="gray", height=50, width=50)
X0Y2.grid(row=2, column=0)
X1Y2 = tk.Canvas(game, bg="gray", height=50, width=50)
X1Y2.grid(row=2, column=1)
X2Y2 = tk.Canvas(game, bg="gray", height=50, width=50)
X2Y2.grid(row=2, column=2)
X3Y2 = tk.Canvas(game, bg="gray", height=50, width=50)
X3Y2.grid(row=2, column=3)
X4Y2 = tk.Canvas(game, bg="gray", height=50, width=50)
X4Y2.grid(row=2, column=4)
X5Y2 = tk.Canvas(game, bg="gray", height=50, width=50)
X5Y2.grid(row=2, column=5)
X6Y2 = tk.Canvas(game, bg="gray", height=50, width=50)
X6Y2.grid(row=2, column=6)

X0Y3 = tk.Canvas(game, bg="gray", height=50, width=50)
X0Y3.grid(row=3, column=0)
X1Y3 = tk.Canvas(game, bg="gray", height=50, width=50)
X1Y3.grid(row=3, column=1)
X2Y3 = tk.Canvas(game, bg="gray", height=50, width=50)
X2Y3.grid(row=3, column=2)
X3Y3 = tk.Canvas(game, bg="gray", height=50, width=50)
X3Y3.grid(row=3, column=3)
X4Y3 = tk.Canvas(game, bg="gray", height=50, width=50)
X4Y3.grid(row=3, column=4)
X5Y3 = tk.Canvas(game, bg="gray", height=50, width=50)
X5Y3.grid(row=3, column=5)
X6Y3 = tk.Canvas(game, bg="gray", height=50, width=50)
X6Y3.grid(row=3, column=6)

X0Y4 = tk.Canvas(game, bg="gray", height=50, width=50)
X0Y4.grid(row=4, column=0)
X1Y4 = tk.Canvas(game, bg="gray", height=50, width=50)
X1Y4.grid(row=4, column=1)
X2Y4 = tk.Canvas(game, bg="gray", height=50, width=50)
X2Y4.grid(row=4, column=2)
X3Y4 = tk.Canvas(game, bg="gray", height=50, width=50)
X3Y4.grid(row=4, column=3)
X4Y4 = tk.Canvas(game, bg="gray", height=50, width=50)
X4Y4.grid(row=4, column=4)
X5Y4 = tk.Canvas(game, bg="gray", height=50, width=50)
X5Y4.grid(row=4, column=5)
X6Y4 = tk.Canvas(game, bg="gray", height=50, width=50)
X6Y4.grid(row=4, column=6)

X0Y5 = tk.Canvas(game, bg="gray", height=50, width=50)
X0Y5.grid(row=5, column=0)
X1Y5 = tk.Canvas(game, bg="gray", height=50, width=50)
X1Y5.grid(row=5, column=1)
X2Y5 = tk.Canvas(game, bg="gray", height=50, width=50)
X2Y5.grid(row=5, column=2)
X3Y5 = tk.Canvas(game, bg="gray", height=50, width=50)
X3Y5.grid(row=5, column=3)
X4Y5 = tk.Canvas(game, bg="gray", height=50, width=50)
X4Y5.grid(row=5, column=4)
X5Y5 = tk.Canvas(game, bg="gray", height=50, width=50)
X5Y5.grid(row=5, column=5)
X6Y5 = tk.Canvas(game, bg="gray", height=50, width=50)
X6Y5.grid(row=5, column=6)

button = ttk.Button(game, text="drop",command=lambda: drop0(X0Ylevel)) #using lambda so the functions don't run automatically
button.grid(row=6,column=0,sticky="W") 
button1 = ttk.Button(game, text="drop",command=lambda: drop1(X1Ylevel)) 
button1.grid(row=6,column=1,sticky="W")
button2 = ttk.Button(game, text="drop",command=lambda: drop2(X2Ylevel)) 
button2.grid(row=6,column=2,sticky="W")
button3 = ttk.Button(game, text="drop",command=lambda: drop3(X3Ylevel)) 
button3.grid(row=6,column=3,sticky="W")
button4 = ttk.Button(game, text="drop",command=lambda: drop4(X4Ylevel)) 
button4.grid(row=6,column=4,sticky="W")
button5 = ttk.Button(game, text="drop",command=lambda: drop5(X5Ylevel)) 
button5.grid(row=6,column=5,sticky="W")
button6 = ttk.Button(game, text="drop",command=lambda: drop5(X6Ylevel)) 
button6.grid(row=6,column=6,sticky="W")
game.pack

def drop0(level):
    global nextColour,X0Ylevel
    if level == 0:
        if nextColour == "red":
            X0Y5.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X0Y5.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X0Ylevel = X0Ylevel+1

    elif level == 1:
        if nextColour == "red":
            X0Y4.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X0Y4.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X0Ylevel = X0Ylevel+1

    elif level == 2:
        if nextColour == "red":
            X0Y3.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X0Y3.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X0Ylevel = X0Ylevel+1
    
    elif level == 3:
        if nextColour == "red":
            X0Y2.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X0Y2.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X0Ylevel = X0Ylevel+1

    elif level == 4:
        if nextColour == "red":
            X0Y1.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X0Y1.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X0Ylevel = X0Ylevel+1

    elif level == 5:
        if nextColour == "red":
            X0Y0.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X0Y0.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X0Ylevel = X0Ylevel+1
    else:
        pass

def drop1(level):
    global nextColour,X1Ylevel
    if level == 0:
        if nextColour == "red":
            X1Y5.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X1Y5.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X1Ylevel = X1Ylevel+1

    elif level == 1:
        if nextColour == "red":
            X1Y4.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X1Y4.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X1Ylevel = X1Ylevel+1

    elif level == 2:
        if nextColour == "red":
            X1Y3.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X1Y3.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X1Ylevel = X1Ylevel+1
    
    elif level == 3:
        if nextColour == "red":
            X1Y2.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X1Y2.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X1Ylevel = X1Ylevel+1

    elif level == 4:
        if nextColour == "red":
            X1Y1.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X1Y1.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X1Ylevel = X1Ylevel+1

    elif level == 5:
        if nextColour == "red":
            X1Y0.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X1Y0.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X1Ylevel = X1Ylevel+1
    else:
        pass

def drop2(level):
    global nextColour,X2Ylevel
    if level == 0:
        if nextColour == "red":
            X2Y5.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X2Y5.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X2Ylevel = X2Ylevel+1

    elif level == 1:
        if nextColour == "red":
            X2Y4.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X2Y4.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X2Ylevel = X2Ylevel+1

    elif level == 2:
        if nextColour == "red":
            X2Y3.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X2Y3.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X2Ylevel = X2Ylevel+1
    
    elif level == 3:
        if nextColour == "red":
            X2Y2.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X2Y2.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X2Ylevel = X2Ylevel+1

    elif level == 4:
        if nextColour == "red":
            X2Y1.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X2Y1.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X2Ylevel = X2Ylevel+1

    elif level == 5:
        if nextColour == "red":
            X2Y0.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X2Y0.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X2Ylevel = X2Ylevel+1
    else:
        pass

def drop3(level): 
    global nextColour,X3Ylevel
    if level == 0:
        if nextColour == "red":
            X3Y5.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X3Y5.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X3Ylevel = X3Ylevel+1

    elif level == 1:
        if nextColour == "red":
            X3Y4.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X3Y4.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X3Ylevel = X3Ylevel+1

    elif level == 2:
        if nextColour == "red":
            X3Y3.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X3Y3.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X3Ylevel = X3Ylevel+1
    
    elif level == 3:
        if nextColour == "red":
            X3Y2.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X3Y2.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X3Ylevel = X3Ylevel+1

    elif level == 4:
        if nextColour == "red":
            X3Y1.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X3Y1.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X3Ylevel = X3Ylevel+1

    elif level == 5:
        if nextColour == "red":
            X3Y0.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X3Y0.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X3Ylevel = X3Ylevel+1
    else:
        pass

def drop4(level):
    global nextColour,X4Ylevel
    if level == 0:
        if nextColour == "red":
            X4Y5.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X4Y5.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X4Ylevel = X4Ylevel+1

    elif level == 1:
        if nextColour == "red":
            X4Y4.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X4Y4.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X4Ylevel = X4Ylevel+1

    elif level == 2:
        if nextColour == "red":
            X4Y3.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X4Y3.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X4Ylevel = X4Ylevel+1
    
    elif level == 3:
        if nextColour == "red":
            X4Y2.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X4Y2.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X4Ylevel = X4Ylevel+1

    elif level == 4:
        if nextColour == "red":
            X4Y1.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X4Y1.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X4Ylevel = X4Ylevel+1

    elif level == 5:
        if nextColour == "red":
            X4Y0.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X4Y0.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X4Ylevel = X4Ylevel+1
    else:
        pass

def drop5(level):
    global nextColour,X5Ylevel
    if level == 0:
        if nextColour == "red":
            X5Y5.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X5Y5.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X5Ylevel = X5Ylevel+1

    elif level == 1:
        if nextColour == "red":
            X5Y4.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X5Y4.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X5Ylevel = X5Ylevel+1

    elif level == 2:
        if nextColour == "red":
            X5Y3.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X5Y3.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X5Ylevel = X5Ylevel+1
    
    elif level == 3:
        if nextColour == "red":
            X5Y2.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X5Y2.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X5Ylevel = X5Ylevel+1

    elif level == 4:
        if nextColour == "red":
            X5Y1.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X5Y1.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X5Ylevel = X5Ylevel+1

    elif level == 5:
        if nextColour == "red":
            X5Y0.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X5Y0.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X5Ylevel = X5Ylevel+1
    else:
        pass

def drop6(level):
    global nextColour,X6Ylevel
    if level == 0:
        if nextColour == "red":
            X6Y5.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X6Y5.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X6Ylevel = X6Ylevel+1

    elif level == 1:
        if nextColour == "red":
            X6Y4.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X6Y4.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X6Ylevel = X6Ylevel+1

    elif level == 2:
        if nextColour == "red":
            X6Y3.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X6Y3.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X6Ylevel = X6Ylevel+1
    
    elif level == 3:
        if nextColour == "red":
            X6Y2.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X6Y2.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X6Ylevel = X6Ylevel+1

    elif level == 4:
        if nextColour == "red":
            X6Y1.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X6Y1.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X6Ylevel = X6Ylevel+1

    elif level == 5:
        if nextColour == "red":
            X6Y0.create_oval(6,6,50,50, fill="red")
            board[35] = "R"
            nextColour = "yellow"
        else:
            X6Y0.create_oval(6,6,50,50, fill="yellow")
            board[35] = "Y"
            nextColour = "red"
        X6Ylevel = X6Ylevel+1
    else:
        pass

def scan():
    print("yeah")

drawSplashScreen()
root.mainloop()