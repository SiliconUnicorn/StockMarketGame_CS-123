'''
File: getEvents.py
Project: Stock Market Game
Date: 6 Nov 2021
Author(s): Micah Hansonbrook
'''

from stockMarket.code.csvInteraction.csvImporter import *

def getEvents():
    '''
    Gets all of the stock information, in a dictionary format
    returns: The stock information!
    '''
    return importCSV('../../assets/csv/events.csv')
