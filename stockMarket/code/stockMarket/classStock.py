"""
Names: Arnika Abeysekera, Micah Hansonbrook, Sarah Ali, Tina Chen
Course: COMP123-01
Instructor: Lauren Milne
Description: This file contains the Stock class. 
"""

import random

class Stock:
    def __init__(self, name, currentValue, category):
        '''Initializes a stock instance'''
        self.name = name
        self.currentValue = float(currentValue)
        self.category = category
        self.valueHistory = []

    def updateStock(self, marketValue, categoryValue, additionalValue):
        '''Performs changes neccessary to update a stock'''
        marketChange = marketValue + categoryValue + additionalValue + float(random.randint(0,2))/100
        self.valueHistory.append(self.currentValue)
        self.currentValue = self.currentValue + marketChange
