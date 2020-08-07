import websocket
import threading
import json
import time
import queue


class BybitWebSockets():
    """
    Link: https://bybit-exchange.github.io/docs/inverse/#t-websocket
    """


    PRIVATE_TOPIC = ['position', 'execution', 'order']


    def ws_exit(self):
        '''Call this to exit - will close websocket.'''
        self.ws_exited = True
        self.ws.close()

    def ws_connect(self, logger):
        '''Connect to the websocket in a thread.'''
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.web_socket_url,
                                         on_message=self.ws_on_message,
                                         on_close=self.ws_on_close,
                                         on_open=self.ws_on_open,
                                         on_error=self.ws_on_error,
                                         keep_running=True)

        self.wst = threading.Thread(target=lambda: self.ws.run_forever()) 
        self.wst.daemon = True
        self.wst.start()

        # Wait for connect before continuing
        retry_times = 10
        while not self.ws.sock or not self.ws.sock.connected and retry_times:
            time.sleep(1)
            retry_times -= 1
        if retry_times == 0 and not self.ws.sock.connected: 
            self.ws_exit()
            logger.log('Unable to connect to WebSocket.', 'ERROR')

        if self.api_key and self.api_secret:
            self.ws_do_auth()


    def ws_create_connection(self):
        """ 
        Create connection to websocket. This should be used when you do not want to thread your data consumption

        Alternative to slow down websocket app.
        """
        self.ws = websocket.create_connection(self.web_socket_url)


    def ws_do_auth(self):

        expires = str(int(round(time.time())+3))+"000"
        signature = self.get_ws_signature(expires)

        auth = {}
        auth["op"] = "auth"
        auth["args"] = [self.api_key, expires, signature]

        args = json.dumps(auth)

        self.ws.send(args)

    def ws_on_message(self, message):
        '''Handler for parsing WS messages.'''
        message = json.loads(message)

        if 'success' in message and message["success"]:   
            if 'request' in message and message["request"]["op"] == 'auth':
                self.ws_auth = True
            if 'ret_msg' in message and message["ret_msg"] == 'pong':
                self.ws_data["pong"].put("PING success")


        if 'topic' in message and 'data' in message:
            if 'orderBook' in message.get('topic') and message.get('type') == 'delta': 
                for mes in message.get('data').get('insert'):
                    mes['timestamp_e6'] = message.get('timestamp_e6')
                    mes['type'] = 'insert'
                    self.ws_data[message.get('topic')].put(mes)
                
                for mes in message.get('data').get('update'):
                    mes['timestamp_e6'] = message.get('timestamp_e6')
                    mes['type'] = 'update'
                    self.ws_data[message.get('topic')].put(mes)

                for mes in message.get('data').get('delete'):
                    mes['timestamp_e6'] = message.get('timestamp_e6')
                    mes['type'] = 'delete'
                    self.ws_data[message.get('topic')].put(mes)

            elif 'orderBook' in message.get('topic') and message.get('type') == 'snapshot': 
                for mes in message.get('data'):
                    mes['timestamp_e6'] = message.get('timestamp_e6')
                    mes['type'] = 'snapshot'
                    self.ws_data[message.get('topic')].put(mes)
            

            elif 'data' in message:
                for mes in message["data"]:
                    self.ws_data[message["topic"]].put(mes)

            elif 'Data' in message:
                for mes in message["Data"]:
                    self.ws_data[message["topic"]].put(mes)


    def ws_on_error(self, error):
        '''Called on fatal websocket errors. We exit on these.'''
        if not self.ws_exited:
            self.ws_exit()
            raise websocket.WebSocketException(error)

    def ws_on_open(self):
        '''Called when the WS opens. Placeholder function for now.'''
        None

    def ws_on_close(self):
        '''Called on websocket close. Placeholder function for now.'''
        None

    def ws_ping(self):
        q = queue.Queue()
        self.ws.send('{"op":"ping"}')
        if 'pong' not in self.ws_data:
            self.ws_data['pong'] = q

    def ws_subscribe_kline(self, symbol:str, interval:str): 
        q = queue.Queue()
        param = {}
        param['op'] = 'subscribe'
        param['args'] = ['klineV2.' + interval + '.' + symbol]
        self.ws.send(json.dumps(param))
        if 'klineV2.' + interval + '.' + symbol not in self.ws_data:
            self.ws_data['klineV2.' + interval + '.' + symbol] = q

    def ws_subscribe_trade(self):
        self.ws.send('{"op":"subscribe","args":["trade"]}')
        if "trade.BTCUSD" not in self.ws_data:
            q1, q2, q3, q4 = queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue()
            self.ws_data["trade.BTCUSD"] = q1
            self.ws_data["trade.ETHUSD"] = q2
            self.ws_data["trade.EOSUSD"] = q3
            self.ws_data["trade.XRPUSD"] = q4

    def ws_subscribe_insurance(self):
        self.ws.send('{"op":"subscribe","args":["insurance"]}')
        if 'insurance.BTC' not in self.ws_data:
            q1, q2, q3, q4 = queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue()
            self.ws_data['insurance.BTC'] = q1
            self.ws_data['insurance.XRP'] = q2
            self.ws_data['insurance.EOS'] = q3
            self.ws_data['insurance.ETH'] = q4


    def ws_subscribe_orderBook(self, symbol, depth="25"):
        assert depth in ["25", "200"]
        q = queue.Queue()
        arg_value = "orderBookL2_25.BTCUSD" if depth == "25" else "orderBook_200.100ms.BTCUSD"
        param = {}
        param['op'] = 'subscribe'
        param['args'] = [arg_value]
        self.ws.send(json.dumps(param))
        if arg_value not in self.ws_data:
            self.ws_data[arg_value] = q
        return arg_value

    def ws_subscribe_instrument_info(self, symbol):
        q = queue.Queue()
        param = {}
        param['op'] = 'subscribe'
        param['args'] = ['instrument_info.100ms.' + symbol]
        self.ws.send(json.dumps(param))
        if 'instrument_info.100ms.' + symbol not in self.ws_data:
            self.ws_data['instrument_info.100ms.' + symbol] = q

    def ws_subscribe_position(self):
        q = queue.Queue()
        self.ws.send('{"op":"subscribe","args":["position"]}')
        if 'position' not in self.ws_data:
            self.ws_data['position'] = q

    def ws_subscribe_execution(self):
        q = queue.Queue()
        self.ws.send('{"op":"subscribe","args":["execution"]}')
        if 'execution' not in self.ws_data:
            self.ws_data['execution'] = q

    def ws_subscribe_order(self):
        q = queue.Queue()
        self.ws.send('{"op":"subscribe","args":["order"]}')
        if 'order' not in self.ws_data:
            self.ws_data['order'] = q

    def ws_subscribe_stop_order(self):
        q = queue.Queue()
        self.ws.send('{"op":"subscribe","args":["stop_order"]}')
        if 'stop_order' not in self.ws_data:
            self.ws_data['order'] = q

    def ws_get_data(self, topic):
        if topic not in self.ws_data:
            return [" The topic {} is not subscribed.".format(topic)]
        if topic.split('.')[0] in BybitWebSockets.PRIVATE_TOPIC and not self.ws_auth:
            return ["Authentication failed. Please check your api_key and api_secret. Topic: {}".format(topic)]
        else:
            return_list = []
            while not self.ws_data.get(topic).empty(): 
                return_list.append( self.ws_data.get(topic).get(block=False, timeout=2))
                
            return return_list


