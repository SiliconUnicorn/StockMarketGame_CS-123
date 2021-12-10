"""
File: gameInterface.py
Project: Stock Market Game
Date: 8 Nov 2021
Author: Sarah
"""

import tkinter as tk

import stockMarket.code.stockMarket.classStock
from stockMarket.code.events.getEvents import getAllEvents
from stockMarket.code.stockMarket.getAllStocks import getAllStocks
from stockMarket.code.stockMarket.portfolio import Portfolio
from functools import partial
from stockMarket.code.coreCode.helpInterface import HelpInterface





class GameGUI:
    def __init__(self): # construter to create instance of the class
        self.helpResponse = None
        self.rootWin = tk.Tk()
        stocks = getAllStocks()
        events = getAllEvents()
        portfolio = Portfolio()



        row = 0
        for i in portfolio.ownedStocks:
            myLabel = tk.Label(self.rootWin, text = i)
            myLabel.grid(row = row, column = 1, padx=2, pady=2)
            numStocksLabel = tk.Label(self.rootWin, text =portfolio.ownedStocks[i])
            numStocksLabel.grid(row = row, column = 2, padx=10, pady=2)
            stockValLabel = tk.Label(self.rootWin, text = portfolio.getStockValue(stocks[i]))
            stockValLabel.grid(row = row, column = 3, padx=2, pady=2)
            totalStock =  portfolio.ownedStocks[i] * portfolio.getStockValue(stocks[i])
            totalValueLabel = tk.Label(self.rootWin, text=totalStock )
            totalValueLabel.grid(row=row, column=4, padx=2, pady=2)


            buyButton = tk.Button(self.rootWin, command = partial(self.buyResponse, portfolio, i, numStocksLabel, stockValLabel, totalValueLabel))
            buyButton["text"] = "buy"
            buyButton["font"] = "Arial 12"
            buyButton["bg"] = "#aafaa1"
            buyButton["fg"] = "black"
            buyButton.grid(row=row, column=6)

            sellButton = tk.Button(self.rootWin, command = partial(self.sellResponse, portfolio, i, numStocksLabel, stockValLabel, totalValueLabel))
            sellButton["text"] = "sell"
            sellButton["font"] = "Arial 12"
            sellButton["bg"] = "#e8b6f9"
            sellButton["fg"] = "black"
            sellButton.grid(row=row, column=7)

            helpButton = tk.Button(self.rootWin, command=partial(self.open_HelpInterface))
            helpButton["text"] = "Need Help?"
            helpButton["font"] = "Arial 10"
            helpButton["bg"] = "#b8e6fa"
            helpButton["fg"] = "black"
            helpButton.grid(row=0, column=10, padx=5, pady=0)


            row += 1

    def buyResponse(self, port, stock_name, numSharesLabl, shareValueLabl, totalValLabl):
        """ makes it so when you click the buy button the number of shares goes up"""
        port.ownedStocks[stock_name] += 1
        numSharesLabl["text"] = str(port.ownedStocks[stock_name])
        totalValLabl["text"] =  str(int( numSharesLabl["text"]) * float( shareValueLabl["text"]))


    def sellResponse(self, port, stock_name, numSharesLabl, shareValueLabl, totalValLabl):
        """makes it so when you click sell the number of shares goes down but doesn't allow it to go past zero """
        if port.ownedStocks[stock_name] > 0:
            port.ownedStocks[stock_name] -= 1
            numSharesLabl["text"] = str(port.ownedStocks[stock_name])
            totalValLabl["text"] = str(int(numSharesLabl["text"]) * float(shareValueLabl["text"]))


    def open_HelpInterface(self):
        """ opens the help interface when "Need Help?" is clicked """
        interface = HelpInterface()
        interface.run()
        HelpInterface.geometry("750x250")
        HelpInterface.title("New Window")







    def run(self):
        self.rootWin.mainloop()







if __name__ == "__main__":
    myGUI = GameGUI()
    myGUI.run()
