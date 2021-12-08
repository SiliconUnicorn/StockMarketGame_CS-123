"""
File: gameInterface.py
Project: Stock Market Game
Date: 8 Nov 2021
Author: Sarah
"""

import tkinter as tk

from stockMarket.code.events.getEvents import getAllEvents
from stockMarket.code.stockMarket.getAllStocks import getAllStocks
from stockMarket.code.stockMarket.portfolio import Portfolio


class GameGUI:
    def __init__(self): # construter to create instance of the class
        self.rootWin = tk.Tk()
        stocks = getAllStocks()
        events = getAllEvents()
        portfolio = Portfolio()

        row = 0
        for i in portfolio.ownedStocks:
            myLabel = tk.Label(self.rootWin, text = i)
            myLabel.grid(row = row, column = 1, padx=2, pady=2)
            numStocksLabel = tk.Label(self.rootWin, text = portfolio.ownedStocks[i])
            numStocksLabel.grid(row = row, column = 2, padx=10, pady=2)

        # change padding from 10 after buttons are fixed
            #print(portfolio.getStockValue(i))
            row += 1


        #
        # buyButton = tk.Button(self.rootWin)
        # buyButton["text"] = "buy"
        # buyButton["font"] = "Arial 12"
        # buyButton["bg"] = "#aafaa1"
        # buyButton["fg"] = "black"
        # buyButton.grid(row=1, column=6)
        #
        # sellButton = tk.Button(self.rootWin)
        # sellButton["text"] = "sell"
        # sellButton["font"] = "Arial 12"
        # sellButton["bg"] = "#e8b6f9"
        # sellButton["fg"] = "black"
        # sellButton.grid(row=1, column=7)












    def run(self):
        self.rootWin.mainloop()


    def testButtonResponse(self):
        pass




if __name__ == "__main__":
    myGUI = GameGUI()
    myGUI.run()