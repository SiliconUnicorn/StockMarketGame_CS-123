"""
File: stockMarket_main.py
Project: Stock Market Game
Date: 5 Nov 2021
Author(s): Arnika
"""


import numpy as np
import matplotlib.pyplot as plt

def stock(start_price):
    mu = 0.004
    sigma = 0.01
    np.random.seed(0)
    returns = np.random.normal(loc=mu, scale=sigma, size=100)
    price = start_price*(1+returns).cumprod()
    plt.plot(price)
    plt.show()
