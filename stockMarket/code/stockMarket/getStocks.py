'''
File: getStocks.py
Project: Stock Market Game
Date: 6 Nov 2021
Author(s): Micah Hansonbrook
'''

from stockMarket.code.csvInteraction.csvImporter import *

def getStocks():
    '''
    Gets all of the stock information, in a dictionary format
    returns: The stock information!
    '''
    return importCSV('../../assets/csv/stocks.csv')
