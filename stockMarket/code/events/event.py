"""
Names: Arnika Abeysekera, Micah Hansonbrook, Sarah Ali, Tina Chen
Course: COMP123-01
Instructor: Lauren Milne
Description: This file defines the Event class, which represents an event that the user experiences during the game.
"""


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
        self.mostRecentEventFocus = Stock("None", 0, "None")

    def generateDynamicEvent(self):
        '''
        Generates a dynamically generated event, to compliment the hardcoded ones
        returns: A new event.
        Testing methodology: this function was tested by checking outputs in the program and confirming realistic distribution of events.
        '''
        randomValue = random.randint(0, 4)
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
        elif randomValue == 3:
            randomValue = float(random.randint(3, 7)) / 100
            return Event(finalCompany.name + ' Makes Large Acquisition', finalCompany.name + ' has made a major acquisition that analysts believe will boost its bottom line.', finalCompany.name, randomValue)
        elif randomValue == 4:
            randomValue = float(random.randint(-25, -15)) / 100
            return Event(finalCompany.name + ' Struggling', 'Sources indicate that ' + finalCompany.name + ' is struggling to pay its debts.', finalCompany.name, randomValue)
        else:
            assert 0 == 1