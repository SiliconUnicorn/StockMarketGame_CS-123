"""
Names: Arnika Abeysekera, Micah Hansonbrook, Sarah Ali, Tina Chen
Course: COMP123-01
Instructor: Lauren Milne
Description: This file contains the Stock class. The Stock Class represents an individual stock.
Testing: Testing is done at the bottom of the file.
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
        self.currentValue = float(int((self.currentValue + marketChange*self.currentValue)*100))/100

# if __name__ == "__main__":
#     '''Tests the Stock class'''
#     print("Beginning Testing of the Stock Class")
#     stock = Stock("Test", 1.80, "Tech")
#     print(stock.currentValue)
#     stock.updateStock(0.07, 0.02, 0.09)
#     print(stock.currentValue)
#     print("Finished Testing; Check Results Manually")