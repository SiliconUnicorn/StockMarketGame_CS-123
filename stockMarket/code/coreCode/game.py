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

    def updateTurn(self):
        '''Updates the game to begin a new turn.'''
        self.currentTurnNumber += 1
        if self.currentTurnNumber >= self.maxTurnNumber:
            if self.userPortfolio.userCash > 1000.00:
                self.userWins()
            else:
                self.userLoses()

    def userWins(self):
        '''Lets the user know they have won.'''
        print("You have won!")

    def userLoses(self):
        '''Lets the user know they have lost.'''
        print("You have lost!")

    def play(self):
        '''Play the game'''
        for turn in range(self.maxTurnNumber):
            self.updateTurn()