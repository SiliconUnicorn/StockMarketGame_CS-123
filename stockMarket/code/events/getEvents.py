"""
Names: Arnika Abeysekera, Micah Hansonbrook, Sarah Ali, Tina Chen
Course: COMP123-01
Instructor: Lauren Milne
Description: This file allows events to be pulled from the events.csv CSV file. It provides formatting conveniance
and allows easy return of a List of events to the user.
Testing: Everything in this file can be tested in the test_getEvents.py file.
"""

from stockMarket.code.csvInteraction.csvImporter import *
from stockMarket.code.events.event import *

def getEvents():
    '''
    Gets all of the event information, in a dictionary format
    returns: The event information!
    '''
    directory = os.getcwd()
    newDirectory = ''
    for character in directory:
        if len(newDirectory) > 13 and newDirectory[len(newDirectory)-13:len(newDirectory)-1] == '/stockMarket':
            break
        else:
            newDirectory += character
    return importCSV(newDirectory + '/assets/csv/events.csv')

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