"""
Names: Arnika Abeysekera, Micah Hansonbrook, Sarah Ali, Tina Chen
Course: COMP123-01
Instructor: Lauren Milne
Description: This file contains the game's main program. The user will go to this file to run and play the game.
"""

from stockMarket.code.coreCode.gameInterface import *


def main():
    """Displays the game interface to be used, and for the user to play to the game."""
    myGUI = GameGUI()
    myGUI.run()


if __name__ == "__main__":
    main()