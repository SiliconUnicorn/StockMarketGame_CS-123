"""
File: stockMarket_main.py
Project: Stock Market Game
Date: 5 Nov 2021
Author(s): Arnika, Tina
"""

import numpy as np
import matplotlib.pyplot as plt


def stock(start_price):
    """Takes in the the starting price of a stock as an input, and generates a randomized graph representing the 
    stock, starting at the initial price. """
    mu = 0.004
    sigma = 0.01
    np.random.seed(0)
    returns = np.random.normal(loc=mu, scale=sigma, size=100)
    price = start_price*(1+returns).cumprod()
    plt.plot(price)
    plt.show()
