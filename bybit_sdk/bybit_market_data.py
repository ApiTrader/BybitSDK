import bybit_sdk.transforms.bybit_market_data_transforms as market_data_transforms
import json

class MarketData(market_data_transforms.MarketDataTransforms):

    def get_symbol_data(self, api_url='v2/public/tickers'):
        """
        Gets ticker information for all symbols. 

        Link: https://bybit-exchange.github.io/docs/inverse/#t-latestsymbolinfo

        :param api_url: the api url. Default is 'v2/public/tickers'
        :type api_url: string
        :return json response data
        """
        data = self.get_request(api_url)
        return json.loads(data.decode('utf-8'))

    def get_order_book(self, symbol="BTCUSD", api_url="/v2/public/orderBook/L2"):
        """
        Get the orderbook. Response is in the snapshot format

        Link: https://bybit-exchange.github.io/docs/inverse/#t-orderbook

        :param symbol: 	Valid options: BTCUSD, ETHUSD, EOSUSD, XRPUSD. Default 'BTCUSD'
        :type symbol: Required. string

        """

        params_dict = {'symbol': symbol}

        data = self.get_request(api_url=api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))


    def get_trading_records(self, frm=None, limit=None, symbol='BTCUSD', api_url='/v2/public/trading-records'):
        """
        Link: https://bybit-exchange.github.io/docs/inverse/#t-publictradingrecords

        :param frm: From Id, int, not required.
        :param limit: number of results. Max is 1000, default is 500. 
        """
        assert symbol is not None

        params_dict = {'from': frm,
            'limit': limit,
            'symbol': symbol
            }

        # get rid of any values that are 'None' 
        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.get_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))



    def get_symbols(self, api_url='/v2/public/symbols'):
        """
        Link: https://bybit-exchange.github.io/docs/inverse/#t-querysymbol

        :param frm: From Id, int, not required.
        :param limit: number of results. Max is 1000, default is 500. 
        """
        data = self.get_request(api_url)
        return json.loads(data.decode('utf-8'))