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
    def __init__(self): # consttruter to create instance of the class
        self.rootWin = tk.Tk()
        stocks = getAllStocks()
        events = getAllEvents()
        portfolio = Portfolio()

        row = 0
        for i in portfolio.ownedStocks:
            myLabel = tk.Label(self.rootWin, text = i)
            myLabel.grid(row = row, column = 1, padx=2, pady=2)
            numStocksLabel = tk.Label(self.rootWin, text = portfolio.ownedStocks[i])
            numStocksLabel.grid(row = row, column = 2, padx=2, pady=2)
            # print(portfolio.getStockValue(i))
            row = row + 1










    def run(self):
        self.rootWin.mainloop()


    def testButtonResponse(self):
        self.testButton["text"] = "start"



if __name__ == "__main__":
    myGUI = GameGUI()
    myGUI.run()