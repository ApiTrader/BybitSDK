import json

class HistoricalKline:

    def get_kline_data(self, interval, from_ts, limit=200, symbol='BTCUSD', api_url='v2/public/kline/list'):
        """
        Gets historical kline data from bybit api

        Link: https://bybit-exchange.github.io/bybit-official-api-docs/en/index.html#operation/query_kline
        """

        params_dict = {"interval": interval,
        "from": from_ts,
        "symbol": symbol,
        "limit": limit}

        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.get_request(api_url, parameters=params_dict)

        return json.loads(data.decode('utf-8'))



