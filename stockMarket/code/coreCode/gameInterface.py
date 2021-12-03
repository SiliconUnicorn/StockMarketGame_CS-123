"""
File: gameInterface.py
Project: Stock Market Game
Date: 8 Nov 2021
Author: Sarah
"""

import tkinter as tk

class GameGUI:
    def __init__(self): # consttruter to create instance of the class
        self.rootWin = tk.Tk()
        self.rootWin.config(background= "white")
        self.testButton = tk.Button(self.rootWin)
        self.testButton.grid(row=1, column=3)
        self.testButton["command"] = self.testButtonResponse()
        self.testButton["bg"] = "cyan"

        myCanvas = tk.Canvas(self.rootWin)
        myCanvas["width"] = 200
        myCanvas["height"] = 30
        myCanvas["bg"] = "white"
        myCanvas["bd"] = 5
        #myCanvas["relief"] = tk.SUNKEN
        myCanvas.grid()

        t1 = myCanvas.create_text(0, 0, text="Hello, players " + " Welcome to the Stock Market game",
                              fill="darkblue", anchor=tk.NW)

    def run(self):
        self.rootWin.mainloop()


    def testButtonResponse(self):
        self.testButton["text"] = "start"



if __name__ == "__main__":
    myGUI = GameGUI()
    myGUI.run()