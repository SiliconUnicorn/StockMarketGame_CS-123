'''
File: main.py
Project: Stock Market Game
Date: 5 Nov 2021
Author(s): Micah Hansonbrook
'''

from turnUpdater import *
from stockMarket.code.stockMarket.getStocks import *

def main():
    '''
    The main function of the program
    :return: None
    '''
    stocks = getStocks()
    for turn in range(31):
        stocks = turnUpdater(turn, stocks)

if __name__ == "__main__":
    main()