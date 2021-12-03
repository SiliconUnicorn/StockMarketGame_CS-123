"""
File: eventInterface.py
Project: Stock Market Game
Date: 17 Nov 2021
Author: Sarah
"""


import tkinter as tk
from tkinter import ttk

class eventsExample:
    def __init__(self):
        self.rootWin = tk.Tk()
        self.rootWin.title("events example")
        self.rootWin.config(background= "black")


        f2 = tk.Frame(self.rootWin, bg = "black", bd=5,
                      relief=tk.SUNKEN, padx = 10, pady = 10)
        f2.grid(row = 1, column = 2)
        self.frame2Buttons = []
        for i in range(3):
            bName = "Event " + str(i)
            button = ttk.Button(f2, text = bName) # font="Arial 14")
            button.grid(row = 1, column = i, padx=10, pady=10)
            self.frame2Buttons.append(button)
# anchor = tk.nw


    def run(self):
        self.rootWin.mainloop()



if __name__ == "__main__":
    # Main program:
    eventGui = eventsExample()
    eventGui.run()



