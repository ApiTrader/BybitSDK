import requests
import datetime
import hmac
import hashlib
import json
import websocket

import bybit_sdk.libs.bybit_active_orders as active_orders
import bybit_sdk.libs.bybit_conditional_orders as conditional_orders
import bybit_sdk.libs.bybit_executions as executions
import bybit_sdk.libs.bybit_funding as funding
import bybit_sdk.libs.bybit_market_data as market_data
import bybit_sdk.libs.bybit_positions as positions
import bybit_sdk.libs.bybit_wallet as wallet
import bybit_sdk.libs.bybit_websockets as bws
import bybit_sdk.libs.bybit_kline as kline



class ByBitClient(active_orders.ActiveOrders
                , conditional_orders.ConditionalOrders
                , executions.Execution
                , funding.Funding
                , market_data.MarketData
                , positions.Positions
                , wallet.Wallet
                , bws.BybitWebSockets
                , kline.HistoricalKline):

    def __init__(self, base_url='https://api-bybit.com/', api_secret=None, api_key=None, Session=None, logger=None, web_socket_url=None):
        """
        Link: https://bybit-exchange.github.io/docs/inverse/#t-introduction
        """
        # required api values even for public endpoints
        self.api_secret = api_secret
        self.api_key = api_key
        self.base_url = base_url
        # optional web socket objects
        self.web_socket_url = web_socket_url
        self.ws = None
        self.ws_data = {}
        self.ws_exited = False
        self.ws_auth = False
        self.Session = Session
        self.logger = logger


    def get_param_string(self, parameters=None):
        """
        Generates a hash parameter string for our api call. 

        Link: https://bybit-exchange.github.io/docs/inverse/#t-authentication
        """
        if parameters is None:
            parameters = {}
            
        time_to_send = int(float(self.get_server_time()['time_now'][0:10]+"000"))
        parameters['api_key'] = self.api_key
        parameters['timestamp'] = time_to_send

        _val = '&'.join([str(k)+"="+str(v) for k, v in sorted(parameters.items()) if (k != 'sign') and (v is not None)])
        sign = str(hmac.new(bytes(self.api_secret, "utf-8"), bytes(_val, "utf-8"), digestmod="sha256").hexdigest())
        parameters['sign'] = sign
        return parameters



    def get_ws_signature(self, expires, msg_val = 'GET/realtime'):
        """
        Generates signature for bybit web sockets.
        Link: https://bybit-exchange.github.io/docs/inverse/#t-authentication
        """
        expire = str(expires)

        return str(hmac.new(bytes(self.api_secret, "utf-8"), msg = bytes(msg_val+expire , 'utf-8'), digestmod = "sha256").hexdigest())

    def get_request(self, api_url, parameters=None):
        """
        Generalized method to make a GET request to the bybit api. 
        This method will be the only way to perform get requests with the client, however, this will turn into a helper method to different modules making the client a little easier. 

        :param api_url: the desired api url not including the base url 
        :type api_url: string
        :param parameters: the parameter dictionary to complete the request. The key is the name of the parameter and the value is the parameter value. 
        :type parameters: dictionary 
        :return request data
        """
        request_params = self.get_param_string(parameters)

        try : 
            data = requests.get(self.base_url+api_url, params=request_params)
            return data.content
        except Exception as e:
            return 'Unable to complete request: {}'.format(str(e))


    def post_request(self, api_url, parameters=None):
        """
        Generalized method to make a POST request to the bybit api.
        This method will be the only way to perform post requests with the client, however, this will turn into a helper method to different modules making the client a little easier. 

        :param api_url: the desired api url not including the base url 
        :type api_url: string
        :param parameters: the parameter dictionary to complete the request. The key is the name of the parameter and the value is the parameter value. 
        :type parameters: dictionary 
        :return request data
        """
        request_params = self.get_param_string(parameters)

        try :
            data = requests.post(self.base_url+api_url, params=request_params)
            return data.content

        except Exception as e:
            return 'Unable to complete request: {}'.format(str(e))


    def get_server_time(self, api_url='/v2/public/time'):
        """
        Gets ByBit server time.  

        Link: https://bybit-exchange.github.io/docs/inverse/#t-servertime

        :param api_url: the api url. Default is 'v2/public/tickers'
        :type api_url: string
        :return json response data
        """
        data = json.loads(requests.get(self.base_url+api_url).content.decode('utf-8'))
        return data

    
    def get_api_key_information(self, api_url='/open-api/api-key'):
        """
        Gets ByBit API Key information. 

        Link: https://bybit-exchange.github.io/docs/inverse/#t-key

        :return json response data
        """
        data = json.loads(requests.get(self.base_url+api_url).content.decode('utf-8'))
        return data
