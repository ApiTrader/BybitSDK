import json 

# Documentation: https://bybit-exchange.github.io/docs/inverse/#t-conditionalorders

class ConditionalOrders:


    def cancel_conditional_order(self, stop_order_id, api_url='/open-api/stop-order/cancel'):
        """
        Cancels an conditional order given an order id.

        Link: https://bybit-exchange.github.io/docs/inverse/#t-cancelcond

        :param stop_order_id: The unique 36 characters order ID was returned to you when the active order was created successfully.
        :type stop_order_id: Required. string.
        :param api_url: the url to the api. Default '/open-api/order/cancel'
        :type api_url: Required. string.
        """
        # ensure required values are not None
        assert stop_order_id is not None

        params_dict = {'stop_order_id': stop_order_id}
        data = self.post_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))


    def get_conditional_order(self, stop_order_id=None, order_link_id=None, symbol=None, order=None, page=None, limit=None, api_url="/open-api/stop-order/list"):
        """
        Gets a conditional order list. 

        Link: https://bybit-exchange.github.io/docs/inverse/#t-getcond

        :param stop_order_id: Order ID of conditional order
        :type stop_order_id: string
        :param order_link_id: Customized order ID
        :type order_link_id: string
        :param symbol: Contract type. Default BTCUSD
        :type symbol: string
        :param order: Sort field is created_at, ascending or descending. Default as descending (desc, asc )
        :type order: string
        :param page: Page. Default getting first page data
        :type page: integer
        :param limit: Limit for data size per page, max size is 50. Default as showing 20 pieces of data per page
        :type limit: integer
        :param api_url: the url to the api. Default '/open-api/stop-order/list'
        :type api_url: Required. string.
        """

        params_dict = {"stop_order_id": stop_order_id,
        "order_link_id": order_link_id,
        "symbol": symbol,
        "order": order,
        "page": page,
        "limit": limit}

        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.get_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))

    def place_conditional_order(self, side, order_type, qty, price, base_price, stop_px, time_in_force='GoodTillCancel', close_on_trigger=None, trigger_by=None, reduce_only=None, order_link_id=None, symbol="BTCUSD", api_url="/open-api/stop-order/create"):
        """
        A traditional market price order, will be filled at the best available price.

        Link: https://bybit-exchange.github.io/docs/inverse/#t-placecond

        :param side: Side. Valid option: Buy, Sell
        :type side: Required. string. 
        :param order_type: Conditional order type. Valid option: Limit, Market
        :type order_type: Required. string. 
        :param qty: Order quantity. Maximum quantity of $1 million USD.  
        :type qty: Required. integer.  
        :param price: Execution price for conditional order
        :type price: Required. integer.   
        :param base_price: Send current market price. It will be used to compare with the value of 'stop_px', to decide whether your conditional order will be triggered by crossing trigger price from upper side or lower side. Mainly used to identify the expected direction of the current conditional order.
        :type base_price: Required. integer.   
        :param stop_px: Trigger price
        :type stop_px: Required. integer.   
        :param time_in_force: Time in force, Valid option: GoodTillCancel, ImmediateOrCancel, FillOrKill,PostOnly. Default 'GoodTillCancel'
        :type time_in_force: Required. string
        :param close_on_trigger: close on trigger
        :type close_on_trigger:  bool. 
        :param order_link_id: Customized order ID, maximum length at 36 characters, and order ID under the same agency has to be unique.
        :type order_link_id: string. 
        :param symbol: Contract type. Valid option: BTCUSD, ETHUSD
        :type symbol: Required. string. 
        :param api_url: the url to the api. Default '/open-api/stop-order/create'
        :type api_url: Required. string.
        """

        # ensure required values are not None
        assert side is not None
        assert order_type is not None
        assert qty is not None
        assert price is not None
        assert base_price is not None
        assert stop_px is not None
        assert time_in_force is not None
        assert symbol is not None

        
        params_dict = {"side":side, 
        "order_type":order_type, 
        "qty":qty, 
        "price":price, 
        "base_price":base_price, 
        "stop_px":stop_px, 
        "time_in_force":time_in_force, 
        "close_on_trigger":close_on_trigger, 
        "order_link_id":order_link_id, 
        "symbol":symbol, 
        "trigger_by": trigger_by,
        "reduce_only": reduce_only
        }

        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.post_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))



    def cancel_all_conditional_orders(self, symbol='BTCUSD', api_url='/v2/private/stop-order/cancelAll'):
        """
        Cancel all conditional orders

        Link: https://bybit-exchange.github.io/docs/inverse/#t-cancelallcond
        """

        params_dict = {"symbol":symbol}

        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.post_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))


    def change_conditional_orders(self, order_id, stop_order_id, p_r_trigger_price=None, qty=None, price=None, symbol='BTCUSD', api_url='/open-api/stop-order/replace'):
        """
        Replace/Change a conditional orders

        Link: https://bybit-exchange.github.io/docs/inverse/#t-replacecond
        """

        params_dict = {'symbol': symbol, 
        'order_id': order_id, 
        'stop_order_id': stop_order_id, 
        'p_r_qty': qty, 
        'p_r_price': price, 
        'p_r_trigger_price': p_r_trigger_price
        }


        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.post_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))


    def get_realtime_conditional_order(self, stop_order_id=None, order_link_id=None, symbol='BTCUSD', api_url='/v2/private/order'):
        """ 
        Gets active order list on the ByBit exchange.

        Link: https://bybit-exchange.github.io/docs/inverse/#t-querycond

        :param stop_order_id: Order Id
        :type stop_order_id: string.
        :param order_link_id: custom order id
        :type order_link_id: string.
        :param symbol: Contract type. Default is BTCUSD. 
        :type symbol: string.
        :param api_url: the url to the api. Default ''/open-api/order/list''
        :type api_url: Required. string.
        """

        params_dict = {'stop_order_id': stop_order_id,
                    'order_link_id': order_link_id,
                    'symbol': symbol
                    }

        # get rid of any values that are 'None' 
        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.get_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))