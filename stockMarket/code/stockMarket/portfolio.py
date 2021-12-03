'''
File: portfolio.py
Project: Stock Market Game
Date: 21 Nov 2021
Author(s): Micah Hansonbrook
'''

from stockMarket.code.stockMarket.stock import *
from stockMarket.code.stockMarket.getAllStocks import *

class Portfolio:
    def __init__(self):
        self.userCash = 100.00
        self.playerID = "Human Player"
        self.ownedStocks = {}
        for stock in getAllStocks():
            self.ownedStocks[stock.name] = 0

    def getCashValue(self, currentStocks):
        '''Calculates the cash value of the portfolio'''
        accumulator = 0
        for stock in currentStocks:
            accumulator += float(stock.currentValue) * float(self.ownedStocks[stock.name])
        return self.userCash + accumulator