import json 


class Funding:

    def get_funding_rate(self, symbol='BTCUSD', api_url='/open-api/funding/prev-funding-rate'):
        """
        Get the latest funding rate. Funding rate is generated every 8 hours at 00:00 UTC, 08:00 UTC and 16:00 UTC. If it's 12:00 UTC now, what you will get is the funding rate generated at 08:00 UTC.

        Link: https://bybit-exchange.github.io/docs/inverse/#t-fundingrate

        :param symbol: Contract type. Valid option: BTCUSD, ETHUSD. Default is 'BTCUSD'
        :type symbol: Required. string. 
        :param api_url: the url to the api. Default '/open-api/stop-order/create'
        :type api_url: Required. string.
        """
        params_dict = {'symbol': symbol}

        data = self.get_request(api_url=api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))

    
    def get_funding_fee(self, symbol='BTCUSD', api_url='/open-api/funding/prev-funding'):
        """
        Get the latest funding fee. 
        Funding settlement occurs every 8 hours at 00:00 UTC, 08:00 UTC and 16:00 UTC. The current intervals's fund fee settlement is based on the previous intervals's fund rate. For example, at 16 o'clock, the settlement is based on the fund rate generated at 8 o'clock. The fund rate generated at 16 o'clock will be used at 0:00 on the next day.

        Link: https://bybit-exchange.github.io/docs/inverse/#t-mylastfundingfee

        :param symbol: Contract type. Valid option: BTCUSD, ETHUSD. Default is 'BTCUSD'
        :type symbol: Required. string. 
        :param api_url: the url to the api. Default '/open-api/stop-order/create'
        :type api_url: Required. string.
        """
        params_dict = {'symbol': symbol}

        data = self.get_request(api_url=api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))


    def get_predicted_funding(self, symbol='BTCUSD', api_url='/open-api/funding/predicted-funding'):
        """
        Get predicted funding rate and funding fee

        Link: https://bybit-exchange.github.io/docs/inverse/#t-predictedfunding

        :param symbol: Contract type. Valid option: BTCUSD, ETHUSD. Default is 'BTCUSD'
        :type symbol: Required. string. 
        :param api_url: the url to the api. Default '/open-api/stop-order/create'
        :type api_url: Required. string.
        """
        params_dict = {'symbol': symbol}

        data = self.get_request(api_url=api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))

