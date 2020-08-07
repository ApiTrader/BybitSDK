import bybit_sdk.transforms.bybit_positions_transforms as positions_transforms
import json

# Documentation: https://bybit-exchange.github.io/docs/inverse/#t-position
# Documentation: https://bybit-exchange.github.io/docs/inverse/#t-leverage


class Positions(positions_transforms.PositionTransforms):

    def get_user_leverage(self, api_url='/user/leverage'):
        """
        Get User Leverage.

        Link: https://bybit-exchange.github.io/docs/inverse/#t-getleverage

        :param api_url: url to the rest api.
        """
        data = self.get_request(api_url=api_url)
        return json.loads(data.decode('utf-8'))
    def change_user_leverage(self, leverage, symbol='BTCUSD', api_url='/user/leverage/save'):
        """
        Change user leverage.

        Link: https://bybit-exchange.github.io/docs/inverse/#t-changeleverage

        :param symbol: Contract type (BTCUSD ETHUSD). Default is BTCUSD
        :type symbol: Required. string.
        :param leverage: Leverage
        :type leverage: Required. string.
        """

        assert leverage is not None

        params_dict = {'symbol': symbol, 'leverage': leverage}
        data = self.post_request(api_url=api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))

    def get_position_list(self, api_url='/position/list'):
        """
        Gets the current position lists for all 4 symbols.
         
        :param api_url: url to the rest api.
        """
        data = self.get_request(api_url=api_url)
        return json.loads(data.decode('utf-8'))

    def update_margin(self, margin, symbol='BTCUSD', api_url='/position/change-position-margin'):
        """
        Updates Margin.

        Link: https://bybit-exchange.github.io/docs/inverse/#t-changemargin

        :param margin: Margin.
        :type margin: Required. string. 
        :param symbol: Contract type (BTCUSD ETHUSD). Default is BTCUSD
        :type symbol: Required. string. 
        """
        assert margin is not None

        params_dict = {'symbol': symbol, 'margin': margin}
        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.post_request(api_url=api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))


    def get_position_list_v2(self, symbol='BTCUSD', api_url='/v2/private/position/list'):
        """
        Gets the current position lists for a symbol.

        Link: https://bybit-exchange.github.io/docs/inverse/#t-mypositionv2
         
        :param api_url: url to the rest api.
        :param symbol: the position symbol type 
        """
        assert symbol is not None
        params_dict = {'symbol': symbol}
        data = self.get_request(api_url=api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))



    def set_trading_stop(self, symbol='BTCUSD', take_profit=None, stop_loss=None, trailing_stop=None, api_url='/open-api/position/trading-stop'):
        """
        Gets the current position lists for a symbol.

        Link: https://bybit-exchange.github.io/docs/inverse/#t-mypositionv2
         
        :param api_url: url to the rest api.
        :param symbol: the position symbol type 
        """
        assert symbol is not None

        params_dict = {'symbol': symbol, 'take_profit': take_profit, 'stop_loss': stop_loss, 'trailing_stop': trailing_stop}
        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.get_request(api_url=api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))



        
    def get_closed_pnl_list(self, symbol='BTCUSD', start_time=None, end_time=None, exec_type=None, page=None, limit=None, api_url='/v2/private/trade/closed-pnl/list'):
        """
        GGet user's closed profit and loss records. The results are ordered in descending order (the first item is the latest).

        Link: https://bybit-exchange.github.io/docs/inverse/#t-closedprofitandloss
         
        :param api_url: url to the rest api.
        :param symbol: the position symbol type 
        """
        assert symbol is not None


        params_dict = {'symbol': symbol, 
            'start_time': start_time, 
            'end_time': end_time, 
            'exec_type': exec_type, 
            'page': page, 
            'limit': limit
            }

        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)

        data = self.get_request(api_url=api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))

