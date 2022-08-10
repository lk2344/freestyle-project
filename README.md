# Python Trading Bot Project

## Requirements
+ python 3.8+
+ pip 
+ Anaconda 3.7+

## Setup

1. Clone repository onto desktop.
2. Create a pip environment ```pipenv shell```
3. Install Alpaca API ```pipenv install alpaca_trade_api```
4. Create an account on alpaca.markets, navigate to your account homepage and collect your API key on the right side of the page. 

![image](https://raw.githubusercontent.com/lk2344/freestyle-project/main/img.png)

5. To connect to your Alpaca account, you will need to correctly enter your API Keys. Please note, that the base url is for paper trading only, omit it you're going to do real trading.

```python
SEC_KEY = 'enter your secret key here' 
PUB_KEY = 'enter your public key here'
BASE_URL = 'https://paper-api.alpaca.markets' 
api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL) 

```

6. Activate the virtual environment, navigate to and run the python file 'trade.py':
```python
pipenv shell
```
then,
```python
cd ~/desktop/freestyle-project
```
then,
```python
python trade.py
```