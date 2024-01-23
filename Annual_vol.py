#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:46:41 2024

@author: artempontaplev
"""

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

#  Downloading S&P 500 front month futures price data using yfinance
sp500_futures = yf.download("ES=F")

prices = sp500_futures["Adj Close"]
sp500_futures["log_returns"] = np.log(prices).diff()
annual_vol = sp500_futures["log_returns"].std() * np.sqrt(252)
