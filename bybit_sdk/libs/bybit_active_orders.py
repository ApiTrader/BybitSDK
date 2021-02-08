import bybit_sdk.transforms.bybit_order_transforms as orders
import json



class ActiveOrders(orders.OrderTransforms):


    def place_active_order(self, side, symbol, order_type, qty, price, time_in_force='GoodTillCancel', take_profit=None, stop_loss=None, reduce_only=None, close_on_trigger=None, order_link_id=None, api_url='open-api/order/create'): 
        """ 
        Places an order on the ByBit exchange.

        :param side: The side of the exchange i.e. 'Buy' or 'Sell'
        :type side: Required. string.
        :param symbol: contract type i.e. 'BTCUSD', 'ETHUSD', 'EOSUSD', or 'XRPUSD'
        :type symbol: Required. string.
        :param order_type: Active order type i.e. 'Market' or 'Limit' 
        :type order_type: Required. string.
        :param qty: order quantity in USD. Max of 1M.
        :type qty: Required. integer.
        :param price: Order price. If you held no position, order price has to be more than 10% of the market price and less than 1 million. If you has held any position already, your order price has to be better than liquidation price. The minimum unit of order price's increment or decrement is 0.5.
        :type price: Required. integer.
        :param time_in_force: i.e. 'GoodTillCancel', 'ImmediateOrCancel', 'FillOrKill', 'PostOnly'
        :type time_in_force: Required. string.
        :param take_profit: the take profit price 
        :type take_profit: number 
        :param stop_loss: the stop loss price
        :type stop_loss: number
        :param reduce_only: reduce only
        :type reduce_only: bool
        :param close_on_trigger: close_on_trigger
        :type close_on_trigger: bool
        :param order_link_id: Customized order ID, maximum length at 36 characters, and order ID under the same agency has to be unique.
        :type order_link_id: string
        """

        # ensure required values are not None
        assert side is not None
        assert symbol is not None
        assert order_type is not None
        assert qty is not None
        assert price is not None
        assert time_in_force is not None

        params_dict = {'side': side, 
                'symbol': symbol, 
                'order_type': order_type, 
                'qty': qty, 
                'price': price, 
                'time_in_force': time_in_force, 
                'take_profit': take_profit, 
                'stop_loss': stop_loss, 
                'reduce_only': reduce_only, 
                'close_on_trigger': close_on_trigger, 
                'order_link_id': order_link_id
                }

        # get rid of any values that are 'None' 
        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.post_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))



    def get_active_orders(self, symbol='BTCUSD', direction=None, cursor=None, limit=None, order_status=None, api_url='/v2/private/order/list'):
        """ 
        Gets active order list on the ByBit exchange.

        Link: https://bybit-exchange.github.io/docs/inverse/#t-getactive

        :param symbol: Contract type. Default is BTCUSD. 
        :type symbol: string.
        :param limit: Limit for data size per page, max size is 50. Default as showing 20 pieces of data per page
        :type limit: integer
        :param order_status: Query your orders for all statuses if 'order_status' is empty. If you want to query orders with specific statuses , you can pass the order_status split by ','. Available order_status: Created, New, PartiallyFilled, Filled, Cancelled, Rejected
        :type order_status: string 
        :param api_url: the url to the api. Default ''/open-api/order/list''
        :type api_url: Required. string.
        """

        params_dict = {'symbol': symbol,
                    'limit': limit, 
                    'order_status': order_status,
                    'direction': direction,
                    'cursor': cursor
                    }

        # get rid of any values that are 'None' 
        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.get_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))


    def cancel_active_order(self, order_id, symbol='BTCUSD', api_url='/open-api/order/cancel'):
        """
        Cancels an active order given an order id.

        :param order_id: The unique 36 characters order ID was returned to you when the active order was created successfully.
        :type order_id: Required. string.
        :param symbol:  Recommended, otherwise, there will be a small probability of failure. Default is 'BTCUSD'.
        :type symbol: string.
        :param api_url: the url to the api. Default ''/open-api/order/cancel''
        :type api_url: Required. string.
        """
        assert order_id is not None

        params_dict = {'order_id': order_id,
            'symbol': symbol
            }

        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.post_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))



    def change_active_order(self, order_id, qty=None, price=None, symbol='BTCUSD', api_url='open-api/order/replace'): 
        """ 
        Edits an order on the ByBit exchange.

        Link: https://bybit-exchange.github.io/docs/inverse/#t-replaceactive

        :param order_id: The unique 36 characters order ID was returned to you when the active order was created successfully.
        :type order_id: Required. string.
        :param symbol: contract type i.e. 'BTCUSD', 'ETHUSD', 'EOSUSD', or 'XRPUSD'
        :type symbol: Required. string.
        :param qty: order quantity in USD. Max of 1M.
        :type qty: Required. integer.
        :param price: Order price. If you held no position, order price has to be more than 10% of the market price and less than 1 million. If you has held any position already, your order price has to be better than liquidation price. The minimum unit of order price's increment or decrement is 0.5.
        :type price: Required. integer.
        """

        # ensure required values are not None
        assert symbol is not None
        assert order_id is not None

        params_dict = {'symbol': symbol, 
                'order_id': order_id, 
                'p_r_qty': qty, 
                'p_r_price': price
                }

        # get rid of any values that are 'None' 
        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.post_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))



    def place_active_order_v2(self, side, symbol, order_type, qty, price=None, time_in_force='GoodTillCancel', take_profit=None, stop_loss=None, reduce_only=None, close_on_trigger=None, tp_trigger_by=None, sl_trigger_by=None, order_link_id=None, api_url='v2/private/order/create'): 
        """ 
        Places an order on the ByBit exchange.

        Link: https://bybit-exchange.github.io/docs/inverse/#t-placev2active

        :param side: The side of the exchange i.e. 'Buy' or 'Sell'
        :type side: Required. string.
        :param symbol: contract type i.e. 'BTCUSD', 'ETHUSD', 'EOSUSD', or 'XRPUSD'
        :type symbol: Required. string.
        :param order_type: Active order type i.e. 'Market' or 'Limit' 
        :type order_type: Required. string.
        :param qty: order quantity in USD. Max of 1M.
        :type qty: Required. integer.
        :param price: Order price. If you held no position, order price has to be more than 10% of the market price and less than 1 million. If you has held any position already, your order price has to be better than liquidation price. The minimum unit of order price's increment or decrement is 0.5.
        :type price: Required. integer.
        :param time_in_force: i.e. 'GoodTillCancel', 'ImmediateOrCancel', 'FillOrKill', 'PostOnly'
        :type time_in_force: Required. string.
        :param take_profit: the take profit price 
        :type take_profit: number 
        :param stop_loss: the stop loss price
        :type stop_loss: number
        :param reduce_only: reduce only
        :type reduce_only: bool
        :param close_on_trigger: close_on_trigger
        :type close_on_trigger: bool
        :param order_link_id: Customized order ID, maximum length at 36 characters, and order ID under the same agency has to be unique.
        :type order_link_id: string
        """

        # ensure required values are not None
        assert side is not None
        assert symbol is not None
        assert order_type is not None
        assert qty is not None
        assert time_in_force is not None

        params_dict = {'side': side, 
                'symbol': symbol, 
                'order_type': order_type, 
                'qty': qty, 
                'price': price, 
                'time_in_force': time_in_force, 
                'take_profit': take_profit, 
                'stop_loss': stop_loss, 
                'reduce_only': reduce_only, 
                'close_on_trigger': close_on_trigger, 
                'order_link_id': order_link_id,
                'tp_trigger_by': tp_trigger_by, 
                'sl_trigger_by': sl_trigger_by
            }

        # get rid of any values that are 'None' 
        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.post_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))



    def cancel_all_active_orders(self, symbol='BTCUSD', api_url='/v2/private/order/cancelAll'):
        """
        Cancells all active orders. 

        Link: https://bybit-exchange.github.io/docs/inverse/#t-cancelallactive
        
        :param symbol: contract type i.e. 'BTCUSD', 'ETHUSD', 'EOSUSD', or 'XRPUSD'
        :type symbol: Required. string.
        """

        params_dict = {'symbol': symbol}

        # get rid of any values that are 'None' 
        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.post_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))


    def cancel_active_order_v2(self, order_id, order_link_id=None, symbol='BTCUSD', api_url='/v2/private/order/cancel'):
        """
        Cancels an active order given an order id.

        Link: https://bybit-exchange.github.io/docs/inverse/#t-cancelv2active

        :param order_id: The unique 36 characters order ID was returned to you when the active order was created successfully.
        :type order_id: Required. string.
        :param order_link_id: The unique 36 characters order ID was returned to you when the active order was created successfully.
        :type order_link_id: Required. string.
        :param symbol:  Recommended, otherwise, there will be a small probability of failure. Default is 'BTCUSD'.
        :type symbol: string.
        :param api_url: the url to the api. Default ''/open-api/order/cancel''
        :type api_url: Required. string.
        """
        params_dict = {'order_id': order_id,
            'symbol': symbol, 
            'order_link_id': order_link_id
            }

        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.post_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))


    
    def get_realtime_active_order(self, order_id=None, order_link_id=None, symbol='BTCUSD', api_url='/v2/private/order'):
        """ 
        Gets active order list on the ByBit exchange.

        Link: https://bybit-exchange.github.io/docs/inverse/#t-queryactive

        :param order_id: Order Id
        :type order_id: string.
        :param order_link_id: custom order id
        :type order_link_id: string.
        :param symbol: Contract type. Default is BTCUSD. 
        :type symbol: string.
        :param api_url: the url to the api. Default ''/open-api/order/list''
        :type api_url: Required. string.
        """

        params_dict = {'order_id': order_id,
                    'order_link_id': order_link_id,
                    'symbol': symbol
                    }

        # get rid of any values that are 'None' 
        params_dict = dict((k, v) for k, v in params_dict.items() if v is not None)
        data = self.get_request(api_url, parameters=params_dict)
        return json.loads(data.decode('utf-8'))
