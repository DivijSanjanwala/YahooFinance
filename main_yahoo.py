import yfinance as yf
import numpy as np
import pandas as pd

tickerSymbol = 'MSFT'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')
print(tickerDf.columns)
