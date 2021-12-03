'''
File: turnUpdater.py
Project: Stock Market Game
Date: 6 Nov 2021
Author(s): Micah Hansonbrook
'''

from stockMarket.code.coreCode.eventInterface import *

def turnUpdater(turnNumber, stocks, events):
    '''
    This will update the code for a new turn
    :param turnNumber: The current turn number
    :param stocks: The current stock data
    :param events: The current events pool.
    :return: Stocks data
    '''
    if turnNumber == 0:
        print("Welcome")
        print("Current Stocks: " + str(stocks))
    else:
        for stock in stocks:
            stock.valueHistory.append(stock.currentValue)
            stock.currentValue = float(stock.currentValue) * 1.07
        print("Turn " + str(turnNumber) + ":")
        print("Current Stocks: " + str(stocks))
    ui = eventsExample()
    ui.run()
    return stocks
