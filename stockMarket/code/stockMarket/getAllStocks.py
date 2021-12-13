"""
Names: Arnika Abeysekera, Micah Hansonbrook, Sarah Ali, Tina Chen
Course: COMP123-01
Instructor: Lauren Milne
Description: This file allows events to be pulled from the stocks.csv CSV file. It provides formatting conveniance
and allows easy return of a List of stocks or a Dictionary of stocks to the user.
"""

from stockMarket.code.stockMarket.classStock import *
from stockMarket.code.csvInteraction.csvImporter import *
import os

def getAllStocks():
    '''
    Loads all stocks into the game, and returns a list of stocks using the stock class
    '''
    accumulator = {}
    for value in getStocks():
        newStock = Stock(value["Real Name"], value["Initial Price per Share"], value["Category"])
        accumulator[value["Real Name"]] = newStock
    return accumulator


def getStockList():
    '''Generates a list containing every single stock.'''
    accumulator = []
    for value in getStocks():
        newStock = Stock(value["Real Name"], value["Initial Price per Share"], value["Category"])
        accumulator.append(newStock)
    return accumulator

def getStocks():
    '''
    Gets all of the stock information, in a dictionary format
    returns: The stock information!
    '''
    directory = os.getcwd()
    newDirectory = ''
    for character in directory:
        if len(newDirectory) > 13 and newDirectory[len(newDirectory)-13:len(newDirectory)-1] == '/stockMarket':
            break
        else:
            newDirectory += character
    return importCSV(newDirectory + '/assets/csv/stocks.csv')
