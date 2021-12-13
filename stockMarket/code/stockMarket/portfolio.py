"""
Names: Arnika Abeysekera, Micah Hansonbrook, Sarah Ali, Tina Chen
Course: COMP123-01
Instructor: Lauren Milne
Description: This file defines the Portfolio class, which represents the player's stock portfolio.
The portfolio also tracks the users net worth and owned stocks.
Testing: This class was tested using the commented out code below.
"""

from stockMarket.code.stockMarket.getAllStocks import *

class Portfolio:
    def __init__(self):
        self.userCash = 100.00
        self.playerID = "Human Player"
        self.ownedStocks = {}
        stocks = getAllStocks()
        for stock in stocks:
            self.ownedStocks[stocks[stock].name] = 0

    def getCashValue(self, currentStocks):
        '''Calculates the cash value of the portfolio'''
        accumulator = 0
        for stock in currentStocks:
            accumulator += float(stock.currentValue) * float(self.ownedStocks[stock.name])
        return float(int((self.userCash + accumulator)*100))/100

    def getStockValue(self, stock):
        '''Calculates the cash value of the stock in the portfolio'''
        return float(stock.currentValue) * float(self.ownedStocks[stock.name])

    def confirmUserPurchasable(self, stock, shares):
        '''
        Checks to see whether or not a user has enough cash to make a stock purchase, and returns True if it does work
        '''
        return self.userCash > shares * stock.currentValue


    def changeStock(self, stock, shares):
        '''Adjusts the number of stocks owned by this player's portfolio'''
        if self.confirmUserPurchasable(stock, shares):
            name = stock.name
            self.ownedStocks[name] += shares
            self.userCash -= shares * stock.currentValue
            self.userCash = float(int(self.userCash * 100))/100
        else:
            'This should never happen. Confirm that user can purchase stocks before making purchase'
            assert 0 == 1

# if __name__ == "__main__":
    # '''Tests the Portfolio class.'''
    # print("Beginning Portfolio Test")
    # portfolio = Portfolio()
    # testStock = getStockList()[0]
    # assert portfolio.confirmUserPurchasable(testStock, 2) == True
    # portfolio.changeStock(testStock, 2)
    # print(portfolio.ownedStocks)
    # print(portfolio.getStockValue(testStock))
    # print(portfolio.getCashValue([testStock]))
    # print("Portfolio Test Successful")
