"""
Names: Arnika Abeysekera, Micah Hansonbrook, Sarah Ali, Tina Chen
Course: COMP123-01
Instructor: Lauren Milne
Description: This file contains the interface code for our game. All the buttons, calls and labels for our display is below.
Testing: This file was tested by repeatedly running the gameInterface from the main_program.py file.
"""


import tkinter as tk
import tkinter.scrolledtext as sTk
from stockMarket.code.stockMarket.portfolio import Portfolio
from stockMarket.code.stockMarket.classStockMarket import *
from stockMarket.code.coreCode.helpInterface import HelpInterface
from functools import partial

class GameGUI:
    def __init__(self):
        """ displays the event buttons and labels so they user can seek out the stocks """
        """ loop: the list of stocks, the # of stocks, the value of the stocks, total of both(# of stocks * value)
        and help button for user to seek assistant for the game """
        self.helpResponse = None
        self.rootWin = tk.Tk()
        stocks = getAllStocks()
        events = getAllEvents()
        portfolio = Portfolio()
        self.market = StockMarket()

        self.market.updateEvents()

        self.currentTurnNumber = 0

        self.eventText = sTk.ScrolledText(self.rootWin, font="Helvetica", wrap=tk.WORD)
        self.eventText.grid(row=1, column=8)
        self.eventText.insert(1.0, self.market.currentEvents[0].name + ": " + self.market.currentEvents[0].detail + "\n\n" +
                              self.market.currentEvents[1].name + ": " + self.market.currentEvents[1].detail + "\n\n" +
                              self.market.currentEvents[2].name + ": " + self.market.currentEvents[2].detail)

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
        helpButton["text"] = "How To:"
        helpButton["font"] = "Arial 10"
        helpButton["bg"] = "#b8e6fa"
        helpButton["fg"] = "black"
        helpButton.grid(row=0, column=10, padx=5, pady=0)

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

    def getCurrentYear(self):
        '''Returns the current year in the game'''
        return self.currentTurnNumber + 1990

    def nextTurn(self):
        '''Begins the next turn of the game.'''
        self.market.updateEvents()
        self.market.updateStocks()

        self.eventText = sTk.ScrolledText(self.rootWin, font="Helvetica", wrap=tk.WORD)
        self.eventText.grid(row=1, column=8)
        self.eventText.insert(1.0, self.market.currentEvents[0].name + ": " + self.market.currentEvents[0].detail + "\n\n" +
                              self.market.currentEvents[1].name + ": " + self.market.currentEvents[1].detail + "\n\n" +
                              self.market.currentEvents[2].name + ": " + self.market.currentEvents[2].detail)

    def open_HelpInterface(self):
        """ opens the help interface/page when "Need Help?" is clicked """
        interface = HelpInterface()
        interface.run()



    def run(self):
        self.rootWin.mainloop()

