#!/usr/bin/python

# ~~~~~==============   HOW TO RUN   ==============~~~~~
# 1) Configure things in CONFIGURATION section
# 2) Change permissions: chmod +x bot.py
# 3) Run in loop: while true; do ./bot.py; sleep 1; done

from __future__ import print_function
from collections import deque

import sys
import socket
import json

# ~~~~~============== CONFIGURATION  ==============~~~~~
# replace REPLACEME with your team name!
team_name = "Ekans"
# This variable dictates whether or not the bot is connecting to the prod
# or test exchange. Be careful with this switch!
test_mode = True

# This setting changes which test exchange is connected to.
# 0 is prod-like
# 1 is slower
# 2 is empty
test_exchange_index = 2
prod_exchange_hostname = "production"

port = 25000 + (test_exchange_index if test_mode else 0)
exchange_hostname = "test-exch-" + team_name if test_mode else prod_exchange_hostname

# Symbol: deque containing pairs of (quantity, price)
positions = dict()
prices = dict()
books = {}
limits = {
    "BOND": 100,
    "VALBZ": 10,
    "VALE": 10,
    "GS": 100,
    "MS": 100,
    "WFC": 100,
    "XLF": 100
}
ids = 0
cash = 0


# ~~~~~============== NETWORKING CODE ==============~~~~~
def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((exchange_hostname, port))
    return s.makefile('rw', 1)


def write_to_exchange(exchange, obj):
    json.dump(obj, exchange)
    exchange.write("\n")


def read_from_exchange(exchange):
    return json.loads(exchange.readline())


# ~~~~~============== MAIN LOOP ==============~~~~~

def setup():
    for key in limits:
        positions[key] = 0
        prices[key] = deque()
        books[key] = 0


# Arbitrage Calculations
# def calculateArbitrage():
#   arbitrage = (3*sum((prices.get("BOND"))[0])/len((prices.get("BOND"))[0]) + 2*sum((prices.get("GS"))[0])/len((prices.get("GS"))[0]) + 3*sum((prices.get("MS"))[0])/len((prices.get("MS"))[0]) + 2*sum((prices.get("WFC"))[0])/len((prices.get("WFC"))[0]))
#   - 10*sum(prices.get("XLF"))/len(prices.get("XLF"))


def main():
    exchange = connect()
    write_to_exchange(exchange, {"type": "hello", "team": team_name.upper()})
    hello_from_exchange = read_from_exchange(exchange)
    print(hello_from_exchange)
    # A common mistake people make is to call write_to_exchange() > 1
    # time for every read_from_exchange() response.
    # Since many write messages generate marketdata, this will cause an
    # exponential explosion in pending messages. Please, don't do that!

    setup()
    # write_to_exchange(exchange, {"type":"add", "order_id":id, "symbol":"BOND", "dir":"SELL", "price":1001, "size":100})
    # write_to_exchange(exchange, {"type":"add", "order_id":id, "symbol":"BOND", "dir":"BUY", "price":999, "size":100})


while True:
    message = read_from_exchange(exchange)
    if message["type"] == "ack":
        print(message)
        pass
    if message["type"] == "close":
        print("The round has ended")
        break
    if message["type"] == "open":
        write_to_exchange(exchange, {"type": "add", "order_id": ids, "symbol": "BOND", "dir": "SELL", "price": 1001, "size": 100})
        write_to_exchange(exchange, {"type": "add", "order_id": ids, "symbol": "BOND", "dir": "BUY", "price": 999, "size": 100})

print("The exchange replied:", hello_from_exchange, file=sys.stderr)
while True:
    message = read_from_exchange(exchange)
    print(message)
    if message["type"] == "close":
        print("The round has ended")
        break
    if message["type"] == "open":
        write_to_exchange(exchange, {"type": "add", "order_id": id, "symbol": "BOND", "dir": "SELL", "price": 1001, "size": 100})
        write_to_exchange(exchange, {"type": "add", "order_id": id, "symbol": "BOND", "dir": "BUY", "price": 999, "size": 100})
    elif message["type"] == "trade":
        if message["symbol"] == "BOND":
            prices["BOND"].append((message["price"], message["size"]))
        elif message["symbol"] == "VALBZ":
            prices["VALBZ"].append((message["price"], message["size"]))
        elif message["symbol"] == "VALE":
            prices["VALE"].append((message["price"], message["size"]))
        elif message["symbol"] == "GS":
            prices["GS"].append((message["price"], message["size"]))
        elif message["symbol"] == "MS":
            prices["MS"].append((message["price"], message["size"]))
        elif message["symbol"] == "WFC":
            prices["WFC"].append((message["price"], message["size"]))
        elif message["symbol"] == "XLF":
            prices["XLF"].append((message["price"], message["size"]))
    elif message["type"] == "reject":
        print(message)
    elif message["type"] == "ack":
        print(message)
        pass
    elif message["type"] == "fill":
        security = message["symbol"]
        if message["dir"] == "BUY":
            positions[security] += message["size"]
            cash -= message["price"] * message["size"]
        if message["dir"] == "SELL":
            positions[security] -= message["size"]
            cash += message["price"] * message["size"]
    elif message["type"] == "book":
        books[message["symbol"]] = message
        # {"type":"book","symbol":"SYM","buy":[[PRICE,SIZE], ...],"sell":[...]}

        # write_to_exchange(exchange, {"type":"add", "order_id":ids, "symbol":"BOND", "dir":"SELL", "price":1001, "size":100})
        # write_to_exchange(exchange, {"type":"add", "order_id":ids, "symbol":"BOND", "dir":"BUY", "price":999, "size":100})
        # bond stuff {"type": "add", "order_id": 5, "symbol": "BOND", "dir": "BUY", "price": 1002, "size": 50}

