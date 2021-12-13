"""
Names: Arnika Abeysekera, Micah Hansonbrook, Sarah Ali, Tina Chen
Course: COMP123-01
Instructor: Lauren Milne
Description: This file runs tests of the getEvents file
"""

from stockMarket.code.events.getEvents import *
from stockMarket.code.csvInteraction.csvImporter import importCSV

def runTests():
    '''Runs all getEvents tests.'''
    test_getEvents()
    test_getAllEvents()

def test_getEvents():
    '''Tests the getEvents function.'''
    print("Testing getEvents")
    assert importCSV('../assets/csv/events.csv') == getEvents()
    print("Testing successful.")

def test_getAllEvents():
    '''Tests the getAllEvents function'''
    print("Testing getAllEvents()")
    assert getAllEvents()[0].name == 'Apple Releases iPod'
    assert getAllEvents()[0].detail == 'The first iPod holds up to 1000 songs with a battery life of 10 hours—all for the price of $399.'
    assert getAllEvents()[0].category == 'APPL'
    assert getAllEvents()[0].effect == '6.6%'
    print("Testing Successful")

if __name__ == "__main__":
    runTests()