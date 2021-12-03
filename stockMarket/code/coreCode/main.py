'''
File: main.py
Project: Stock Market Game
Date: 5 Nov 2021
Author(s): Micah Hansonbrook
'''

from turnUpdater import *
from stockMarket.code.events.getEvents import *
from stockMarket.code.coreCode.gameInterface import *
from stockMarket.code.stockMarket.getAllStocks import *

def main():
    '''
    The main function of the program
    :return: None
    '''
    stocks = getAllStocks()
    events = getEvents()
    for turn in range(31):
        stocks = turnUpdater(turn, stocks)
    myGUI = BasicGUI()
    myGUI.run()

if __name__ == "__main__":
    main()