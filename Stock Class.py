import datetime
import pandas as pd
import numpy as np
import yfinance as yf


class Stock:

    def __init__(self, ticker):
        self.ticker = ticker

    def get_3MMA(self, ticker: str, start_date: datetime.datetime,
                 end_date: datetime.datetime) -> int:
        """
        :param ticker: Ticker of the Stock
        :type ticker: str
        :param start_date: Thr start date of the period
        :type start_date: datetime from the library datetime
        :param end_date: The end date of the period
        :type end_date: datetime from the library datetime
        :return: Returns the 3-month-moving average of the Stock
        :rtype: int
        """

        ticker_data = yf.Ticker(self.ticker)
        # Query to obtain the stock data
        tickerDf = ticker_data.history(period='30d', start=start_date,
                                       end=end_date)
        # TODO:
        return 5
