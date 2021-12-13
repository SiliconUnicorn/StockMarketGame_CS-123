"""
Names: Arnika Abeysekera, Micah Hansonbrook, Sarah Ali, Tina Chen
Course: COMP123-01
Instructor: Lauren Milne
Description: This file contains the Stock Market class. This represents the stock market as a whole,
and it also manages events.
Testing: Testing is performed at the bottom of the file.
"""


import random
from stockMarket.code.stockMarket.getAllStocks import *
from stockMarket.code.events.getEvents import *

class StockMarket:
    def __init__(self):
        """Initializes the Stock Market with event pools and stocks."""
        self.stocks = getStockList()
        self.pastEvents = []
        self.currentEvents = []
        self.futureEventPool = getAllEvents()

    def updateStocks(self):
        """Decides whether the stock will change according to the events in the game, and makes the corresponding change to value."""
        stockChanges = {}
        stocks = {}
        marketChange = float(random.randint(-2, 6))/100
        for stock in stocks:
            stockChanges[stock.category] = float(random.randint(-1, 5))/100
            stockChanges[stock.name] = 0

        for stock in stocks:
            stock.updateStock(marketChange, stockChanges[stock.category], 0)

    def updateEvents(self):
        """Randomly chooses three events to be displayed on the game interface."""
        self.pastEvents.append(self.currentEvents)
        self.currentEvents = []
        self.currentEvents = random.choices(self.futureEventPool, k=1)
        self.currentEvents.append(self.currentEvents[0].generateDynamicEvent())
        self.currentEvents.append(self.currentEvents[0].generateDynamicEvent())

if __name__ == "__main__":
    '''Tests the Stock Market class'''
    print("Testing Stock Market Class")
    market = StockMarket()

    print("Test Successful")
