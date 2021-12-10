"""
File: stockMarket_main.py
Project: Stock Market Game
Date: 21 Nov 2021
Author(s): Arnika
"""

import random


class StockMarket:
    def __init__(self, stock, pastEvents, currentEvents, futureEventPool):
        self.stock = stock
        self.pastEvents = pastEvents
        self.currentEvents = currentEvents
        self.futureEventPool = futureEventPool

    def updateStocks(self):
        stockChanges = {}
        stocks = {}
        marketChange = float(random.randint(-2, 6))/100
        for stock in stocks: # Change Here
            stockChanges[stock.category] = float(random.randint(-1, 5))/100
            stockChanges[stock.name] = 0
        for event in self.currentEvents:
            stockChanges[event.category] *= 10000 * event.effect

        for stock in stocks: # Change Here
            stock.updateStock(marketChange, stockChanges[stock.category], 0) # Maybe change this later?

    def updateEvents(self):
        self.pastEvents.append(self.currentEvents)
        self.currentEvents.clear()
        tempEvents = random.choices(self.futureEventPool, k=3)
        for tempEvents in self.futureEventPool:
            tempEvents.clear()
        self.currentEvents.append(tempEvents)




