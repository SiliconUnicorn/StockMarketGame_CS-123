'''
File: portfolio.py
Project: Stock Market Game
Date: 21 Nov 2021
Author(s): Micah Hansonbrook
'''

from stockMarket.code.stockMarket.stock import *

class Portfolio:
    def __init__(self, stocks):
        self.userCash = 100.00
        self.playerID = "Human Player"
        self.ownedStocks = {}

        for stock in stocks:
            self.ownedStocks[0:Stock(stock['Real Name'], stock['Initial Price per Share'], stock['category'], {})]

    def getCashValue(self):
        '''Calculates the cash value of the portfolio'''
        return self.userCash