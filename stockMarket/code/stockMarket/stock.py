"""
File: classStock.py
Project: Stock Market Game
Date: 21 Nov 2021
Author(s): Arnika Abeysekera
"""

import random


class Stock:
    def __init__(self, name, currentValue, category, valueHistory):
        self.name = name
        self.currentValue = currentValue
        self.category = category
        self.valueHistory = valueHistory

    def updateStock(self, marketValue, categoryValue, additionalValue):
        marketChange = marketValue + categoryValue + additionalValue + random.Random(50)
        self.currentValue = self.currentValue + marketChange
        self.valueHistory[self.name] = self.currentValue
