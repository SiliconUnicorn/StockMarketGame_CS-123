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
        self.rootWin.title("Stock Market Game")
        self.portfolio = Portfolio()
        self.market = StockMarket()

        self.market.updateEvents()

        self.currentTurnNumber = 0

        self.stockChangeValue = 1

        self.stockChangePlusButton = tk.Button(self.rootWin, command=self.increaseButtonClicked, text="+")
        self.stockChangePlusButton.grid(row=2, column=6)

        self.stockChangeMinusButton = tk.Button(self.rootWin, command=self.decreaseButtonClicked, text='-')
        self.stockChangeMinusButton.grid(row=2, column=8)

        self.changeLabel = tk.Label(self.rootWin, text=1)
        self.changeLabel.grid(row=2,column=7)

        self.eventText = sTk.ScrolledText(self.rootWin, font="Helvetica", wrap=tk.WORD)
        self.eventText.grid(row=1, column=9)
        self.eventText.insert(1.0, "Current Year: " + str(self.getCurrentYear()) + '\t\tUser Cash: $' + str(
            self.portfolio.userCash) + '\t\tUser Net Worth: $' + str(self.portfolio.getCashValue(self.market.stocks)) +
                              '\n\n' + self.market.currentEvents[0].name + ": " + self.market.currentEvents[
                                  0].detail + "\n\n" +
                              self.market.currentEvents[1].name + ": " + self.market.currentEvents[1].detail + "\n\n" +
                              self.market.currentEvents[2].name + ": " + self.market.currentEvents[2].detail)

        self.nextTurnButton = tk.Button(self.rootWin, command=self.nextTurn, text='Next Turn >')
        self.nextTurnButton.grid(row=0, column=0)

        corpLabel = tk.Label(self.rootWin, text='Company Name')
        corpLabel.grid(row=2, column=1)

        sharesLabel = tk.Label(self.rootWin, text='Shares Held')
        sharesLabel.grid(row=2, column=2)

        shareValLabel = tk.Label(self.rootWin, text='Share Value')
        shareValLabel.grid(row=2, column=3)

        userSharesLabel = tk.Label(self.rootWin, text='Value of User Shares')
        userSharesLabel.grid(row=2, column=4)

        self.performStockInterfaceLayout()

        helpButton = tk.Button(self.rootWin, command=partial(self.open_HelpInterface))
        helpButton["text"] = "How To"
        helpButton["font"] = "Arial 10"
        helpButton["bg"] = "#b8e6fa"
        helpButton["fg"] = "black"
        helpButton.grid(row=0, column=10, padx=5, pady=0)

    def increaseButtonClicked(self):
        '''Called when the increase button is clicked'''
        self.stockChangeValue += 1
        self.changeLabel['text'] = str(self.stockChangeValue)

    def decreaseButtonClicked(self):
        '''Called when the increase button is clicked'''
        if self.stockChangeValue > 0:
            self.stockChangeValue -= 1
        self.changeLabel['text'] = str(self.stockChangeValue)

    def buyResponse(self, stock_name, numSharesLabl, shareValueLabl, totalValLabl):
        """ makes it so when you click the buy button the number of shares goes up"""
        if self.portfolio.confirmUserPurchasable(self.market.getCurrentDictionary()[stock_name], self.stockChangeValue):
            self.portfolio.changeStock(self.market.getCurrentDictionary()[stock_name], self.stockChangeValue)
            numSharesLabl["text"] = str(self.portfolio.ownedStocks[stock_name])
            totalValLabl["text"] = str(float(int((self.portfolio.ownedStocks[stock_name] * self.market.getCurrentDictionary()[stock_name].currentValue)*100))/100)
            self.updateEventText()


    def sellResponse(self, stock_name, numSharesLabl, shareValueLabl, totalValLabl):
        """makes it so when you click sell the number of shares goes down but doesn't allow it to go past zero """
        if self.portfolio.confirmUserPurchasable(self.market.getCurrentDictionary()[stock_name], self.stockChangeValue*-1):
            self.portfolio.changeStock(self.market.getCurrentDictionary()[stock_name], -1*self.stockChangeValue)
            numSharesLabl["text"] = str(self.portfolio.ownedStocks[stock_name])
            totalValLabl["text"] = str(float(int((self.portfolio.ownedStocks[stock_name] * self.market.getCurrentDictionary()[stock_name].currentValue)*100))/100)
            self.updateEventText()

    def getCurrentYear(self):
        '''Returns the current year in the game'''
        return self.currentTurnNumber + 1990

    def performStockInterfaceLayout(self):
        '''Performs essential interface layout tasks for the stock items'''
        row = 3

        for i in self.portfolio.ownedStocks:
            myLabel = tk.Label(self.rootWin, text=i)
            myLabel.grid(row=row, column=1, padx=2, pady=2)
            numStocksLabel = tk.Label(self.rootWin, text=self.portfolio.ownedStocks[i])
            numStocksLabel.grid(row=row, column=2, padx=10, pady=2)
            stockValLabel = tk.Label(self.rootWin, text=self.market.getCurrentDictionary()[i].currentValue)
            stockValLabel.grid(row=row, column=3, padx=2, pady=2)
            totalStock = float(
                int((self.portfolio.getStockValue(self.market.getCurrentDictionary()[i])) * 100)) / 100
            totalValueLabel = tk.Label(self.rootWin, text=totalStock)
            totalValueLabel.grid(row=row, column=4, padx=2, pady=2)

            buyButton = tk.Button(self.rootWin,
                                  command=partial(self.buyResponse, i, numStocksLabel, stockValLabel, totalValueLabel))
            buyButton["text"] = "buy"
            buyButton["font"] = "Arial 12"
            buyButton["bg"] = "#aafaa1"
            buyButton["fg"] = "black"
            buyButton.grid(row=row, column=6)

            sellButton = tk.Button(self.rootWin, command=partial(self.sellResponse, i, numStocksLabel, stockValLabel,
                                                                 totalValueLabel))
            sellButton["text"] = "sell"
            sellButton["font"] = "Arial 12"
            sellButton["bg"] = "#e8b6f9"
            sellButton["fg"] = "black"
            sellButton.grid(row=row, column=8)

            row += 1

    def updateEventText(self):
        '''Updates the event text display, to reflect new information'''
        self.eventText = sTk.ScrolledText(self.rootWin, font="Helvetica", wrap=tk.WORD)
        self.eventText.grid(row=1, column=9)
        self.eventText.insert(1.0, "Current Year: " + str(self.getCurrentYear()) + '\t\tUser Cash: $' + str(
            self.portfolio.userCash) + '\t\tUser Net Worth: $' + str(self.portfolio.getCashValue(self.market.stocks)) +
                              '\n\n' + self.market.currentEvents[0].name + ": " + self.market.currentEvents[
                                  0].detail + "\n\n" +
                              self.market.currentEvents[1].name + ": " + self.market.currentEvents[1].detail + "\n\n" +
                              self.market.currentEvents[2].name + ": " + self.market.currentEvents[2].detail)

        self.nextTurnButton = tk.Button(self.rootWin, command=self.nextTurn, text='Next Turn >')
        self.nextTurnButton.grid(row=0, column=0)

    def nextTurn(self):
        '''Begins the next turn of the game.'''
        self.currentTurnNumber += 1

        self.market.updateStocks()
        self.market.updateEvents()

        self.performStockInterfaceLayout()

        self.updateEventText()

        if self.currentTurnNumber >= 30:
            if self.portfolio.getCashValue(self.market.stocks) >= 10000:
                self.eventText = sTk.ScrolledText(self.rootWin, font="Helvetica", wrap=tk.WORD)
                self.eventText.grid(row=1, column=8)
                self.eventText.insert(1.0, "You have successfully won the game! Congragulations!")
            else:
                self.eventText = sTk.ScrolledText(self.rootWin, font="Helvetica", wrap=tk.WORD)
                self.eventText.grid(row=1, column=8)
                self.eventText.insert(1.0, "You have lost the game. Better luck next time."
                                           "")

    def open_HelpInterface(self):
        """ opens the help interface/page when "Need Help?" is clicked """
        interface = HelpInterface()
        interface.run()



    def run(self):
        self.rootWin.mainloop()

