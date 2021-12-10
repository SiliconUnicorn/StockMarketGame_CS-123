"""
File: stock_graph.py
Project: Stock Market Game
Date: 5 Nov 2021
Author(s): Tina, Arnika
"""

import numpy as np
import matplotlib.pyplot as plt


def stock(start_price, monetaryEffect, startingYr):
    """Takes in the the starting price of a stock as an input, and generates a randomized graph representing the
    stock, starting at the initial price."""
    sigma = 0.0023
    np.random.seed(0)
    returns = np.random.normal(loc=monetaryEffect/100, scale=sigma, size=30)
    price = start_price*(1+returns).cumprod()
    plt.plot(price)
    x = [1, 5, 10, 15, 20, 25, 30]
    values = [startingYr, startingYr + 1, startingYr + 2, startingYr + 3, startingYr + 4, startingYr + 5,
              startingYr + 6]
    plt.xticks(x, values)
    plt.xlabel("Time")
    plt.ylabel("Value of Stock")
    plt.title("Graph of Stock")
    plt.show()


stock(4, 0.12, 1990)