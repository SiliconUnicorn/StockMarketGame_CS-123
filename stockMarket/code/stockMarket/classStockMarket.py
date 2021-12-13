"""
File: stockMarket_main.py
Project: Stock Market Game
Date: 21 Nov 2021
Author(s): Arnika
"""

import random
from stockMarket.code.stockMarket.getAllStocks import *
from stockMarket.code.events.getEvents import *

class StockMarket:
    def __init__(self, stocks, pastEvents, currentEvents, futureEventPool):
        self.stocks = stocks
        self.pastEvents = pastEvents
        self.currentEvents = currentEvents
        self.futureEventPool = futureEventPool

    def updateStocks(self):
        stockChanges = {}
        stocks = {}
        marketChange = float(random.randint(-2, 6))/100
        for stock in getStockList(): # Change Here
            stockChanges[stock.category] = float(random.randint(-1, 5))/100
            stockChanges[stock.name] = 0
        # for event in self.currentEvents:
        #     stockChanges[event.category] *= 10000 * event.effect

        for stock in getStockList(): # Change Here
            stock.updateStock(marketChange, stockChanges[stock.category], 0) # Maybe change this later?

    def updateEvents(self):
        self.pastEvents.append(self.currentEvents)
        self.currentEvents = []
        self.currentEvents = random.choices(self.futureEventPool, k=1)
        self.currentEvents.append(self.currentEvents[0].generateDynamicEvent())
        self.currentEvents.append(self.currentEvents[0].generateDynamicEvent())


