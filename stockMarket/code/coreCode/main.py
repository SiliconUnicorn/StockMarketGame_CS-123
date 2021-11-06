'''
File: main.py
Project: Stock Market Game
Date: 5 Nov 2021
Author(s): Micah Hansonbrook
'''

from turnUpdater import *

def main():
    '''
    The main function of the program
    :return: None
    '''
    for turn in range(31):
        turnUpdater(turn)

if __name__ == "__main__":
    main()