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
        self.scroll.insert(1.0, """\tIn real life, the stock market allows individuals to trade shares of large corporations. Every quarter, shareholders either receive a portion of corporate profits, or pay a portion of corporate losses.""")

        self.button = tk.Button(self.rootWin)
        self.button.grid(column=1, row=3)
        self.button['text'] = 'Close'
        self.button['command'] = self.closeWindow

    def run(self):
        '''
        Runs the interface's main loop
        '''
        self.rootWin.mainloop()

    def closeWindow(self):
        '''
        Closes the window.
        '''
        self.rootWin.destroy()

if __name__ == "__main__":
    interface = HelpInterface()
    interface.run()