import alpaca_trade_api as tradeapi
import numpy as np
import time

SEC_KEY = 'RSUbIPiL0wwB9RPAol4qx3iy3Ds6h6k9gSwrrPO3'
PUB_KEY = 'PKGCDFGTX33SFDNMT757'
BASE_URL = 'https://paper-api.alpaca.markets'
api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL)


# Buy a stock
api.submit_order(
  symbol='SPY', # Replace with the ticker of the stock you want to buy
  qty=1,
  side='buy',
  type='market', 
  time_in_force='gtc' # Good 'til cancelled
)