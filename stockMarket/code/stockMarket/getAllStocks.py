'''
File: getAllStocks.py
Project: Stock Market Game
Date: 3 Dec 2021
Author(s): Micah Hansonbrook
'''

from stockMarket.code.stockMarket.classStock import *
from stockMarket.code.stockMarket.getStocks import *

def getAllStocks():
    '''
    Loads all stocks into the game, and returns a list of stocks using the stock class
    '''
    accumulator = {}
    for value in getStocks():
        newStock = Stock(value["Real Name"], value["Initial Price per Share"], value["Category"])
        accumulator[value["Real Name"]] =newStock
    return accumulator


