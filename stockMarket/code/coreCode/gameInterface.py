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

class GameGUI:
    def __init__(self): # construter to create instance of the class
        self.rootWin = tk.Tk()
        stocks = getAllStocks()
        events = getAllEvents()
        portfolio = Portfolio()

        button1 = tk.Button(self.rootWin, text=events[0].generateDynamicEvent().name)
        button1.grid(row=0, column=2)

        button2 = tk.Button(self.rootWin, text=events[0].name)
        button2.grid(row=0, column=3)

        button3 = tk.Button(self.rootWin, text=events[0].generateDynamicEvent().name)
        button3.grid(row=0, column=4)

        row = 2
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
            #totalStock.

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

            row += 1

    def buyResponse(self, port, stock_name, numSharesLabl, shareValueLabl, totalValLabl):
        port.ownedStocks[stock_name] += 1
        numSharesLabl["text"] = str(port.ownedStocks[stock_name])
        totalValLabl["text"] =  str(int( numSharesLabl["text"]) * float( shareValueLabl["text"]))


    def sellResponse(self, port, stock_name, numSharesLabl, shareValueLabl, totalValLabl):
        if port.ownedStocks[stock_name] > 0:
            port.ownedStocks[stock_name] -= 1
            numSharesLabl["text"] = str(port.ownedStocks[stock_name])
            totalValLabl["text"] = str(int(numSharesLabl["text"]) * float(shareValueLabl["text"]))

#  if we have a function that handles events for the quarter, it will:
    # choose a random event from the list
    # remove that event from the list
    # show a pop up window that tells user the details of the event
    # update the internal information and corresponding labels accordingly, just like we did in sell/buy response functions

    #this function will need to be passed:
        # the events
        # the portfolio
        # the stocks
        # a list of all the labels (or just access them thru self.rootwin.children )



    def run(self):
        self.rootWin.mainloop()


    def testButtonResponse(self):
        pass




if __name__ == "__main__":
    myGUI = GameGUI()
    print("b4 calling run")
    myGUI.run()
    print("after calling run")