if __name__ == "__main__":
    main()

# The exchange replied: {u'symbols': [{u'position': 0, u'symbol': u'BOND'}, {u'position': 0, u'symbol': u'GS'}, {u'position': 0, u'symbol': u'MS'}, {u'position': 0, u'symbol': u'USD'}, {u'position': 0, u'symbol': u'VALBZ'}, {u'position': 0, u'symbol': u'VALE'}, {u'position': 0, u'symbol': u'WFC'}, {u'position': 0, u'symbol': u'XLF'}], u'type': u'hello'}
# {u'symbols': [u'BOND', u'GS', u'MS', u'VALBZ', u'VALE', u'WFC', u'XLF'], u'type': u'open'}
# {u'sell': [[4215, 1], [4219, 2], [4224, 1], [4226, 6], [4232, 2]], u'symbol': u'VALE', u'buy': [[4197, 6], [4185, 4], [4183, 1], [4178, 1]], u'type': u'book'}
# {u'sell': [[4217, 2], [4219, 1], [4220, 2], [4221, 2]], u'symbol': u'VALBZ', u'buy': [[4216, 1], [4213, 2], [4211, 1], [4209, 1], [4208, 2]], u'type': u'book'}
# {u'sell': [[5571, 3], [5572, 1], [5575, 1], [5579, 1]], u'symbol': u'WFC', u'buy': [[5570, 3], [5564, 1], [5559, 1], [5555, 1], [5552, 2], [5549, 3], [5546, 4], [5541, 1]], u'type': u'book'}
# {u'sell': [[4332, 1]], u'symbol': u'XLF', u'buy': [[4310, 2], [4309, 3], [4304, 5], [4301, 1], [4296, 2], [4295, 5], [4294, 2], [4291, 3], [4288, 2], [4287, 1], [4277, 4], [4272, 1], [4265, 3]], u'type': u'book'}
# {u'sell': [[4100, 1], [4102, 1]], u'symbol': u'MS', u'buy': [[4090, 4], [4089, 1], [4086, 6], [4083, 1]], u'type': u'book'}
# {u'sell': [[1000, 1], [1001, 2], [1002, 11]], u'symbol': u'BOND', u'buy': [[999, 8], [998, 4]], u'type': u'book'}
# {u'sell': [[8310, 2], [8312, 4], [8313, 6], [8316, 1], [8317, 8], [8318, 1], [8335, 2], [8344, 2]], u'symbol': u'GS', u'buy': [[8309, 2], [8307, 1], [8306, 1], [8305, 1], [8304, 4], [8303, 3], [8301, 3], [8300, 1], [8293, 5]], u'type': u'book'}
# {u'sell': [[4215, 1], [4219, 2], [4224, 1], [4226, 6], [4232, 2]], u'symbol': u'VALE', u'buy': [[4197, 6], [4185, 4], [4183, 1], [4181, 1], [4178, 1]], u'type': u'book'}
# {u'symbol': u'GS', u'type': u'trade', u'price': 8310, u'size': 1}
# {u'sell': [[8310, 1], [8312, 4], [8313, 6], [8316, 1], [8317, 8], [8318, 1], [8335, 2], [8344, 2]], u'symbol': u'GS', u'buy': [[8309, 2], [8307, 1], [8306, 1], [8305, 1], [8304, 4], [8303, 3], [8301, 3], [8300, 1], [8293, 5]], u'type': u'book'}
# {u'sell': [[5571, 3], [5572, 1], [5575, 1], [5579, 1]], u'symbol': u'WFC', u'buy': [[5570, 3], [5564, 1], [5559, 1], [5552, 2], [5549, 3], [5546, 4], [5541, 1]], u'type': u'book'}
# {u'sell': [[4100, 1], [4102, 1]], u'symbol': u'MS', u'buy': [[4090, 4], [4089, 1], [4086, 6], [4084, 1], [4083, 1]], u'type': u'book'}
# {u'sell': [[4217, 2], [4219, 1], [4220, 2], [4221, 2]], u'symbol': u'VALBZ', u'buy': [[4216, 1], [4213, 2], [4211, 1], [4209, 1]], u'type': u'book'}
# {u'sell': [[4215, 1], [4216, 1], [4219, 2], [4224, 1], [4226, 6], [4232, 2]], u'symbol': u'VALE', u'buy': [[4197, 6], [4185, 4], [4183, 1], [4181, 1], [4178, 1]], u'type': u'book'}
# {u'sell': [[4332, 1]], u'symbol': u'XLF', u'buy': [[4310, 2], [4304, 5], [4301, 1], [4296, 2], [4295, 5], [4294, 2], [4291, 3], [4288, 2], [4287, 1], [4277, 4], [4272, 1], [4265, 3]], u'type': u'book'}
# {u'sell': [[4217, 2], [4219, 1], [4220, 1], [4221, 2]], u'symbol': u'VALBZ', u'buy': [[4216, 1], [4213, 2], [4211, 1], [4209, 1]], u'type': u'book'}
# {u'sell': [[4095, 3], [4100, 1], [4102, 1]], u'symbol': u'MS', u'buy': [[4090, 4], [4089, 1], [4086, 6], [4084, 1], [4083, 1]], u'type': u'book'}
# {u'sell': [[5571, 5], [5572, 1], [5575, 1], [5579, 1]], u'symbol': u'WFC', u'buy': [[5570, 3], [5564, 1], [5559, 1], [5552, 2], [5549, 3], [5546, 4], [5541, 1]], u'type': u'book'}
# {u'sell': [[5571, 5], [5572, 1], [5575, 1], [5579, 1]], u'symbol': u'WFC', u'buy': [[5570, 3], [5564, 1], [5559, 1], [5552, 2], [5549, 3], [5546, 3], [5541, 1]], u'type': u'book'}
# {u'sell': [[5571, 5], [5572, 1], [5575, 1], [5579, 1]], u'symbol': u'WFC', u'buy': [[5564, 1], [5559, 1], [5552, 2], [5549, 3], [5546, 3], [5541, 1]], u'type': u'book'}
# {u'sell': [[5571, 5], [5572, 1], [5575, 1], [5579, 1]], u'symbol': u'WFC', u'buy': [[5564, 1], [5559, 1], [5556, 1], [5552, 2], [5549, 3], [5546, 3], [5541, 1]], u'type': u'book'}
# {u'sell': [[4217, 2], [4219, 1], [4220, 1], [4221, 2]], u'symbol': u'VALBZ', u'buy': [[4216, 1], [4214, 1], [4213, 2], [4211, 1], [4209, 1]], u'type': u'book'}
# {u'sell': [[4095, 3], [4100, 1]], u'symbol': u'MS', u'buy': [[4090, 4], [4089, 1], [4086, 6], [4084, 1], [4083, 1]], u'type': u'book'}
# {u'sell': [[8310, 1], [8312, 4], [8313, 6], [8316, 1], [8317, 8], [8318, 1], [8335, 2], [8344, 2]], u'symbol': u'GS', u'buy': [[8309, 3], [8307, 1], [8306, 1], [8305, 1], [8304, 4], [8303, 3], [8301, 3], [8300, 1], [8293, 5]], u'type': u'book'}
# {u'sell': [[5571, 5], [5572, 1], [5575, 1], [5579, 1]], u'symbol': u'WFC', u'buy': [[5564, 1], [5559, 2], [5556, 1], [5552, 2], [5549, 3], [5546, 3], [5541, 1]], u'type': u'book'}
# {u'sell': [[5569, 2], [5571, 5], [5572, 1], [5575, 1], [5579, 1]], u'symbol': u'WFC', u'buy': [[5564, 1], [5559, 2], [5556, 1], [5552, 2], [5549, 3], [5546, 3], [5541, 1]], u'type': u'book'}
# {u'sell': [[4217, 2], [4219, 1], [4220, 1], [4221, 2]], u'symbol': u'VALBZ', u'buy': [[4216, 1], [4214, 1], [4213, 2], [4212, 2], [4211, 1], [4209, 1]], u'type': u'book'}
# {u'sell': [[4094, 3], [4095, 3], [4100, 1]], u'symbol': u'MS', u'buy': [[4090, 4], [4089, 1], [4086, 6], [4084, 1], [4083, 1]], u'type': u'book'}
# {u'sell': [[8310, 1], [8311, 2], [8312, 4], [8313, 6], [8316, 1], [8317, 8], [8318, 1], [8335, 2], [8344, 2]], u'symbol': u'GS', u'buy': [[8309, 3], [8307, 1], [8306, 1], [8305, 1], [8304, 4], [8303, 3], [8301, 3], [8300, 1], [8293, 5]], u'type': u'book'}
# {u'sell': [[1000, 1], [1001, 2], [1002, 11]], u'symbol': u'BOND', u'buy': [[999, 8], [998, 5]], u'type': u'book'}
# {u'sell': [[4217, 2], [4219, 1], [4220, 1]], u'symbol': u'VALBZ', u'buy': [[4216, 1], [4214, 1], [4213, 2], [4212, 2], [4211, 1], [4209, 1]], u'type': u'book'}
