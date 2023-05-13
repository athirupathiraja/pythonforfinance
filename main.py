
import pandas as pd
import math
import random
import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt

yf.pdr_override()
PG = pdr.get_data_yahoo('PG', start='1995-1-1')


#simple return -> for returns of multiple securities over same period
PG['simple_return']= (PG['Adj Close']/PG['Adj Close'].shift(1)) -1
#print(PG['simple_return'])

#average annual simple return
annualAvgReturns = PG['simple_return'].mean()*250


#log returns -> for returns of one security over multiple time periods
PG['log_returns'] = np.log(PG['Adj Close']/PG['Adj Close'].shift(1))

#average annual log return
annualLogAvgReturns = PG['simple_return'].mean()*250

#rate of return of portfolio
tickers = ['PG', 'MSFT','F', 'GE']
portfolio = pd.DataFrame()
for t in tickers:
    portfolio[t] = pdr.get_data_yahoo(t, start='1995-1-1')['Adj Close']

print(portfolio.iloc[0])

portfolio.plot(figsize=(15,6))
plt.show()

#normalizing portfolio to 100 (all securities now start at 100)
(portfolio/portfolio.iloc[0]*100).plot(figsize = (15,6))
plt.show()

#return of security -> simple return
returns = (portfolio/portfolio.shift(1))-1

#return of portfolio= rate of return for a security * weight in portfolio
weights = np.array([0.25,0.25,0.25,0.25])

annual_returns = returns.mean()*250
np.dot(annual_returns, weights)
