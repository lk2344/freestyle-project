import logging

from alpaca_trade_api.stream import Stream

log = logging.getLogger(__name__)


async def print_trade(t):
    print('trade', t)


async def print_quote(q):
    print('quote', q)


async def print_trade_update(tu):
    print('trade update', tu)

def main():
    logging.basicConfig(level=logging.INFO)
    feed = 'iex'  # <- replace to SIP if you have PRO subscription
    stream = Stream(data_feed=feed, raw_data=True)
    stream.subscribe_trade_updates(print_trade_update)
    stream.subscribe_trades(print_trade, 'SPY')
    stream.subscribe_quotes(print_quote, 'SPY')

    @stream.on_bar('SPY')
    async def _(bar):
        print('bar', bar)

    @stream.on_updated_bar('SPY')
    async def _(bar):
        print('updated bar', bar)

    @stream.on_status("*")
    async def _(status):
        print('status', status)

    @stream.on_luld('SPY')
    async def _(luld):
        print('LULD', luld)

    stream.run()


if __name__ == "__main__":
    main()
