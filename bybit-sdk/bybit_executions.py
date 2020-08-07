import json

class Execution():

    def get_trade_records(self, order_id=None, symbol='BTCUSD', start_time=None, page=None, limit=None, api_url='/v2/private/execution/list'):
        """
        Get user's trade records

        Link: https://bybit-exchange.github.io/docs/inverse/#t-usertraderecords

        :param order_id: 
        :type order_id: 
        :param symbol: 
        :type symbol:  
        :param start_time: 
        :type start_time: 
        :param page: 
        :type page: 
        :param limit: 
        :type limit: 
        """

        params_dict = {
            'order_id': order_id,
            'symbol': symbol,
            'start_time': start_time,
            'page': page,
            'limit': limit
        }

        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.get_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))
