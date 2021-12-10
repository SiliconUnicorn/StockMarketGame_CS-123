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
from stockMarket.code.stockMarket.classStockMarket import *
from stockMarket.code.coreCode.helpInterface import HelpInterface
from functools import partial

class GameGUI:
    def __init__(self): # construter to create instance of the class
        self.rootWin = tk.Tk()
        stocks = getAllStocks()
        events = getAllEvents()
        portfolio = Portfolio()
        self.market = StockMarket(getAllStocks(), [], [], getAllEvents())

        self.market.updateEvents()

        self.currentTurnNumber = 0

        self.eventText = tk.Label(self.rootWin, text="None")
        self.eventText.grid(row=3, column=8)

        self.button1 = tk.Button(self.rootWin, command=partial(self.eventResponse, self.market.currentEvents[0]), text=self.market.currentEvents[0].name)
        self.button1.grid(row=0, column=8)

        self.button2 = tk.Button(self.rootWin, command=partial(self.eventResponse, self.market.currentEvents[1]), text=self.market.currentEvents[1].name)
        self.button2.grid(row=1, column=8)

        self.button3 = tk.Button(self.rootWin, command=partial(self.eventResponse, self.market.currentEvents[2]), text=self.market.currentEvents[2].name)
        self.button3.grid(row=2, column=8)

        self.nextTurnButton = tk.Button(self.rootWin, command=self.nextTurn, text='Next Turn >')
        self.nextTurnButton.grid(row=0, column=0)

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

        helpButton = tk.Button(self.rootWin, command=partial(self.open_HelpInterface))
        helpButton["text"] = "Need Help?"
        helpButton["font"] = "Arial 10"
        helpButton["bg"] = "#b8e6fa"
        helpButton["fg"] = "black"
        helpButton.grid(row=0, column=10, padx=5, pady=0)

    def buyResponse(self, port, stock_name, numSharesLabl, shareValueLabl, totalValLabl):
        port.ownedStocks[stock_name] += 1
        numSharesLabl["text"] = str(port.ownedStocks[stock_name])
        totalValLabl["text"] =  str(int( numSharesLabl["text"]) * float( shareValueLabl["text"]))


    def sellResponse(self, port, stock_name, numSharesLabl, shareValueLabl, totalValLabl):
        if port.ownedStocks[stock_name] > 0:
            port.ownedStocks[stock_name] -= 1
            numSharesLabl["text"] = str(port.ownedStocks[stock_name])
            totalValLabl["text"] = str(int(numSharesLabl["text"]) * float(shareValueLabl["text"]))

    def eventResponse(self, event):
        '''Responds when an event button is pressed by the user'''
        self.eventText['text'] = event.detail

    def getCurrentYear(self):
        '''Returns the current year in the game'''
        return self.currentTurnNumber + 1990

    def nextTurn(self):
        '''Begins the next turn of the game.'''
        self.market.updateEvents()
        self.market.updateStocks()
        self.button1['text'] = self.market.currentEvents[0].name
        self.button1['command'] = partial(self.eventResponse, self.market.currentEvents[0])
        self.button2['text'] = self.market.currentEvents[1].name
        self.button2['command'] = partial(self.eventResponse, self.market.currentEvents[1])
        self.button3['text'] = self.market.currentEvents[2].name
        self.button2['command'] = partial(self.eventResponse, self.market.currentEvents[2])

    def open_HelpInterface(self):
        """ opens the help interface when "Need Help?" is clicked """
        interface = HelpInterface()
        interface.run()
        HelpInterface.geometry("750x250")
        HelpInterface.title("New Window")

#  if we have a function that handles events for the quarter, it will:
    # choose a random event from the list
    # remove that event from the list
    # show a pop up window that tells user the details of the event
    # update the internal information and corresponding labels accordingly, just like we did in sell/buy response functions



    def run(self):
        self.rootWin.mainloop()


    def testButtonResponse(self):
        pass




if __name__ == "__main__":
    myGUI = GameGUI()
    print("b4 calling run")
    myGUI.run()
    print("after calling run")