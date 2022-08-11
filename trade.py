import alpaca_trade_api as tradeapi
import numpy as np
import time
import talib
from matplotlib import pyplot as plt

SEC_KEY = 'RSUbIPiL0wwB9RPAol4qx3iy3Ds6h6k9gSwrrPO3'
PUB_KEY = 'PKGCDFGTX33SFDNMT757'
BASE_URL = 'https://paper-api.alpaca.markets'
api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL)
#https://curatedpython.com/p/alpaca-trade-api-python-alpacahq-alpaca-trade-api-python/index.html



account = api.get_account() # gets account data
bp = (account.buying_power) # gets account buying power

clock = api.get_clock() #make sure market is open to make trades
print('The market is {}'.format('open.' if clock.is_open else 'closed.'))

barset = api.get_bars("SPY", '1Min', limit=7200, adjustment='raw') #getting stock price data
#https://forum.alpaca.markets/t/http-error-on-get-barset/8811/8

print(barset)



#api.submit_order(
# 	symbol='SPY',
#  	qty=bp * 0.25,
#  	side='buy',
#  	type='market', 
#  	time_in_force='gtc' 
#	)

#api.submit_order(
# 	symbol='SPY',
#  	qty=bp * 0.25,
#  	type='market',
#  	time_in_force='gtc'
#	)

