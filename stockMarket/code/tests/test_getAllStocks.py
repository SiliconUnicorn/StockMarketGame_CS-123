"""
Names: Arnika Abeysekera, Micah Hansonbrook, Sarah Ali, Tina Chen
Course: COMP123-01
Instructor: Lauren Milne
Description: This file runs tests of the getAllStocks file
"""

from stockMarket.code.events.getEvents import *
from stockMarket.code.csvInteraction.csvImporter import importCSV

def runTests():
    '''Runs all getAllStocks tests.'''
    test_getStocks()
    test_getAllStocks()

def test_getStocks():
    '''Tests the getStocks function.'''
    print("Testing getStocks")
    assert importCSV('../../assets/csv/stocks.csv') == getStocks()
    print("Testing successful.")

def test_getAllStocks():
    '''Tests the getAllStocks function'''
    print("Testing getAllStocks()")
    assert getAllStocks()['Apple'].name == 'Apple'
    assert getAllStocks()['Apple'].category == 'Tech'
    print("Testing Successful")

def test_getStockList():
    '''Tests the getStockList() function'''
    print("Testing getStockList()")
    assert getStockList()[2].name == 'Meta Corp.'
    assert getStockList()[2].category == 'Tech'
    print("Testing Successful")

if __name__ == "__main__":
    runTests()