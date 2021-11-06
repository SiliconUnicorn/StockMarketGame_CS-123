'''
File: turnUpdater.py
Project: Stock Market Game
Date: 6 Nov 2021
Author(s): Micah Hansonbrook
'''

def turnUpdater(turnNumber):
    '''
    This will update the code for a new turn
    :return: None
    '''
    if turnNumber == 0:
        print("Welcome")
    else:
        print("Turn " + str(turnNumber) + ":")
