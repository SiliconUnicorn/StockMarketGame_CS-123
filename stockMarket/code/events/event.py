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
        randomValue = random.randint(0, 2)
        companies = getStockList()
        finalCompany = companies[random.randint(0, len(companies)-1)]
        if randomValue == 0:
            randomValue = float(random.randint(6,15))/100
            return Event(finalCompany.name + ' Releases Hit New Product!', 'Everyone wants to purchase the hit new product from ' + finalCompany.name, finalCompany.name, randomValue)
        elif randomValue == 1:
            randomValue = float(random.randint(9, 19)) / 100
            return Event(finalCompany.name + ' is Undervalued', 'Investment sources claim that ' + finalCompany.name + ' is severely undervalued.', finalCompany.name, randomValue)
        elif randomValue == 2:
            randomValue = float(random.randint(-8, -2)) / 100
            return Event(finalCompany.name + ' Under Investigation', 'Antitrust authorities are currently investigating ' + finalCompany.name + ' for anticompetitive behavior.', finalCompany.name, randomValue)
        else:
            assert 0 == 1