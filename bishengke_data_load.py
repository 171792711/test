# -*- coding:utf-8 -*- 

import sys
import os

sys.path.append(os.path.abspath('..'))
import ccxt
import redis

# import json

_zb_sec_params = {'apiKey': 'xjsbm8674NGfSrPsn0GWxddfT4Zcns66fWbEjmlo4LAy4hJJxSNhWs0ZeINEDC9C',
                  'secret': 'RzvGfUoVQwo0UZOgyIBzU2xSKCFEXEIdkZWPUSMpcbgnKm5t1g23QdgpGbgoe2DK', }


##########################################################################################################
# binance

class ccxt_load():
    def __init__(self):
        print('开始构建ccxt_load')


    # ticker 截止到当前，过去24小时的 交易统计/汇总信息
    def _load_binance_ticker_data(symbol):
        binance = ccxt.binance({'verbose': True})
        markets = binance.load_markets()
        ticker = binance.fetch_ticker(symbol)

        ticker.pop('info')
        ticker2 = {}
        ticker2['symbol'] = ticker.pop('symbol')
        ticker2['priceChange'] = ticker.pop('change')
        ticker2['priceChangePercent'] = ticker.pop('percentage')
        ticker2['weightedAvgPrice'] = ticker.pop('vwap')
        ticker2['prevClosePrice'] = ticker.pop('previousClose')
        ticker2['lastPrice'] = ticker.pop('last')
        ticker2['lastQty'] = 'none'
        ticker2['bidPrice'] = ticker.pop('bid')
        ticker2['bidQty'] = ticker.pop('bidVolume')
        ticker2['askPrice'] = ticker.pop('ask')
        ticker2['askQty'] = ticker.pop('askVolume')
        ticker2['openPrice'] = ticker.pop('open')
        ticker2['highPrice'] = ticker.pop('high')
        ticker2['lowPrice'] = ticker.pop('low')
        ticker2['volume'] = ticker.pop('baseVolume')
        ticker2['quoteVolume'] = ticker.pop('quoteVolume')
        ticker2['openTime'] = ticker.pop('datetime')
        ticker2['closeTime'] = ticker.pop('timestamp')
        ticker2['firstId'] = 'none'
        ticker2['lastId'] = 'none'
        ticker2['count'] = 'none'
        ticker = ticker2
        return ticker
        # print(ticker2)

    # trades过去一段时间（最多返回500条数据）的交易记录，包括成交价、成交量 ……
    def _load_binance_trades_data(symbol):
        binance = ccxt.binance({'verbose': True})
        markets = binance.load_markets()
        trades = binance.fetch_trades(symbol)

        l = len(trades)
        L = list(range(l))
        trades_bak = []
        i = 0
        for i in L:
            trades_1 = trades[i]
            trades2 = {}
            trades2['a'] = trades_1.pop('id')
            trades2['p'] = trades_1.pop('price')
            trades2['q'] = trades_1.pop('amount')
            trades2['f'] = 'none'
            trades2['l'] = 'none'
            trades2['T'] = trades_1.pop('timestamp')
            trades2['m'] = 'none'
            trades2['M'] = 'none'
            trades_bak.append(trades2)
        trades = trades2
        return trades

    # ohlcv 获取指定数币对的K线数据
    def _load_binance_orderbook_data(symbol):
        binance = ccxt.binance({'verbose': True})
        markets = binance.load_markets()

        ohlcv = binance.fetch_ohlcv(symbol)
        return ohlcv
    # orderbook 获取指定数币对的当前的报价（深度），以及相应的交易量
    def _load_binance_trades_data(symbol):
        binance = ccxt.binance({'verbose': True})
        markets = binance.load_markets()

        orderbook = binance.fetch_order_book(symbol)
        return orderbook
    ##########################################################################################################
    # zb
    # ticker 截止到当前，过去24小时的 交易统计/汇总信息
    def _load_zb_ticker_data(symbol):
        zb = ccxt.zb({'verbose': True})
        markets = zb.load_markets()
        ticker = zb.fetch_ticker(symbol)

        ticker.pop('info')
        ticker2 = {}
        ticker2['symbol'] = ticker.pop('symbol')
        ticker2['priceChange'] = ticker.pop('change')
        ticker2['priceChangePercent'] = ticker.pop('percentage')
        ticker2['weightedAvgPrice'] = ticker.pop('vwap')
        ticker2['prevClosePrice'] = ticker.pop('previousClose')
        ticker2['lastPrice'] = ticker.pop('last')
        ticker2['lastQty'] = 'none'
        ticker2['bidPrice'] = ticker.pop('bid')
        ticker2['bidQty'] = ticker.pop('bidVolume')
        ticker2['askPrice'] = ticker.pop('ask')
        ticker2['askQty'] = ticker.pop('askVolume')
        ticker2['openPrice'] = ticker.pop('open')
        ticker2['highPrice'] = ticker.pop('high')
        ticker2['lowPrice'] = ticker.pop('low')
        ticker2['volume'] = ticker.pop('baseVolume')
        ticker2['quoteVolume'] = ticker.pop('quoteVolume')
        ticker2['openTime'] = ticker.pop('datetime')
        ticker2['closeTime'] = ticker.pop('timestamp')
        ticker2['firstId'] = 'none'
        ticker2['lastId'] = 'none'
        ticker2['count'] = 'none'
        ticker = ticker2
        return ticker
    # print(ticker2)

    # trades过去一段时间（最多返回500条数据）的交易记录，包括成交价、成交量 ……
    def _load_zb_trades_data(symbol):
        zb = ccxt.zb({'verbose': True})
        markets = zb.load_markets()
        trades = zb.fetch_trades(symbol)

        l = len(trades)
        L = list(range(l))
        trades_bak = []
        i = 0
        for i in L:
            trades_1 = trades[i]
            trades2 = {}
            trades2['a'] = trades_1.pop('id')
            trades2['p'] = trades_1.pop('price')
            trades2['q'] = trades_1.pop('amount')
            trades2['f'] = 'none'
            trades2['l'] = 'none'
            trades2['T'] = trades_1.pop('timestamp')
            trades2['m'] = 'none'
            trades2['M'] = 'none'
            trades_bak.append(trades2)
        trades = trades2
        return trades
    # ohlcv 获取指定数币对的K线数据
    def _load_zb_ohlcv_data(symbol):
        zb = ccxt.zb({'verbose': True})
        markets = zb.load_markets()
        ohlcv = zb.fetch_ohlcv(symbol)
        return ohlcv
    # orderbook 获取指定数币对的当前的报价（深度），以及相应的交易量
    def _load_zb_orderbook_data(symbol):
        zb = ccxt.zb({'verbose': True})
        markets = zb.load_markets()
        orderbook = zb.fetch_order_book(symbol)
        return orderbook
    ##########################################################################################################
    # okex

    # ticker 截止到当前，过去24小时的 交易统计/汇总信息
    def _load_okex_ticker_data(symbol):
        okex = ccxt.okex({'verbose': True})
        markets = okex.load_markets()
        ticker = okex.fetch_ticker(symbol)

        ticker.pop('info')
        ticker2 = {}
        ticker2['symbol'] = ticker.pop('symbol')
        ticker2['priceChange'] = ticker.pop('change')
        ticker2['priceChangePercent'] = ticker.pop('percentage')
        ticker2['weightedAvgPrice'] = ticker.pop('vwap')
        ticker2['prevClosePrice'] = ticker.pop('previousClose')
        ticker2['lastPrice'] = ticker.pop('last')
        ticker2['lastQty'] = 'none'
        ticker2['bidPrice'] = ticker.pop('bid')
        ticker2['bidQty'] = ticker.pop('bidVolume')
        ticker2['askPrice'] = ticker.pop('ask')
        ticker2['askQty'] = ticker.pop('askVolume')
        ticker2['openPrice'] = ticker.pop('open')
        ticker2['highPrice'] = ticker.pop('high')
        ticker2['lowPrice'] = ticker.pop('low')
        ticker2['volume'] = ticker.pop('baseVolume')
        ticker2['quoteVolume'] = ticker.pop('quoteVolume')
        ticker2['openTime'] = ticker.pop('datetime')
        ticker2['closeTime'] = ticker.pop('timestamp')
        ticker2['firstId'] = 'none'
        ticker2['lastId'] = 'none'
        ticker2['count'] = 'none'
        ticker = ticker2
        return ticker
    # trades过去一段时间（最多返回500条数据）的交易记录，包括成交价、成交量 ……
    def _load_okex_trades_data(symbol):
        okex = ccxt.okex({'verbose': True})
        markets = okex.load_markets()
        trades = okex.fetch_trades(symbol)
        print(trades)

        l = len(trades)
        L = list(range(l))
        trades_bak = []
        i = 0
        for i in L:
            trades_1 = trades[i]
            trades2 = {}
            trades2['a'] = trades_1.pop('id')
            trades2['p'] = trades_1.pop('price')
            trades2['q'] = trades_1.pop('amount')
            trades2['f'] = 'none'
            trades2['l'] = 'none'
            trades2['T'] = trades_1.pop('timestamp')
            trades2['m'] = 'none'
            trades2['M'] = 'none'
            trades_bak.append(trades2)
        trades = trades2
        return trades
        # ohlcv 获取指定数币对的K线数据
    def _load_okex_ohlcv_data(symbol):
        okex = ccxt.okex({'verbose': True})
        markets = okex.load_markets()
        ohlcv = okex.fetch_ohlcv(symbol)
        return ohlcv
    # orderbook 获取指定数币对的当前的报价（深度），以及相应的交易量
    def _load_okex_orderbook_data(symbol):
        okex = ccxt.okex({'verbose': True})
        markets = okex.load_markets()
        orderbook = okex.fetch_order_book(symbol)
        return orderbook
    ##########################################################################################################
    # bitfinex

    # ticker 截止到当前，过去24小时的 交易统计/汇总信息
    def _load_bitfinex_ticker_data(symbol):
        bitfinex = ccxt.bitfinex({'verbose': True})
        markets = bitfinex.load_markets()
        ticker = bitfinex.fetch_ticker(symbol)

        ticker.pop('info')
        ticker2 = {}
        ticker2['symbol'] = ticker.pop('symbol')
        ticker2['priceChange'] = ticker.pop('change')
        ticker2['priceChangePercent'] = ticker.pop('percentage')
        ticker2['weightedAvgPrice'] = ticker.pop('vwap')
        ticker2['prevClosePrice'] = ticker.pop('previousClose')
        ticker2['lastPrice'] = ticker.pop('last')
        ticker2['lastQty'] = 'none'
        ticker2['bidPrice'] = ticker.pop('bid')
        ticker2['bidQty'] = ticker.pop('bidVolume')
        ticker2['askPrice'] = ticker.pop('ask')
        ticker2['askQty'] = ticker.pop('askVolume')
        ticker2['openPrice'] = ticker.pop('open')
        ticker2['highPrice'] = ticker.pop('high')
        ticker2['lowPrice'] = ticker.pop('low')
        ticker2['volume'] = ticker.pop('baseVolume')
        ticker2['quoteVolume'] = ticker.pop('quoteVolume')
        ticker2['openTime'] = ticker.pop('datetime')
        ticker2['closeTime'] = ticker.pop('timestamp')
        ticker2['firstId'] = 'none'
        ticker2['lastId'] = 'none'
        ticker2['count'] = 'none'
        ticker = ticker2
        return ticker
    # print(ticker2)

    # trades过去一段时间（最多返回500条数据）的交易记录，包括成交价、成交量 ……
    def _load_bitfinex_trades_data(symbol):
        bitfinex = ccxt.bitfinex({'verbose': True})
        markets = bitfinex.load_markets()
        trades = bitfinex.fetch_trades(symbol)

        l = len(trades)
        L = list(range(l))
        trades_bak = []
        i = 0
        for i in L:
            trades_1 = trades[i]
            trades2 = {}
            trades2['a'] = trades_1.pop('id')
            trades2['p'] = trades_1.pop('price')
            trades2['q'] = trades_1.pop('amount')
            trades2['f'] = 'none'
            trades2['l'] = 'none'
            trades2['T'] = trades_1.pop('timestamp')
            trades2['m'] = 'none'
            trades2['M'] = 'none'
            trades_bak.append(trades2)
        trades = trades2
        return trades
    # ohlcv 获取指定数币对的K线数据
    def _load_bitfinex_ohlcv_data(symbol):
        bitfinex = ccxt.bitfinex({'verbose': True})
        markets = bitfinex.load_markets()
        ohlcv = bitfinex.fetch_ohlcv(symbol)
        return ohlcv
    # orderbook 获取指定数币对的当前的报价（深度），以及相应的交易量
    def _load_bitfinex_orderbook_data(symbol):
        bitfinex = ccxt.bitfinex({'verbose': True})
        markets = bitfinex.load_markets()
        orderbook = bitfinex.fetch_order_book(symbol)
        return orderbook
        ##########################################################################################################
        # gateio

        # ticker 截止到当前，过去24小时的 交易统计/汇总信息
    def _load_gateio_ticker_data(symbol):
        gateio = ccxt.gateio({'verbose': True})
        markets = gateio.load_markets()
        ticker = gateio.fetch_ticker(symbol)
        ticker.pop('info')
        ticker2 = {}
        ticker2['symbol'] = ticker.pop('symbol')
        ticker2['priceChange'] = ticker.pop('change')
        ticker2['priceChangePercent'] = ticker.pop('percentage')
        ticker2['weightedAvgPrice'] = ticker.pop('vwap')
        ticker2['prevClosePrice'] = ticker.pop('previousClose')
        ticker2['lastPrice'] = ticker.pop('last')
        ticker2['lastQty'] = 'none'
        ticker2['bidPrice'] = ticker.pop('bid')
        ticker2['bidQty'] = ticker.pop('bidVolume')
        ticker2['askPrice'] = ticker.pop('ask')
        ticker2['askQty'] = ticker.pop('askVolume')
        ticker2['openPrice'] = ticker.pop('open')
        ticker2['highPrice'] = ticker.pop('high')
        ticker2['lowPrice'] = ticker.pop('low')
        ticker2['volume'] = ticker.pop('baseVolume')
        ticker2['quoteVolume'] = ticker.pop('quoteVolume')
        ticker2['openTime'] = ticker.pop('datetime')
        ticker2['closeTime'] = ticker.pop('timestamp')
        ticker2['firstId'] = 'none'
        ticker2['lastId'] = 'none'
        ticker2['count'] = 'none'
        ticker = ticker2
        return ticker

    # trades过去一段时间（最多返回500条数据）的交易记录，包括成交价、成交量 ……
    def _load_gateio_trades_data(symbol):
        gateio = ccxt.gateio({'verbose': True})
        markets = gateio.load_markets()
        trades = gateio.fetch_trades(symbol)
        l = len(trades)
        L = list(range(l))
        trades_bak = []
        i = 0
        for i in L:
            trades_1 = trades[i]
            trades2 = {}
            trades2['a'] = trades_1.pop('id')
            trades2['p'] = trades_1.pop('price')
            trades2['q'] = trades_1.pop('amount')
            trades2['f'] = 'none'
            trades2['l'] = 'none'
            trades2['T'] = trades_1.pop('timestamp')
            trades2['m'] = 'none'
            trades2['M'] = 'none'
            trades_bak.append(trades2)
        trades = trades2
        return trades

    # ohlcv 获取指定数币对的K线数据
    def _load_gateio_ohlcv_data(symbol):
        gateio = ccxt.gateio({'verbose': True})
        markets = gateio.load_markets()
        ohlcv = gateio.fetch_ohlcv(symbol)
        return ohlcv
    # orderbook 获取指定数币对的当前的报价（深度），以及相应的交易量
    def _load_gateio_orderbook_data(symbol):
        gateio = ccxt.gateio({'verbose': True})
        markets = gateio.load_markets()
        orderbook = gateio.fetch_order_book(symbol)
        return orderbook
    ##########################################################################################################
    # huobipro
    # ticker 截止到当前，过去24小时的 交易统计/汇总信息
    def _load_huobipro_ticker_data(symbol):
        huobipro = ccxt.huobipro({'verbose': True})
        markets = huobipro.load_markets()
        ticker = huobipro.fetch_ticker(symbol)
        ticker.pop('info')
        ticker2 = {}
        ticker2['symbol'] = ticker.pop('symbol')
        ticker2['priceChange'] = ticker.pop('change')
        ticker2['priceChangePercent'] = ticker.pop('percentage')
        ticker2['weightedAvgPrice'] = ticker.pop('vwap')
        ticker2['prevClosePrice'] = ticker.pop('previousClose')
        ticker2['lastPrice'] = ticker.pop('last')
        ticker2['lastQty'] = 'none'
        ticker2['bidPrice'] = ticker.pop('bid')
        ticker2['bidQty'] = ticker.pop('bidVolume')
        ticker2['askPrice'] = ticker.pop('ask')
        ticker2['askQty'] = ticker.pop('askVolume')
        ticker2['openPrice'] = ticker.pop('open')
        ticker2['highPrice'] = ticker.pop('high')
        ticker2['lowPrice'] = ticker.pop('low')
        ticker2['volume'] = ticker.pop('baseVolume')
        ticker2['quoteVolume'] = ticker.pop('quoteVolume')
        ticker2['openTime'] = ticker.pop('datetime')
        ticker2['closeTime'] = ticker.pop('timestamp')
        ticker2['firstId'] = 'none'
        ticker2['lastId'] = 'none'
        ticker2['count'] = 'none'
        ticker = ticker2
        return ticker
    # trades过去一段时间（最多返回500条数据）的交易记录，包括成交价、成交量 ……
    def _load_huobipro_trades_data(symbol):
        huobipro = ccxt.huobipro({'verbose': True})
        markets = huobipro.load_markets()
        trades = huobipro.fetch_trades(symbol)
        print(trades)
        l = len(trades)
        L = list(range(l))
        trades_bak = []
        i = 0
        for i in L:
            trades_1 = trades[i]
            trades2 = {}
            trades2['a'] = trades_1.pop('id')
            trades2['p'] = trades_1.pop('price')
            trades2['q'] = trades_1.pop('amount')
            trades2['f'] = 'none'
            trades2['l'] = 'none'
            trades2['T'] = trades_1.pop('timestamp')
            trades2['m'] = 'none'
            trades2['M'] = 'none'
            trades_bak.append(trades2)
        trades = trades2
        return trades
    # ohlcv 获取指定数币对的K线数据
    def _load_huobipro_ohlcv_data(symbol):
        huobipro = ccxt.huobipro({'verbose': True})
        markets = huobipro.load_markets()
        ohlcv = huobipro.fetch_ohlcv(symbol)
        return ohlcv
    # orderbook 获取指定数币对的当前的报价（深度），以及相应的交易量
    def _load_huobipro_orderbook_data(symbol):
        huobipro = ccxt.huobipro({'verbose': True})
        markets = huobipro.load_markets()
        orderbook = huobipro.fetch_order_book(symbol)
        return orderbook

#binance_result = _load_binance_ticker_data('BTC/USDT')
#print(binance_result)
# huobipro_result = _load_huobipro_data('BTC/USDT')
# gateio_result = _load_gateio_data('BTC/USDT')
# bitfinex_result = _load_bitfinex_data('BTC/USDT')
# okex_result = _load_okex_data('BTC/USDT')
# zb_result = _load_zb_data('BTC/USDT')

# r = redis.Redis(host='localhost',port=6379,db=0)
# r.hmset('okex', o