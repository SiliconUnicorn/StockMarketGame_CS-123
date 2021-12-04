"""
File: helpInterface.py
Project: Stock Market Game
Date: 3 Dec 2021
Author: Micah Hansonbrook
"""

import tkinter as tk
import tkinter.scrolledtext as sTk

class HelpInterface:
    def __init__(self):
        '''
        Instantiates an instance of the HelpInterface class
        '''
        self.rootWin = tk.Tk()
        self.rootWin.config(background='light blue')
        self.rootWin.title("Game Info")

        self.mainText = tk.Label(self.rootWin)
        self.mainText.grid(column=1, row=1)
        self.mainText['text'] = "How the Stock Market Works"

        self.scroll = sTk.ScrolledText(self.rootWin)
        self.scroll.grid(column=1, row=2)
        self.scroll.insert(1.0, "This is some really fancy placeholder text right here!")

    def run(self):
        '''
        Runs the interface's main loop
        '''
        self.rootWin.mainloop()

if __name__ == "__main__":
    interface = HelpInterface()
    interface.run()