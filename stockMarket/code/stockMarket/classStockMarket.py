"""
Names: Arnika Abeysekera, Micah Hansonbrook, Sarah Ali, Tina Chen
Course: COMP123-01
Instructor: Lauren Milne
Description: This file contains the Stock Market class. 
"""


import random
from stockMarket.code.stockMarket.getAllStocks import *
from stockMarket.code.events.getEvents import *

class StockMarket:
    def __init__(self, stocks, pastEvents, currentEvents, futureEventPool):
        """Initializes the Stock Market with event pools."""
        self.stocks = stocks
        self.pastEvents = pastEvents
        self.currentEvents = currentEvents
        self.futureEventPool = futureEventPool

    def updateStocks(self):
        """Decides whether the stock will change according to the events in the game, and makes the corresponding change to value."""
        stockChanges = {}
        stocks = {}
        marketChange = float(random.randint(-2, 6))/100
        for stock in getStockList():  
            stockChanges[stock.category] = float(random.randint(-1, 5))/100
            stockChanges[stock.name] = 0

        for stock in getStockList():  
            stock.updateStock(marketChange, stockChanges[stock.category], 0)

    def updateEvents(self):
        """Randomly chooses three events to be displayed on the game interface."""
        self.pastEvents.append(self.currentEvents)
        self.currentEvents = []
        self.currentEvents = random.choices(self.futureEventPool, k=1)
        self.currentEvents.append(self.currentEvents[0].generateDynamicEvent())
        self.currentEvents.append(self.currentEvents[0].generateDynamicEvent())


