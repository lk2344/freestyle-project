import alpaca_trade_api as tradeapi
import numpy as np
import pandas as pd
import time
import logging
from alpaca_trade_api.stream import Stream
from alpaca_trade_api.common import URL
import talib
from matplotlib import pyplot as plt
from alpaca_trade_api.rest import TimeFrame
import datetime

now = datetime.datetime.now()


SEC_KEY = 'tH5XzgJtBaaHyoIApD3va0rezNuu7SdTCltnSwqj'
PUB_KEY = 'PKOO6LEMJEKR40536XHB'
BASE_URL = 'https://paper-api.alpaca.markets'
api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL)
#https://curatedpython.com/p/alpaca-trade-api-python-alpacahq-alpaca-trade-api-python/index.html

#stream = Stream(PUB_KEY, 
			#SEC_KEY,
			#base_url=URL('https://paper-api.alpaca.markets'),
            #data_feed='iex')

account = api.get_account() # gets account data
buying_power = (account.buying_power) # gets account buying power

x = float(buying_power)
y = int(x)
trade_limit = y * 0.25 #this is to size our trades based on buying power

clock = api.get_clock() #make sure market is open to make trades
print('The market is {}'.format('open.' if clock.is_open else 'closed.'))

#setting time frame for which we want data
today = now.strftime('%Y-%m-%d')
tomorrow = (now + pd.Timedelta('1day')).strftime('%Y-%m-%d') #if you have real time data, use this variable

end = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(minutes=15)).strftime('%Y-%m-%dT%H:%M:%SZ')
#your subscription does not permit querying data from the past 15 minutes
#for some reason Alpaca Api is not letting me fetch data that is within 15 min of now! Probably need to pay subscription.
#this needs to be deleted if one has access to real time data.

position = api.get_position('SPY')
#https://alpaca.markets/deprecated/docs/api-documentation/how-to/portfolio/

i=1
while True:

	barset = api.get_bars(symbol='SPY',
				timeframe=TimeFrame.Minute, 
				start=today, 
  				end=end, #this needs to be edited to 'tomorrow' if you have real time data subscription
				limit=7000)._raw #getting stock price data #https://forum.alpaca.markets/t/http-error-on-get-barset/8811/8

	price_list = [(p['o']) for p in barset] #extract open price from barset data
	price = price_list[-1] #extract most recent price

	q = trade_limit / price #find out how many shares we can buy, given our trade limit
	share_quantity = int(q-1) # to ensure we always round down to the nearest whole number. 

	df = pd.DataFrame(data=barset)
	#https://stackoverflow.com/questions/56944197/how-to-get-raw-data-from-alpaca-trade-api-barset


	data = df
	rsi = talib.RSI(data['o'])

	v = list(rsi)
	rsi_now = (v[-1])

	#just to see a cool graph of historical rsi data, and to confirm that the fuctions above are fetching correct data values.
	#fig = plt.figure()
	#fig.set_size_inches((25, 18))
	#ax_rsi = fig.add_axes((0, 0.24, 1, 0.2))
	#ax_rsi.plot(data.index, [70] * len(data.index), label="overbought")
	#ax_rsi.plot(data.index, [30] * len(data.index), label="oversold")
	#ax_rsi.plot(data.index, rsi, label="rsi")
	#ax_rsi.plot(data['o'])
	#ax_rsi.legend()
	#https://towardsdatascience.com/algorithmic-trading-with-rsi-using-python-f9823e550fe0


	if rsi_now < 35:
		api.submit_order(
 			symbol='SPY',
  			qty=share_quantity,
  			side='buy',
  			type='market', 
  			time_in_force='gtc' 
			)

	if rsi_now > 65:
		api.submit_order(
 			symbol='SPY',
  			qty=position.qty,
  			type='market',
  			time_in_force='gtc'
			)

	if i==1:
		i=i+1
		if rsi_now > 35 or rsi_now < 65:
			print('waiting to enter/exit')
	else:
		continue

