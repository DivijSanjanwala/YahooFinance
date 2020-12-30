import pandas as pd
import numpy as np
import yfinance as yf

# Ticker symbol for each company
tickerSymbol = 'TSLA'
tickerData = yf.Ticker(tickerSymbol)
# Sample Query to obtain the stock data
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')


def data_clean(ticker_dataframe: pd.core):
    """This function returns a None type and cleans the DataFrame object by
    doing the following.
    1. Cleaning the NaN values of the DataFrame object
    2. Rounding the Opening Stock Prices and the Closing Stock Prices
       to 3 decimal places.
    3. add as needed
    """
    # TODO
    ticker_dataframe.dropna()
    ticker_dataframe['Open'] = np.round(ticker_dataframe['Open'], 3)
    ticker_dataframe['Close'] = np.round(ticker_dataframe['Close'], 3)

    return ticker_dataframe


if __name__ == '__main__':
    # *************************************************************************
    # Testing the function
    print(data_clean(tickerDf).head())
    print(tickerDf.head())
# *****************************************************************************
