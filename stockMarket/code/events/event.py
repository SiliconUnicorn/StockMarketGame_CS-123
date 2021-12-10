'''
File: event.py
Project: Stock Market Game
Date: 3 Dec 2021
Author(s): Micah Hansonbrook
'''

import random
from stockMarket.code.stockMarket.getAllStocks import *

class Event:
    def __init__(self, name, detail, stockCategory, monetaryEffect):
        '''
        Creates an instance of the event class.
        '''
        self.name = name
        self.detail = detail
        self.category = stockCategory
        self.effect = monetaryEffect

    def generateDynamicEvent(self):
        '''Generates a dynamically generated event, to compliment the hardcoded ones'''
        randomValue = random.randint(0, 0)
        companies = getStockList()
        finalCompany = companies[random.randint(0, len(companies))]
        if randomValue == 0:
            randomValue = float(random.randint(6,15))/100
            return Event(finalCompany.name + ' releases a hit new product!', 'Everyone wants to purchase the hit new product from ' + finalCompany.name, finalCompany.name, randomValue)
        else:
            assert 0 == 1