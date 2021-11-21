'''
File: portfolio.py
Project: Stock Market Game
Date: 21 Nov 2021
Author(s): Micah Hansonbrook
'''

class Portfolio:
    def __init__(self):
        self.userCash = 100.00
        self.playerID = "Human Player"
        # self.ownedStocks = {100: Stock("AAPL")} (Uncomment once stock class exists.

    def getCashValue(self):
        '''Calculates the cash value of the portfolio'''
        return self.userCash