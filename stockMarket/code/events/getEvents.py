'''
File: getEvents.py
Project: Stock Market Game
Date: 6 Nov 2021
Author(s): Micah Hansonbrook
'''

from stockMarket.code.csvInteraction.csvImporter import *
from stockMarket.code.events.event import *

def getEvents():
    '''
    Gets all of the event information, in a dictionary format
    returns: The event information!
    '''
    return importCSV('../../assets/csv/events.csv')

def getAllEvents():
    '''
    Loads all of the event information as event class instances and returns it
    inside of a List
    '''
    accumulator = []
    for value in getEvents():
        event = Event(value["Event Name"], value["Detail"], value["Stock Category"], value["Monetary Effect"])
        accumulator.append(event)
    return accumulator