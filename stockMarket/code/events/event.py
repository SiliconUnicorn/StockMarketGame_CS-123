'''
File: event.py
Project: Stock Market Game
Date: 3 Dec 2021
Author(s): Micah Hansonbrook
'''

class Event:
    def __init__(self, name, detail, stockCategory, monetaryEffect):
        '''
        Creates an instance of the event class.
        '''
        self.name = name
        self.detail = detail
        self.category = stockCategory
        self.effect = monetaryEffect
