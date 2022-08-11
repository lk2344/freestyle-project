
import alpaca_trade_api as tradeapi
import numpy as np
import time
import logging
from alpaca_trade_api.stream import Stream
from alpaca_trade_api.common import URL

SEC_KEY = 'RSUbIPiL0wwB9RPAol4qx3iy3Ds6h6k9gSwrrPO3'
PUB_KEY = 'PKGCDFGTX33SFDNMT757'
BASE_URL = 'https://paper-api.alpaca.markets'


logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

ALPACA_API_KEY = PUB_KEY
ALPACA_SECRET_KEY = SEC_KEY


def run_connection(conn):
    try:
        conn.run()
    except KeyboardInterrupt:
        print("Interrupted execution by user")
        loop.run_until_complete(conn.stop_ws())
        exit(0)
    except Exception as e:
        print(f'Exception from websocket connection: {e}')
    finally:
        print("Trying to re-establish connection")
        time.sleep(3)
        run_connection(conn)


async def print_quote(q):
    print('quote', q)


if __name__ == '__main__':
    conn = Stream(ALPACA_API_KEY,
                  ALPACA_SECRET_KEY,
                  base_url=URL('https://paper-api.alpaca.markets'),
                  data_feed='iex')

    conn.subscribe_quotes(print_quote, 'SPY')

    run_connection(conn)
