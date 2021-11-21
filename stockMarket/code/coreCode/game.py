'''
File: game.py
Project: Stock Market Game
Date: 5 Nov 2021
Author(s): Micah Hansonbrook
'''

from stockMarket.code.stockMarket.portfolio import *

class Game:
    def __init__(self):
        self.currentTurnNumber = 0
        # self.market = StockMarket
        self.userPortfolio = Portfolio()
        self.maxTurnNumber = 30

    def userWins(self):
        '''Lets the user know they have won.'''
        print("You have won!")

    def userLoses(self):
        '''Lets the user know they have lost.'''
        print("You have lost!")