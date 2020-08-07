import bybit_sdk.transforms.bybit_wallet_transforms as wallet_transforms
import json

class Wallet(wallet_transforms.WalletDataTransforms):


    def get_wallet_data(self, start_date=None, end_date=None, currency=None, wallet_fund_type=None, page=None, limit=None, api_url='open-api/wallet/fund/records'): 
        """ 
        Gets wallet funding information. 

        Link: https://bybit-exchange.github.io/docs/inverse/#t-walletrecords

        
        :param start_date: start point for result 
        :type start_date: string. Optional. 
        :param end_date: end point for result
        :type end_date: string. Optional.
        :param currency: contract type
        :type currency: string. Optional.
        :param wallet_fund_type: contract type 
        :type wallet_fund_type: string. Optional.
        :param page: default is the first page
        :type page: integer. optional.
        :param limit: records per page. max is 50. Default is 20.
        :type limit: integer. optional.
        :param api_url: default 'open-api/wallet/fund/records' 
        :type api_url: string. 
        """


        params_dict = {'start_date': start_date, 
                'end_date': end_date, 
                'currency': currency, 
                'wallet_fund_type': wallet_fund_type, 
                'page': page, 
                'limit': limit,
                }

        # get rid of any values that are 'None' 
        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.get_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))


    def get_wallet_balance(self, coin='BTC', api_url='/v2/private/wallet/balance'):
        """ 
        Gets wallet balance information. 

        Link: https://bybit-exchange.github.io/docs/inverse/#t-balance

        
        :param coin: the coin wallet type 
        :type coin: string ('BTC', 'EOS', 'XRP', 'ETH', 'USDT') 
        """
        assert coin in ['BTC', 'EOS', 'XRP', 'ETH', 'USDT']
        params_dict = {'coin': coin}

        # get rid of any values that are 'None' 
        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.get_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))


    def get_withdraw_records(self, start_date=None, end_date=None, status=None, page=None, limit=None, coin='BTC', api_url='/open-api/wallet/withdraw/list'):
        """ 
        Gets wallet withdraw information

        Link: https://bybit-exchange.github.io/docs/inverse/#t-withdrawrecords

        
        :param coin: the coin wallet type 
        :type coin: string ('BTC', 'EOS', 'XRP', 'ETH', 'USDT') 
        :param start_date: starting point for result
        :param end_date: ending point for result
        :param status: withdraw status
        :param page: page number. default is 1. 
        :param limit: number of records per page. default is 20 max is 50
        """
        params_dict = {'start_date': start_date,
            'end_date': end_date,
            'status': status,
            'page': page,
            'limit': limit,
            'coin': coin
            }

        # get rid of any values that are 'None' 
        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.get_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))